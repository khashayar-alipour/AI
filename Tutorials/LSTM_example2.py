# -*- coding: utf-8 -*-

'''
===============================================================================
===============================================================================
================       Created on Thu Oct 22 22:59:50 2026     ================
================                IDE: Spyder                    ================
================         Author: Khashayar Alipour             ================
================           LSTM ANN model Coding               ================
===============================================================================
===============================================================================
'''

# در این فایل کدزنی 0 تا 100 مدل LSTM با استفاده از دیتاهای سایت ganjoor انجام شده
# با استفاده از روش website scraping اومدیم رباعی های خیام رو از سایت گرفتیم و دانلود کردیم
# سپس این دیتا رو توی یک فایل ذخیره، و به عنوان دیتاست خودمون ازش استفاده میکنیم

# پس این فایل 2 قسمت اصلی داره
# قسمت اول استخراج دیتا، ساخت دیتاست و ...
# قسمت دوم استفاده از دیتاست برای آموزش مدل




"-------------------------------------------------------"
"    🟠 Importing library and preaparing dataset 🟠    "
"-------------------------------------------------------"

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time


BASE_URL = "https://ganjoor.net"
KHAYYAM_URL = "https://ganjoor.net/khayyam/robaee"

response = requests.get( KHAYYAM_URL, timeout=30 )

response.raise_for_status()

soup = BeautifulSoup( response.text, "html.parser" )

print("Page downloaded successfully")


poem_links = []

for a in soup.find_all("a", href=True):

    href = a["href"]

    if re.fullmatch( r"/khayyam/robaee/sh\d+", href ):
        full_url = BASE_URL + href
        poem_links.append( full_url )
        
        
        
poem_links = list( dict.fromkeys(poem_links) )

print( "Number of poems found:", len(poem_links) )

print(poem_links[:10])


test_url = poem_links[0]

response = requests.get(
    test_url,
    timeout=30
)

response.raise_for_status()

poem_soup = BeautifulSoup(
    response.text,
    "html.parser"
)

print(poem_soup.get_text()[:2000])



#---------------
#---------------
#---------------
#---------------
# Find the poem verses only

verses = []

for element in poem_soup.select(".m1, .m2"):

    text = element.get_text( " ", strip=True )

    if text:
        verses.append(text)


print("Number of verses:", len(verses))

for verse in verses:
    print(verse)
    

# Number of verses: 4
# برخیز بُتا، بیا ز بهر دل ما
# حل کن به جمال خویشتن مشکل ما
# یک کوزه شراب تا به هم نوش کنیم
# زآن پیش که کوزه‌ها کنند از گِل ما
    
    
    


"---------------------------------------------"
"    🟠 Defining extract_poem function 🟠    "
"---------------------------------------------"

