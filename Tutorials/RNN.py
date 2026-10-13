
'''
===============================================================================
===============================================================================
================       Created on Mon Oct  5 16:31:40 2026     ================
================                IDE: Spyder                    ================
================         Author: Khashayar Alipour             ================
================        Recurrent Neural Networks (RNN)        ================
===============================================================================
===============================================================================
'''

# شبکه عصبی مصنوعی (Artificial Neural Network) اسم کلی یک خانواده از مدل‌هاست
# که از لایه‌هایی از نورون‌ها تشکیل شده‌اند و از داده یاد می‌گیرند 
# این شبکه از معماری های مختلفی تشکیل شده که هرکدوم ویژگی‌ها، کاربردها و ساختارهای مخصوص خودشون دارن
# مثلا MLP/ANN که تا الان درموردش یاد گرفتیم شبکه عصبی معمولی هست که کاربرد اصلی آن داده‌های جدولی، classification/regression هست

#                ANN
#         ┌───────┼──────┐
#         ↓       ↓      ↓
#       MLP     CNN   ⭐RNN
#                    ┌───┴──┐
#                    ↓      ↓
#                   LSTM   GRU



# اینجا LSTM نوع پیشرفته‌تر RNN با حافظه بهتر هست که کاربرد اصلی آن متن و سری زمانی طولانی هست
# اینجا GRU نسخه ساده‌تر LSTM هست که کاربرد اصلی آن متن، سری زمانی هست
# اینجا Transformer معماری مبتنی بر Attention هست که کاربرد اصلی آن LLM، ترجمه، متن، تصویر و... هست



#✅ 1-RNN basics:
        # Hidden state
        # RNN Cell
        # Recurrent

#✅ 2-RNN coding with Pytroch

#✅ 3-RNN coding with Tensorflow/Keras

#✅ 4-Coding differences between Tensorflow/Keras and Pytorch

#✅ 5-RNN concepts, Stock price example

#✅ 6-RNN limitations(Vanishing gradient, Exploding gradient)




'''
==========================================================
=======  ⭐  Recurrent Neural Networks (RNN)  ⭐  =======
==========================================================
'''
# در کل RNN نوعی Neural Network است که برای داده‌های ترتیبی (Sequential) طراحی شده؛ یعنی داده‌هایی که ترتیبشان مهم است
# این معماری شبکه عصبی دارای حافظه از مراحل قبلی هست، که کاربرد اصلی آن متن، سری زمانی و صدا هست
# تفاوت اصلی RNN با یک شبکه معمولی این است که RNN می‌تواند اطلاعات قبلی را در هنگام پردازش اطلاعات جدید در نظر بگیرد
# هنگام پردازش ترتیب رو حفظ میکنه، چون برای پیشبینی بعدی به اطلاعات ترتیبی دیتاهای قبلی نیاز داره

# داده های ترتیبی مثل:
# متن و جمله‌ها    
# صدا    
# سری‌های زمانی (Time Series)    
# قیمت سهام    
# سنسورها    
# پیش‌بینی کلمه بعدی    

# مشکل این معماری اینه که RNN ساده در یادآوری اطلاعات خیلی دور مشکل دارد
# مثلاً در یک جمله طولانی ممکنه اطلاعات ابتدای جمله را به‌خوبی حفظ نکنه و برای همین LSTM و GRU بوجود اومده



"✅ Hidden state - RNN Cell "

# تعریف hidden state چیه؟ آن را مثل یک حافظه کوتاه‌مدت تصور کن
# مثلا دیتای ورودی ما این جمله هست و RNN مثلا میاد به اینصورت دیتارو تقسیم بندی میکنه:
# Data = I Love Programming     
# I=x₁  Love=x₂   Programming=x₃

# سپس در هر مرحله پردازش، دیتای پردازش شده از مراحل قبلی در حافظه کوتاه مدت میمونه
# در نهایت H₄ اطلاعاتی از کل دنباله دارد و می‌توانیم از آن برای Classification استفاده کنیم

#           ┌─────────────┐
# x₁ ──────→│   RNN Cell  │──────→ H₁=I
#           └─────────────┘
#                  ↓
#           ┌─────────────┐
# x₂ ──────→│   RNN Cell  │ <──── H₁
#           └─────────────┘
#                  │ H₂=Love
#                  ↓
#           ┌─────────────┐
# x₃ ──────→│   RNN Cell  │──────→ H₃=Programming
#           └─────────────┘
#                  ↓
#                  H₄

