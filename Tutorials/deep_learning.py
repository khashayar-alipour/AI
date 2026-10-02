
'''
===============================================================================
===============================================================================
================       Created on Fri Sep 11 12:50:30 2026     ================
================                IDE: Spyder                    ================
================         Author: Khashayar Alipour             ================
================                AI Deep Learning               ================
===============================================================================
===============================================================================
'''

#✅ 1-Activation functions:
         # ReLu
         # Leaky Relu
         # Linear/Identity
         # Sigmoid
         # Tanh
         # ELU
         # GELU
         # Softmax
    
#✅ 2-Layers:
         # Input layer
         # Hidden layers
         # output layer

#✅ 3-Data feeding:
        # Batch / Full-Batch
        # Mini-Batch
        # Stochastic / Online
    
#✅ 4-Epoch

#✅ 5-Types of loss function:
        # MSE (Mean squared error)
        # MAE (Mean absolute error)
        # Binary Cross Entropy (BCE)
        # Categorial Cross Entropy (CCE)

#✅ 6-Optimizer:
        # SGD
        # SGD + Momentum
        # AdaGrad
        # RMSProp
        # adam
        # adamW

#✅ 7-MLP(Multi Layer Perceptron):
        # MLPclassifier
        # MLPregressor
        # solver

#✅ 8-MLP real example

#✅ 9-Special and specific libraries for deep learning:
        # Tensorflow
        # Keras
        # MNIST dataset
        # Pytorch





# ANN = Artificial Neural Network



'''
===============================================
=======  ⭐  Activation functions  ⭐  =======
===============================================
'''

 # چرا Activation Function لازم است؟

# x₁ ── w₁ ──┐
# x₂ ── w₂ ──┤
# x₃ ── w₃ ──┤──→  z  ──→ Activation Function ──→ Output
#            │
#            b ──┘

# ابتدا هر نورون ورودی‌ها را با وزن‌ها ترکیب می‌کند:     z = w_1x_1+w_2x_2+w_3x_3+b
# بعد activation function روی z اعمال می‌شود:     a=f(z)
# پس Activation Function تعیین می‌کند خروجی نورون، بعد از ترکیب ورودی‌ها، چه مقداری باشد

# حالا اگه Activation function نباشه چی میشه؟
# حتی اگر 10 لایه هم بسازیم، کل شبکه در نهایت فقط یک تبدیل خطی خواهد بود    y=ax+b
# یعنی شبکه نمی‌تواند روابط پیچیده و غیرخطی را یاد بگیرد
# درواقع af باعث میشه شبکه بتواند non-linear patterns را یاد بگیرد



"----------------------------------------------"
"   ⭐  Types of activation functions   ⭐    "
"----------------------------------------------"
# ___________________________________________________________________
# | Function   |        کاربرد رایج       |           ایده اصلی    |
# |------------|-----------------------------|-----------------------|
# | Linear     |       بدون تغییر           | Regression output     |
# | Sigmoid    |       خروجی 0 تا 1         | Binary classification |
# | Tanh       |      خروجی -1 تا 1    |      شبکه‌های قدیمی‌تر      |
# | ReLU       |       مقادیر منفی → 0      |   Hidden layers       |
# | Leaky ReLU | منفی‌ها کاملاً حذف نمی‌شوند   |   Hidden layers       |
# | Softmax    |     احتمال بین چند کلاس    |   Multiclass output    |
# --------------------------------------------------------------------


"---------------------------------------"
"✅ linear/Identity activation function"
"---------------------------------------"
# ساده ترین نوع af هست. هر چیزی وارد شود همان خارج می‌شود:      f(x)=x
# -5 → -5
#  0 →  0
#  3 →  3

# در کل identity بیشتر در regression کاربرد دارد

# در sklearn
MLPRegressor(activation="identity")

        y
       ↑   /    
       |  /
       | /
       |/
-------|------- → x
       |
       |
              


"----------------------------------------"
"✅ Sigmoid/Logistic activation function"
"----------------------------------------"
# f(x) = 1 / (1 + e⁻ˣ)
# یعنی نتیجه بین 0 و 1 هست
# پس خروجی normalize شده هست

              y
              ↑
              1   
              |  ───────────
              | /
              |/
              / 0.5
             /|
            / |
-∞  ───────/--|------------ ∞  → x
              0


# یکی از معروف‌ترین activation functions است
# هر ورودی را به محدوده 0 تا 1 میبره
# input:   -∞ ───────── 0 ───────── +∞
# output:   0 ───────── .5 ───────── 1

# x = -10 → 0.000
# x =  -2 → 0.119
# x =   0 → 0.500
# x =   2 → 0.881
# x =  10 → 1.000

# ازونجایی که با این af می‌توانیم خروجی را به شکل probability تفسیر کنیم، بنابراین برای classification مناسبه. مثلا:
0.92 → high probability  class 1
0.15 → low probability  class 2
# پس برای binary classification کاربردیه

# اما sigmoid یک مشکل دارد. در قسمت‌های خیلی مثبت یا خیلی منفی، شیب sigmoid در نمودار خیلی کوچک می‌شود
# یعنی اگر خروجی نورون خیلی بزرگ باشه، وقتی وارد sigmoid میشه مشتقش تقریبا 0 میشه (روی نمودار خط صاف میشه)
# این می‌تواند باعث vanishing gradient شود
# به همین دلیل امروزه در hidden layerها معمولاً ReLU انتخاب محبوب‌تری است


# در sklearn
# در sklearn اسم sigmoid را مینویسیم logistic
MLPRegressor(activation="logistic")

#----------------------------
# رسم نمودار:
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

y_sigmoid = sigmoid(x)

plt.figure(figsize=(7, 5))
plt.plot(x, y_sigmoid, label="Sigmoid")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.xlabel("x")
plt.ylabel("Sigmoid(x)")
plt.title("Sigmoid Activation Function")
plt.grid(True)
plt.legend()
plt.show()
#----------------------------



"----------------------------"
"✅ Tanh activation function"
"----------------------------"
# f(x) = tanh(x)    همون تانژانت هست
# همون sigmoid هست با این تفاوت که عدد خروجی بین 1 و 1- هست
               y
               ↑
               |   
             1 |  ─────────────
               | /
               |/
-∞  -----------/------------ +∞  → x
              /|0
             / |
────────────/  | -1
               |
               |
    
# خروجی آن بین 1- تا 1 هست. یعنی:
# input:  -∞ ───── 0 ───── +∞
# output: -1 ───── 0 ───── +1

# همچنین tanh(0) = 0

# اما tanh همون مشکل sigmoid را دارد. در قسمت‌های خیلی مثبت یا خیلی منفی، شیب نمودار خیلی کوچک می‌شود
# یعنی اگر عدد خروجی نورون خیلی بزرگ باشه، وقتی وارد tanh میشه مشتقش تقریبا 0 میشه (روی نمودار خط صاف میشه)
# این می‌تواند باعث vanishing gradient شود


# در sklearn
MLPRegressor(activation="tanh")


#-------------------------
# رسم نمودار:
import numpy as np
import matplotlib.pyplot as plt

def tanh(x):
    return np.tanh(x)

# Generate x values
x = np.linspace(-5, 5, 500)

# Calculate Tanh
y = tanh(x)

# Plot
plt.figure(figsize=(7, 5))
plt.plot(x, y, label="Tanh")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.xlabel("x")
plt.ylabel("Tanh(x)")
plt.title("Tanh Activation Function")
plt.grid(True)
plt.legend()
plt.show()
#-------------------------



"----------------------------"
"✅ ReLu activation function"
"----------------------------"
# این AF در سال 2014 برای حل مشکل Sigmoid و tanh اومد و ازون موقع انتخاب پیش فرض برای af در کتابخوانه‌ها شد
               y
               ↑
               1   
               |      /
               |     /
               |    /
               |   /
               |  /
               | /
               |/
