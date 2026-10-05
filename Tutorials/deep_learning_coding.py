
'''
===============================================================================
===============================================================================
================       Created on Thu Oct  1 14:59:56 2026     ================
================                IDE: Spyder                    ================
================         Author: Khashayar Alipour             ================
================           AI Deep Learning Coding             ================
===============================================================================
===============================================================================
'''


# در این فایل کدزنی تمام درسنامه های قبلی مربوط به شبکه عصبی انجام شده
# برای کدزنی میشه از کتابخوانه های Sklearn, Pytorch و Tensorflow استفاده کرد



⭐ Tensorflow Library Tutorial:
    ✅ 1-Tensorflow core:
             Tensor
             Autodiff
    ✅ 2-Tensorflow data
    ✅ 3-Keras
    ✅ 4-TensorBoard
    ✅ 5-Tensorflow lite
    ✅ 6-Tensorflow serving
    ✅ 7-Tensorflow real coding - Dataset: Breast cancer


⭐ Pytorch Library Tutorial:
    ✅ 1-Intro
    ✅ 2-Tensorflow real coding - Dataset: Breast cancer 









'''
==================================
=======  ⭐  Sklearn  ⭐  =======
==================================
'''

# این کتابخوانه بیشتر برای traditional machine learning کاربرد داره:
    # Example: Linear regression, KNN, Decision Tree, SVM, Random Forest ...

# از کاربردهای دیگر این کتابخوانه در زمینه traditional machine learning این موارد رو داریم:
    # Feature engineering, Pipeline, Cross validation, ...

# همچنین از دو کلاس MLPClassifier و MLPRegressor پشتیبانی میکنه

# مشکل این کتابخانه این بود که بصورت تخصصی برای deep learning و neural network ساخته نشده
# پس در ادامه بصورت تخصصی درمورد کدزنی کتابخوانه های مخصوص Deep learning صحبت میشه









'''
======================================================
=======  ⭐  Tensorflow Library Tutorial  ⭐  =======
======================================================
'''

#-------------------------------------------
# pip install tensorflow

import tensorflow as tf
print(tf.__version__)   # 2.21.0

# ما اول باید ببینیم tensorflow روی سیستم ما داره روی CPU اجرا میشه یا GPU
# بصورت پیش فرض روی CPU اجرا میشه ولی اگه روی GPU باشه خیلی بهتره
# چون میشه هزاران کار کوچیک بصورت موازی هم انجام بشه که به Training ما شتاب میده
print(tf.config.list_physical_devices("gpu"))   # []
# وقتی 0 یا [] میده یعنی روی CPU هست
#-------------------------------------------


# کلا اکوسیستم tensorflow خودش چند بخش  مختلف داره
# کتابخوانه TensorFlow فقط یک کتابخانه برای ساخت شبکه عصبی نیست
# بلکه چند بخش مختلف برای ساخت، آموزش، مانیتور کردن و Deploy کردن مدل دارد

#                  TensorFlow
#                       |
#  --------------------------------------------------
#  |    |    |          |        |         |        |            
# Core  |  Keras   TensorBoard   |     Deployment   |
#       |                        |                  |
#  Tensorflow data     Tensorflow lite    Tensorflow serving



"-------------------"
"✅ Tensorflow core"
"-------------------"
# هسته اصلی tensorflow هست که شامل این بخش‌ها میشه:
# Tensor
# Variable
# Gradient
# Operations
# Computational Graph
# Automatic Differentiation


" What is Tensor? "
# واحد های سازنده Tensorflow همون Tensor ها هستن
# ما میتونیم input یا حتی دیتاهای hidden layer یا حتی output layer رو به tensor تبدیل کنیم
# در نتیجه شبکه عصبی میشه جریانی از tensorها و برای همین بهش میگن tensorflow

# تنسورها مثل همون numpy array ها هستن
# برای ساخت tensor در Tensorflow دو روش وجود داره: یکیش استفاده از constant هست و یکی دیگه Variable
# وقتی constant میسازیم وزن‌ها ثابت هستن ولی اگه بخوایم Weightها تغییر کنن باید با Variable بسازیم


