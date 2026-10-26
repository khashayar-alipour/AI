
'''
===============================================================================
===============================================================================
================       Created on Wed Oct 21 21:58:43 2026     ================
================                IDE: Spyder                    ================
================         Author: Khashayar Alipour             ================
================               RNN model codes                 ================
===============================================================================
===============================================================================
'''

# در این فایل کدزنی 0 تا 100 مدل RNN با استفاده از دیتاست imdb انجام میدیم
# اینجا task اینه که ورودی(movie review text)  خودمون رو وارد کنیم و خروجی اینجوری میشه:  positive/negative sentiment


# Pipeline is:
    
#      Text
#       ↓
#    Tokenizer
#       ↓
#  Embedding Layer
#       ↓
#      RNN
#       ↓
#  Linear Layer
#       ↓
#    Sigmoid
#       ↓
# Positive / Negative




"-------------------------------------"
"    Importing library and dataset    "
"-------------------------------------"

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from torch.nn.utils.rnn import pad_sequence

from datasets import load_dataset


dataset = load_dataset("imdb")
print(dataset)

# اطلاعات مربوط به دیتاست
# DatasetDict({
#     train: Dataset({
#         features: ['text', 'label'],
#         num_rows: 25000  })

#     test: Dataset({
#         features: ['text', 'label'],
#         num_rows: 25000  })

#     unsupervised: Dataset({
#         features: ['text', 'label'],
#         num_rows: 50000  })


print(dataset["train"][0])

# {'text': 'I rented I AM CURIOUS-YELLOW from my video store because 
#  of all the controversy that surrounded it when it was first 
#  released in 1967. .... this film doesn't have much of a plot.', 
# 'label': 0}

# اینجا رفتیم از داخل Train dataset و از بین Feature هایی که داشت text روو انتخاب کردیم
# میبینیم که نظر طولانی یک مخاطب درمورد یک فیلم هست و آخرش یک لیبل 0 داره یعنی نظر negative هست


# ازونجایی که تعداد این دیتا خیلی زیاده، برای راحتی، برای train_data از 25000 تا میخوایم فقط 5000 تاشو جدا کنیم
# برای test data از بین 25000 تا میخوایم فقط 1000 تاشو جدا کنیم
train_data = dataset["train"].shuffle(seed=42).select(range(5000))    # Training: 5000 reviews
test_data = dataset["test"].shuffle(seed=42).select(range(1000))      # Testing: 1000 reviews




"-------------------------"
"    Creating Tokenizer   "
"-------------------------"

# pip install torchtext
# from torchtext.data.utils import get_tokenizer
# tokenizer = get_tokenizer("basic_english")


import re

def tokenizer(text):
    
    text = text.lower()
    
    tokens = re.findall( r"\b\w+\b|[^\w\s]", text )
    
    return tokens


#---------------------
#  Testing tokenizer  
#---------------------
 
print( tokenizer("This movie was amazing!") )
# ['this', 'movie', 'was', 'amazing', '!']




"--------------------------"
"    Creating Vocabulary   "
"--------------------------"

from torchtext.vocab import build_vocab_from_iterator

def yield_tokens(data):
    for item in data:
        yield tokenizer(item["text"])


vocab = build_vocab_from_iterator(
    yield_tokens(train_data),
    min_freq=5,
    specials=["<unk>", "<pad>"]
)

vocab.set_default_index( vocab["<unk>"] )

print(vocab["movie"]) #20


#---------------------------
# convert text into tensors
#---------------------------

text = train_data[0]["text"]

tokens = tokenizer(text)

ids = vocab(tokens)

print(tokens[:10])    # ['there', 'is', 'no', 'relation', 'at', 'all', 'between', 'fortier', 'and', 'profiler']

print(ids[:10])   # [46, 10, 68, 7381, 38, 37, 211, 11497, 5, 0]




"----------------------------------------------------"
"    Creating Vocabulary and tokenizer (Better way)  "
"----------------------------------------------------"

from collections import Counter