-10 ───────────/------------ 10  → x
               0

# f(x)=max(0,x) فرمولش اینه
# یعنی:
# اگر x <= 0   ->  پس  output = 0  میشه
# اگر x > 0   ->   پس   output = x میشه

x       ReLU(x)
-5  →     0
-2  →     0
-1  →     0
 0  →     0
 1  →     1
 3  →     3
 7  →     7


# چرا ReLU محبوب است؟  چون بسیار ساده است:
negative → 0
positive → unchanged
# و در مقایسه با sigmoid/tanh در بخش مثبت، گرادیان آن به شکل ساده‌تری رفتار می‌کند
# پس مشکل vanishing gradient رو حل کرده و به همین دلیل در hidden layers شبکه‌های عصبی بسیار رایج است

# با این‌وجود، ReLU خودش مشکلاتی هم داره
# اگر یک نورون همیشه مقدارش منفی باشه، نه تنها خروجی 0 هست، همچنین گرادیان هم 0 هست
# پس مشکل dead neuron داریم و درواقع اون نورون کلا میمیره
# پس اون قسمت از شبکه کلا نمیتونه یادگیری انجام بده و مرده حساب میشه
# برای حل این مشکل اومدن گفتن قبل از صفر دیگه شیب نمودار 0 مطلق نباشه
# به اینصورت Variant های مختلفی از ReLU درست شد تا مشکل drying ReLU رو حل کنن. مثلا:
    # leaky relu, ELU, GeLu, SiLu, Swish, ...


# در sklearn
MLPRegressor(activation="relu")


#---------------------
# رسم نمودار:
import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0, x)

x = np.linspace(-5, 5, 500)
y_relu = relu(x)

plt.figure(figsize=(7, 5))
plt.plot(x, y_relu, label="ReLU")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.xlabel("x")
plt.ylabel("ReLU(x)")
plt.title("ReLU Activation Function")
plt.grid(True)
plt.legend()
plt.show()
#--------------------



"----------------------------------"
"✅ Leaky ReLu activation function"
"----------------------------------"
# f(x) = max(αx, x)

# یکی از مشکلا ReLu اینه: x < 0 → 0
# یعنی نورون ممکن است برای ورودی‌های منفی همیشه خروجی صفر بدهد
# ولی Leaky ReLu برای بخش منفی یک شیب کوچک نگه می‌دارد

# برای مقدار x هایی که کمتر مساوی 0 هست اومدهیه ضریب آلفا (α) درنظر گرفته
# که از صفر شدن شیب اونها جلوگیری میکنه