#---------------------Tensor Ranks ------------
# Rank 0 - Scaler
# همون عدد ثابت هست
import tensorflow as tf
x = tf.constant(5)
y = tf.variable(5)

# Rank 1 - Vector
# یک بردار هست
x = tf.constant([1,2,3])
y = tf.variable([1,2,3])

# Rank 2 - Matrix
# 2 بعدی هست مثل یک table یا جدول
# کاربرد اصلیش در weight یا وزن های یک nerual net هست
x = tf.constant([ [1,2], [3,4] ])
y = tf.variable([ [1,2], [3,4] ])

# Rank 3 - Tensor
# Like RGB which is height*width*channel
#---------------------------------------------


#-------------- توابع مهم tensor ---------------------------------------------
print(x.shape)
print(x.dtype)
print(tf.rank(x)) #dimension
print(tf.size(x))

# میتونیم مقدار جدیدی به تنسور assign کنیم
x.assign(10)

# میتونیم تایپ تنسور رو همون موقع که میسازیمش مشخص کنیم
x = tf.constant([1,2,3], dtype=tf.float32)
# درکل وزن‌ها اکثرا float32 هستن

# میتونیم تایپ تنسورها رو بهم دیگه تبدیل کنیم
x = tf.cast(x, tf.int32)

# میتونیم Reshape کنیم
# مثلا این ماتریکس 4 در 2 رو میخوایم به 1 در 4 تبدیل کنیم
a = tf.constant([[1,2],[4,5]])
x = tf.reshape(a, (1,4))
print(x)   # tf.Tensor([[1 2 4 5]], shape=(1, 4), dtype=int32)

# میتونیم dimension رو تغییر بدیم و بیشترش کنیم
x = tf.constant([[1,2,4,5]])    # shape=(1, 4) 
x_epand = tf.expand_dims(x, axis=0)
print(x_epand)   # [[[1 2 4 5]]], shape=(1, 1, 4)

# وقتی بخوایم به هر المنت یه عدد اضافه کنیم
# به این ویژگی broadcasting میگن
# کاربردش جایی هست که مثلا بخوایم bias + weight*X کنیم
a = tf.constant([1,2,3])
b = a + 5 
print(b)   # [6 7 8], shape=(3,)

# تبدیل تنسور به numpy :
x = tf.constant([1,2,3])
x_nump = x.numpy()
print(x_nump)        # [1 2 3]
print(type(x_nump))  # <class 'numpy.ndarray'>

# indexing:
# getting one element
x=tf.constant([10,20,30,40,50])
x[0] 

# Slice:
x[1:4]

tf.transpose(x)

tf.concat([a,b],axis=0)

# Reduction functions (important for loss and metrics):
x=[1,2,3]
tf.reduce_sum(x) #6
tf.reduce_mean([1,2,3]) #2  used in MSE
tf.reduce_max(x)   # it gives you the maximum values
tf.reduce_min(x)   # # It gives you the lowest values

# Comparison functions:
tf.greater( [1,5], [2,3])
tf.equal(a,b)

# Random number:
tf.random.normal([3,3])
tf.random.uniform([3,3])
tf.random.set_seed(42)
#----------------------------------------------------------------------


#-------------------------Mathematical operations of tensors-----------
import tensorflow as tf 
a = tf.constant([1,2,3])
b = tf.constant([4,5,6])

c  = a + b 
print(c)    # tf.Tensor([5 7 9], shape=(3,), dtype=int32)

c = a*b     #element wise product
print(c)    # tf.Tensor([ 4 10 18], shape=(3,), dtype=int32)

a = tf.constant([[1,2],[4,5]])
b = tf.constant([[4,5],[7,8]])
c = tf.matmul(a,b)   #matrix multiplication   
print(c)    # tf.Tensor( [ [18 21] [51 60] ], shape=(2, 2), dtype=int32)
#-----------------------------------------------------------------------


#---------- توابع generator در تنسورها --------------------------------------
print(tf.zeros([2,3]))

print(tf.ones([2,3]))

x=tf.fill([2,3],5)
print(x)

