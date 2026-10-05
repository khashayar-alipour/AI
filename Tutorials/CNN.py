
'''
===============================================================================
===============================================================================
================       Created on Sun Oct  4 20:23:14 2026     ================
================                IDE: Spyder                    ================
================         Author: Khashayar Alipour             ================
================     Convolutional Neural Networks (CNNs)      ================
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
#       MLP    ⭐CNN    RNN
#                    ┌───┴──┐
#                    ↓      ↓
#                   LSTM   GRU


# اینجا RNN شبکه عصبی دارای حافظه از مراحل قبلی هست که کاربرد اصلی آن متن، سری زمانی، صدا هست
# اینجا LSTM نوع پیشرفته‌تر RNN با حافظه بهتر هست که کاربرد اصلی آن متن و سری زمانی طولانی هست
# اینجا GRU نسخه ساده‌تر LSTM هست که کاربرد اصلی آن متن، سری زمانی هست
# اینجا Transformer معماری مبتنی بر Attention هست که کاربرد اصلی آن LLM، ترجمه، متن، تصویر و... هست



#✅ Filter / Kernel
#✅ Convolution - ّFeature map
#✅ Stride
#✅ Padding
#✅ Pooling
#✅ CNN Layers
#✅ Hierarchical Feature Learning
#✅ Real example CNN coding




'''
===============================================================
=======  ⭐  Convolutional Neural Networks (CNNs)  ⭐  =======
===============================================================
'''
# یک نوع Neural Network است که مخصوصاً برای کار با داده‌های دارای ساختار مکانی طراحی شده؛ مهم‌ترین کاربردش هم تصاویر است

# تفاوت CNN با Neural Network معمولی چیست؟
# فرض کن یک تصویر 28×28 داشته باشیم
# در یک MLP معمولی معمولاً تصویر را به یک بردار تبدیل می‌کنیم:
# 28 × 28
#    ↓
# تعداد 748 عدد
#    ↓
# Neural Network

# اما CNN سعی می‌کند ساختار دو‌بعدی تصویر را حفظ کند:
#  28 × 28 image
#      ↓
#     CNN
#      ↓
# Features
#      ↓
# Classification


"✅ Filter / Kernel"
# ایده اصلی CNN همینه. CNN یک فیلتر کوچک روی تصویر حرکت می‌دهد
# یک Kernel مثلاً 3×3 داریم که روی قسمت‌های مختلف تصویر حرکت می‌کند
# هدفش پیدا کردن ویژگی هایی مثل:  Edge, Line, Corner, Texture, ...
# به این عملیات میگن Convolution

Image
┌─────────────┐
│ ░ ░ ░ ░ ░ ░ │
│ ░ █ █ ░ ░ ░ │
│ ░ █ █ ░ ░ ░ │
│ ░ ░ ░ ░ ░ ░ │
└─────────────┘

# نکته اینه که CNN از ابتدا نمی‌داند مثلاً «چشم» چیست
# اگر هزاران عکس گربه و سگ به آن بدهی، در طول Training
#  مقدار Kernelها/Weights را طوری یاد می‌گیرد که ویژگی‌های مفید را استخراج کنند
# بنابراین CNN خودش Feature Extraction را یاد می‌گیرد
# لازم نیست ما دستی بگوییم «این قسمت چشم است، این قسمت گوش است»



"✅ Convolution - ّFeature map"
# فرض کنیم یک تصویر خیلی ساده داریم:
Image 5×5
1  1  0  0  0
0  1  0  0  1
0  0  1  1  0
0  0  1  1  0
1  0  0  0  1

# و یک Kernel/Filter با اندازه 3x3
# این Kernel را می‌توانی مثل یک ذره‌بین کوچک تصور کنی که روی قسمت‌های مختلف تصویر حرکت می‌کند
# این kernel داخل خودش ضریب هایی مخصوص به خودش داره که در پروسه convolution استفاده میکنه
-------------
| 1   0  -1 |
| 1   0  -1 |
| 1   0  -1 |
-------------

# در مرحله اول Kernel روی گوشه بالا-چپ تصویر قرار می‌گیرد
----------
|1  1  0 | 0  0
|0  1  0 | 0  1
|0  0  1 | 1  0
----------
 0  0  1   1  0
 1  0  0   0  1
# فقط این قسمت را نگاه می‌کنیم:
1  1  0
0  1  0
0  0  1

# حالا هر عدد را در عدد متناظر Kernel ضرب می‌کنیم:
1×1   1×0   0×-1
0×1   1×0   0×-1
0×1   0×0   1×-1

# نتیجه:
1   0   0
0   0   0
0   0  -1

# حالا همه رو باهم جمع میکنیم:     1+0+0+0+0+0+0+0−1=0
# پس اولین عدد Feature Map می‌شود:   0

# در مرحله بعد Kernel یک خانه به سمت راست حرکت می‌کند
# سپس ضرب و جمع و دوباره یه عدد جدید
# در نهایت مجموعه این اعداد میشن Feature Map


# اما Kernel چه چیزی را پیدا می‌کند؟
# درواقع Kernelهای مختلف می‌توانند ویژگی‌های مختلفی را تشخیص دهند
# Kernel A → Edge عمودی
# Kernel B → Edge افقی
# Kernel C → Corner
# Kernel D → Texture
# ...

# در CNN واقعی، ما معمولاً این Kernelها را دستی تعیین نمی‌کنیم
# شبکه در زمان Training خودش یاد می‌گیرد که
# چه فیلترهایی برای تشخیص گربه، سگ، عدد، تومور و... مفید هستند

# پس در کل پروسه convolution این میشه که Kernel روی تصویر حرکت می‌کند،
# در هر موقعیت با بخشی از تصویر محاسبه انجام می‌دهد و نتیجه را در Feature Map ذخیره می‌کند
# Image -> Convolution -> Feature Maps -> ReLU -> Pooling -> Convolution -> Feature Maps -> ... -> Classification



"✅ Stride"
# تعریف: Stride یعنی Kernel هر بار چند خانه حرکت کند
# مثلا اگه stride=1 باشه، kernel موقع حرکت 1خانه 1خانه جلو میره
# پس هرچی stride بزگتر باشه، feature map کوچکتر میشه



"✅ Padding"
# یه مشکلی که وجود داره اینه که اگر Kernel 3×3 را روی تصویر 5×5 حرکت دهیم و Padding نداشته باشیم:
    # 5x5 -> 3x3
# اندازه تصویر کوچک می‌شود
# ضمن اینکه پیکسل‌های گوشه و لبه کمتر در محاسبات دیده می‌شوند
# برای حل این مشکل، اطراف تصویر صفر اضافه می‌کنیم
# حالا Kernel می‌تواند روی قسمت‌های کناری هم حرکت کند

Original:
1  2  3
4  5  6
7  8  9

padding=1
0  0  0  0  0
0  1  2  3  0
0  4  5  6  0
0  7  8  9  0
0  0  0  0  0



"✅ Pooling"
# تعریف: Pooling یک نوع Downsampling است
# اندازه Feature Map را کوچک می‌کند، در حالی که سعی می‌کند مهم‌ترین اطلاعات را حفظ کند

# مثلا این feature map رو داریم و میخوایم یک 2×2 Max Pooling انجام بدیم:
4  2  1  3           4 2 | 1 3
5  8  2  1           5 8 | 2 1
7  1  6  4   ->      ---- ----
3  2  5  9           7 1 | 6 4
                     3 2 | 5 9
# قسمت اول:
4  2
5  8
# بزرگترین عدد = 8

# قسمت بعدی:
1  3
2  1
# بزرگترین عدد = 3

# همینطوری ادامه میدیم و نتیجه میشه این:
8  3
7  9
# 4×4 -> Max Pooling 2×2 -> 2×2


# چرا pooling انجام میدیم؟
# 1- کاهش حجم محاسبات
# برای کاهش مقادیر محاسباتی    
# مثلا 28×28  ->  14×14    

# 2-نگه داشتن ویژگی‌های مهم
# مثلا max pooling میگه در این ناحیه، قوی‌ترین activation کدام است    
# مثلاً اگر یک Edge در یک ناحیه وجود داشته باشد، مقدار activation آن ممکن است زیاد باشد و Max Pooling آن را نگه می‌دارد    

# 3- کمی مقاوم‌تر شدن نسبت به جابه‌جایی کوچک
# مثلاً اگر یک ویژگی کمی جابه‌جا شود، احتمالاً هنوز در همان ناحیه قرار دارد و Max Pooling می‌تواند آن را حفظ کند    


# Max Pooling vs Average Pooling
# اولی بزرگ‌ترین مقدار را انتخاب می‌کند
# دومی میانگین را می‌گیرد
1  3
2  8   → (1+3+2+8)/4 → 3.5



"✅ CNN Layers"
# درواقع CNN معمولا این لایه هارو داره

#    Image
       ↓
# Convolution Layer
       ↓
# Activation (ReLU)
       ↓
#   Pooling
       ↓
# Convolution Layer
       ↓
# Activation (ReLU)
       ↓
#   Pooling
       ↓
#   Flatten
       ↓
# Fully Connected Layer
       ↓
#   Output


① Input Layer:
# مثلاً یک تصویر RGB با اندازه 64 × 64:
    # 64 * 64 * 3   (3=channels   Red Green Blu)
# در این لایه CNN هنوز نمی‌داند گربه چیست؛ فقط یک مجموعه عدد دریافت می‌کند


② Convolution Layer:
# اینجا Convolution Layer با استفاده از Filter / Kernel ویژگی‌های مختلف تصویر را پیدا می‌کند
# یک Convolution Layer می‌تواند تعداد زیادی Filter داشته باشد
# این Filterها را ما تعیین نمی‌کنیم بلکه در زمان train شدن CNN خودش یاد می‌گیرد که چه Filterهایی مفید هستن

# Input Image
#      ↓
#  ┌───────────┐
#  │ Filter 1  │ → Edge
#  │ Filter 2  │ → Line
#  │ Filter 3  │ → Corner
#  │ Filter 4  │ → Texture
#  │ Filter 5  │ → ...
#  └───────────┘
#      ↓
# Feature Maps


③ Activation Layer:
# معمولاً بعد از Convolution از ReLU استفاده می‌شود
# در واقع ReLU باعث میشه شبکه روابط غیرخطی رو یاد بگیره
# ReLU(x) = max(0, x)
# مثلا با relu همچین تبدیلی انجام میشه:
    # [-2,  3, -1,  5] -> [ 0,  3,  0,  5]
    

④ Pooling Layer:
# عملیات downsizing رو انجام میده


⑤ Fully Connected Layer:
# در انتهای CNN معمولاً Feature Mapها را به یک بردار تبدیل می‌کنیم
# Feature Maps -> Flatten ->  [0.2, 0.8, 0.1, 0.6, ...] ->  Fully Connected -> Output



"✅ Hierarchical Feature Learning"
# یعنی یادگیری سلسله مراتبی. عملا CNN ویژگی هارو از ساده به پیچیده یاد میگیره
# یعنی Layerهای ابتدایی چیزهای ساده را یاد می‌گیرند و Layerهای عمیق‌تر از ترکیب آن‌ها چیزهای پیچیده‌تر را می‌سازن

# مثلا اگر دیتای ورودی یک عکس گربه باشه
# اولین Convolution Layer ممکن است ویژگی‌های بسیار ساده‌ای یاد بگیرد
# Layer 1
# → Edge
# → Horizontal line    ____
# → Vertical line    |    
# → Diagonal line  /\

# حالا Layer بعدی می‌تواند این Edgeها را ترکیب کند
# edge + edge + edge = shape
# می‌تواند یک شکل ساده مثل گوش یا چشم ایجاد کند
#  \    /
#   \  /
#    \/

# در لایه های عمیق تر حالا شبکه می‌تواند از این Shapeها استفاده کنه
# Edge -> Shape -> Texture/Part -> Eye  Ear  Nose

# لایه های خیلی خیلی عمیق
# Eye + Ear + Nose + Fur + Face -> cat face

# در نهایت:   Cat 🐱







"============================="
" ⭐ Real example CNN coding "
"============================="

"Codng with Tensorflow"

import tensorflow as tf
from tensorflow.keras import layers, models

model = models.Sequential([
    layers.Input(shape=(28,28,1)),
    
    # layer 1 (conv + relu + maxpool)
    layers.Conv2D(filters=32, kernel_size=(3,3), activation="relu"),
    
    layers.MaxPooling2D(pool_size=(2,2)),
    
    # layer 2
    layers.Conv2D(filters=64, kernel_size=(3,3), activation="relu"),
    
    layers.MaxPooling2D(pool_size=(2,2)),
    
    # layer 3
    layers.Flatten(),
    
    # NN --> 728 * 128 * 64 * 32 * 10
    # CNN --> conv1 --> conv2 --> 128 --> 10
    layers.Dense(128, activation = "relu"),
    
    layers.Dense(10, activation = "softmax"),
    
    ])




model.summary()
# Model: "sequential_1"
# ┌─────────────────────────────────┬────────────────────────┬───────────────┐
# │ Layer (type)                    │ Output Shape           │       Param # │
# ├─────────────────────────────────┼────────────────────────┼───────────────┤
# │ conv2d (Conv2D)                 │ (None, 26, 26, 32)     │           320 │
# ├─────────────────────────────────┼────────────────────────┼───────────────┤
# │ max_pooling2d (MaxPooling2D)    │ (None, 13, 13, 32)     │             0 │
# ├─────────────────────────────────┼────────────────────────┼───────────────┤
# │ conv2d_1 (Conv2D)               │ (None, 11, 11, 64)     │        18,496 │
# ├─────────────────────────────────┼────────────────────────┼───────────────┤
# │ max_pooling2d_1 (MaxPooling2D)  │ (None, 5, 5, 64)       │             0 │
# ├─────────────────────────────────┼────────────────────────┼───────────────┤
# │ flatten (Flatten)               │ (None, 1600)           │             0 │
# ├─────────────────────────────────┼────────────────────────┼───────────────┤
# │ dense_3 (Dense)                 │ (None, 128)            │       204,928 │
# ├─────────────────────────────────┼────────────────────────┼───────────────┤
# │ dense_4 (Dense)                 │ (None, 10)             │         1,290 │
# └─────────────────────────────────┴────────────────────────┴───────────────┘
#  Total params: 225,034 (879.04 KB)
#  Trainable params: 225,034 (879.04 KB)
#  Non-trainable params: 0 (0.00 B)


# در مراحل بعد fit, predict, evaluation, ...



"CNN Coding with Pytorch"

import torch
import torch.nn as nn

class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, padding=1)
        
        self.pool = nn.MaxPool2d(2,2)
        
        self.relu = nn.ReLU()
        
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1)
        
        self.fc1 = nn.Linear(in_features=64*7*7, out_features=128)
        
        self.fc2 = nn.Linear(in_features=128, out_features=10)
        
        self.softmax = nn.Softmax(dim=1)
    
    def forward(self,x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)
        
        x = self.conv2(x)
        x = self.relu(x)
        x = self.pool(x)
        
        x = self.flatten(x)
        
        x = self.fc1(x)
        x = self.relu(x)
        
        x = self.fc2(x)
        
        x = self.softmax(x)
        
        return x

       

# در مراحل بعدی ست کردن optimizer و حلقه for و ... انجام میدیم


        






