f(x)={ x x>0   αx x≤0​

# مثلا اگه α=0.01 باشه:
#  x       Leaky ReLU
# -5  →   -0.05
# -2  →   -0.02
# -1  →   -0.01
#  0  →    0
#  1  →    1
#  3  →    3

# در sklearn
MLPClassifier(activation="leaky_relu")    # این معتبر نیست
# در sklearn هیچ estimator بنام leaky_relu نداریم


#-----------------------------
# رسم نمودار:
import numpy as np
import matplotlib.pyplot as plt

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

# Generate x values
x = np.linspace(-5, 5, 500)

# Calculate Leaky ReLU
y = leaky_relu(x)

# Plot
plt.figure(figsize=(7, 5))
plt.plot(x, y, label="Leaky ReLU")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.xlabel("x")
plt.ylabel("Leaky ReLU(x)")
plt.title("Leaky ReLU Activation Function")
plt.grid(True)
plt.legend()
plt.show()
#----------------------------------



"-----------------------------------------------------"
"✅ ELU (Exponential Linear Unit) activation function"
"-----------------------------------------------------"
# برای x < 0 برخلاف ReLU که صفر می‌شود، مقدار منفی و نرم تولید می‌کند
# حتی smooth تر از leaky relu هست
# وقتی x خیلی منفی شود، خروجی ELU به -α نزدیک می‌شود
# x > 0  --> output = x
# x = 0  --> output = 0
# x < 0  --> output approaches -alpha

# فرمول:
#            x                  if x > 0
# ELU(x) = {
#            α * (e^x - 1)       if x <= 0
# معمولا α = 1 درنظر گرفته میشه

#----------------------------------
# رسم نمودار ELU:
import numpy as np
import matplotlib.pyplot as plt

# ELU function
def elu(x, alpha=1):
    return np.where(x > 0, x, alpha * (np.exp(x) - 1))

# Generate x values
x = np.linspace(-5, 5, 500)
# Calculate ELU
y = elu(x)
# Plot
plt.plot(x, y, label="ELU")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.xlabel("x")
plt.ylabel("ELU(x)")
plt.title("ELU Activation Function")
plt.grid(True)
plt.legend()
plt.show()
#---------------------------------



"---------------------------------------------------------"
"✅ GELU (Gaussian Error Linear Unit) activation function"
"---------------------------------------------------------"
# در معماری‌های مدرن مثل Transformerها بسیار استفاده می‌شود؛ مثلاً در BERT و بسیاری از مدل‌های زبانی
# برای xهای مثبت، تقریباً همان مقدار را عبور می‌دهد و برای xهای منفی، به‌تدریج آن‌ها را سرکوب می‌کند

# فرمول اصلی:
GELU(x)=xΦ(x)
# اینجا Φ(x) تابع توزیع تجمعی نرمال استاندارد است

# یک فرمول معروف دیگر GELU این هست:
GELU(x) = x/2 * (1 + erf(x / sqrt(2)))

# رفتار GELU
# x >> 0  --> GELU(x) ≈ x
# x << 0  --> GELU(x) ≈ 0
# x = 0   --> GELU(x) = 0
# در واقع GELU بطور smooth کنترل میکنه که چه مقدار از x باید از activation عبور کنه


#-------------------------
# رسم نمودار:
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

# GELU function
def gelu(x):
    return 0.5 * x * (1 + erf(x / np.sqrt(2)))

# Generate x values
x = np.linspace(-5, 5, 500)

# Calculate GELU
y = gelu(x)

# Plot
plt.plot(x, y, label="GELU")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.xlabel("x")
plt.ylabel("GELU(x)")
plt.title("GELU Activation Function")
plt.grid(True)
plt.legend()
plt.show()
#----------------------



"------------------------------"
"✅ Softmax activation function"
"------------------------------"
# مخصوص multi-class classification

# برعکس بقیه af ها که در hidden layers استفاده میشن، این در output layer استفاده میشه

# فرض کن شبکه برای سه کلاس این خروجی خام را تولید کرده:
class 0 → 2.5
class 1 → 1.0
class 2 → 0.2
# این اعداد مستقیما probability نیستند
# بلکه Softmax آنها را به probabilityهایی تبدیل می‌کند که مجموعشان 1 باشد
class 0 → 0.75
class 1 → 0.18
class 2 → 0.07

# پس میتوانیم بگوییم:
Class 0: 75%
Class 1: 18%
Class 2:  7%
# این برای multiclass classification بسیار مهم است


#      z₁      z₂      z₃
#      ↓       ↓       ↓
#    ┌─────────────────────┐
#    │       Softmax       │   Output layer
#    └─────────────────────┘
#      ↓       ↓       ↓
#      P₁      P₂      P₃
#       ┌────┬────┬────┐
#       │0.7 │0.2 │0.1 │
#       └────┴────┴────┘
#         P₁ + P₂ + P₃ = 1
        
        
# در sklearn
activation="softmax"   # این اسم معتبر نیست
# برای softmax هم مثل leark relu اسمی نداریم و sklearn بخش خروجی classification را خودش مدیریت می‌کند

#------------------------------
# رسم نمودار:
import numpy as np
import matplotlib.pyplot as plt

def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / np.sum(exp_x)

# Example logits
logits = np.linspace(-5, 5, 100)

# Calculate Softmax
y_softmax = softmax(logits)

plt.figure(figsize=(7, 5))
plt.plot(logits, y_softmax, label="Softmax")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.xlabel("Logit")
plt.ylabel("Softmax Probability")
plt.title("Softmax Function")
plt.grid(True)
plt.legend()
plt.show()
#----------------------------










"---------------------------------------------------------------------------"
"   ⭐    ANN Layers:  Input layer - Hidden layers - output layer    ⭐    "
"---------------------------------------------------------------------------"

#                Neural Network
                     
#Input Layer       Hidden Layer        Output Layer          
#   x₁  ● ───────→  ●
#                   │
#   x₂  ● ───────→  ● ───────→  ● y
#                   │
#   x₃  ● ───────→  ●
#                   │
#   x₄  ● ───────→  ●

✅ Input layer
# این لایه ویژگی‌های (Features) داده را دریافت می‌کند
# مثلا اگه در یک دیتا 4 تا feature داشته باشیم، 4 تا نورون ورودی خواهیم داشت

✅ Hidden layer
# اینجا جایی است که شبکه الگوهای موجود در داده را یاد می‌گیرد
# تعداد hidden layer رو خودمون میتونیم مشخص کنیم

✅ Output layer
# در classification به تعداد class ها نورون خروجی داریم
# در regression یه نورون خروجی داریم  که یک عدد هست










"-------------------------------------"
"   ⭐  ANN Data feeding Types ⭐    "
"-------------------------------------"

# بطور کلی Data feeding یعنی وارد کردن داده‌های آموزشی به شبکه عصبی تا شبکه بتواند از آن‌ها یاد بگیرد
# مثلا فرض کنیم 1000 تا نمونه داریم
# شبکه باید این داده‌ها را دریافت کند، Forward Pass انجام دهد، خطا را محاسبه کند و سپس وزن‌هایش را به‌روزرسانی کند

# بطور کلی 3 روش مهم برای Data feeding داریم که فرقشون اینه که در هر مرحله چندتا دیتا وارد شبکه بشه:
    # 1. Batch / Full-Batch
    # 2. Mini-Batch
    # 3. Stochastic / Online


"----------------------"
✅ Full-Batch feeding
"----------------------"
# در این روش کل دیتاست یکجا وارد شبکه میشه
# سپس یک دور تا آخر میره و loss محاسبه میشه
# دوباره weight آپدیت میشه و کل دیتاست باز وارد شبکه میشه

# مزیت این روش محاسبات دقیق هست ولی مصرف منابع خیلی زیادی میخواد

#     Dataset = 1000 samples
#             ↓
# ┌─────────────────────────┐
# │ Sample 1                │
# │ Sample 2                │
# │ Sample 3                │
# │ ...                     │
# │ Sample 1000             │
# └─────────────────────────┘
#             ↓
#        Neural Network



-------------------------------
✅ Stochastic / Online Feeding
-------------------------------
# در این روش هر بار فقط یک نمونه وارد شبکه می‌شود
# درواقع batch size = 1 هست
# این روش می‌تواند باعث شود به‌روزرسانی‌ها سریع ولی پرنوسان‌تر باشند

# Sample 1 → Network → Update
# Sample 2 → Network → Update
# Sample 3 → Network → Update
# Sample 4 → Network → Update
#   ...



----------------------
✅ Mini-Batch Feeding
----------------------
# این روش در Deep learning رایج تر است
# در این روش دیتاست را به گروه‌های کوچک‌تر (batch) تقسیم می‌کنیم
# هر batch میره توی شبکه و یه دور pass forward میشه که به این چرخه iteration میگن
# سپس loss محاسبه میشه و weight update انجام میشه
# در مرحله بعد batch بعدی وارد میشه و ... تا اینکه دیتاست تموم بشه

# Dataset = 1000 samples
# Batch 1 → 100 samples  → Network  → Loss  → Update
# Batch 2 → 100 samples  → Network  → Loss  → Update
# ...    ...      ...        ...       ...     ...
# Batch 10 → 100 samples  → Network  → Loss  → Update

# در اینجا batch size = 100 هست








"---------------------"
"   ⭐  Epoch  ⭐    "
"---------------------"

# هر Epoch یعنی شبکه کل دیتاست آموزشی رو یکبار دیده باشه

# مثلا اگه تعداد نمونه ما 1000 تا باشه و 10 تا batch داشته باشیم که هرکدوم 100 تا نمونه دارن
# پس یک epoch شامل این میشه که 10 دور (هر دور یک batch) وارد شبکه بشه و دیده بشه
# پس پروسه training ممکنه در چندین epoch انجام بشه

# اگه بگیم Epochs = 5 پس شبکه کل دیتاست رو 5 بار میبینه
# Epoch 1 → 10 batches
# Epoch 2 → 10 batches
# Epoch 3 → 10 batches
# Epoch 4 → 10 batches
# Epoch 5 → 10 batches
# در مجموع    5 × 10 = 50 updates


# Number of Batches per Epoch = Number of Training Samples / Batch Size
# 1000 samples
# Batch Size = 100
# 1000 / 100 = 10 batches per epoch











'''
==================================================
=======  ⭐  Types of loss functions  ⭐  =======
==================================================
'''
# در عمل، شبکه عصبی برای شروع به کارش میاد random initialization انجام میده
# یعنی بصورت تصادفی میاد یه سری مقدار برای weight و bias در نظر میگیره
# سپس یه دور تا آخر میره و خروجی رو محاسبه میکنه
# حالا این پیشبینی میتونه در ابتدا اشتباه باشه. پس شبکه عصبی از کجا باید بفهمه اشتباه کرده؟
# در واقع loss function ابزاری هست که به شبکه عصبی کمک میکنه واقعیت رو با پیشبینی مقایسه کنه
# درواقع Loss Function به مدل میگه «چقدر اشتباه کردی؟» تا در زمان آموزش، وزن‌ها طوری تغییر کنن که این خطا کمتر بشه

# به اولین باری که دیتای ورودی میره توی شبکه و تا آخر پردازش میشه و خروجی میاد بیرون feed forward میگن
# در انتهای feed forward، مقدار خروجی که بدست اومده مقدار خطاش محاسبه میشه
# سپس عملیات back propagation شروع میشه
# مقدار error در جهت برعکس به داخل نورون ها فرستاده میشه
# با توجه به وزن‌ها (وزن ها سهم هر نورون از error رو تعیین میکنن)، مقدار gradient برای هر error محاسبه میشه
# حالا این مقدار مشتق (گرادیان) رو بر وزن تقسیم میکنه و اینجوری در جهت کاهش loss حرکت میکنه
# به تدریج (شدتش براساس learning rate مشخص میشه) این loss کم میشه و مقادیر update میشه
# اینقد ادامه میدیم تا به کمترین مقدار loss برسیم
# اینجوری optimize ترین weight و bias بدست میاد

# در عمل loss میاد اختلاف واقعیت با مقدار پیشبینی شده رو محاسبه میکنه
# حالا اگه regression باشه از MSE و MAE استفاده میکنه
# اگه classification باشه از BCE و CCE استفاده میکنه


"----------------------------"
# ✅ MSE (Mean Square Error)
"----------------------------"

# MSE = (1/n) * Σ(yi - ŷi)²

# مقدار پیشبینی رو از واقعی کم میکنه و به توان 2 میرسونه
# این توان 2 باعث میشه خطاهای بزرگ را شدیدتر جریمه کنه

# y = 10
# ŷ = 7
# 10 - 7 = 3
# 3² = 9


"----------------------------"
# ✅ MAE (Mean absolute error)
"----------------------------"

# تفاوت اصلی با MSE این است که به‌جای مربع کردن خطا، قدر مطلق خطا را می‌گیرد
# در نتیجه MAE نسبت به خطاهای خیلی بزرگ (outlier)، نسبت به MSE حساسیت کمتری دارد

# MSE = (1/n) * Σ|yi - ŷi|

# Actual = 10
# Prediction = 7
# Error = 3
# MAE = |3| = 3


"----------------------------"
# ✅ Binary Cross Entropy (BCE)
"----------------------------"

# برای Binary Classification استفاده می‌شود؛ یعنی وقتی فقط دو کلاس داریم. مثلا:
# Spam / Not Spam
# Cat / Dog
# Disease / No Disease
# 0 / 1

# معمولاً مدل در خروجی یک احتمال بین 0 و 1 تولید می‌کند، مثلاً:
# Prediction = 0.9
# یعنی مدل احتمال کلاس 1 را 90٪ می‌داند

# متود BCE زمانی جریمه زیادی می‌دهد که مدل با اعتماد بالا پیش‌بینی اشتباه کند
# BCE = (-1/n) * Σ[ yi * log(ŷi)   +   (1-yi) * log(1-ŷi) ]

# yi  = Actual label (0 or 1)
# ŷi  = Predicted probability


"----------------------------"
# ✅ Categorial Cross Entropy
"----------------------------"

# برای Multi-Class Classification استفاده می‌شود؛ یعنی بیشتر از دو کلاس داریم. مثلا در تشخیص تصویر:
# Cat      0.70
# Dog      0.20
# Horse    0.08
# Bird     0.02
# در مورد بالا اگر جواب واقعی Cat باشد، Categorical Cross Entropy مقدار loss نسبتاً کمی خواهد داشت

# اما اگر مدل اینجوری پیشبینی کنه:
# Cat      0.01
# Dog      0.90
# Horse    0.07
# Bird     0.02
# در حالی که جواب واقعی Cat است، loss زیادی می‌گیرد

# # CCE = -Σ[yi * log(ŷi)]
# y = مقدار واقعی
# ŷ = احتمال پیش‌بینی‌شده توسط مدل











'''
=============================================
=======  ⭐  Types of optimizer  ⭐  =======
=============================================
'''
# اصلا optimizer چه کاری انجام میده؟
# در شبکه عصبی، ما یک Loss داریم که می‌گوید مدل چقدر اشتباه کرده
# درواقع Optimizer با استفاده از Gradient تصمیم می‌گیرد وزن‌های شبکه را چطور تغییر دهد تا Loss کمتر شود
# فرمولش اینه:        Weight_new = Weight_old - η*gradient
# η=learning rate

# یعنی Loss میگه چقدر اشتباه کردی
# سپس Gradient میگه در چه جهتی اشتباه کردی
# سپس Optimizer تصمیم میگیره چطور وزن‌ها را تغییر بده

# نکته مهم اینه که optimizer با loss function برابر نیست
# Model -> Prediction -> Loss Function -> Gradient / Backpropagation -> Optimizer -> Update Weights -> Model بهتر
# یعنی Loss مقدار اشتباه را اندازه می‌گیرد، Backpropagation گرادیان را حساب می‌کند، و Optimizer از آن گرادیان برای تغییر وزن‌ها استفاده می‌کند


"-------------------------------------"
"✅ SGD (Stochastic Gradient Descent) "
"-------------------------------------"

# ساده ترین نوع optimizer هست که فرمولش اینه:
    # Weight_new = Weight_old - η*gradient
    # η=learning rate

# مشکل SGD اینه که همیشه با یک Learning Rate ثابت حرکت می‌کنه
# در نتیجه ممکنه مشکلاتی واسش پیش بیاد. مثلا:
# حرکتش به سمت minimum کند باشه
# در مسیر نوسان داشته باشه
# در بعضی شرایط سخت بهینه‌سازی، آموزش طولانی بشه

# pytorch
torch.optim.SGD(...)



"-------------------"
"✅ SGD + momentum "
"-------------------"

# ایده‌ی Momentum شبیه اضافه کردن حافظه به SGD است.
# به‌جای اینکه فقط Gradient فعلی را در نظر بگیریم، بخشی از حرکت قبلی را هم حفظ می‌کنیم

# فرمول:
# Vt​=βVt−1​+gt​    β = معمولا 0.9     g=gradient
# Wt+1​=Wt​−ηV     η = learning rate   

# در نتیجه اگر Gradientها چند مرحله پشت سر هم در یک جهت باشند، Momentum سرعت حرکت را بیشتر می‌کند
# درواقع SGD -> گرادیان حرکت فعلی
# ولی SGD + momentum -> گرادیان حرکت فعلی + حرکت قبلی = حرکت جدید
# این کار معمولاً باعث حرکت روان‌تر و سریع‌تر در مسیر بهینه‌سازی می‌شود

# مشکل اینه که خیلی وقتا ما بجای پیدا کردن global minima، داخل local minima گیر میوفتیم
# برای اینکه داخل local minima گیر نکنیم باید یه سرعت و شتاب مناسب داشته باشیم
# تا وقتی رفت توی minima بتونیم ازش خارج بشیم وگرنه اگه سرعت خیلی کم باشه کلا اونجا گیر میکنیم
# پس باید داخل update formula خودمون یک فرمولی بزاریم که سرعت و شتاب مناسب بهمون بده
# به این مجموع سرعت و شتاب میگن momentum

# pytorch
import torch
torch.optim.SGD(
    model.parameters(), 
    lr=0.01, 
    momentum=0.9)



"--------------------------------"
"✅ AdaGrad (Adaptive Gradient) "
"--------------------------------"

# ایده اصلی پشتش اینه که Learning Rate برای هر پارامتر می‌تواند متفاوت باشه
# پارامترهایی که Gradientهای بزرگ‌تری داشته‌اند، به مرور Learning Rate مؤثر کوچک‌تری می‌گیرند

# مزیت این روش اینه که Learning Rate را به‌صورت تطبیقی (dynamic) برای پارامترهای مختلف تنظیم می‌کنه
# مشکلش اینه که گرادیان همیشه در حال جمع شدن هست:
    # G = gradient² + gradient² + gradient² + ...

# بنابراین ممکن است Learning Rate مؤثر به مرور خیلی کوچک شود و آموزش تقریباً متوقف شود
# به همین دلیل روش‌های بعدی مثل RMSProp توسعه پیدا کردند

# pytorch
torch.optim.Adagrad(...)



"------------"
"✅ RMSProp "
"------------"

# این الگوریتم برای حل مشکل AdaGrad اومد
# الگوریتم AdaGrad یه history از گرادیان های قبلی جمع میکنه که باعث میشه گرادیان کلی اینقد بزرگ بشه که lr مجبور بشه خیلی کوچیک بشه
# ولی RMSProp دیگه اینکارو نمیکنه. بجای اینکه کلی گرادیان بیاد Accumulate کنه میاد تعداد محدودی گرادیان جمع میکنه
# درواقع یک میانگین نمایی متحرک از مربع Gradientها نگه می‌داریم
# با وجود این forgetting mechanism دیگه از بزرگ شدن بیش از حد گرادیان جلوگیری میکنه
# درنتیجه learning rate قابل کنترل تر میشه

# pytorch
torch.optim.RMSprop(...)



"-------------------------------------"
"✅ Adam (Adaptive Moment Estimation) "
"-------------------------------------"

# ترکیبی از momentum و RMSProp هست
# یعنی هم:
# میانگین Gradientها را دنبال می‌کنه
# میانگین مربع Gradientها را دنبال می‌کنه

# چرا Adam محبوب است؟
# چون هم Momentum دارد و هم Learning Rate تطبیقی

# pytorch
torch.optim.adam(...)



"-----------"
"✅ AdamW  "
"-----------"
# الگوریتم AdamW بسیار شبیه Adam است، اما یک تفاوت مهم در نحوه‌ی اعمال Weight Decay دارد
# امروزه transformer model های مدرن مثل BERT و GPT و ... از مدل جدید AdamW استفاده میکنن

# ایده پشتش اینه:
    # Adam + Weight Decay جداشده از به‌روزرسانی Gradient

# در Adam معمولی، Weight Decay معمولاً به شکل L2 regularization وارد Gradient می‌شود
# اما AdamW آن را به‌صورت decoupled weight decay جداگانه اعمال می‌کند

# pytorch
torch.optim.AdamW(...)














"--------------------------------------------"
"   ⭐  Multi Layer Perceptron (MLP)  ⭐    "
"--------------------------------------------"

# برای ساخت شبکه عصبی مصنوعی (ANN) معماری (architecture) های مختلفی وجود داره که یکیش MLP هست
# Artificial Neural Network (ANN) architecture
#  ├── MLP
#  ├── CNN
#  ├── RNN
#  ├── LSTM
#  ├── Transformer
#  └── ...

# ساختار ANN که توسط MLP ساخته میشه یکی از این دو حالته:
# فقط یک hidden layer داشته باشیم:     Input → Hidden → Output
# اگر چند hidden layer داشته باشیم:    Input → Hidden 1 → Hidden 2 → Hidden 3 → Output

# در واقع MLP یک Feedforward Neural Network میباشد
# یعنی اطلاعات به طور معمول در یک جهت حرکت می‌کنند
# و به عقب برنمی‌گردند تا مثلاً اطلاعات زمانی را نگه دارند
# بطور کلی MLP شبکه‌ای از نورون‌های کاملاً متصل است که با عبور داده از چند لایه
# و محاسبه Loss و سپس Backpropagation و به‌روزرسانی Weightها، الگوهای موجود در داده را یاد می‌گیرد


✅ حالا MLP چطوری کار میکنه؟

# هر نورون این اتفاق واسش میوفته
# هر input یک weight داره که در همدیگه ضرب میشن و میره توی نورون
# حالا مثلا اگر 4 تا ورودی باشه، 4 تا x*w میره به نورون
# سپس این x*w ها با هم جمع میشن که میشه weighted sum
# این weighted sum با یک bias جمع میشه که به حاصلش میگیم z
# این z عملیاتی توسط Activation function روش انجام میشه
# سپس نتیجه ای که حاصل میشه به نورون لایه بعدی در hidden layer بعدی پاس داده میشه

x₁*w₁ ──┐
x₂*w₂ ──┤                      activation function
x₃*w₃ ──┼──→ Neuron 1 + bias ──────[a = f(z)]───────→ hidden layer 2
x₄*w₄ ──┘
      z = w₁x₁ + w₂x₂ + w₃x₃ + w₄x₄ + b


✅ Training process of MLP
# Training Data → Input Layer → Hidden Layer → Output Layer → Prediction → Loss → Backpropagation → Weight Update → دوباره آموزش


-----------
✅ sklearn
-----------

# MLPClassifier
# برای classification کاربرد داره
# Input → MLP → Class

# MLPRegresor
# برای regression کاربرد داره
# Input → MLP → Numerical Value

from sklearn.neural_network import MLPClassifier

model = MLPClassifier(
    hidden_layer_sizes=(10,),
    activation="relu",
    batch_size=32,
    max_iter=1000,
    random_state=42  )

model.fit(X_train, y_train)

# hidden_layer_sizes=(10,)
# Input → 10 Neurons → Output
#       |hidden layer|

# hidden_layer_sizes=(10,20)
# Input → 10 Neurons → 20 Neurons → Output
#         |----Hidden layer------|

# batch_size = 32
# یعنی داده‌های Training به گروه‌های 32تایی پردازش می‌شوند


----------
✅ solver
----------

# با MLP نوع ساختار شبکه رو میسازیم
# داخل MLP یچیزی بنام Solver داریم که مشخص میکنه این شبکه ای که الان ساختیم داخلش وزن ها و bias چطوری حین آموزش آپدیت بشن

# MLP
# │
# ├── Architecture
# │   ├── Input
# │   ├── Hidden Layer(s)
# │   └── Output
# │
# └── Training
#     └── Solver
#          ↓
#       Update Weights

# در MLPClassifier و MLPRegressor در scikit-learn سه Solver اصلی داریم:
    # 1. lbfgs
    # 2. sgd (Stochastic Gradient Descent)
    # 3. adam (Adaptive Moment Estimation)

# sgd
    # میگه ببین Loss در چه جهتی کمتر می‌شود، سپس Weightها را کمی در آن جهت حرکت بده
# به همراهش یک پارامتر learning_rate هم باید بیاد
# برای دیتاست های بزرگ کاربرد بیشتری داره

# adam
# اینم بر پایه گرادیان نزولی هست ولی تنظیمات تطبیقی بیشتری نسبت به sgd برای آپدیت کردن Weight داره
# در بسیاری از مسائل، Adam انتخاب راحت و رایجی است
# نکته مهم اینکه MLPClassifier بطور پیش فرض از solver=Adam استفاده میکنه

# lbfgs
# در کل یک روش quasi-Newton optimization است که از اطلاعات مربوط به Gradient برای پیدا کردن نقطه مناسب‌تر استفاده می‌کند
# در scikit-learn معمولاً برای دیتاست های کوچک و شبکه های کوچک مناسبه






--------------------
⭐ Real example MLP
--------------------

from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()

x = data.data
y = data.target

x.shape   # (569, 30)   569 samples / 30 features
y.shape   # (569,)      569 samples / 1 output
data.target_names   # output = ['malignant', 'benign']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.2, random_state=42,shuffle=True, stratify=y)


from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPClassifier

model = Pipeline([
    ("scaler",StandardScaler()),
    ("mlp",MLPClassifier(hidden_layer_sizes=(16,8),max_iter=1000, alpha=0.0001, activation="relu", random_state=42, solver="adam", learning_rate_init=0.001))
    ])
# اینجا کاربرد آلفا اینجوریه که هر مقدارش بیشتر باشه -> weight هامون کمتر میشه و میره سمت underfitting
# پس اگر overfitting شدیم باید مقدار آلفا رو افزایش بدیم


model.fit(x_train, y_train)

y_pred = model.predict(x_test)

from sklearn.metrics import accuracy_score
test_score_accuracy = accuracy_score(y_test, y_pred)

print(test_score_accuracy)   # 0.95


#--------------------
#--------------------
# دسترسی به مقادیر weight

mlp = model.named_steps["mlp"]

for i, weights in enumerate(mlp.coefs_):
    print(f"weights layers {i+1}: {weights.shape}")

# weights layers 1: (30, 16)
# weights layers 2: (16, 8)
# weights layers 3: (8, 1)

weights_count = sum(w.size for w in mlp.coefs_)
print(f"weights: {weights_count}")

# weights: 616


#--------------------
#--------------------
# دسترسی به مقادیر bias

mlp = model.named_steps["mlp"]

for i, bias in enumerate(mlp.intercepts_):
    print(f"bias layers {i+1}: {bias}")

# bias layers 1: [ 0.22679169  0.22662303  0.32567108  0.4237957   0.17781801  0.50777457
#  -0.25559919  0.02222865  0.6357842   0.31958382  0.08149843  0.11597043
#   0.14166058 -0.25559884  0.29884946  0.00942322]
# bias layers 2: [ 0.49314144  0.20901928 -0.03755885  0.33259727 -0.13072107 -0.30281112
#   0.19847474  0.33849299]
# bias layers 3: [-0.59949394]

biases_count = sum(b.size for b in mlp.intercepts_)
print(f"biases: {biases_count}")

# biases: 25


#--------------------
#--------------------
# دسترسی به همه پارامترها

print(f"Total parameters: {weights_count + biases_count}")
# Total parameters: 641


#--------------------
#--------------------
# مشاهده و رسم loss در هر step

import matplotlib.pyplot as plt
mlp = model.named_steps["mlp"]

plt.plot(mlp.loss_curve_)
plt.xlabel("Iteration")
plt.ylabel("Loss")
plt.title("Training Loss Curve")
plt.show()


#--------------------
#--------------------
# میخوایم ببینیم چندتا iteration داشتیم

print(f"Number of iterations: {mlp.n_iter_}")
# Number of iterations: 345
# ما حداکثر مقدار iteration روی 1000 گذاشتیم ولی بعد از 345 iteration دیده که مشتق ثابت مونده
# با ثابت شدن مشتق دیگه پروسه آپدیت کردن weight و bias متوقف شده



#--------------------
#--------------------
# حالا اصلا از کجا بفهمیم که عدد hidden_layer_size و activation_function که تعیین کردیم
# بهترین مقادیر ممکن برای مدل ما هست؟؟
# مسئله اینه که ما یا باید دونه دونه حالت هارو بصورت دستی حساب کنیم و accuracy_score همرو باهم مقایسه کنیم
# یا اینکه بیایم grid_search بزنیم روش و خودش بیاد بهترین مقدار رو برامون پیدا کنه

from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

model = Pipeline([
    ("scaler",StandardScaler()),
    ("mlp",MLPClassifier(hidden_layer_sizes=(16,8),max_iter=1000, alpha=0.0001, activation="relu", random_state=42, solver="adam", learning_rate_init=0.001, early_stopping=True))
    ])

param_grid = {
    "mlp__hidden_layer_sizes" : [(16,) ,(32,) ,(32, 16) ,(64, 32)],
    "mlp__activation" : ["tanh", "relu"],
    "mlp__solver" : ["adam", "lbfgs"],
    "mlp__alpha" : [0.0001, 0.001, 0.1],
    "mlp__learning_rate_init": [0.0005, 0.001, 0.01]
    }

grid_search = GridSearchCV(
    estimator = Pipeline,
    param_grid = param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=1,
    verbose=1
    )

grid_search.fit(x_train, y_train)

test_score = grid_search.score(x_test, y_test)

print(f"Best parameters: {grid_search.best_params_}")
print(f"Best scores: {grid_search.best_score_}")
print(f"Test score: {test_score}")












"----------------------------------------------------------------"
"   ⭐  Special and specific libraries for deep learning  ⭐    "
"----------------------------------------------------------------"

# درواقع درسته که sklearn قابلیت اینو داره که باهاش شبکه عصبی بسازیم
# ولی بصورت تخصصی برای اینکار ساخته نشده و خیلی باگ داره
# برای اینکار میایم از این 2 کتابخوانه تخصصی استفاده میکنیم:
    # Tensorflow (keras) -> made by Google
    # Pytorch -> Developed by Facebook



"-----------------------"
✅ Tensorflow Framework
"-----------------------"
# یک فریم ورک متن باز هست که توسط گوگل برای محاسبات عددی و یادگیری ماشین توسعه داده شده
# هدفش ساخت neural network و deep learning models و استفاده از GPU/TPU

# همه داده ها در Tensorflow یک تایپ مشخص بنام tensor دارن که درواقع همون آرایه هست
# پس درواقع Tensorflow یک flow از tensor های ورودی هست که از مرحله input تا آخر جریان پیدا میکنه
x = 5               # tensor martabe 0
x = [1,2,3]         # bordar - tensor 1 bodi - 1D array
x = [[1,2],[3,4]]   # jadval - matrix - tensor 2D - 2D array

# pip install tensorflow

# برای اینکه ببینیم gpu کافی برای run کردن مدل های deep رو داریم یا نه از این دستور استفاده میکنیم
import tensorflow as tf
print(tf.config.list_physical_devices("GPU"))



"----------------"
✅ MNIST dataset
"----------------"
# Modified National Institute of Standards and Technology
# pip install mnist

#   ███
#  █   █
#      █
#     █
#    █
#   █
#  █████

# یک دیتاست مرجع در deep learning هست
# اومدن از دست خط افراد واقعی عکس گرفتن، اعداد 0 تا 9 رو افراد روی کاغذ با دست خطشون نوشتن
# همچنین هر دیتا label خورده (از 0 تا 9)
# مدل باید از روی تصویر تشخیص دهد که این عدد مثلاً 2 است
# درواقع MNIST خودش یک «مدل» نیست؛ یک دیتاست است
# ما از آن برای آموزش و ارزیابی مدل‌های مختلف مثل Logistic Regression، MLP و CNN استفاده می‌کنیم

# هر نمونه یک عکس سیاه و سفید هست که یکم بی‌کیفیته و 28*28 پیکسل هست
# یعنی ما یک ماتریکس 28 در 28 داریم که 784 پیکسل داره
# هر پیکسل یک مقدار شدت روشنایی دارد که معمولاً بین 0 تا 250 هست
# 0 میشه سیاه و 250 میشه سفید

# این دیتاست شامل موارد زیر است:
# 60,000 تصویر برای آموزش (Training)
# 10,000 تصویر برای تست (Test)
# در مجموع 70,000 تصویر

# در mnist مسائل Multiclass Classification رو حل میکنیم
# این دیتاست 10 تا class داره از 0 تا 9
# پس 10 تا x داریم و y میشه جواب ما که همون تصویر هست


from tensorflow.keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_test.shape)
# دیتای تست ما 10000 نمونه داره    (10000, 28, 28)