# هر بار که یک ورودی وارد RNN می‌شود، دو چیز به Cell داده می‌شود
# و اینجوری RNN همیشه بین گذشته و حال ارتباط برقرار می‌کند
#          Previous Hidden State
#                  ↓
# Input ────→ [ RNN Cell ] ──→ New Hidden State
#                  ↓
#                Output



"✅ Recurrent"

# کلمه Recurrent یعنی چیزی که دوباره برمی‌گردد
# در واقع Hidden State قبلی دوباره به Cell برمی‌گردد
# پس اطلاعات مرحله قبل به مرحله بعد منتقل می‌شود
# به همین دلیل RNN می‌تواند Context / Contextual Information را در نظر بگیرد

#         ┌───────────────────┐
#         │                   ↓
# x₁ → [ RNN ] → h₁
#               │
#               ↓
# x₂ → [ RNN ] → h₂
#               │
#               ↓
# x₃ → [ RNN ] → h₃












'''
==================================================
=======  ⭐  RNN Coding with Pytorch  ⭐  =======
==================================================
'''

"--------Regression---------"

# فرض کنیم ورودی ما یک sequence با 5 تا time step است و در هر time step ما 3 تا ویژگی داریم:
    # Batch = 2
    # Sequence length = 5
    # Features = 3

# یعنی شکل داده میشه اینجوری:
    # (batch, sequence, features)
    #   (2,      5,        3)


import torch
import torch.nn as nn

# Input
x = torch.randn(2, 5, 3)

# RNN
rnn = nn.RNN(input_size=3, hidden_size=4, batch_first=True)

# Forward pass
output, hidden = rnn(x)

print("Output shape:", output.shape)    # torch.Size([2, 5, 4])
print("Hidden shape:", hidden.shape)    # torch.Size([1, 2, 4])


# توضیح پارامترها:

# Hidden_size=4
# یعنی RNN در هر time step یک Hidden State با 4 عدد دارد:
    # hₜ = [0.21, -0.43, 0.72, 0.15]
# اگر بنویسیم hidden_size=128 حافظه داخلی hidden state بزرگتر میشود:
    # hₜ = [128 numbers]


# سوال: output و hidden چه فرقی دارند؟
# فرض کنیم الان:
    # x₁ → RNN → h₁
    # x₂ → RNN → h₂
    # x₃ → RNN → h₃
    # x₄ → RNN → h₄
    # x₅ → RNN → h₅

# الان output شامل همه اینها میشه (همه اطلاعات time step هارو نگه میداره):
    # output = [ h₁  h₂ h₃ h₄ h₅ ]

# ولی hidden معمولاً آخرین Hidden State را نگه می‌دارد:
    # Hidden = h₅



"--------Classification--------"

# یک RNN برای Classification
# مثلاً می‌خواهیم یک sequence را به یکی از دو کلاس تقسیم کنیم
#  Input Sequence
#       ↓
#      RNN
#       ↓
# Last Hidden State
#       ↓
# Linear Layer
#       ↓
# Class 0 / Class 1


import torch
import torch.nn as nn

class RNNClassifier(nn.Module):

    def __init__(self, vocab_size, embedding_dim, hidden_size):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.rnn = nn.RNN(input_size=embedding_size, hidden_size=hidden_size, batch_first=True )
        self.fc = nn.Linear(hidden_size, 1)
        self.sigmoid = nn.sigmoid()

    def forward(self, x):
        
        x = self.embedding(x)
        
        output, hidden = self.rnn(x)

        # Last hidden state
        last_hidden = hidden[-1]

        # Classification
        x = self.fc(last_hidden)

        return self.sigmoid(x)


model = RNNClassifier()

x = torch.randn(8, 5, 3)

output = model(x)
print(output.shape)    # torch.Size([a, b])
# a  → batch size
# b  → number of classes



"----------model training-------------"

# در PyTorch باید Training Loop را خودمان بنویسیم

criterion = nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(model.parameters(), lr=0.001 )

for epoch in range(10):

    optimizer.zero_grad()

    output = model(x_train)

    loss = criterion(output, y_train)

    loss.backward()

    optimizer.step()

    print(loss.item())


# ساختار: 
# Forward Pass
#      ↓
# Prediction
#      ↓
#    Loss
#      ↓
# loss.backward()
#      ↓
#  Gradients
#      ↓
#    Adam
#      ↓
# Update Weights











'''
===========================================================
=======  ⭐  RNN Coding with Tensorflow/Keras  ⭐  =======
===========================================================
'''

"-----------Regression-------------"

import tensorflow as tf