def extract_poem(url):

    response = requests.get(
        url,
        timeout=30
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    verses = []

    for element in soup.select(".m1, .m2"):

        text = element.get_text(" ", strip=True)

        if text:
            verses.append(text)

    return verses



verses = extract_poem(poem_links[0])
print(verses)

# ['برخیز بُتا، بیا ز بهر دل ما', 'حل کن به جمال 
# خویشتن مشکل ما', 'یک کوزه شراب تا به هم نوش کنیم', 'زآن 
# پیش که کوزه\u200cها کنند از گِل ما']




"---------------------------------------------------"
"    🟠 Download and gathering all 178 poems 🟠    "
"---------------------------------------------------"

import time

all_poems = []

for i, url in enumerate(poem_links):

    try:

        verses = extract_poem(url)

        if len(verses) > 0:

            poem_text = "\n".join( verses )

            all_poems.append({
                "poem_number": i + 1,
                "url": url,
                "text": poem_text,
                "num_verses": len(verses)
            })

        print( f"{i + 1}/{len(poem_links)} "
               f"downloaded"  )

        time.sleep(0.3)

    except Exception as e:

        print(f"Error for {url}:", e)
        
        
        
# 1/178 downloaded
# 2/178 downloaded
# ...      ...
# 177/178 downloaded
# 178/178 downloaded




"------------------------------------------------"
"    🟠 Turning all poems into Data Frame 🟠    "
"------------------------------------------------"

#------ADFTER DOWNLOAD ALL 178

poems_df = pd.DataFrame( all_poems )

print(poems_df.head())

print("Total poems:", len(poems_df) )

print(poems_df["num_verses"].value_counts() )


# poem_number     ...   num_verses
# 0            1  ...            4
# 1            2  ...            4
# 2            3  ...            4
# 3            4  ...            4
# 4            5  ...            4

# [5 rows x 4 columns]
# Total poems: 178
# num_verses
# 4    178
# Name: count, dtype: int64




"-------------------------------------------"
"    🟠 Saving dataset into csv file 🟠    "
"-------------------------------------------"

#CHECK BEFORE
print( poems_df[["poem_number", "num_verses"]].head(20) )

#     poem_number  num_verses
# 0             1           4
# 1             2           4
# 2             3           4
# ...          ...         ...
# 18           19           4
# 19           20           4



#save that
poems_df.to_csv(
    "khayyam_rubaiyat.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Saved as khayyam_rubaiyat.csv")







#------------------------------
#------------------------------
#------------------------------
#------------------------------
#------------------------------
#------------------------------
#------------------------------
'''
for tokenization we have different choices


character-level --> character to lSTM, easy, best for low data 

woerd-level --> words and good for high data

hugging face/subword like BPE/Wordpeiece and fo rnow not




poems_df
   ↓
Persian normalization
   ↓
split poems into Train / Validation / Test
   ↓
create character vocabulary
   ↓
character → integer
   ↓
create sequences
   ↓
X = previous 60 characters
y = next character
   ↓
save everything
   ↓
PyTorch

'''


import pandas as pd
import numpy as np
import re
import json
import pickle

print(poems_df.head())

for i in range(3):

    print("=" * 70)

    print( f"Poem {poems_df.iloc[i]['poem_number']}")

    print(poems_df.iloc[i]["text"])





"----------------------------------------"
"    🟠 Refining persian language 🟠    "
"----------------------------------------"

def normalize_persian(text):

    # ---------------------------------
    # Arabic Yeh -> Persian Yeh
    # ---------------------------------
    text = text.replace( "ي", "ی" )
    text = text.replace( "ى", "ی")

    # ---------------------------------
    # Arabic Kaf -> Persian Kaf
    # ---------------------------------
    text = text.replace( "ك", "ک" )

    # ---------------------------------
    # Remove Tatweel
    # ---------------------------------
    text = text.replace( "ـ", "" )


    # ---------------------------------
    # Remove Arabic/Persian diacritics
    # َ ِ ُ ّ ْ etc.
    # ---------------------------------
    text = re.sub( r"[\u064B-\u065F\u0670]", "", text )


    # ---------------------------------
    # ZWNJ → normal space
    # ---------------------------------
    text = text.replace( "\u200c", " " )


    # ---------------------------------
    # Multiple spaces → one space
    # ---------------------------------
    text = re.sub( r"[ \t]+", " ", text )


    # ---------------------------------
    # Remove spaces around newline
    # ---------------------------------
    text = re.sub( r" *\n *", "\n", text )


    # ---------------------------------
    # More than 2 newlines → 2
    # ---------------------------------
    text = re.sub( r"\n{3,}", "\n\n", text )
    

    return text.strip()



poems_df["clean_text"] = (
    poems_df["text"]
    .apply(normalize_persian)
)





"-------------------------------------------"
"    🟠 Comparing clean and original 🟠    "
"-------------------------------------------"

print("ORIGINAL:")
print()

print(poems_df.iloc[0]["text"])

print("\n" + "=" * 70)

print("CLEAN:")
print()

print(poems_df.iloc[0]["clean_text"])


# ORIGINAL:
# برخیز بُتا، بیا ز بهر دل ما
# حل کن به جمال خویشتن مشکل ما
# یک کوزه شراب تا به هم نوش کنیم
# زآن پیش که کوزه‌ها کنند از گِل ما

# ======================================================================

# CLEAN:
# برخیز بتا، بیا ز بهر دل ما
# حل کن به جمال خویشتن مشکل ما
# یک کوزه شراب تا به هم نوش کنیم
# زآن پیش که کوزه ها کنند از گل ما





"----------------------------------------"
"    🟠 Dataset unique characters 🟠    "
"----------------------------------------"

all_characters = sorted(
    set("".join(poems_df["clean_text"]) )
 )

print(all_characters)

print("\nNumber of unique characters:",  len(all_characters) )


#the first vocabulary

# ['\n', ' ', '!', '.', ':', '\xa0', '«', '»', '،', '؟', 'آ', 'أ', 'ئ', 'ا', 'ب', 'ت'
#  , 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 
#  'ر', 'ز', 'س', 'ش', 'ص'
#  , 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ل', 'م', 'ن', 'ه', 'و', 'پ'
#  , 'چ', 'ژ', 'ک', 'گ', 'ۀ', 'ی']

# Number of unique characters: 46





"----------------------------------------"
"    🟠 Dataset characters counts 🟠    "
"----------------------------------------"

from collections import Counter


all_text_for_analysis = "".join(
    poems_df["clean_text"]
)


char_counts = Counter(
    all_text_for_analysis
)


char_frequency = pd.DataFrame(
    char_counts.items(),
    columns=[
        "character",
        "count"
    ]
)


char_frequency = (
    char_frequency
    .sort_values(
        "count",
        ascending=False
    )
)


print(char_frequency.head(30))

#    character  count
# 5              4385
# 7          ا   1721
# 3          ی   1363
# 16         ن   1305
# 1          ر   1293
# 10         د   1212
# 9          ه   1130
# 18         و   1074
# 12         م    929
# 0          ب    806
# 6          ت    676
# 15         ک    652
# 25         س    547
#13        \n    534
# 4          ز    504
# 19         ش    414
# 2          خ    340
# 22         گ    330
# 11         ل    297
# 26         ف    212
# 23         چ    201
# 20         آ    180
# 17         ج    147
# 24         ع    116
# 21         پ    114
# 27         ق    109
# 14         ح     81
# 29         غ     57
# 30         ص     51
#8          ،     43





"---------------------------------------------------"
"    🟠 Shuffle - train_end - validation_end 🟠    "
"---------------------------------------------------"

RANDOM_SEED = 42

poems_shuffled = (
    poems_df
    .sample(
        frac=1,
        random_state=RANDOM_SEED
    )
    .reset_index(drop=True)
)

n_poems = len(poems_shuffled)

train_end = int(n_poems * 0.80)

val_end = int(n_poems * 0.90)

train_df = poems_shuffled[:train_end].copy()

val_df = poems_shuffled[train_end:val_end].copy()

test_df = poems_shuffled[val_end:].copy()


    
#check---
    
print("Total:", len(poems_shuffled))

print("Train:", len(train_df))

print("Validation:", len(val_df))

print( "Test:", len(test_df))


# اینجا 178 تا شعر داریم
# از این تعداد 142 تا میذاریم برای train
# تعداد 18 تا میذاریم برای test و برای Validation

# Total: 178
# Train: 142
# Validation: 18
# Test: 18




"------------------------------"
"    🟠 Creating curpus 🟠    "
"------------------------------"

#create on curpus for them -- 
#between two rubaei we have two newline

def create_corpus(df):

    return "\n\n".join( df["clean_text"] )


train_text = create_corpus( train_df )

val_text = create_corpus( val_df )

test_text = create_corpus( test_df )

print(train_text[:1500])


#look at size of them
print("Train characters:", len(train_text) )
print("Validation characters:", len(val_text) )
print("Test characters:", len(test_text) )

# Train characters: 17022
# Validation characters: 2141
# Test characters: 2165





"----------------------------------"
"    🟠 Creating Vocabulary 🟠    "
"----------------------------------"

train_characters = sorted( set(train_text) )

SPECIAL_TOKENS = ["<UNK>"]

vocab = ( SPECIAL_TOKENS + train_characters )


print( "Vocabulary size:", len(vocab) )
print( vocab )

# Vocabulary size: 46
# ['<UNK>', '\n', ' ', '!', ':', '\xa0', '«', '»', '،', '؟', 'آ', 'أ', 'ئ', 'ا', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ل', 'م', 'ن', 'ه', 'و', 'پ', 'چ', 'ژ', 'ک', 'گ', 'ۀ', 'ی']




"-----------------------------------"
"    🟠 Character to integer 🟠    "
"-----------------------------------"

#character --> index

char_to_idx = {
    char: idx
    for idx, char
    in enumerate(vocab)
}


#index --> otken id

idx_to_char = {
    idx: char
    for char, idx
    in char_to_idx.items()
}


#for example

print(char_to_idx.get("ا"))    #13
print(char_to_idx.get("ب"))   #14
print(char_to_idx.get("ی"))    #45

UNK_IDX = char_to_idx["<UNK>"]






"--------------------------------------------"
"    🟠 Creating encode text function 🟠    "
"--------------------------------------------"

# Turn the whole text into token ID

def encode_text(text):

    encoded = []

    for char in text:

        encoded.append(
            char_to_idx.get(
                char,
                UNK_IDX
            )
        )

    return np.array(
        encoded,
        dtype=np.int64
    )


train_encoded = encode_text(
    train_text
)

val_encoded = encode_text(
    val_text
)

test_encoded = encode_text(
    test_text
)


print(train_encoded[:100])

# [39 45 25  2 13 23  2 35 36  2 38  2 15 38  2 34 45 34  2 38  2 36 37 13
#  22 45  2 14 38 20 37  2 24 15  1 43 22 20 36 20 37  2 32 34 42  2 36 45
#  23  2 14 37  2 42 13 22 45  2 14 38 20 37  2 13 24 15  1 37 22  2 17 13
#   2 42 37  2 33 20 35  2 36 37 45  2 15 38  2 14 22  2 22 38 45  2 23 35
#  45 36  1 10]



"--------------------------------------------"
"    🟠 Creating decode text function 🟠    "
"--------------------------------------------"

def decode_ids(ids):

    chars = []

    for idx in ids:

        chars.append(
            idx_to_char[
                int(idx)
            ]
        )

    return "".join(chars)


#test
sample = train_encoded[:100]

print(decode_ids(sample))
# پیش از من و تو لیل و نهاری بوده ست
# گردنده فلک نیز به کاری بوده است
# هر جا که قدم نهی تو بر روی زمین




"---------------------------------------"
"    🟠 Create sequence function 🟠    "
"---------------------------------------"

# میخوایم 60 تا کاراکتر بدیم تا کاراکتر بعدی رو برامون پیشبینی کنه


# now for creation x and y 

# 60 character input
#     ↓
# predict next character


SEQUENCE_LENGTH = 60

#train -> 160 * 4 -->> 170000 charactyer
#60x   y
#60x   y


def create_sequences( encoded_text, sequence_length=60, stride=1 ):

    X = []
    y = []

    for i in range( 0, len(encoded_text) - sequence_length, stride):

        input_sequence = encoded_text[ i: i + sequence_length ]

        target = encoded_text[ i + sequence_length ]

        X.append( input_sequence )

        y.append( target )

    return (
        np.array( X, dtype=np.int64 ),
        np.array( y, dtype=np.int64 )
    )





X_train, y_train = create_sequences(
    train_encoded,
    sequence_length=SEQUENCE_LENGTH,
    stride=1
)


X_val, y_val = create_sequences(
    val_encoded,
    sequence_length=SEQUENCE_LENGTH,
    stride=1
)


X_test, y_test = create_sequences(
    test_encoded,
    sequence_length=SEQUENCE_LENGTH,
    stride=1
)


print("X_train:", X_train.shape)    #X_train: (16962, 60)

print("y_train:", y_train.shape)    #y_train: (16962,)

print("X_val:", X_val.shape)        #X_val: (2081, 60)

print("y_val:", y_val.shape)        #y_val: (2081,)

print("X_test:", X_test.shape)      #X_test: (2105, 60)

print("y_test:", y_test.shape)      #y_test: (2105,)



#---look at one example (455 random number)
sample_index = 455

#inputs
input_ids = X_train[
    sample_index
]

target_id = y_train[
    sample_index
]

#decode
input_text = decode_ids(
    input_ids
)

target_character = idx_to_char[
    int(target_id)
]



print("INPUT:")

print(repr(input_text))

print("\nTARGET:")

print(repr(target_character))


# INPUT:
# 'آمد ، شکستن از بهر چه بود ؟\nور نیک نیامد این صور، عیب که راس'

# TARGET:
# 'ت'






"-----------------------------------"
"    🟠 Save cleaned dataset 🟠    "
"-----------------------------------"

'''
embeding like word2vec or fasttext is better for word-level

but here in our model because we have character-level
we can go have LSTM and itself embeding characters during trainings
'''



#save clean dtaaset
poems_df.to_csv(
    "khayyam_clean.csv",
    index=False,
    encoding="utf-8-sig"
)


#save corpuses
with open(
    "khayyam_train.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write( train_text )


with open(
    "khayyam_validation.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write( val_text )


with open(
    "khayyam_test.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write( test_text )
    
    
    
#save vocabulary
with open(
    "char_to_idx.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        char_to_idx,
        f,
        ensure_ascii=False,
        indent=2
    )
    
    

with open(
    "vocab.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        vocab,
        f,
        ensure_ascii=False,
        indent=2
    )
    
    
    
    
#save ready dataset of pytorch with numpy
np.savez_compressed(

    "khayyam_sequences.npz",

    X_train=X_train,
    y_train=y_train,

    X_val=X_val,
    y_val=y_val,

    X_test=X_test,
    y_test=y_test
)


#for loading


dataset = np.load(
    "khayyam_sequences.npz"
)
X_train = dataset[
    "X_train"
]

y_train = dataset[
    "y_train"
]







"============================================================================="
"============================================================================="
"==================== 🟠   🟠   🟠   🟠   🟠   🟠  ========================"
"==================== 🟠   🟠   🟠   🟠   🟠   🟠  ========================"
"==================== 🟠   🟠   🟠   🟠   🟠   🟠  ========================"
"============================================================================="
"============================================================================="


# تا اینجا، هر کاری انجام شده فقط آماده سازی و پردازش و ذخیره دیتاست بوده
# ازین به بعد میخوایم از دیتاستی که ساختیم در pytorch استفاده کنیم


#             poems_df
#                 ↓
#       Persian normalization
#                 ↓
#        split by complete poem
#
#       ↙         ↓          ↘
#    Train       Val        Test
#      ↓          ↓           ↓
#   corpus      corpus       corpus
#      ↓          ↓           ↓
#          character IDs
#                 ↓
#           sliding window
#                 ↓
#              X_train
#           (samples, 60)

#              y_train
#            (samples,)

#                ↓
#        READY FOR PYTORCH

      
      


import torch
import torch.nn as nn

from torch.utils.data import (
    TensorDataset,
    DataLoader
)

import numpy as np
import matplotlib.pyplot as plt




"------------------------------"
"    🟠 Creating tensor 🟠    "
"------------------------------"


torch.manual_seed(42)
np.random.seed(42)


X_train_tensor = torch.tensor(
    X_train,
    dtype=torch.long
)

y_train_tensor = torch.tensor(
    y_train,
    dtype=torch.long
)


X_val_tensor = torch.tensor(
    X_val,
    dtype=torch.long
)

y_val_tensor = torch.tensor(
    y_val,
    dtype=torch.long
)


X_test_tensor = torch.tensor(
    X_test,
    dtype=torch.long
)

y_test_tensor = torch.tensor(
    y_test,
    dtype=torch.long
)





"-------------------------------"
"    🟠 Creating dataset 🟠    "
"-------------------------------"

train_dataset = TensorDataset(
    X_train_tensor,
    y_train_tensor
)

val_dataset = TensorDataset(
    X_val_tensor,
    y_val_tensor
)

test_dataset = TensorDataset(
    X_test_tensor,
    y_test_tensor
)




"-----------------------------------"
"    🟠 Creating data loader 🟠    "
"-----------------------------------"

BATCH_SIZE = 64

train_loader = DataLoader(
    train_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True
)

val_loader = DataLoader(
    val_dataset,
    batch_size=BATCH_SIZE,
    shuffle=False
)

test_loader = DataLoader(
    test_dataset,
    batch_size=BATCH_SIZE,
    shuffle=False
)




"-----------------------------------"
"    🟠 Device configuration 🟠    "
"-----------------------------------"

if torch.cuda.is_available():

    device = torch.device("cuda")

elif torch.backends.mps.is_available():

    device = torch.device("mps")

else:

    device = torch.device("cpu")


print("Device:", device)   #Device: cpu





"----------------------------------------"
"    🟠 Creating LSTM Model class 🟠    "
"----------------------------------------"

VOCAB_SIZE = len(vocab)

print("Vocabulary size:", VOCAB_SIZE)    #Vocabulary size: 46


# Input:  60 characters

# Output:  one of 46 possible characters

#    Character IDs
#      (64, 60)
#          ↓
#      Embedding
#    (64, 60, 64)
#          ↓
#        LSTM
#   (64, 60, 256)
#          ↓
#    Last timestep
#     (64, 256)
#          ↓
#       Linear
#  (64, vocab_size)
#          ↓
#   next character



class KhayyamLSTM(nn.Module):

    def __init__( self, vocab_size, embedding_dim=64, hidden_size=256, num_layers=2, dropout=0.2 ):
        super().__init__()

        # ----------------------------------
        # Embedding
        # ----------------------------------
        self.embedding = nn.Embedding(
            num_embeddings=vocab_size,
            embedding_dim=embedding_dim
        )

        # ----------------------------------
        # LSTM
        # ----------------------------------
        self.lstm = nn.LSTM(

            input_size=embedding_dim,

            hidden_size=hidden_size,

            num_layers=num_layers,

            batch_first=True,

            dropout=(
                dropout
                if num_layers > 1
                else 0
            )
        )

        # ----------------------------------
        # Output layer
        # ----------------------------------
        self.fc = nn.Linear( hidden_size, vocab_size )



    def forward(self, x):

        # x:
        # (batch, sequence_length)
        # example:
        # (64, 60)

        embedded = self.embedding(x)
        # embedded:
        # (64, 60, 64)

        output, (hidden, cell) = self.lstm(embedded)
        # output:
        # (64, 60, 256)

        last_output = output[:, -1, :]
        # last_output:
        # (64, 256)

        logits = self.fc(last_output)
        # logits:
        # (64, vocab_size)


        return logits



embedding_dim = 64

model = KhayyamLSTM(

    vocab_size=VOCAB_SIZE,
    embedding_dim=embedding_dim,
    hidden_size=256,
    num_layers=1,
    dropout=0.2
)


model = model.to(device)
print(model)

# KhayyamLSTM(
#   (embedding): Embedding(46, 64)
#   (lstm): LSTM(64, 256, batch_first=True)
#   (fc): Linear(in_features=256, out_features=46, bias=True)
# )



# (64,60)
#    ↓
# Embedding
#    ↓
# (64,60,64)



"---------------------------------"
"    🟠 Creating optimizer 🟠    "
"---------------------------------"

criterion = nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)




"-------------------------------------"
"    🟠 Creating Training loop 🟠    "
"-------------------------------------"

EPOCHS = 30

train_losses = []
val_losses = []

for epoch in range(EPOCHS):

    # ==================================================
    # TRAIN
    # ==================================================
    model.train()

    total_train_loss = 0


    for ( X_batch, y_batch ) in train_loader:

        X_batch = X_batch.to( device )

        y_batch = y_batch.to( device )


        # --------------------------
        # Forward
        # --------------------------
        logits = model( X_batch )


        # --------------------------
        # Loss
        # --------------------------
        loss = criterion( logits, y_batch )


        # --------------------------
        # Clear gradients
        # --------------------------
        optimizer.zero_grad()


        # --------------------------
        # Backpropagation
        # --------------------------
        loss.backward()


        # --------------------------
        # Gradient clipping
        # --------------------------
        torch.nn.utils.clip_grad_norm_(
            model.parameters(),
            max_norm=1.0
        )


        # --------------------------
        # Update
        # --------------------------
        optimizer.step()

        total_train_loss += ( loss.item() )


    average_train_loss = ( total_train_loss / len(train_loader) )

    train_losses.append( average_train_loss )



    # ==================================================
    # VALIDATION
    # ==================================================
    model.eval()

    total_val_loss = 0


    with torch.no_grad():

        for ( X_batch, y_batch ) in val_loader:


            X_batch = X_batch.to( device )

            y_batch = y_batch.to( device )

            logits = model( X_batch )

            loss = criterion(
                logits,
                y_batch
            )

            total_val_loss += (
                loss.item()
            )


    average_val_loss = ( total_val_loss / len(val_loader) )

    val_losses.append( average_val_loss )


    # ==================================================
    # PRINT
    # ==================================================

    print(

        f"Epoch "
        f"{epoch + 1:02d}/{EPOCHS}"

        f" | Train Loss: "
        f"{average_train_loss:.4f}"

        f" | Val Loss: "
        f"{average_val_loss:.4f}"
    )


# 23 October
# Epoch 01/30 | Train Loss: 2.5917 | Val Loss: 2.3746
# Epoch 02/30 | Train Loss: 2.2864 | Val Loss: 2.2671
# Epoch 03/30 | Train Loss: 2.1354 | Val Loss: 2.1880
# Epoch 04/30 | Train Loss: 2.0143 | Val Loss: 2.1311
# Epoch 05/30 | Train Loss: 1.9255 | Val Loss: 2.1028
# Epoch 06/30 | Train Loss: 1.8403 | Val Loss: 2.1009
# Epoch 07/30 | Train Loss: 1.7504 | Val Loss: 2.0938
# Epoch 08/30 | Train Loss: 1.6630 | Val Loss: 2.0867
# Epoch 09/30 | Train Loss: 1.5695 | Val Loss: 2.0953
# Epoch 10/30 | Train Loss: 1.4719 | Val Loss: 2.1351
# Epoch 11/30 | Train Loss: 1.3805 | Val Loss: 2.1441
# Epoch 12/30 | Train Loss: 1.2758 | Val Loss: 2.1996
# Epoch 13/30 | Train Loss: 1.1776 | Val Loss: 2.2444
# Epoch 14/30 | Train Loss: 1.0764 | Val Loss: 2.2851
# Epoch 15/30 | Train Loss: 0.9838 | Val Loss: 2.3552
# Epoch 16/30 | Train Loss: 0.8798 | Val Loss: 2.4011
# Epoch 17/30 | Train Loss: 0.7859 | Val Loss: 2.5206
# Epoch 18/30 | Train Loss: 0.6986 | Val Loss: 2.5749
# Epoch 19/30 | Train Loss: 0.6077 | Val Loss: 2.6627
# Epoch 20/30 | Train Loss: 0.5292 | Val Loss: 2.7828
# Epoch 21/30 | Train Loss: 0.4579 | Val Loss: 2.8543
# Epoch 22/30 | Train Loss: 0.3953 | Val Loss: 2.9699
# Epoch 23/30 | Train Loss: 0.3310 | Val Loss: 3.0366
# Epoch 24/30 | Train Loss: 0.2737 | Val Loss: 3.1844
# Epoch 25/30 | Train Loss: 0.2254 | Val Loss: 3.2758
# Epoch 26/30 | Train Loss: 0.1860 | Val Loss: 3.3742
# Epoch 27/30 | Train Loss: 0.1493 | Val Loss: 3.5037
# Epoch 28/30 | Train Loss: 0.1232 | Val Loss: 3.6126
# Epoch 29/30 | Train Loss: 0.0987 | Val Loss: 3.6885
# Epoch 30/30 | Train Loss: 0.0757 | Val Loss: 3.8123






"----------------------------"
"    🟠 Creating plot 🟠    "
"----------------------------"

plt.figure( figsize=(10, 5) )
plt.plot( train_losses, label="Training Loss" )
plt.plot( val_losses, label="Validation Loss" )
plt.xlabel( "Epoch" )
plt.ylabel( "Cross Entropy Loss" )
plt.title( "Khayyam LSTM Training" )
plt.legend()
plt.grid( alpha=0.3 )
plt.show()





"-----------------------"
"    🟠 Accuracy 🟠    "
"-----------------------"

def calculate_accuracy( model, data_loader, device ):

    model.eval()

    correct = 0
    total = 0

    with torch.no_grad():

        for ( X_batch, y_batch ) in data_loader:


            X_batch = X_batch.to(device)

            y_batch = y_batch.to(device)


            logits = model(X_batch)


            predictions = torch.argmax( logits, dim=1 )


            correct += ( predictions == y_batch ).sum().item()


            total += ( y_batch.size(0) )


    return (correct / total)




val_accuracy = calculate_accuracy(
    model,
    val_loader,
    device
)

print(
    f"Validation Accuracy: "
    f"{val_accuracy * 100:.2f}%"
)
#Validation Accuracy: 38.30%



test_accuracy = calculate_accuracy(
    model,
    test_loader,
    device
)

print(
    f"Test Accuracy: "
    f"{test_accuracy * 100:.2f}%"
)
#Test Accuracy: 38.86%




model.eval()

total_test_loss = 0


with torch.no_grad():

    for ( X_batch, y_batch ) in test_loader:

        X_batch = X_batch.to(device)

        y_batch = y_batch.to(device)

        logits = model( X_batch )

        loss = criterion( logits, y_batch )

        total_test_loss += ( loss.item() )


average_test_loss = ( total_test_loss / len(test_loader) )

print("Test Loss:", average_test_loss)
#Test Loss: 3.5706039197517163






"-------------------------"
"    🟠 Generation 🟠    "
"-------------------------"

seed_text = train_text[:60]

print(repr(seed_text))
# 'پیش از من و تو لیل و نهاری بوده ست\nگردنده فلک نیز به کاری بو'


def generate_text( model, seed_text, char_to_idx, idx_to_char, sequence_length, device, generation_length=300, temperature=1.0 ):    

    model.eval()

    generated_text = seed_text

    # Unknown token
    unk_idx = char_to_idx["<UNK>"]

    for _ in range(generation_length):

        # ----------------------------------
        # Keep only latest sequence_length
        # characters
        # ----------------------------------
        current_text = generated_text[-sequence_length:]


        # ----------------------------------
        # Encode
        # ----------------------------------
        encoded = [ char_to_idx.get(ch, unk_idx)  for ch in current_text  ]


        # ----------------------------------
        # If seed is shorter than sequence
        # ----------------------------------
        if len(encoded) < sequence_length:

            padding_length = ( sequence_length - len(encoded) )

            encoded = ( [unk_idx] * padding_length + encoded )


        # ----------------------------------
        # Tensor
        # ----------------------------------
        x = torch.tensor(
            encoded,
            dtype=torch.long
        ).unsqueeze(0)

        x = x.to(device)


        # ----------------------------------
        # Prediction
        # ----------------------------------
        with torch.no_grad(): logits = model(x)

        # shape:
        # (1, vocab_size)

        logits = logits[0]


        # ----------------------------------
        # Temperature
        # ----------------------------------
        logits = (logits / temperature)

        probabilities = torch.softmax( logits, dim=0 )


        # ----------------------------------
        # Sample next character
        # ----------------------------------
        next_id = torch.multinomial(
            probabilities,
            num_samples=1
        ).item()

        next_char = idx_to_char[ next_id ]


        # Avoid printing <UNK>
        if next_char == "<UNK>":
            continue


        generated_text += (next_char)


    return generated_text



seed_text = train_text[ :SEQUENCE_LENGTH ]
print(seed_text)

# پیش از من و تو لیل و نهاری بوده ست
# گردنده فلک نیز به کاری بو




generated = generate_text(

    model=model,

    seed_text=seed_text,

    char_to_idx=char_to_idx,

    idx_to_char=idx_to_char,

    sequence_length=SEQUENCE_LENGTH,

    device=device,

    generation_length=100,

    temperature=0.4
)


print(generated)

# پیش از من و تو لیل و نهاری بوده ست
# گردنده فلک نیز به کاری بوده است
# هر جا که قدم نهی تو بر روی زمین
# آن مردمک چشم نگاری بوده ست

# می خوردن و گرد نیکوان گردیدن





"------------------------------------------"
"    🟠 Save and trained model file 🟠    "
"------------------------------------------"

torch.save(
    model.state_dict(),
    "khayyam_lstm.pth"
)



model.load_state_dict(
    torch.load(
        "khayyam_lstm.pth",
        map_location=device
    )
)