print(tf.random.normal([2,3], mean=0, stddev=1))
#----------------------------------------------------------------------


#-------------------------------- Activation functions ----------------
x= tf.constant([10.,20.,30.,-10.,-20.,-30.,0.])
z_x  = tf.nn.relu(x)
print(z_x)   #[10. 20. 30.  0.  0.  0.  0.]

z_x = tf.nn.sigmoid(x)
print(z_x)

x = tf.constant([100.0 , 40.0 , 60.0])
z_x = tf.nn.softmax(x)
print(z_x)
#----------------------------------------------------------------------



"Autodiff"
# ویژگی Automatic Differentiation (Autodiff) یکی از مهم‌ترین قابلیت‌های TensorFlow و PyTorch است
# فرض میکنیم یک مدل داریم که یک weight داره
# و می‌خواهیم بدانیم اگر w را کمی تغییر دهیم، Loss چقدر تغییر می‌کند
# با استفاده از مشتق گیری میفهمیم که اگر w را تغییر دهیم، Loss با نرخ مشخصی تغییر می‌کند

# مشکل اینه که در یک شبکه عصبی واقعی loss ممکنه پیچیده باشه
# در نتیجه باید مشتق Loss نسبت به تک‌تک وزن‌ها و بایاس‌ها محاسبه شود
# اگر شبکه میلیون‌ها پارامتر داشته باشد، انجام این محاسبات به صورت دستی تقریباً غیرممکن است
# اینجاست که Automatic Differentiation وارد می‌شود

# این مفهوم یعنی TensorFlow یا PyTorch خودش محاسبه می‌کند که خروجی یک تابع نسبت به متغیرهای موردنظر چه مشتقی دارد
# پس Autodiff میشه قابلیت TensorFlow/PyTorch برای محاسبه خودکار مشتق و Gradient توابع نسبت به متغیرها و پارامترها

with tf.GradientTape() as tape:
     y = function(x)
gradient = tape.gradient(y, x)

# رابطه Autodiff با Backpropagation:
    # Forward Pass -> Prediction -> Loss -> Backpropagation / Autodiff -> Gradients -> Optimizer -> Update Weights

# ویژگی Autodiff فقط Gradient را محاسبه می‌کند
# الگوریتم Optimizer از Gradient برای تغییر Weightها استفاده می‌کند



"--------------------"
"✅ Tensorflow data "
"--------------------"
# این بخش برای ساخت و مدیریت Pipeline داده‌ها است

# فرض کن 100,000 تصویر داری و نمی‌خواهی همه را یکجا وارد RAM کنی
# اینجا tf.data کمک می‌کند داده‌ها را به‌صورت مناسب برای Training آماده کنی

# در پروژه‌های کوچک MNIST شاید خیلی متوجه اهمیتش نشوی
# ولی وقتی دیتاست بزرگ باشد، tf.data برای موارد زیر خیلی کاربردیه:
    # سرعت Training
# مصرف RAM
# Batch processing
# خواندن داده از Disk
# Data Pipeline


# Raw Data -> Shuffle -> Batch -> Prefetch -> Neural Network
dataset = tf.data.Dataset.from_tensor_slices(  (x_train, y_train)  )
dataset = dataset.shuffle(10000)
dataset = dataset.batch(32)
dataset = dataset.prefetch(tf.data.AUTOTUNE)



"----------------"
"✅ TensorBoard "
"----------------"
# ابزار TensorBoard برای Visualizing و Monitoring در TensorFlow است

# مثلا هنگاه آموزش مدل:
    # Epoch 1 → Loss = 0.8
    # Epoch 2 → Loss = 0.6
    # Epoch 3 → Loss = 0.4
    # ...

# به‌جای اینکه فقط اعداد را ببینی، TensorBoard می‌تواند نمودارهای Training را نشان دهد:
    # Loss
    #  │\
    #  │ \
    #  │  \
    #  │   \____
    #  │
    #  └────────── Epoch

# همچنین میتواند این موارد را نشان دهد:
    # Training Loss
    # Validation Loss
    # Accuracy
    # Learning Rate
    # Model Graph
    # Histograms