class SimpleVocab:
    
    def __init__( self, token_iterator, min_freq=1, specials=None ):
        
        if specials is None:
            specials = []
        
        # Count all tokens
        counter = Counter()
        
        for tokens in token_iterator:
            counter.update(tokens)
        
        # Create vocabulary
        self.stoi = {}
        self.itos = []
        
        # Add special tokens first
        for token in specials:
            
            if token not in self.stoi:
                
                self.stoi[token] = len(self.itos)
                self.itos.append(token)
        
        
        # Add normal words
        for token, freq in counter.items():
            
            if freq >= min_freq:
                
                if token not in self.stoi:
                    
                    self.stoi[token] = len(self.itos)
                    self.itos.append(token)
        
        
        self.default_index = None
    
    
    def __getitem__(self, token):
        
        if token in self.stoi:
            return self.stoi[token]
        
        return self.default_index
    
    
    def __call__(self, tokens):
        
        return [
            self[token]
            for token in tokens
        ]
    
    
    def set_default_index(self, index):

        self.default_index = index
    
    
    def __len__(self):
        
        return len(self.itos)
    
    
def yield_tokens(data):
    
    for item in data:
        
        yield tokenizer( item["text"] )
    
        

# اینجا مشخص میکنیم که اگه چیزی رو نمیشناسه unk بزاره و برای فاصله‌ها unk بزاره
vocab = SimpleVocab(
    yield_tokens(train_data),
    min_freq=5,    
    specials=[ "<unk>", "<pad>" ]
)

vocab.set_default_index(
    vocab["<unk>"]
)


# ---------------
# حالا تست میکنیم
# ---------------

# میایم به این vocab که ساختیم یه سری کلمه رندوم میدیم تا ببینیم چه token id بهش میده
# مثلا کلمه movie بهش token id شماره 89 داده
# مثلا چیزهایی که unk هستن یا pad ها بهشون 0 داده

print(vocab["movie"])
#89

print(vocab["amazing"])
#1243

print(vocab["alidsjhdsbdhd"])
#0

print(vocab[" "])
#0

# vocab databse:
# --------------   
# word    token id   token vector (embeding)
# UNK        0          ...
# PAD        0          ...
# movie     89          ...
# amazing  1243         ...




"-------------------"
"    Tokenization   "
"-------------------"
# حالا یه text به عنوان نمونه میکشیم بیرون ببینیم چطوری تبدیل به توکن میکنه

text = train_data[0]["text"]
print(text)
# There is no relation at all between Fortier and Profiler but the fact that both are police series 
# about violent crimes. Profiler looks crispy, Fortier looks classic.   ....     By the way, the actors
# are really good and funny. The acting is not superficial at all...

tokens = tokenizer(text)
print(tokens)
#  ['there', 'is', 'no', 'relation', 'at', 'all', 'between', 'fortier', 'and', 'profiler', 
#   'but', 'the', 'fact', 'that', 'both', 'are', 'police', 'series', 'about', 'violent',
#   'crimes', '.', 'profiler', 'looks', 'crispy', ',', 'fortier', 'the', 'acting', 'is',
#   'not',    .....    'superficial', 'at', 'all', '.', '.', '.']


# همچنین میتونیم به id تمام توکن های این لیست دسترسی پیدا کنیم
ids = vocab(tokens)
print(ids)
# [2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 0, 
#  23, 0, 24, 9, 23, 25, 22, 0, 26, 16, 27, 28, 22, 9, 29, 30, 31, 16, 32, 33, 34, 
#  22, 22, 22, 9, 23, 33, 35, 36, 37, 24,   .....   38, 39, 6, 7, 22, 22, 22]




"-------------------------------"
"    Creating pytorch dataset   "
"-------------------------------"

from torch.utils.data import Dataset

class IMDBDataset(Dataset):

    def __init__(self,data):
        self.data=data


    def __len__(self):
        return len(self.data)


    def __getitem__(self,index):

        text=self.data[index]["text"]
        label=self.data[index]["label"]

        tokens=tokenizer(text)

        ids=torch.tensor( vocab(tokens), dtype=torch.long )

        return ids,label


#-----------------
# creating dataset
#-----------------
train_dataset=IMDBDataset(train_data)


# review 1:
# [12,54,33,2]

# review 2:
# [8,91]

# padding: [ [12,54,33,2], [8,91,0,0] ]





"-------------------------------"
"    Creating collate function  "
"-------------------------------"

from torch.nn.utils.rnn import pad_sequence
def collate(batch):

    texts=[]
    labels=[]

    for text,label in batch:
        texts.append(text)
        labels.append(label)

    texts=pad_sequence(
        texts,
        batch_first=True,
        padding_value=vocab["<pad>"]
    )

    return texts,torch.tensor(labels)