x = tf.random.normal((2, 5, 3))

rnn = tf.keras.layers.SimpleRNN(4, return_sequences=True, return_state=True )

output, hidden = rnn(x)

print("Output shape:", output.shape)
print("Hidden shape:", hidden.shape)


# چرا TensorFlow شکل Hidden را متفاوت نشان می‌دهد؟
# Pytorch
    # hidden:
    # (1, batch, hidden_size)
    # (1, 2, 4)

# Tensorflow:
    # hidden:
    # (batch, hidden_size)
    # (2, 4)

# چون PyTorch یک dimension اضافی برای number of layers در hidden دارد



"-----------classification-------------"

import tensorflow as tf

model = tf.keras.Sequential([

    tf.keras.layers.SimpleRNN(16, input_shape=(5, 3)),

    tf.keras.layers.Dense(2)
])

model.summary()


# ساختار:
# Input
# (5, 3)
#   ↓
# SimpleRNN
# hidden_size = 16
#   ↓
# Dense
# 2 neurons
#   ↓
# Output



"----------model training-----------"

model.compile(
    optimizer="adam",
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=["accuracy"]
)

model.fit(x_train, y_train, epochs=10, batch_size=32)











'''
=================================================================================
=======  ⭐  Coding differences between Tensorflow/Keras and Pytorch ⭐  =======
=================================================================================
'''

# |  concept  |       PyTorch         |           TensorFlow             |
# | --------- | --------------------- | -------------------------------- |
# | RNN       | nn.RNN                | SimpleRNN                        |
# | Dense     | nn.Linear             | Dense                            |
# | Optimizer | torch.optim.Adam      | optimizer="adam"                 |
# | Loss      | nn.CrossEntropyLoss() | SparseCategoricalCrossentropy()  |
# | Training  | Usually manual Loop   | model.fit()                      |
# | Tensor    | torch.Tensor          | tf.Tensor                        |











'''
===========================================================
=======  ⭐  RNN concepts, Stock price example ⭐  =======
===========================================================
'''

# ما فرض میکنیم در دیتای ما که مربوط به قیمت سهام هست، الگوها به این 4 حالتی هست که در پایین وجود دارد
# ما میخوایم با RNN یک شبکه عصبی بسازیم که با دیتای روز قبل، امروز و فردا رو پیشبینی کنه

#   High |
# Medium |
#    Low |─────────────────────-------- prediction 
#       ─▼──────────▼──────────▼──────
#     Yesterday  [Today]    Tomorrow
# (حالت اول): اگه دیروز قیمت ثابت پایین بوده، امروز و فردا هم ثابت پایین میمونه


#   High |─────────────────────-------- prediction
# Medium |
#    Low |  
#       ─▼──────────▼──────────▼──────
#     Yesterday  [Today]    Tomorrow
# (حالت دوم): اگه دیروز قیمت ثابت بالا بوده، امروز و فردا هم ثابت بالا میمونه


#   High |                   /--------- prediction
# Medium |       /──────────/
#    Low |──────/ 
#       ─▼──────────▼──────────▼──────
#     Yesterday  [Today]    Tomorrow
# (حالت سوم): اگه دیروز قیمت رو به رشد بوده، امروز و فردا هم رشد میکنه میره بالا


#   High |──────\
# Medium |       \_________
#    Low |                 \--------- prediction
#       ─▼──────────▼──────────▼──────
#     Yesterday  [Today]    Tomorrow
# (حالت چهارم): اگه دیروز قیمت رو به سقوط بوده، امروز و فردا هم سقوط میکنه میاد پایین




#                      Tomorrow         W2
#                  Recurrent loop     *-0.5
#                         ┌────────────────┐   
#                         |                |
#                         |                |
#                 W1      ▼   B1      _____|_____      W3       B3
#   [Input] --> *1.8 --> Sum +0.0 --> |Z = relu | --> *1.1 --> +0.0 --> [Output]
#  yesterday                          -----------                        Today
                                                                       W3   B3
               W1    B1                         ____ masire 1 =>  0 * 1.1 + 0.0 = 0   output=0 (today)
0=input   0 * 1.8 + 0.0 = 0 -> relu(0)=0  -----|____ masire 2 =>  0 * -0.5(W2) + 0.0 = 0 --> relu(0)=0 --> 0 * 1.1 + 0.0 = 0   output=0
 yesterday                                                         Recurrent      B1                            W3    B3        tomorrow