# بعضی اطلاعات مربوط به Embeddings    

# در پروژه‌های واقعی بسیار مفید است، چون می‌توانی بفهمی مثلاً:
    # Training Accuracy ↑
    # Validation Accuracy → ثابت
# که میتواند نشانه ای از overfitting باشد



"--------------------"
"✅ Tensorflow Lite "
"--------------------"
# این قسمت برای اجرای مدل روی دستگاه‌های سبک و Edge Devices طراحی شده است
# 📱 Smartphone
# 💻 Embedded Device
# 📷 Camera
# 🚗 Edge Device

# فرض کن یک CNN ساخته‌ای که گربه و سگ را تشخیص می‌دهد. روی کامپیوتر آموزش می‌دهی:
    # PC -> Train CNN -> TensorFlow Model
# بعد مدل را برای اجرای روی دستگاه تبدیل می‌کنی:
    # TensorFlow Model -> TensorFlow Lite -> Android / Embedded Device / Edge



"-----------------------"
"✅ Tensorflow Serving "
"-----------------------"
# اینجا وارد Deployment سمت Server می‌شویم
# ویژگی TensorFlow Serving برای ارائه مدل آموزش‌دیده به‌عنوان یک سرویس استفاده می‌شود

# فرض کن مدل راآموزش دادی:
    # CNN + MNIST + 98% Accuracy
# حالا میخواهی یک web app داشته باشی. کاربر تصویر آپلود میکند:
    # User -> Web App -> API -> TensorFlow Serving -> Model -> Prediction -> Web App



"----------"
"✅ Keras "
"----------"
# اگر TensorFlow را موتور در نظر بگیریم، Keras ابزار سطح بالاتر و راحت‌تر برای ساخت Neural Network است
# یعنی Keras مقدار زیادی از کارهای پیچیده TensorFlow را برایت ساده می‌کند
# برای کسی که می‌خواهد CNN، RNN، LSTM، Transformer و مدل‌های Deep Learning بسازد، Keras بسیار کاربردی است

# مثلا ساخت یک شبکه ساده:
import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(10, activation="softmax")   ])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]   )

model.fit(
    x_train,
    y_train,
    epochs=10  )





"--------------------------------------------------"
"✅ Tensorflow real coding - Dataset: Breast cancer"
"--------------------------------------------------"
# میخوایم یک شبکع عصبی آموزش بدیم که عددها و وزن هاش طوری باشن (طوری train شده باشه که) که
# وقتی ورودی بهش بدیم خروجی بگه سرطان سینه بدخیمه یا خوش خیم

from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
X = data.data
y = data.target
print(X.shape)    # (569, 30)
print(y.shape)    # (569,)

# یعنی 569 نمونه (بیمار) داریم که هر بیمار 30 feature برای وجود داره
# کلا 2 تا output داریم که خوش‌خیم و بدخیم هست


# Train-Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42,stratify=y)


# Standard scaler
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Model
#30 (input) --> 64 (hidden layer 1) -> 32 (hidden layer 2) --> 1 (output)
# اینجا مسئله‌ای که داریم اینه که میتونیم نورون خروجی رو یک بذاریم با 2 تا
# اگه یکی بذاریم خروجی یا میشه 0 یا 1 و میگه یا خوش خیمه یا بدخیم
# در این حالت activation باید روی Sigmoid بذاریم
# با اینکار میتونیم 2 تا Class رو داخل یک نورون نشون بدیم
# یا میتونیم 2 نورون خروجی بذاریم که یکی خوش‌خیم باشه و یکی بدخیم
# در این حالت Activation باید روی softmax بذاریم و 2 عدد خروجی رو باهم مقایسه کنیم تا بفهمیم خروجی خوش‌خیم شده یا بدخیم

import tensorflow as tf  
from tensorflow import keras  
from tensorflow.keras import layers 

model = keras.Sequential([
      layers.Input(shape=(30,)) ,

      layers.Dense(64,activation='relu') , 
      layers.Dense(32,activation='relu'),

      #layers.Dense(2,activation ='softmax') --> 0.2  , 0.8 
      layers.Dense(1,activation = 'sigmoid') 

      #If binary --> 1 neuron -> sigmoid 
      #If regression --> 1 neuron --> Linear (relu)
      #If  multi class --> class neuron --> softmax 
])