print(x_train.shape)    # (60000, 28, 28)
# یعنی 60000 تا عکس (ماتریکس) داریم که 28*28 پیکسل هست

# حالا باید این 0 تا 250 رو normalize کنیم یعنی بیاریمش بین عدد 0 تا 1
x_test = x_test / 255.0
x_train = x_train / 255.0






"------------"
✅ Keras API
"------------"
# یک API سطح بالا هست
# وقتی بخوایم با استفاده از tensor ها شبکه عصبی بسازیم مثل این میمونه که با numpy array ها شبکه عصبی بسازیم
# حالا keras اومده همه این پروسه رو بصورت توابع آماده در اختیار ما قرار میده که کار کردن باهاش خیلی آسون میشه

# User -> Keras -> Tensorflow -> Neural network

# وقتی برای دیتاست mnist از مدلهایی مثل MLP استفاده میکنیم، هر ماتریکس ورودی رو flatten میکنیم
# یعنی 28*28 که میشه 784 تا ماتریکس، دونه دونه در یک ردیف پشت سر هم میذاریم
# یعنی 784 تا feature ورودی داریم و در نهایت 10 تا نورون خروجی داریم
# مثلا خروجی اینجوری میشه [0,0,0,1,0,0,0,0,0,0] که این یعنی تصویر عدد 4 هست