# این input=0 که دادیم درواقع دیتای yesterday بوده
# اینجا masire 1 با استفاده از دیتای yesterday میاد برای today پیشبینی میکنه
# حالا اون recurrent loop میاد با استفاده از خروجی Activation function برامون دیتای tomorrow رو پیشبینی میکنه
# خروجی Activation function از دیتای today بدست اومده
# پس masire 2 میشه همون پیشبینی برای  tomorrow ولی با استفاده از دیتای today

# اینجا دیتایی که برای loop استفاده کردیم یه memory از گذشته بود (hidden state)
# این hidden state ها باعث میشن که در داخل یک شبکه چندین لایه بهم پیوسته تشکیل بشه که وزن‌های یکسان دارن (weight sharing)











'''
=========================================
=======  ⭐  RNN limitations ⭐  =======
=========================================
'''

# ویژگی RNN این بود که در هر مرحله اطلاعاتی از مراحل قبلی را در یک متغیر به نام Hidden State نگه می‌دارد
# هر Hidden State اطلاعاتی از ورودی فعلی و حالت قبلی را ترکیب می‌کند
# مشکل اینجاست که RNN معمولی برای حفظ اطلاعات خیلی دور در یک دنباله، با دشواری‌هایی روبه‌رو می‌شود

# محدودیت‌های مهم آن عبارت‌اند از:
#  محدودیت اول -> Vanishing Gradient: گرادیان‌ها هنگام برگشت به مراحل قبلی بسیار کوچک می‌شوند و یادگیری وابستگی‌های دور سخت می‌شود
# محدودیت دوم -> Exploding Gradient: گرادیان‌ها هنگام برگشت بسیار بزرگ می‌شوند و آموزش ناپایدار می‌شود
# محدودیت سوم -> پردازش ترتیبی: معمولاً نمی‌توان تمام مراحل زمانی یک دنباله را به‌صورت موازی پردازش کرد؛ بنابراین آموزش می‌تواند کند باشد
# محدودیت چهارم -> حافظهٔ محدود برای وابستگی‌های طولانی: Hidden State باید اطلاعات مفید گذشته را نگه دارد؛ با طولانی شدن دنباله، ممکنه بعضی اطلاعات از دست برن



"✅ What is gradient?"
# فرض کن مدل یک جمله را پردازش می‌کند، پیش‌بینی اشتباهی انجام می‌دهد و در نتیجه مقدار Loss یا خطای مدل زیاد می‌شود
# مدل باید بفهمد وزن‌هایش را چطور تغییر دهد تا خطا کمتر شود. گرادیان به ما می‌گوید خطا نسبت به یک پارامتر چقدر و در چه جهتی تغییر می‌کند

# به زبان ساده:
# اول Forward Pass: داده وارد مدل می‌شود و پیش‌بینی تولید می‌شود
# سپس Loss: میزان خطا محاسبه می‌شود
# بعدش Backpropagation: گرادیان‌ها محاسبه می‌شوند تا مشخص شود پارامترها چطور باید اصلاح شوند
# در انتها Optimizer: وزن‌ها را با استفاده از گرادیان‌ها به‌روزرسانی می‌کند

# در RNN، گرادیان باید از مراحل زمانی آخر به مراحل قبلی برگردد. این فرایند Backpropagation Through Time (BPTT) نام دارد
# دقیقاً در همین مسیر برگشت است که مشکل Vanishing یا Exploding Gradient رخ می‌دهد



"✅ Vanishing gradient"
# یعنی گرادیان هنگام برگشت در شبکه، آن‌قدر کوچک شود که وزن‌های لایه‌ها یا مراحل قبلی تقریباً دیگر یاد نگیرند

# فرض کن می‌خواهیم یک RNN جمله‌ای طولانی را پردازش کند:
# The book that I bought several years ago was surprisingly good.
# برای درک درست جمله، مدل باید بتواند اطلاعات مربوط به book را تا قسمت‌های بعدی حفظ کند
# اما هنگام آموزش، گرادیان برای اصلاح وزن‌های مراحل قبلی باید از تعداد زیادی مرحله عبور کند
# اگر در هر مرحله مقداری کوچک‌تر شود، بعد از مراحل زیاد تقریباً صفر می‌شود

# مثلا فرض کنیم گرادیان در هر مرحله در عدد 0.5 ضرب شود. در انتها تقریبا برابر 0 میشه
# البته در یک RNN واقعی مقدار تغییر گرادیان به وزن‌ها و activation function بستگی دارد
# تعداد مراحل برگشت      مقدار گرادیان  
#  0.5                         1
#  0.25                        2
#  0.03125                     5 
#  0.000977                    10
#  0.000000954                 20 