"--------------------------"
"    Creating data loader  "
"--------------------------"

from torch.utils.data import DataLoader

loader=DataLoader(
    train_dataset,
    batch_size=64,
    shuffle=True,
    collate_fn=collate
)


# X:
# (batch, sequence_length)

# Example:
# 64 × 300

# y:
# 64 labels




"-------------------------------"
"    Creating RNN model class   "
"-------------------------------"

import torch.nn as nn

class RNNClassifier(nn.Module):

    def __init__( self, vocab_size, embedding_dim, hidden_dim ):
        super().__init__()

        self.embedding=nn.Embedding(
            vocab_size,
            embedding_dim,
            padding_idx=vocab["<pad>"]
        )

        self.rnn=nn.RNN(
            embedding_dim,
            hidden_dim,
            batch_first=True
        )

        self.fc=nn.Linear( hidden_dim, 1 )


    def forward(self,x):

        embedded=self.embedding(x)
        
        output,hidden=self.rnn( embedded )
        
        out=self.fc( hidden.squeeze(0) )   # 0<out<1

        return out




"--------------------------------"
"    Creating LSTM model class   "
"--------------------------------"

# کلاس LSTM دقیقا همون کلاس RNN هست فقط هرجایی نوشتیم rnn الان مینویسیم lstm
# فرق دیگش اینه که LSTM علاوه بر hidden state اینجا cell state هم داره

class LSTMClassifier(nn.Module):

    def __init__( self, vocab_size, embedding_dim, hidden_dim):
        super().__init__()

        self.embedding = nn.Embedding(
            vocab_size,
            embedding_dim,
            padding_idx=vocab["<pad>"]
        )

        self.lstm = nn.LSTM(
            embedding_dim,
            hidden_dim,
            batch_first=True
        )

        self.fc = nn.Linear( hidden_dim, 1 )


    def forward(self,x):

        embedded = self.embedding(x)

        output,(hidden,cell)=self.lstm( embedded )

        out=self.fc( hidden.squeeze(0) )

        return out




"------------------------------"
"    Creating GRU model class  "
"------------------------------"

# ساختار کلاس مدل GRU هم دقیقا به همون صورت هست
# این مدل همون LSTM هست ولی فقط با دوتا gate ساخته شده

class GRUClassifier(nn.Module):

    def __init__( self, vocab_size, embedding_dim, hidden_dim ):
        super().__init__()

        self.embedding=nn.Embedding(
            vocab_size,
            embedding_dim,
            padding_idx=vocab["<pad>"]
        )

        self.gru=nn.GRU(
            embedding_dim,
            hidden_dim,
            batch_first=True
        )

        self.fc=nn.Linear( hidden_dim, 1 )


    def forward(self,x):

        embedded=self.embedding(x)

        output,hidden=self.gru( embedded )

        out=self.fc( hidden.squeeze(0) )

        return out




"------------------------------------"
"    Creating GRU, RNN, LSTM models  "
"------------------------------------"
# بعد ازینکه کلاس مدل هارو ساختیم، اینجا خودشون رو میسازیم

model=RNNClassifier(
    vocab_size=len(vocab),
    embedding_dim=100,
    hidden_dim=128
)

model=LSTMClassifier(
    vocab_size=len(vocab),
    embedding_dim=100,
    hidden_dim=128
)

model=GRUClassifier(
    vocab_size=len(vocab),
    embedding_dim=100,
    hidden_dim=128
)





"--------------------------------------------------"
"    Creating Text classifier class (Alternative)  "
"--------------------------------------------------"
# ساخت این کلاس، برامون دقیقا همون کاری رو میکنه که ساخت 3 کلاس RNN و LSTM و GRU بصورت جدا از هم میکنه
# این یک روش جایگزین برای این هست که دیگه 3 تا کلاس جدا نسازیم

class TextClassifier(nn.Module):

    def __init__( self, model_type, vocab_size, embedding_dim, hidden_dim ):
        super().__init__()

        self.embedding=nn.Embedding(
            vocab_size,
            embedding_dim,
            padding_idx=vocab["<pad>"]
        )

        if model_type=="RNN":

            self.rnn=nn.RNN(
                embedding_dim,
                hidden_dim,
                batch_first=True
            )


        elif model_type=="LSTM":

            self.rnn=nn.LSTM(
                embedding_dim,
                hidden_dim,
                batch_first=True
            )


        elif model_type=="GRU":

            self.rnn=nn.GRU(
                embedding_dim,
                hidden_dim,
                batch_first=True
            )


        self.fc=nn.Linear( hidden_dim, 1 )

        self.model_type=model_type



    def forward(self,x):

        embedded=self.embedding(x)

        if self.model_type=="LSTM":
            output,(hidden,cell)=self.rnn(embedded)

        else:
            output,hidden=self.rnn(embedded)

        out=self.fc( hidden.squeeze(0) )

        return out
    
    