import tensorflow as tf
input_layer = tf.keras.layers.Flatten(input_shape=(28,28))

# اگه نمونه ورودی ماتریکس نباشه (مثلا عدد باشه فقط) نیازی به flatten نیست و اینجوری ورودی میدیم:
input_layer = tf.keras.layers.input()

# Input
# 784 neurons
#     ↓
# Hidden Layer
# 128 neurons
#     ↓
# Hidden Layer
# 64 neurons
#     ↓
# Output
# 10 neurons

# Output:
# 0 → 0.01
# 1 → 0.01
# 2 → 0.02
# 3 → 0.03
# 4 → 0.87  →  answer
# 5 → 0.02
# 6 → 0.01
# 7 → 0.02
# 8 → 0.02
# 9 → 0.02


# برای ساخت لایه input از flatten استفاده کردیم
# برای ساخت hidden layer و output layer از Dense استفاده میکنیم
# برای لایه خروجی، تعداد نورون برابر تعداد کلاس های خروجی میذاریم
# برای لایه خروجی Activation رو معمولا softmax میذاریم که نتیجه بصورت درصد احتمالات بیان بشه
hidden_layer_1 = tf.keras.layers.Dense(units=128, activation="relu")   # تعداد نورون های این لایه رو 128 تا مشخص کردیم
output_layer = tf.keras.layers.Dense(units=10, activation="softmax")