# ست کردن Compiler
model.compile(optimizer = 'adam' ,loss='binary_crossentropy'  ,metrics=['accuracy'])


# Train model
history = model.fit(X_train,y_train , epochs=50 , batch_size = 32 ,validation_split=0.2)
# Epoch 1/50
#  12/12 ━━━━━━━━━━━━━━━━━━━━ 1s 23ms/step - accuracy: 0.7363 - loss: 0.5290 - val_accuracy: 0.8462 - val_loss: 0.4186
# Epoch 2/50
#  12/12 ━━━━━━━━━━━━━━━━━━━━ 0s 7ms/step - accuracy: 0.8819 - loss: 0.3511 - val_accuracy: 0.9011 - val_loss: 0.3019
# Epoch 3/50
#  12/12 ━━━━━━━━━━━━━━━━━━━━ 0s 7ms/step - accuracy: 0.9176 - loss: 0.2515 - val_accuracy: 0.9451 - val_loss: 0.2151
#  ...          ...              ...          ...       ...         ...           ...           ...         ...
# Epoch 49/50
#  12/12 ━━━━━━━━━━━━━━━━━━━━ 0s 7ms/step - accuracy: 1.0000 - loss: 0.0059 - val_accuracy: 0.9890 - val_loss: 0.0214
# Epoch 50/50
#  12/12 ━━━━━━━━━━━━━━━━━━━━ 0s 7ms/step - accuracy: 1.0000 - loss: 0.0057 - val_accuracy: 0.9890 - val_loss: 0.0213


# Validation
test_loss , test_accuracy = model.evaluate(X_test,y_test)
print('test loss : ',test_loss)
print('test accuracy : ',test_accuracy)
# 4/4 ━━━━━━━━━━━━━━━━━━━━ 0s 13ms/step - accuracy: 0.9649 - loss: 0.1051
# test loss :  0.10512489080429077
# test accuracy :  0.9649122953414917


# Prediction
predictions = model.predict(X_test)
print(predictions[:5])
# 4/4 ━━━━━━━━━━━━━━━━━━━━ 1s 15ms/step 
# [[3.31169248e-09]
#  [1.00000000e+00]
#  [2.74383347e-05]
#  [1.23023026e-01]
#  [1.61428496e-10]]

















'''
===================================================
=======  ⭐  Pytorch Library Tutorial  ⭐  =======
===================================================
'''

# pip install troch

import torch
print(torch.__version__)   # 2.14.0+cpu

print(torch.cuda.is_available())   # False
# این کد در PyTorch بررسی می‌کند که آیا CUDA برای استفاده از GPU در دسترس است یا نه
# اگر خروجی True باشد یعنی PyTorch می‌تواند از یک NVIDIA GPU از طریق CUDA استفاده کند
# اگر False باشه یعنی در محیط فعلی PyTorch امکان استفاده از CUDA وجود ندارد. پس ممکنه که:
    # ممکنه GPU انویدیا نداشته باشی    
    # درایور NVIDIA مناسب نباشد    
    # نسخه PyTorch نصب‌شده CUDA نداشته باشد    
    # ممکنه CUDA/PyTorch با سیستم سازگار نباشند    

# حالا وقتی True باشه می‌توانی Tensor را اینجوری روی GPU قرار بدهی:
x = torch.tensor([1, 2, 3]).cuda()


"-----------"
"✅ Tensor "
"-----------"
# کتابخوانه Pytorch هم مثل Tensorflow داخلش از tensor استفاده میشه

import torch

# 0D
x = torch.tensor(5)

# 1D
x = torch.tensor([1, 2, 3, 4])
print(x.ndim)
print(x.shape)

# 2D
x = torch.tensor([  [1, 2, 3], [4, 5, 6]  ])

# 3D
x = torch.tensor([  [[1, 2],[3, 4]], [[5, 6],[7, 8]]  ]) 


