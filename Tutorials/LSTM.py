
'''
===============================================================================
===============================================================================
================       Created on Wed Oct  7 23:48:59 2026     ================
================                IDE: Spyder                    ================
================         Author: Khashayar Alipour             ================
================           LSTM (Long Short Term Memory)       ================
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
#       MLP     CNN     RNN
#                    ┌───┴──┐
#                    ↓      ↓
#                ⭐LSTM   GRU




#✅ Why LSTM?
#✅ LSTM structure (Time step / Cell state / Gates)
#✅ Complete calculation of a full LSTM time step with real numbers
#✅ LSTM time step codes with Numpy
#✅ LSTM codes with Pytorch
#✅ LSTM codes with Tensorflow/Keras





'''
====================================
=======  ⭐  Why LSTM?  ⭐  =======
====================================
'''

# در RNN معمولی با ورود دیتا یه Hidden state تولید میشه و اطلاعات از مرحله 1 تا آخر (output) از طریق hs منتقل میشه
# وقتی یک forward pass انجام میشه، بعدش backpropagation داریم. برای آپدیت کردن loss نیازه که ...
# ... از output برگردیم تا به hidden state اول. و در طول این مسیر hs ها روی همدیگر ضرب میشن
# درواقع برای پیدا کردن output در معماری RNN ما خیلی به hs وابسته هستیم
# مجبور هستیم که در کل مسیر backpropagation کل وزن و بایاس ها در هم ضرب و جمع بشن
# بنابراین اگر مقدار گرادیان خیلی زیاد یا خیلی کم باشه، با عمیق شدن شبکه و زیاد شدن تعداد لایه ها ...
# ... در نهایت ممکنه به جایی برسیم که گرادیان خیییلی بزرگ یا تقریبا 0 میشه و گرادیان شبکه از دست میره
# در نتیجه یادگیری مختل میشه

# در معماری LSTM وابستگی مطلق به hs از بین رفته و برای مسیر backpropagation ما یک مسیر دیگری در دسترس داریم
# اینجوری دیگه مجبور نیستیم همه hs هارو دونه دونه بروی همدیگه ضرب کنیم
# در واقع LSTM علاوه بر Hidden State، یک مسیر حافظهٔ جداگانه به نام Cell State هم دارد و با Gateها جریان اطلاعات را کنترل می‌کند







'''
============================================
=======  ⭐  LSTM Architecture  ⭐  =======
============================================
'''
# چهار مفهوم پایه برای درک معماری LSTM وجود داره: 
    # Time step - Input - Hidden state - Cell state

"✅ 1-Time step"
# در یک دنباله، هر بخش از داده یک گام زمانی محسوب می‌شود
# مثلاً جملهٔ زیر را در نظر بگیر:    I love machine learning
# می‌توانیم هر کلمه را یک Time Step در نظر بگیریم:
    #x1=I   x2=love   x3=machine   x4=learning
# معماری LSTM کلمات را به‌ترتیب دریافت می‌کند و وضعیت حافظه‌اش را در هر گام به‌روزرسانی می‌کند

"✅ 2-Input"
# ورودی در گام زمانی t را با Xt نشان می‌دهیم.
# ورودی می‌تواند موارد مختلفی باشد:
# یک بردار Embedding از یک کلمه    
# ویژگی‌های یک تصویر یا فریم    
# دمای ثبت‌شده توسط سنسورها    
# قیمت یا حجم معاملات در یک زمان مشخص    

"✅ 3-Hidden state"
# با Ht نشان داده می‌شود
 # درواقع HS اطلاعاتی است که سلول در گام جاری به شبکهٔ بعدی یا گام زمانی بعد منتقل می‌کند
 # این بردار همچنین برای تولید خروجی مدل استفاده می‌شود
# در معماری LSTM این hidden state ها نقش working/current representation (short term memory) رو دارن

"✅ 4-Cell state"
# این بخش، مسیر حافظهٔ داخلی LSTM است که برای حفظ و به‌روزرسانی اطلاعات در طول دنباله طراحی شده است
# نکتهٔ مهم: Cell State یک حافظهٔ شبیه فایل یا دیتابیس نیست؛ یک بردار عددی است که مقادیرش در هر گام زمانی تغییر می‌کنند
# در معماری LSTM این cell state ها نقش long term memory path رو دارن


"⭐ Gates ⭐"
# در ساختار LSTM ما چند نوع Gate داریم که اینها مجموعه‌ای از محاسبات هستند که تعیین می‌کنند اطلاعات با چه شدتی عبور کند
# یک Gate معمولاً از ترکیب ورودی فعلی و Hidden State قبلی، یک بردار تولید می‌کند که مقادیرش بین صفر و یک هستند
# برای این کار معمولاً از تابع Sigmoid استفاده می‌شود

# ورودی Sigmoid        خروجی تقریبی     
#       0.007                  -5
#       0.119                  -2
#       0.5                     0
#       0.881                   2
#       0.993                   5

# برای درک ساده، می‌توانیم خروجی Sigmoid را مثل یک کنترل‌کنندهٔ میزان عبور اطلاعات در نظر بگیریم:
# نزدیک 0: تقریباً هیچ اطلاعاتی عبور نمی‌کند    
# نزدیک 1: تقریباً تمام اطلاعات عبور می‌کند    
# نزدیک 0.5: اطلاعات تا حدی عبور می‌کند    
# این مقادیر به‌صورت خودکار از طریق آموزش یاد گرفته می‌شوند؛ ما معمولاً از قبل تعیین نمی‌کنیم که Gate چه چیزی را حذف یا حفظ کند

"✅ 1-Forget Gate"
# این Gate تعیین می‌کند هر بخش از Cell State قبلی چه مقدار باقی بماند
# فرض کن مدل در حال پردازش این جمله باشد:
# I used to live in Berlin, but now I live in Munich.
# اطلاعات مربوط به Berlin ممکن است در بعضی مراحل مفید باشد، اما در مراحل بعدی اطلاعات Munich اهمیت بیشتری پیدا کند

# فرمولش اینه:
    # Fₜ​=σ(Wf*​Xₜ​ + Uf*​Hₜ₋₁ ​+ Bf​)
    # Fₜ = میزان حفظ اطلاعات قبلی
    # Xₜ= ورودی فعلی
    # Wf-Uf= ماتریس های وزن
    # Hₜ₋₁ = previous hidden state
    # Bf = بایاس

# مثلاً اگر یکی از مؤلفه‌های Forget Gate برابر 0.1 باشد، همان مؤلفه از حافظهٔ قبلی فقط با ضریب 0.1 در به‌روزرسانی حافظه شرکت می‌کند
# اگر مقدار آن 0.95 باشد، بخش زیادی از آن مؤلفه حفظ می‌شود
# درواقع Forget Gate لزوماً یک تصمیم صفر و یک نمی‌گیرد؛ معمولاً کنترل پیوسته‌ای بین صفر و یک دارد

"✅ 2-Input Gate"
# این Gate مشخص می‌کند چه مقدار اطلاعات جدید وارد Cell State شود
# فرض کن جمله این باشد:    I live in Munich and work at Google
# با رسیدن به عبارت work at Google مدل ممکن است بخواهد اطلاعات تازه‌ای دربارهٔ شغل فرد را وارد حافظه کند
# چجوری اون وسط اطلاعات تازه وارد میشه؟ دقیقا همینجا کار Input gate مشخص میشه

# درواقع Input Gate دو بخش اصلی دارد:
# 1-تعیین میزان ورود اطلاعات جدید    
# 2-تولید محتوای پیشنهادی برای اضافه شدن به حافظه    

# ابتدا input gate را محاسبه میکنیم:
    # Iₜ​=σ(Wi*​Xₜ ​+ Ui*​Hₜ₋₁ ​+ Bi​)
    # Iₜ=  چه مقدار از اطلاعات جدید وارد شود؟

# سپس محتوای کاندید را میسازیم:
    # Cₜ​=tanh(Wc*​Xₜ ​+ Uc​*Hₜ₋₁ ​+ Bc​)
    # Cₜ=   چه اطلاعاتی برای اضافه شدن پیشنهاد شده است؟
    # اینجا Cₜ هنوز حافظهٔ نهایی نیست؛ محتوای کاندیدی است که با Input Gate ترکیب می‌شود    
    # تابع tanh خروجی را در محدودهٔ منفی یک تا مثبت یک قرار می‌دهد    
    
"✅ 3-Output Gate"
# این Gate مشخص می‌کند چه مقدار از حافظهٔ داخلی برای ساخت Hidden State فعلی استفاده شود
# فرض کن مدل اطلاعاتی دربارهٔ چند موضوع در Cell State خود دارد، اما برای پیش‌بینی بعدی فقط بخشی از این اطلاعات لازم باشد
# درواقع Output Gate میزان استفاده از اطلاعات حافظه در خروجی فعلی را کنترل می‌کند

# فرمولش اینه:
    # Oₜ​=σ(Wo*​Xₜ ​+ Uo*​Hₜ₋₁ ​+ Bo​)

# سپس Hidden State جدید محاسبه می‌شود:
    # Hₜ​=Oₜ​⊙tanh(Cₜ​)
    # علامت ⊙ یعنی ضرب عنصر به عنصر دو بردار    

# در نتیجه، Hidden State خروجی‌ای است که از حافظهٔ فعلی به‌دست می‌آید، اما مقدار آن با Output Gate کنترل می‌شود



"⭐ How Cell state is updated ⭐"
# حالا که سه Gate را شناختیم، می‌توانیم مهم‌ترین فرمول LSTM را بنویسیم. این فرمول قلب حافظهٔ LSTM است:
    # Cₜ=Fₜ⊙Cₜ₋₁ + Iₜ⊙C^ₜ
# دو بخش دارد:
    # Fₜ⊙Cₜ₋₁​  -> بخشی از حافظهٔ قبلی که باقی می‌ماند
    # Iₜ⊙C^ₜ   -> بخشی از اطلاعات جدید که وارد حافظه می‌شود
# بنابراین:
# حافظهٔ جدید = اطلاعات قدیمیِ حفظ‌شده + اطلاعات جدیدِ انتخاب‌شده    

# Former Cell state (Cₜ₋₁)
#          ▼
#  Forget gate (Fₜ⊙Cₜ₋₁)    ->  حافظهٔ قبلی را با میزان مناسب حفظ می‌کند
#          ▼
# اطلاعات کاندید جدید (C^ₜ)   
#          ▼
#   Input gate (Iₜ⊙C^ₜ)     -> اطلاعات تازه را با میزان مناسب وارد می‌کند
#          ▼
# New cell state (Cₜ=Fₜ⊙Cₜ₋₁ + Iₜ⊙C^ₜ)

# در RNN معمولی، Hidden State در هر مرحله با استفاده از ورودی و Hidden State قبلی ساخته می‌شود
# در LSTM ولی فرق داره. اینجا Cell State مسیر جداگانه‌ای برای حفظ و ترکیب اطلاعات دارد
# این مسیر می‌تواند در بعضی شرایط انتقال گرادیان را بهتر کند و به همین دلیل LSTM معمولاً ...
#... در یادگیری وابستگی‌های طولانی از RNN ساده بهتر عمل می‌کند
# بااین‌حال، این موضوع تضمین نمی‌کند که هر دنبالهٔ طولانی بدون مشکل یاد گرفته شود



#                    OLD MEMORY
#                        Cₜ₋₁
#                         │
#                         ▼
#                    Forget Gate (moadele) --> softmax [0.3 ,0.8 , 0.9]
#                         │
#                         ▼
#                   Keep useful part
#                         │
#                         │
#                         ├───────────┐
#                                     │
#  xₜ + hₜ₋₁                           +
#     │                               │
#     ├────► Input Gate ─────┐        │
#     │                      │        │
#     └────► Candidate ──────×────────┘
#                                     │
#                                     ▼
#                                     Cₜ
#                               NEW MEMORY



#          Previous Cell State
#                  Cₜ₋₁
#                   │
#                   ▼
#          ┌─────────────────┐
#  xₜ ────►│                  │────► hₜ
#          │      LSTM       │
#   hₜ₋₁ ─►│                  │────► Cₜ
#          └─────────────────┘










'''
=========================================================================================
=======  ⭐  Complete calculation of a full LSTM time step with real numbers ⭐  =======
=========================================================================================
'''
# حالا یک مثال عددی کوچک بررسی می‌کنیم تا ببینی Gateها واقعاً چطور روی حافظه اثر می‌گذارند
# برای ساده بودن محاسبات، فرض می‌کنیم Cell State و Hidden State فقط یک عدد دارند

# مقادیر فرضی در یک گام زمانی:
# این مقادیر را صرفاً برای مثال انتخاب کرده‌ایم؛ در مدل آموزش‌دیده، Gateها از محاسبات شبکه به‌دست می‌آیند
# حافظهٔ قبلی=0.8 (Cₜ₋₁)    
    # former Hidden State=0.2  (Hₜ₋₁)
    # Forget Gate=0.75 (Fₜ)
    # Input Gate=0.4 (Iₜ)
# محتوای کاندید جدید=0.5 (C^ₜ)    
    # Output Gate=0.6 (Oₜ)

" Cₜ=Fₜ⊙Cₜ₋₁ + Iₜ⊙C^ₜ "

# گام اول: حفظ حافظهٔ قبلی
    # Fₜ⊙Cₜ₋₁ -> 0.75×0.8=0.6
# پس 0.6 از حافظهٔ قبلی به حافظهٔ جدید منتقل می‌شود    

# گام دوم: اضافه کردن اطلاعات جدید
    # Iₜ⊙C^ₜ -> 0.4×0.5=0.2
# یعنی 0.2 از محتوای کاندید جدید وارد حافظه می‌شود    

# گام سوم: ساخت Cell State جدید
    # Cₜ -> 0.6+0.2=0.8
    # پس حافظهٔ جدید برابر 0.8 است    

# گام چهارم: ساخت Hidden State جدید
    # ابتدا  tanh(0.8)≈0.664    
# سپس  Hₜ=0.6×0.664≈0.398    


# در پایانِ این Time step:
    # متغیر        مقدار        
    #    0.8       new cell state (Cₜ)
    #   ≈0.398     new hidden state (Hₜ)

# این محاسبات در هر Time Step تکرار می‌شوند
# در step بعدی Cₜ و Hₜ به‌عنوان حافظه و وضعیت قبلی استفاده خواهند شد











'''
=========================================================
=======  ⭐  LSTM time step codes with Numpy ⭐  =======
=========================================================
'''
#  در این قسمت فقط می‌خواهیم یک Time step در LSTM را با فرمول‌های numpy اجرا کنیم
# در این پیاده‌سازی، وزن‌ها تصادفی هستند و هیچ آموزش یا Backpropagation انجام نمی‌شود
# در یک مدل واقعی، وزن‌ها با داده‌های آموزشی و الگوریتم بهینه‌سازی یاد گرفته می‌شوند

# علامت @ برای ضرب ماتریسی است
# علامت * در اینجا ضرب عنصر به عنصر دو آرایه است
# هر Gate از ورودی فعلی و Hidden State قبلی محاسبه می‌شود
# c_t  => حافظهٔ جدید را می‌سازد
# h_t  => خروجی داخلی جدید را تولید می‌کند

import numpy as np

# Activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

# Example dimensions
input_size = 2
hidden_size = 3

# Random input and previous states
rng = np.random.default_rng(42)

x_t = rng.normal(size=(input_size, 1))
h_prev = rng.normal(size=(hidden_size, 1))
c_prev = rng.normal(size=(hidden_size, 1))

# Weights and biases for the four transformations
W_f = rng.normal(size=(hidden_size, input_size))
U_f = rng.normal(size=(hidden_size, hidden_size))
b_f = np.zeros((hidden_size, 1))

W_i = rng.normal(size=(hidden_size, input_size))
U_i = rng.normal(size=(hidden_size, hidden_size))
b_i = np.zeros((hidden_size, 1))

W_c = rng.normal(size=(hidden_size, input_size))
U_c = rng.normal(size=(hidden_size, hidden_size))
b_c = np.zeros((hidden_size, 1))

W_o = rng.normal(size=(hidden_size, input_size))
U_o = rng.normal(size=(hidden_size, hidden_size))
b_o = np.zeros((hidden_size, 1))

# 1. Forget gate
f_t = sigmoid(W_f @ x_t + U_f @ h_prev + b_f)

# 2. Input gate
i_t = sigmoid(W_i @ x_t + U_i @ h_prev + b_i)

# 3. Candidate cell state
c_candidate = tanh(W_c @ x_t + U_c @ h_prev + b_c)

# 4. Output gate
o_t = sigmoid(W_o @ x_t + U_o @ h_prev + b_o)

# 5. Update cell state
c_t = f_t * c_prev + i_t * c_candidate

# 6. Calculate new hidden state
h_t = o_t * tanh(c_t)


print("Input shape:", x_t.shape)
print("Forget gate:\n", f_t)
print("Input gate:\n", i_t)
print("Output gate:\n", o_t)
print("New cell state:\n", c_t)
print("New hidden state:\n", h_t)











'''
=================================================
=======  ⭐  LSTM codes with Pytorch ⭐  =======
=================================================
'''
# فرض کن می‌خواهیم بر اساس پنج مقدار متوالی، مقدار بعدی یک سری زمانی را پیش‌بینی کنیم
# مثلا ورودی‌ها می‌توانند مقادیر ثبت‌شدهٔ یک سنسور باشند بنابراین برای شروع، یک دیتاست مصنوعی می‌سازیم

# شکل داده‌ها در PyTorch
# وقتی batch_first=True باشد، شکل ورودی به nn.LSTM به این صورت است:
    # (batch size,sequence length,input size)

# برای مثال، شکل (32, 5, 1) یعنی:
# ۳۲ نمونه در یک Batch    
# ۵ گام زمانی برای هر نمونه    
# ۱ ویژگی در هر گام زمانی    


"✅--------  1-Creating Model and dataset  ------------✅"

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

# Reproducibility
torch.manual_seed(42)
np.random.seed(42)

# Create a synthetic time series
t = np.arange(0, 500, dtype=np.float32)
series = np.sin(0.05 * t) + 0.1 * np.sin(0.2 * t)

# Normalize the series
mean = series.mean()
std = series.std()
series = (series - mean) / std

# Create input sequences and next-step targets
sequence_length = 20

X, y = [], []

for i in range(len(series) - sequence_length):
    X.append(series[i:i + sequence_length])
    y.append(series[i + sequence_length])

X = np.array(X, dtype=np.float32)
y = np.array(y, dtype=np.float32)

# Shape: [samples, sequence_length, features]
X = torch.tensor(X).unsqueeze(-1)
y = torch.tensor(y).unsqueeze(-1)

# Split chronologically: do not shuffle before splitting
split = int(0.8 * len(X))

X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

train_dataset = TensorDataset(X_train, y_train)
train_loader = DataLoader(
    train_dataset,
    batch_size=32,
    shuffle=True  )


# Define the LSTM model
class LSTMRegressor(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_size=32):
        super().__init__()

        self.lstm = nn.LSTM(
            input_size=1,   # input_size=embedding_dim
            hidden_size=hidden_size,
            num_layers=1,
            batch_first=True )

        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        output, (h_n, c_n) = self.lstm(x)       # output, (hidden, cell)

        # Use the final hidden state of the last layer
        last_hidden = h_n[-1]

        # Predict the next value (Regression)
        prediction = self.fc(last_hidden)

        return prediction


model = LSTMRegressor()

criterion = nn.MSELoss()
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001  )

print(model)
print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)


# در این قسمت output, (h_n, c_n) = self.lstm(x)  سه خروجی مهم داریم:
# اول -> output: خروجی Hidden State در تمام time stepها    
# دومی -> h_n: آخرین Hidden State هر لایه    
# سومی -> c_n: آخرین Cell State هر لایه    

# برای مدل ما با یک لایه و hidden_size=32:
# اول -> output شکل (batch_size, 20, 32) دارد    
# دوم -> h_n شکل (1, batch_size, 32) دارد    
# سوم -> c_n نیز شکل (1, batch_size, 32) دارد    

# به همین دلیل در کد از h_n[-1] استفاده کردیم تا Hidden State نهایی آخرین لایه را بگیریم



"✅-------   2-Training the Model  ---------✅"

epochs = 30

for epoch in range(epochs):
    model.train()
    total_loss = 0.0

    for X_batch, y_batch in train_loader:
        # 1. Clear previous gradients
        optimizer.zero_grad()

        # 2. Forward pass
        predictions = model(X_batch)

        # 3. Calculate loss
        loss = criterion(predictions, y_batch)

        # 4. Backpropagation through time
        loss.backward()

        # 5. Optional protection against exploding gradients
        nn.utils.clip_grad_norm_(
            model.parameters(),
            max_norm=1.0
        )

        # 6. Update weights
        optimizer.step()

        total_loss += loss.item() * len(X_batch)

    average_loss = total_loss / len(train_loader.dataset)

    if (epoch + 1) % 5 == 0:
        print(
            f"Epoch {epoch + 1}/{epochs}, "
            f"Loss: {average_loss:.4f}"
        )


# Evaluate on the held-out time period
model.eval()

with torch.no_grad():
    predictions = model(X_test)

test_loss = criterion(predictions, y_test).item()

print("Test MSE:", test_loss)




"✅-------   3-Predictions  ---------✅"

import matplotlib.pyplot as plt

model.eval()

with torch.no_grad():
    predictions = model(X_test).squeeze(-1).numpy()

actual = y_test.squeeze(-1).numpy()

plt.figure(figsize=(12, 5))
plt.plot(actual, label="Actual")
plt.plot(predictions, label="LSTM prediction")
plt.title("LSTM: Next-Step Time-Series Prediction")
plt.xlabel("Test sample")
plt.ylabel("Normalized value")
plt.legend()
plt.grid(True)
plt.show()











'''
==========================================================
=======  ⭐  LSTM codes with Tensorflow/Keras ⭐  =======
==========================================================
'''
# همان مسئله‌ای که با Pytorch حل کردیم، این بار با Tensorflow حل میکنیم

# نکته: این کد از API استاندارد Keras استفاده می‌کند. برای داده‌های زمانی واقعی، تقسیم Train/Test و ....
#... اعتبارسنجی باید با دقت انجام شود تا اطلاعات آینده به‌طور ناخواسته وارد آموزش نشود
# اگر دادهٔ واقعی داشتیم، بهتر است پیش‌پردازش و مقیاس‌بندی نیز فقط بر اساس داده‌های Train تنظیم شود


import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

tf.keras.utils.set_random_seed(42)

# Generate synthetic time-series data
t = np.arange(0, 500, dtype=np.float32)
series = np.sin(0.05 * t) + 0.1 * np.sin(0.2 * t)

# Normalize
mean = series.mean()
std = series.std()
series = (series - mean) / std

sequence_length = 20

X, y = [], []

for i in range(len(series) - sequence_length):
    X.append(series[i:i + sequence_length])
    y.append(series[i + sequence_length])

X = np.array(X, dtype=np.float32)[..., np.newaxis]
y = np.array(y, dtype=np.float32)

# Chronological split
split = int(0.8 * len(X))

X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]


# Build the model
model = tf.keras.Sequential([
    tf.keras.Input(shape=(sequence_length, 1)),
    tf.keras.layers.LSTM(32),
    tf.keras.layers.Dense(1)   ])

model.compile(
    optimizer="adam",
    loss="mse",
    metrics=["mae"]  )

model.summary()

# Train
history = model.fit(
    X_train,
    y_train,
    epochs=30,
    batch_size=32,
    shuffle=True,
    validation_split=0.1,
    verbose=1   )

# Evaluate
test_loss, test_mae = model.evaluate(
    X_test,
    y_test,
    verbose=0    )

print("Test MSE:", test_loss)
print("Test MAE:", test_mae)

# Predict
predictions = model.predict(X_test, verbose=0).squeeze()

plt.figure(figsize=(12, 5))
plt.plot(y_test, label="Actual")
plt.plot(predictions, label="LSTM prediction")
plt.title("LSTM Time-Series Prediction")
plt.xlabel("Test sample")
plt.ylabel("Normalized value")
plt.legend()
plt.grid(True)
plt.show()













'''
==========================================
=======  ⭐  LSTM Limitations ⭐  =======
==========================================
'''
# مدل LSTM نسبت به RNN معمولی حافظهٔ کنترل‌شده‌تری دارد، اما بی‌نقص نیست
# 1-محاسبات ترتیبی: گام‌های زمانی به هم وابسته‌اند، پس آموزش آن معمولاً به‌اندازهٔ Transformerها قابلیت موازی‌سازی ندارد    
# 2-هزینهٔ محاسباتی: چند Gate و محاسبات اضافی نسبت به RNN ساده دارد    
# 3-وابستگی‌های بسیار طولانی: می‌تواند آن‌ها را بهتر مدیریت کند، اما حفظ تمام اطلاعات در دنباله‌های بسیار طولانی تضمین‌شده نیست    
# 4-نیاز به داده و تنظیم مناسب: انتخاب اندازهٔ Hidden State، Learning Rate، طول دنباله و سایر پارامترها روی نتیجه اثر می‌گذارد    
# 5-مشکل Exploding Gradient: هنوز ممکن است رخ دهد؛ به همین دلیل Gradient Clipping در بسیاری از پروژه‌ها مفید است    































































































