# ساخت sequential با keras:
# در نهایت باید همه لایه هایی که ساختیم داخل چیزی بنام Sequential بذاریم
# مثلا ما میخوایم 2 لایه hidden بذاریم و ساختار استانداردش اینجوری میشه:
import tensorflow as tf
model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28,28)),
        tf.keras.layers.Dense(units=128, activation="relu"),
        tf.keras.layers.Dense(units=64, activation="relu"),
        tf.keras.layers.Dense(units=10, activation="softmax")
    ])

# برای دیدن جزئیات مدلی که ساختیم:
model.summary()
# Model: "sequential_1"
# ┌─────────────────────────────────┬────────────────────────┬───────────────┐
# │ Layer (type)                    │ Output Shape           │       Param # │
# ├─────────────────────────────────┼────────────────────────┼───────────────┤
# │ flatten_1 (Flatten)             │ (None, 784)            │             0 │
# ├─────────────────────────────────┼────────────────────────┼───────────────┤
# │ dense_1 (Dense)                 │ (None, 128)            │       100,480 │
# ├─────────────────────────────────┼────────────────────────┼───────────────┤
# │ dense_2 (Dense)                 │ (None, 64)             │         8,256 │
# ├─────────────────────────────────┼────────────────────────┼───────────────┤
# │ dense_3 (Dense)                 │ (None, 10)             │           650 │
# └─────────────────────────────────┴────────────────────────┴───────────────┘
#  Total params: 109,386 (427.29 KB)
#  Trainable params: 109,386 (427.29 KB)
#  Non-trainable params: 0 (0.00 B)