# ساخت tensor:
# قبل از ساخت تنسور باید اول مشخص کنیم که Device مورد استفاده ما CPU هست یا GPU
# وقتی مشخص کردیم، باید اون tensor که ساختیم رو بیاریم روی همین Device که میخوایم
# وقتی Device مشخص میکنیم، ازونجا به بعد دیگه هرچیزی که به اون Tensor مربوطه میاد روی device موردنظر ما انجام میشه

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)    # cpu

# روش مستقیم:
x = torch.tensor([1,2,3], device=device)

# روش غیرمستقیم:
x = torch.tensor([1,2,3])
x = x.to(device)



"-------------"
"✅ functions "
"-------------"
# همون توابعی که در tensorflow هست در اینجا هم استفاده میشه

# Generator:
x = torch.zeros(3, 4)
x = torch.ones(3, 4)


# Random number:
x = torch.rand(3, 4)   # بین 0 تا 1
# [[0.9723, 0.7113, 0.9765, 0.6150], [0.0536, 0.2289, 0.3236, 0.3893], [0.1535, 0.0222, 0.8497, 0.9655]]

x = torch.randn(3, 4)   # عدد رندوم نرمال   miu=0, sigma=1
# [[ 0.9132, -0.4441,  0.6631,  1.1420], [ 0.5997, -1.5329,  0.5690, -0.9699], [-0.7990, -1.0804, -1.9225,  1.6691]]


# Arrange number:
x = torch.arange(0, 10)   # ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
x = torch.linspace(0, 1, 5)    #([0.0000, 0.2500, 0.5000, 0.7500, 1.0000])     از 0 تا 1 به 5 قسمت مساوی تقسیم میکنه


# Alter tensor dtype:
x = torch.tensor([1, 2, 3], dtype=torch.float32)


# Mathematical:
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])
a+b
a-b
a*b
a/b
x.min()
x.max()
x.mean()
x.sum()
torch.matmul(a, b)    #Matrix multiplication    (1*4)+(2*5)+(3*6)=32
a @ b   #Matrix multiplication

# کاربرد matmul در محاسبه این رابطه در شبکه عصبی هست:
    # W * X + B
a = torch.tensor([
    [1., 2.],
    [3., 4.]  ])
b = torch.tensor([
    [5., 6.],
    [7., 8.] ])

c = a @ b
# [[19., 22.],
#  [43., 50.]]


output = torch.tensor([ 0.1, 0.3, 0.2, 0.5, 0.4  ])
output.argmax()




"---------------------------------"
"✅ Input tensor -> Output tensor"
"---------------------------------"
# میخوایم بصورت شماتیک از مرحله input tensor تا اضافه شدن وزن‌ها و بایاس و سپس ورود به نورون و output tensor شبیه‌سازی کنیم

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(device)

"Input"
# این مثلا xهای ورودی هست (مثلا کلا 3 تا x داریم) که قراره وارد یک نورون بشه
x = torch.tensor([2.0,3.0,4.0] , dtype=torch.float32)
x2 = torch.tensor([5.0,6.0,7.0] , dtype=torch.float32)
x3 = torch.tensor([1.0,8.0,9.0] , dtype=torch.float32)

"weights"
w = torch.tensor([0.1,0.2,0.3] , dtype=torch.float32)

"bias"
b = torch.tensor(0.5, dtype=torch.float32)

"Move to device"
x = x.to(device)
w = w.to(device)
b = b.to(device)

"Forward pass"
z = w@x + b 
print(z) 


# X1  -
#      - 
#       -
#        ->
# X2 -----> Neuron(+bias) --->Output
#        ->
#       -
#      -
# x3  -
 


"------------"
"✅ Autograd"
"------------"
# یکی از مهمترین ویژگی های Pytorch ویژگی autograd هست

import torch
x = torch.tensor(3.0, requires_grad=True)
y = x ** 2
y.backward()
print("x =", x)
print("y =", y)
print("gradient =", x.grad)    # gradient = tensor(6.)





"------------------------------------------------"
"✅ Pytorch real coding - Dataset: Breast cancer"
"------------------------------------------------"