#--------------------
#   حالا تست میکنیم  
#--------------------

model = TextClassifier( "RNN", len(vocab), 100, 128 )

model = TextClassifier( "LSTM", len(vocab), 100, 128 )

model = TextClassifier( "GRU", len(vocab), 100, 128 )




"------------------------"
"    Creating Optimizer  "
"------------------------"

criterion=nn.BCEWithLogitsLoss()

optimizer=torch.optim.Adam(
    model.parameters(),
    lr=0.001
)



"----------------------------"
"    Creating Training loop  "
"----------------------------"

EPOCH=5

for epoch in range(EPOCH):

    total_loss=0

    for X,y in loader:

        optimizer.zero_grad()
        
        # اینجا X یک جمله هست که مثلا 4 تا کلمه توشه       
        # این کلمات اول tonekize میشن [token1, token2, token3, token4]       
# سپس هر توکن یک ورودی میشه. این ورودی اول وارد یک embedding میشه که به عدد تبدیل بشه       
       # سپس این عدد وارد RNN میشه و این RNN اینقد back میزنه تا کل جمله رو ببینه       
        # سپس کل این جمله میره توی یک linear و یک عدد بین 0 و 1 بهمون میده       
        prediction=model(X)
        
        # اینجا میایم این 0 یا 1 رو با label مقایسه میکنیم تا بفهمیم این جمله مثبت بوده یا منفی بوده        
        loss=criterion( prediction.squeeze(), y.float() )


        loss.backward()

        optimizer.step()


        total_loss+=loss.item()


    print( epoch, total_loss )




"----------------"
"    Evaluation  "
"----------------"

test_dataset = IMDBDataset(test_data)

test_loader = DataLoader(
    test_dataset,
    batch_size=64,
    shuffle=False,
    collate_fn=collate
)


import torch

def evaluate(model, loader):

    model.eval()

    total_loss = 0
    correct = 0
    total = 0

    with torch.no_grad():

        for X,y in loader:

            output = model(X)

            loss = criterion( output.squeeze(), y.float() )

            total_loss += loss.item()

            # convert logits to probability
            probabilities = torch.sigmoid(output)

            # probability > 0.5 means positive
            predictions = ( probabilities > 0.5 ).int().squeeze()

            correct += ( predictions == y ).sum().item()

            total += y.size(0)


    accuracy = correct / total

    avg_loss = total_loss / len(loader)

    return avg_loss, accuracy



test_loss, test_accuracy = evaluate( model, test_loader )

print( f"Test Loss: {test_loss:.4f}" )    # Test Loss: 0.6917
print( f"Test Accuracy: {test_accuracy:.4f}" )   # Test Accuracy: 0.5150





"----------------------"
"    Confusion Matrix  "
"----------------------"

from sklearn.metrics import confusion_matrix

all_predictions=[]
all_labels=[]


model.eval()


with torch.no_grad():

    for X,y in test_loader:

        output=model(X)

        prediction = (
            torch.sigmoid(output)>0.5
        ).int().squeeze()


        all_predictions.extend( prediction.tolist() )

        all_labels.extend( y.tolist() )


cm = confusion_matrix( all_labels, all_predictions )

print(cm)
# [[266 246]
#  [239 249]]





"----------------"
"    Prediction  "
"----------------"

sentence = "This movie was absolutely amazing"

def predict(sentence):

    model.eval()

    tokens = tokenizer(sentence)

    ids = torch.tensor( vocab(tokens), dtype=torch.long )
    ids = ids.unsqueeze(0)

    with torch.no_grad():
        output=model(ids)
        probability=torch.sigmoid( output )

    if probability.item()>0.5:
        return ( "Positive", probability.item() )
    else:
        return ( "Negative", probability.item() )
    
    

predict("The movie was boring and terrible")
#Out[94]: ('Negative', 0.4596017003059387)






