# برای Set کردن compiler
# یعنی میایم optimizer و loss و اینارو برای model تعریف میکنیم
# این کاری که انجام میدیم فقط Set میکنه، مدل train نمیشه
model.compile(
    optimizer = "adam",
    loss = "sparse_categorical_crossentropy",
    metrics = ["accuracy"]
    )


# برای train کردن مدل
# وقتی validation_split=0.2 میذاریم یعنی 20% دیتاست train رو برای Validation نگه دار
# یعنی اگه 60000 تا train dataset داریم از این بین 48000 تارو train میکنه و 12000 تا میره برای Validation
# برای مدل 10 تا epoch هم مشخص کردیم یعنی 10 بار دیتارو بصورت batch میبره توی مدل و back میکنه
history = model.fit(x_train, y_train, epochs=10, batch_size=32, validation_split=0.2)


# اینم نتیجه epoch ها در زمان train شدن مدل
# میبینیم Accuracy از epoch 1 که شروع کردیم از 0.92 رسیده به 0.99
# همچنین مقدار loss همچنان کاهش پیدا کرده و به مقدار کمینه رسیده
Epoch 1/10
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 5s 3ms/step - accuracy: 0.9205 - loss: 0.2703 - val_accuracy: 0.9559 - val_loss: 0.1449
Epoch 2/10
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 4s 3ms/step - accuracy: 0.9657 - loss: 0.1143 - val_accuracy: 0.9688 - val_loss: 0.1004
Epoch 3/10
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 4s 3ms/step - accuracy: 0.9752 - loss: 0.0801 - val_accuracy: 0.9696 - val_loss: 0.0953
Epoch 4/10
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 4s 3ms/step - accuracy: 0.9808 - loss: 0.0594 - val_accuracy: 0.9732 - val_loss: 0.0877
Epoch 5/10
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 4s 3ms/step - accuracy: 0.9851 - loss: 0.0447 - val_accuracy: 0.9664 - val_loss: 0.1141
Epoch 6/10
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 4s 3ms/step - accuracy: 0.9879 - loss: 0.0364 - val_accuracy: 0.9689 - val_loss: 0.1113
Epoch 7/10
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 4s 3ms/step - accuracy: 0.9900 - loss: 0.0308 - val_accuracy: 0.9741 - val_loss: 0.0948
Epoch 8/10
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 5s 3ms/step - accuracy: 0.9920 - loss: 0.0249 - val_accuracy: 0.9705 - val_loss: 0.1187
Epoch 9/10
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 4s 3ms/step - accuracy: 0.9926 - loss: 0.0225 - val_accuracy: 0.9728 - val_loss: 0.1121
Epoch 10/10
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 5s 3ms/step - accuracy: 0.9940 - loss: 0.0187 - val_accuracy: 0.9748 - val_loss: 0.1088


# تا الان مدل روی دیتای train اومد evaluation انجام داد
# حالا میخوایم همین کارو روی دیتای train انجام بدیم
test_loss, test_accuracy = model.evaluate(x_test, y_test)

# اینم نتیجه نهایی برای مقادیر loss و accuracy پس از مشاهده دیتاست test توسط مدل
313/313 ━━━━━━━━━━━━━━━━━━━━ 1s 2ms/step - accuracy: 0.9760 - loss: 0.0977 


# حالا میخوایم با matplotlib از نتیجه train شدن مدل استفاده کنیم و یه نمونه از دیتاست mnist رو مشاهده کنیم
image = x_test[20]
label_image = y_test[20]

import matplotlib.pyplot as plt
plt.imshow(image, cmap="gray")
plt.title(f"Label:{label_image}")
plt.axis("off")
plt.show()


# انجام prediction توسط model
image = x_test[20]
prediction = model.predict(image.reshape(1,28,28))
print(prediction)
# [[2.8630303e-09 1.2854776e-08 1.7006206e-13 2.8064093e-07 8.3097690e-10
#  7.7680973e-08 3.2636905e-16 1.5450674e-04 4.8263299e-08 9.9984503e-01]]

# برای نتیجه اومده 10 تا عدد بهمون داده
# این 10 تا عدد همون 10 تا نورون خروجی هست
# باید بزرگترین عدد بین اینارو پیدا کنیم
import numpy as np
np.argmax(prediction)    # 9

# پس گفته عدد 9 (اخرین عدد) از بقیه بزرگتره
# یعنی یه همچین چیزی داریم    [0,0,0,0,0,0,0,0,0.99]
# پس حالا میایم prediction رو با Actual مقایسه میکنیم ببینیم مدل چطوری پیشبینی کرده
print("prediction: ", np.argmax(prediction))
print("actual: ", y_test[20])
# prediction:  9
# actual:  9


# برای رسم کردن Accuracy ها اینکارو میکنیم:
# در نمودار مشخص میشه که در 10 تا epoch چطوری validation تغییر میکنه و آپدیت میشه
plt.plot(history.history["accuracy"], label="training_accuracy")
plt.plot(history.history["val_accuracy"], label="validation_accuracy")

plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.show()


# برای رسم کردن نمودار آپدیت شدن loss اینکار میکنیم:
plt.plot(history.history["loss"], label="training_loss")
plt.plot(history.history["val_loss"], label="validation_loss")

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.show()


# save/load model
# میتونیم مدلی که ساختیم رو بصورت فایل ذخیره کنیم و هروقت خواستیم وارد و استفاده کنیم
model.save("/Users/C P C/Desktop/new_model.keras")

# load
import tensorflow as tf
address = "/Users/C P C/Desktop/new_model.keras"
model = tf.keras.models.load_model(address)




"-----------------------"
✅ Pytorch Framework
"-----------------------"
# حالا فریم ورک pytorch بهمون اجازه میده که ساخت شبکه عصبی مصنوعی رو بصورت pythonic انجام بده

# pip install torch
# pip install torchvision
# pip install torchaudio

# در pytorch ما 2 تا مفهوم مهم داریم:
    