# چرا این اتفاق می‌افتد؟
# در RNN، محاسبات مراحل زمانی به یکدیگر وابسته‌اند. هنگام Backpropagation، گرادیان از طریق این محاسبات به عقب منتقل می‌شود
# اگر مشتق‌ها و ضرایب مؤثر در این مسیر بارها در مقادیر کوچک ضرب شوند، گرادیان می‌تواند به‌شدت کاهش یابد
# مثلا، توابع فعال‌سازی مثل sigmoid در بخش بزرگی از دامنهٔ خود مشتق کوچک دارند. تکرار این اثر در یک دنبالهٔ طولانی می‌تواند مشکل را شدیدتر کند

# نتیجهٔ Vanishing Gradient چیست؟
# فرض کن مدل باید یاد بگیرد که یک کلمه در ابتدای جمله، معنای کلمه‌ای را که ۵۰ مرحله بعد می‌آید تغییر می‌دهد
# اگر گرادیان به مراحل اولیه نرسد، وزن‌های مربوط به آن مراحل به‌اندازهٔ کافی اصلاح نمی‌شوند. بنابراین، مدل ممکن است نتواند وابستگی‌های طولانی را خوب یاد بگیرد
# نکته: Vanishing Gradient به این معنی نیست که مدل هیچ چیزی یاد نمی‌گیرد؛ مشکل این است که یادگیری وابستگی‌های دور دشوار می‌شود

# راهکار جلوگیری از vanishing gradient چیه؟؟
# راهکار خاصی وجود نداره، این محدودیت در ذات RNN هست و برای حل کردنش باید از سایر معماری ها مثل LSTM یا GRU استفاده بشه



"✅ Exploding gradient"
# در این حالت برعکس Vanishing gradient، مقدار گرادیان هنگام Backpropagation به‌شدت بزرگ می‌شود

# فرض کن یک RNN در حال یادگیری وابستگی بین کلمات یک متن طولانی است
# این بار، به‌جای ضرب شدن در اعداد کوچک، گرادیان در هر مرحله در عدد 2 ضرب می‌شود
# تعداد مراحل برگشت    مقدار گرادیان   
#    2                        1
#    4                        2
#    32                       5  
#    1,024                    10
#    1,048,576                20

# چرا Exploding gradient مشکل ساز هست؟
# وزن‌ها معمولاً با استفاده از گرادیان به‌روزرسانی می‌شوند. در ساده‌ترین حالت:
    #Wnew​=Wold​−ηg
    # η=learning rate   W=weight   g=gradient
# اگر مقدار گرادیان بسیار بزرگ شود، تغییر وزن نیز ممکن است بیش‌ازحد بزرگ باشد
# نتیجه می‌تواند شامل موارد زیر باشد:
# ممکنه Loss ناگهان بسیار زیاد شود    
# آموزش ناپایدار شود و Loss نوسان شدید داشته باشد    
# وزن‌ها مقادیر بسیار بزرگی پیدا کنند    
# محاسبات به NaN یا Inf برسند و آموزش شکست بخورد    


"-------Gradient clipping---------"
# یکی از روشهای رایج برای جلوگیری از Exploding Gradient هست
# این روش گرادیان را محدود می‌کند تا اندازهٔ آن از یک حد مشخص بیشتر نشود
# مثلاً اگر اندازهٔ گرادیان از حد تعیین‌شده بیشتر باشد، جهت آن حفظ می‌شود اما اندازه‌اش کاهش می‌یابد

#### Gradient clipping in pytorch  #####
# اینجا max_norm=1.0 یعنی اندازهٔ کلی گرادیان پارامترها محدود می‌شود
# این روش می‌تواند از به‌روزرسانی‌های بیش‌ازحد بزرگ جلوگیری کند، اما تضمین نمی‌کند که همهٔ مشکلات آموزش حل شوند
# این قطعه فقط بخش آموزش را نشان می‌دهد؛ متغیرهای model، inputs و labels باید قبلاً تعریف شده باشند

import torch
import torch.nn as nn

# Assume model and optimizer have already been created.
criterion = nn.CrossEntropyLoss()
optimizer.zero_grad()

# Forward pass
outputs = model(inputs)
loss = criterion(outputs, labels)

# Backpropagation through time
loss.backward()

# Limit the gradient norm
torch.nn.utils.clip_grad_norm_(
    model.parameters(),
    max_norm=1.0  )

# Update model parameters
optimizer.step()



