from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
X = data.data
y = data.target


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42,stratify=y)


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# اول از همه باید numpy array های خودمون رو به tensor تبدیل کنیم
# چون برای ساخت Dataloader خودمون به tensor نیاز داریم
import numpy as np
import torch
X_train = torch.tensor(X_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.float32)


# ساخت TensorDataset
from torch.utils.data import TensorDataset
train_dataset = TensorDataset(X_train, y_train)
test_dataset = TensorDataset(X_test, y_test)


# ساخت Dataloader
# کلا Dataloader میاد بهمون امکان اینو میده که از داخلش batch batch دیتا بگیریم
# اینجا Batch_size=32 گذاشتیم یعنی 32تا 32تا دیتارو میگیریم
# توی tensorflow دیتا رو بصورت یکجا میگرفتیم ولی اینجا میایم for میزنیم روی dataloader
batch_size = 32
from torch.utils.data import DataLoader
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)


# --------------------------------ساخت کلاس شبکه عصبی به 2 روش ------------------------
# روش اول مثل Tensorflow هست و روش دوم که روش محبوب تری هم هست، فقط توی Pytorch هست
import torch.nn as nn   #from torch import nn 

#-----------------[1st method]---------------------
class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(30,64),
            nn.ReLU(),
            nn.Linear(64,32),
            nn.ReLU(),
            nn.Linear(32,1),    )
        
    def forward(self,x):
        return self.network(x)

model = NeuralNetwork()
#--------------------------------------------------

#-----------------[2nd method]---------------------
class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
 
        self.layer1 = nn.Linear(30,64)
        self.relu1 = nn.ReLU()

        self.layer2 = nn.Linear(64,32)
        self.relu2 = nn.ReLU()

        self.output = nn.Linear(32,1)

        #Sigmoid --> binary --> Loss havaseton 
        #Multi class --> softmax
        #Regression --> linear (activation = none)

    def forward(self,x):        
        # توی تابع forward میتونیم Sigmoid رو بزاریم ولی نمیذاریم. میخوایم توی loss بیاریمش        
        
        x = self.layer1(x)
        x = self.relu1(x)

        x = self.layer2(x)
        x = self.relu2(x)

        x = self.output(x)

        return x

model = NeuralNetwork()
#--------------------------------------------------


# ساخت تابع loss
criterion = nn.BCEWithLogitsLoss()    # for setting loss, we used BCE 


#ساخت optimizer
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)


# ساخت training loop
# روی dataloader حلقه میزنیم، براش Epoch مشخص میکنیم و دونه دونه Data batch هارو میگیریم
# و مشخص میکنیم که مرحله به مرحله چه عملیاتی روی Data batch ها انجام بشه
epochs = 50 
for epoch in range(epochs):
    for x_batch, y_batch in train_loader:

        output = model(x_batch)    # feed forward

        loss = criterion(output,y_batch.reshape(-1,1))

        #clear old gradient
        optimizer.zero_grad()

        loss.backward()  # حساب کردن مشتق‌ها -> dloss/dWeight

        optimizer.step() # weight new = weight old - learning_rate * gradient loss / weight

    print(f'Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}')

# Epoch 1/50, Loss: 0.5746
# Epoch 2/50, Loss: 0.3349
#  ...   ...   ...    ... 
# Epoch 49/50, Loss: 0.0042
# Epoch 50/50, Loss: 0.0125


# Evaluation phase
model.eval() 

with torch.no_grad():
    logits = model(X_test) #x_test --> 3d3232
    probabilities = torch.sigmoid(logits)
    predictions = (probabilities >= 0.5).float()
    acccuracy = (predictions == y_test.reshape(-1,1)).float().mean()

# اینجا prediction ما یه عددی میشه مثلا 3433 و با probabilities تبدیلش میکنیم به Sigmoid (یعنی بین 0 و 1)    
# سپس میایم با predictions میگیم اگه بالاتر از 0.5 باشه میکنیمش 1 و اگه پایین تر باشه میکنیمش 0    

print(f'Test Accuracy: {acccuracy:.4f}')

# Test Accuracy: 0.9561


























































































