1-tensor
# مثل tensorflow تمام داده های روی pytorch هم tensor هستن
# اینجا tensor مثل همون np.array هست که قابلیت های بیشتری داره و بجای CPU میتونه روی GPU اجرا بشه
# درکل CPU مثلا میتونه بصورت موازی 5 تا کار سنگین انجام بده
# ولی GPU میتونه مثلا 10000 تا کار سبک بصورت موازی انجام بده که برای شبکه عصبی خیلی کاربردی تره

2-Automatic differentiation (Autograd)
# مهمترین ویژگی pytorch هست
# درواقع pytoch مثل tensorflow خودش مشتق هارو حساب میکنه
# ولی فرق اصلیش اینه که pytoch یک گراف میسازه
# با ویژگی dynamic computation graph کل مراحل عملیاتی که روی x ها انجام میشه رو ذخیره میکنه
# در نتیجه میتونیم هروقت که خواستیم به این مقادیر دسترسی پیدا کنیم



-----------------------------
# MNIST example with pytorch
-----------------------------
# میخوایم با دیتاست mnist با استفاده از فریم ورک pytoch یک شبکه عصبی مصنوعی بسازیم
# توی tensorflow ما میومدیم چیزی بنام Sequential میساختیم و داخلش لایه لایه با dense و اینچیزا میساختیم
# ولی توی pytorch برای ساخت یک ANN باید Class با اسم دلخواه بسازیم

# توی pytorch بجای Dense از Linear استفاده میشه
# فرق دیگش اینه که تعداد لایه هارو باید یه اینصورت بدیم:
    # مثلا بگیم چنتا بوده و میخوایم چنتا بشه. اینجا میگیم 784 تا بوده میخوام بشه 128 تا

# ولی همچنان Flatten مثل tensorflow وجود داره

import torch
import torch.nn as nn   # nn = neural network

class Khashaya_Neural_Network(nn.Module):
    
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.layer1 = nn.Linear(784,128)
        self.layer2 = nn.Linear(128, 64)
        self.output = nn.Linear(64,10)

    def forward(self,x):
        x = self.flatten(x)
        x = torch.relu(self.layer1(x))
        x = torch.relu(self.layer2(x))
        output = self.output(x)
        return output
        # Input → 784 → Linear → 128 → relu → 64 → Linear → 10
        

import torch

if torch.cuda.is_available():
    device = torch.device("cuda")
elif torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")
print("device: ", device)    # cpu


from torchvision import datasets, transforms
transform = transforms.ToTensor()
train_datasets = datasets.MNIST(root="./data", train=True, download=True, transform=transform)
test_datasets = datasets.MNIST(root="./data", train=False, download=True, transform=transform)
# 100%|██████████| 9.91M/9.91M [00:02<00:00, 3.32MB/s]
# 100%|██████████| 28.9k/28.9k [00:00<00:00, 323kB/s]
# 100%|██████████| 1.65M/1.65M [00:00<00:00, 2.36MB/s]
# 100%|██████████| 4.54k/4.54k [00:00<00:00, 3.55MB/s]


print(type(train_datasets))    # <class 'torchvision.datasets.mnist.MNIST'>
print(type(test_datasets))    # <class 'torchvision.datasets.mnist.MNIST'>
print(len(train_datasets))    # 60000
print(len(test_datasets))     # 10000


# ما نمیخوایم کل این 60000 تا دیتا یکجا باهم وارد بشه
# میخوایم بصورت batch وارد بشه
# توی tensorflow میومدیم batch_size رو داخل compile ست میکردیم
# اینجا یه چیزی بنام Data_loader داریم که توش دیتاست رو میریزیم و دونه دونه بهمون دیتارو پس میده
from torch.utils.data import DataLoader
BATCH_SIZE = 64
train_loader = DataLoader(train_datasets, batch_size = BATCH_SIZE, shuffle=True)
test_loader = DataLoader(test_datasets, batch_size = BATCH_SIZE, shuffle=True)


# ساخت model
# ّرای ساخت model هم باید class پایتونی بسازیم

import torch.nn as nn
class MNISTModelKhashayar(nn.Module):
    
    def __init__(self):
        super().__init__()
        
        self.flatten = nn.Flatten()
        
        self.fc1 = nn.Linear(28*28,128)   #forward1
        self.relu1 = nn.ReLU()
        
        self.fc2 = nn.Linear(128, 64)
        self.relu2 = nn.ReLU()
        
        self.fc3 = nn.Linear(64,10)
    
    def forward(self,x):
        x = self.flatten(x)
        
        x = self.fc1(x)
        x = self.relu1(x)
        
        x = self.fc2(x)
        x = self.relu2(x)
        
        x = self.fc3(x)
        
        return x

model = MNISTModelKhashayar()
model = model.to(device)
print(model)
# MNISTModelKhashayar(
#   (flatten): Flatten(start_dim=1, end_dim=-1)
#   (fc1): Linear(in_features=784, out_features=128, bias=True)
#   (relu1): ReLU()
#   (fc2): Linear(in_features=128, out_features=64, bias=True)
#   (relu2): ReLU()
#   (fc3): Linear(in_features=64, out_features=10, bias=True)
# )


# در مرحله بعدی اگر classification بود crossEntropy و اگر regression بود MSE میگیریم
# اینجا دیگه نیازی به softmaxt هم نداریم و خودش بصورت درصدی خروجی میده
criterion = nn.CrossEntropyLoss()  # classification
# criterion = nn.MSELoss()   regression


# ست کردن optimizer
import torch.optim as optim
# adam, sgd, lbfs, learning rate
optimizer = optim.Adam(model.parameters(), lr=0.001)


# Model training
epochs = 10
for epoch in range(epochs):
    
    model.train()
    total_loss = 0
    
    for image,labels in train_loader:
        image = image.to(device)
        labels = labels.to(device)
        optimizer.zero_grad()   # 1-Reset gradients
        outputs = model(image)  # 2-Forward pass
        loss = criterion(outputs, labels)   # 3-Calculate loss
        loss.backward()   # 4-Backpropagation
        optimizer.step()  # 5-Update weights
        total_loss += loss.item()
    
    average_loss = total_loss / len(train_loader)
    print(f"Epoch {epoch+1}/{epochs}, Loss: {average_loss:.4f}")

# نتیجه:
# Epoch 1/10, Loss: 0.0173
# Epoch 2/10, Loss: 0.0176
# Epoch 3/10, Loss: 0.0136
# Epoch 4/10, Loss: 0.0130
# Epoch 5/10, Loss: 0.0111
# Epoch 6/10, Loss: 0.0113
# Epoch 7/10, Loss: 0.0077
# Epoch 8/10, Loss: 0.0117
# Epoch 9/10, Loss: 0.0069
# Epoch 10/10, Loss: 0.0079


# تا اینجا فقط مدل رو آموزش دادیم
# الان میخوایم تست کنیم و evaluation رو انجام بدیم

model.eval()
correct = 0
total = 0

with torch.no_grad():
    for images, labels in test_loader:
        
        images = images.to(device)
        labels = labels.to(device)
        
        outputs = model(images)
        
        _,predicted = torch.max(outputs, dim=1)
        
        total += labels.size(0)
        
        correct += (predicted == labels).sum().item()
        
accuracy = 100 * correct / total
print(f"Accuracy of the network on the 10000 test images: {accuracy:.2f}%")

# Accuracy of the network on the 10000 test images: 97.75%


# انجام دادن پیشبینی (Prediction)

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

image, true_label = test_datasets[0]
plt.imshow(image.squeeze(), cmap="gray")
plt.title(f"True label: {true_label}")
plt.axis("off")

plt.savefig("mnist_test.png", dpi=150, bbox_inches="tight")
plt.close()
print("Image saved successfully")


model.eval()

with torch.no_grad():
    input_Image = image.unsqueeze(0).to(device)
    
    output = model(input_Image)
    
    predicted = torch.argmax(output, dim=1)

print("True label: ", true_label)  #7
print("Predicted label: ", predicted.item())   #7



































