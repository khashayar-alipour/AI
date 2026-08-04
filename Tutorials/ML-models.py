
'''
===============================================================================
===============================================================================
================       Created on Tue Jul 21 11:47:09 2026     ================
================                IDE: Spyder                    ================
================         Author: Khashayar Alipour             ================
================              Statistical models               ================
================                 ML Models                     ================
===============================================================================
===============================================================================
'''

#
#                                 ___ Batch gradient descent
# Types of gradient descent  ----|___ Mini-batch gradient descent
#                                |___ Stochastic gradient descent (SGD)
# Supervised Learning
# └── Regression
#     ├── Linear Regression
#     │   ├── LinearRegression   اینو قبلا یاد گرفته بودیم
#     │   ├── Ridge ⭐
#     │   ├── Lasso ⭐
#     │   ├── ElasticNet ⭐
#     │   └── SGDRegressor  اینو قبلا یاد گرفته بودیم
#     │
#     └── Nonlinear Regression
#         ├── Polynomial Regression
#         ├── Decision Tree Regressor ⭐
#         ├── Random Forest Regressor ⭐
#         ├── KNeighborsRegressor ⭐
#         ├── SVR (Support Vector Regression)  ⭐
#         ├── Gaussian Process Regressor
#         └── Neural Network Regressor


# Ensemble Models
# │
# ├── Bagging
# │   ├── Bagging Regressor
# │   ├── Bagging Classifier
# │   └── Random Forest  ⭐
# │
# ├── Boosting
# │   ├── AdaBoost
# │   ├── Gradient Boosting
# │   ├── XGBoost
# │   ├── LightGBM
# │   └── CatBoost
# │
# └── Stacking
#     ├── Stacking Regressor
#     └── Stacking Classifier        



#              Supervised ML
#                    |
#          ---------------------
#          |                   |
#    Classification        Regression
#          |                   |
#     SVC, linearSVC ⭐     SVR, linearSVR ⭐

#          ____ Support Vector Classification = SVC
# SVM ----|____ Support Vector Regression = SVR



# Hyperparameter tuning in ML --> Overfitting / Underfitting 


# Generalization






'''
====================================
====================================
=======   gradient descent   =======
====================================
====================================
'''

# Batch gradient descent - mini-batch gradient descent - stochastic gradient descent
# These three concepts are actually the same algorithm (Gradient Descent) with different ways of feeding data to the algorithm.

# What does gradient descent do?
# Machine learning does the same thing as a blind man does, trying to find the lowest bottom in a mountain.
# Instead of finding the bottom of a mountain, ML tries to find the best model parameters (weights).

# Suppose we have a linear regression model  ->  y=ax+b
# The computer initially guess   a=100 b=500
# These numbers at first are probably wrong
# It predicts values -> Some predictions are too high -> Some are too low.
# So we calculate the error -> That error is called the Loss Function


"Gradient Descent asks: "
# How should I change a and b so that Loss becomes smaller?
# It computes the slope (gradient), updates the parameters (a,b), and repeats.

# Suppose your dataset has 100,000 rows
# How should Gradient Descent calculate the gradient?
# There are three ways


#==========================
"1. Batch Gradient Descent"
#==========================
# It uses every single row before making one update.
# It has excellent stability but it is very slow

# Read row 1
# Read row 2
#   ...
# Read row 100000
#    ↓
# Calculate ONE gradient
#    ↓
# Update parameters

# Then it starts over:
# 100000 rows
#    ↓
# One update

"  _________________________________________"
" |   Advantages          |  Disadvantages |"
# | ✅ Very stable       |   ❌ Very slow |
# | ✅ Smooth learning   |                 | 
# ------------------------------------------



#===============================
"2. Mini-Batch Gradient Descent"
#===============================

# Instead of 100000 or 1 row
# we choose 32 or 64 or 128 rows

# For example Batch-size=64
# Rows 1-64
#  ↓
# Update
# Rows 65-128
#  ↓
# Update
# Rows 129-192
#  ↓
# Update

"  _____________________________"
" |    Advantages              |"
# |  ✅ Faster than Batch     |
# |  ✅ More stable than SGD  | 
# |  ✅ Uses GPU efficiently  |
# -----------------------------

# This is why almost every deep learning framework uses Mini-Batch.
# Mini-batch gives a good balance between speed and stability


#======================================
"3: Stochastic Gradient Descent (SGD)"
#======================================
# Now imagine you don't want to wait
# Instead you update after every sample (samples are picked stochastically -> randomly)

# Row 1 -> update -> Row 150 -> update -> Row 13 -> update -> Row 8 -> update ...

# The loss jumps around. Eventually it reaches the minimum, but not smoothly.
# SGD is very fast but the results are noisy

"  _______________________________________________________________________"
" |      Advantages                   Disadvantages                      |"
# |  ✅ Extremely fast updates |   ❌ The direction is noisy.           |
# |  ✅ Works on huge datasets |   ❌ Imagine hiking down the mountain  |
# |  ✅ Uses little memory     |        Instead of walking smoothly,    |
# |                            |               you zigzag.               |
# ------------------------------------------------------------------------


#====================================
"Which one is uses it scikit-learn?"
#====================================

"LinearRegression"  # -->  Uses a direct mathematical solution. No Gradient Descent
"SGDRegressor"      # -->  Uses Stochastic Gradient Descent
"Neural Networks"   # -->  Almost always use Mini-Batch Gradient Descent












'''
================================================================
================================================================
=======       Supervised Linear Regression Models        =======
=======    Ridge(l2) - Lasso(l1) - Elastic net(l1/l2)    =======
================================================================
================================================================
'''

# تا اینجای کار 2 مدل ازین قسمت رو یاد گرفتیم
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
# قراره 3 تا دیگه یاد بگیریم


"What is loss/cost function?"

# loss function = minΣ(y - ŷ)²

# y = مقدار واقعی (Ground Truth)
# ŷ = مقداری که مدل پیشبینی کرده
# ∑ sign = علامت سیگما یعنی همه را باهم جمع کن
# power 2 = علت توان 2 اینه که مقادیر منفی مثبت بشن و هیچ مقداری در جمع حذف نشه

# به این فرمول Σ(y - ŷ)² میگن Sum of Squared Errors یا SSE
# به کمترین (min) مقدار SSE میگن loss function
# در واقع SSE مجموع خطاهاست

# گاهی قبل SSE یه ضریب 1/n میاد که اون میشه Mean Squared Error (MSE)
# درواقع MSE میشه میانگین خطاها
# MSE=(1/n)Σ(y - ŷ)²




#===========================================================
"========== Ridge Regression (L2 Regularization) =========="
#===========================================================

# این مدل میاد یه ورژن پیشرفته تر از loss function عادی که تا الان حساب میکردیم بهمون میده
# Ridge loss function = min(Σ(y - ŷ)² + λΣw²)    یا پارامتر وزن بهش اضافه کرده


"what is this formula?"
# این قسمت Σ(y - ŷ)² همون Prediction Error ما میشه که تا الان انجام میدادیم
# یعنی میگیم مدل چقدر اشتباه پیشبینی کرده
# اگر این قسمت کوچک شود، مدل بهتر پیشبینی میکنه

# به این قسمت λΣw² میگن Regularization Term یا Penalty
# یعنی مدل بابت بزرگ بودن ضرایب جریمه می‌شود

# علامت ∑ یعنی مجموع. اینجا Σ(y - ŷ)² میگیم اختلاف همه نقاط پیشبینی با نقاط واقعی رو اول به توان 2 برسون
# سپس بیا همه رو باهم جمع کن

# اینجا lambda یا λ به مدل میگه که چقدر روی بزرگ بودن ضرایب سختگیر باشه؟
# اگر λ = 0 باشه یعنی loss=prediction error + 0 یعنی اصلا جریمه‌ای وجود ندارد که میشه همون linear regression معمولی
# اگر λ = 1000 باشه یعنی ضرایب بزرگ ممنوع!! و مدل ضرایب رو کوچک نگه میداره
# درواقع با بزرگ بودن مقدار λ ، حاصل loss زیاد میشه
# بنابراین مدل تمایل پیدا میکنه برای کاهش loss بیاد ضرایب رو کاهش بده


"what is Weight?"
# هر دیتا از ستون هایی تشکیل شده که میشن feature یا ویژگی
# همچنین ردیف داره که بهش میگن sample یا نمونه

# مثلا ما 3 تا feature بنام distance و speed و Traffic داریم
# حالا مثلا مدل این رابطه فرضی رو برای دیتای ما پیشبینی کرده:
    # y​ = 2×distance −0.5×speed +3×traffic +10
    #   w₁=2        w₂=-0.5     w₃=3
# کنار هر feature یک عدد هست که بهش weight یا coefficient (ضریب) میگن
# اینا ضرایب مدل ما هستن و یکیش منفی هست پس یعنی ممکنه ضراب منفی داشته باشیم
# برای همین میایم به توان 2 میرسونیم که همه مقادیر مثبت بشه


"What does Ridge do?"
# در Ridge میایم میگیم بیا وزن های بزرگ رو جریمه کن
# وزن یا weight میشه همون a و b و ...
# حتی اگه مدل خوب هم پیشبینی کنه یعنی این Σ(y - ŷ)² کم باشه
# ولی اگه با وزن های بزرگ λΣw² این کار رو انجام بده، loss function بازم یک عدد بزرگ میشه

# پس مدل Ridge سعی میکنه نه تنها خوب پیشبینی کنه، بلکه وزن‌هارو هم تا جاییکه میشه بیاره پایین
# درواقع مدل Ridge بوسیله penalty L2 میاد weight رو کم میکنه تا دقت محاسبه loss function بره بالا
# درواقع بین Prediction error و Regularization یک تعادل بوجود میاره جوریکه به کمترین loss برسه

#                Loss Function
#        ┌──────────────────────────────┐
#        │ Prediction Error             │
#        │ Σ(y - ŷ)²                    │
#        └──────────────┬───────────────┘
#                       +
#        ┌──────────────▼───────────────┐
#        │ Regularization (Penalty)     │
#        │ λ Σw²                        │
#        └──────────────┬───────────────┘
#                       ▼
     #      مدل Ridge مقدار مجموع این دو را      
   #        تا حد ممکن کوچک می‌کند              


"important tip"
# در فرمول محاسبه loss توسط Ridge یعنی min(Σ(y - ŷ)² + λΣw²) ما 2 بخش جدا از هم داریم
# قسمت اول یعنی Σ(y - ŷ)² فقط مجموع نمونه ها یا همون ردیف های دیتای ما هست
# قسمت دوم یعنی λΣw² اصلا کاری با تعداد Sample یا نمونه و ردیف نداره
# این قسمت فقط ضریب‌هارو به توان 2 میرسونه و باهم جمع میکنه و فقط با تعداد feature ها کار داره


"What is L1 and L2 ?"
# اینجا L مخفف Norm (Length / Magnitude) هست
# در ریاضیات، برای اندازه‌گیری بزرگی یک بردار، چند روش مختلف وجود دارد که به آن‌ها Norm می‌گویند
# دو مورد معروف آن:
    # L1 Norm
    # L2 Norm

# اینجا L2 که مربوط به Ridge هست رو توضیح میدیم و L1 مربوط به Lasso میشه
# حالا L1 یعنی چی؟
#  یعنی مجموع قدر مطلق (Absolute Value) وزن‌ها را جریمه کن
    # w₁=2, w₂=-0.5, w₃=3  =>  L1=|2|+|-0.5|+|3| = 5.5

# حالا L2 چیه؟ یعنی مجموع مربع (Square) وزن‌ها را جریمه کن
    # L2 = 2² + (-0.5)² + 3² = 38

# پس مدل های Lasso و Ridge فقط از این دو نوع Norm برای ساختن عبارت جریمه (Penalty) در تابع هزینه استفاده می‌کنند



"Ridge regression in scikit-learn"
# در فرمول Ridge در sklearn به جای λ از alpha استفاده می‌کند و قسمت Error را بر 2n تقسیم می‌کند
# Loss= 1/2n(​∑(y−y^​)2 + α∑w2)
# آلفا میزان شدت جریمه رو مشخص میکنه

from sklearn.linear_model import Ridge
model = Ridge(alpha=1.0)

# alpha = 0 --> Linear Regression
# alpha = 10 --> سختگیر









#===========================================================
"========== Lasso Regression (L1 Regularization) =========="
#===========================================================

# Lasso loss function = min(Σ(y - ŷ)² + λΣ∣w∣)
# تفاوت Lasso با Ridge اینه که در Lasso به جای مربع وزن‌ها، قدر مطلق وزن‌ها را جمع می‌کنیم
# در Ridge پنالتی w² هست ولی در Lasso پنالتی ∣w∣ هست


"main difference betweeen Lasso and Ridge?"
# در Ridge مثلا اگه ضرایب به اینصورت باشن:
    # 6 8 3 7
# تهش Ridge اونارو بخوام کم بکنه میشه این:
    # 5 6 2 7
# پس ضرایب کاهش پیدا میکنن ولی هیچوقت دقیقا صفر نمیشن
# یعنی تاثیر یک Feature رو ممکنه کم کنه، ولی هیچوقت 0 نمیکنه

# حالا اگه همین وزن هارو به Lasso بدیم ممکنه بعضی ها صفر بشن:
    # 0 0 3 6
    

"Whats is feature selection in Lasso?"
# اگر Lasso بعضی ضرایب رو صفر کنه چه تاثیری داره؟
# تاثیر Lasso بر رابطه زیر رو میبینیم:
    # y= 2×distance +5×speed +3×traffic +7×rain+10
    # y= 2×distance +0×speed +3×traffic +0×rain+10

# میبینیم که با ضریب 0 دوتا feature رو عملا از رابطه حذف کرد و مدل دیگر از آنها استفاده نمیکند
# فرض کنیم 100 تا Feature داریم و فقط از بین اینا 10 تاش واقعا مفیده
# خود Lasso میاد این 10 تارو پیدا میکنه و هر کدون بی‌فایده باشه تشخیص میده و وزنش رو 0 میکنه
# به همین دلیل است که Lasso علاوه بر کاهش بیش‌برازش، یک روش بسیار محبوب برای انتخاب خودکار ویژگی‌های مهم نیز محسوب می‌شود


"Lasso in scikit-learn"
# در Lasso هم مثل Ridge در فرمولش تغییر داریم و آلفا جایگزین میشه:
    # Loss= 1/2n(​∑(y−y^​)2 + α∑|w|)
    
from sklearn.linear_model import Lasso
model = Lasso(alpha=1)

# alpha = 0 --> Linear Regression
# alpha = 10 --> سختگیر






#====================================================================
"========== Elastic Net Regression (L1/L2 Regularization) =========="
#====================================================================

# این مدل ترکیبی از Ridge و Lasso هست
# یعنی میگه من بعضی وزن هارو صفر میکنم، هم بعضی هارو نزدیک 0 میبرم

# Lasso = Prediction Error + L1 Penalty
# Ridge = Prediction Error + L2 Penalty
# Elastic Net = Prediction Error + L1 Penalty + L2 Penalty

#  در این مدل فرمول loss function اینجوری میشه:
    # loss = min(Σ(y - ŷ)² + λΣ∣w∣ + λΣw²)
#                ___|         |       |
#               ↓             ↓       ↓
#    Prediction Error       Lasso     Ridge
#      (sample)            (weight/feature)


"Real usage of Elastic Net?"
# مثلا دیتاست پزشکی داریم که 100 تا feature داره ولی فقط 20 تا ستونش دیتای ارزشمندی هست
# Ridge -> وزن هر 100 ویژگی رو کم میکنه
# Lasso -> همه ویژگی ها 0 میشه غیر از اون 20 ستون
# Elastic Net -> میاد علاوه بر اون 20 ستون، 5 تا دیگه هم کم میکنه نگه میداره و بقیه 0 میکنه

"Why not always use Lasso?"
# مشکل Lasso اینه که بین ستون های مشابه یکی رو حذف میکنه
# Height (cm)       Income in Dollar
# Height (m)        Income in Euro
# ولی EN بین اینا میاد تعادل ایجاد میکنه


"example"
# فرض میکنیم مدیر یک شرکت هستیم با 10 تا کارمند
# مدل Ridge میگه همه کارمندها بمونن ولی کمتر کار کنن
# مدل Lasso میگه 5 تا کارمند مفید نیستن و اخراج بشن و فقط افراد مفید بمونن
# مدل EN میگه 5 تا کارمند بی فایده اخراج بشن و افراد مفید ساعت کاریشون متعادل تر بشه



"Elastic Net in scikit-learn"
   
from sklearn.linear_model import ElasticNet
model = ElasticNet(alpha=100, l1_ratio=0.5)
 # در پیاده‌سازی EN در scikit-learn معمولاً به‌جای دو پارامتر جداگانه λ1 و λ1 از l1_ratio و alpha استفاده میشه
# یعنی در عمل در هنگام کدزنی بجای فرمول های بالا (فقط جنبه آموزشی دارن) از این دو پارامتر استفاده میشه

"1- l1_ratio"
# مهمترین پارامتر این مدل، l1_ratio هست
# در واقع این پارامتر سهم L1 در مقابل L2 هست و مشخص میکند از مقدار Penalty چه مقدارش L1 باشه و چقدش L2
# اکر مقدار این l1_ratio بشه 1 سهم L1 میشه 100% و سهم L2 میشه 0 و مدل تقریبا Lasso میشود
# اگر مقدارش 0 بشه مقدار L1 میشه 0 و L2 میشه 100 و مدل تقریبا Ridge میشود
# اگر مقدارش 0.5 بشه یه تعادلی از هردو میشه
# اگر مقدارش برابر 0.8 باشه یعنی سهم L1 میشه 80% و سهم L1 میشه 20%

"2- alpha"
# یعنی شدت کلی Regularization
# مقدار آلفا مشخص میکنه شدت جریمه چقدر باشه
# اگر آلفا برابر 0 باشه مقدار جریمه 0 میشه و همان Linear Regression میشه
# اگر آلفا مثلا برابر 10 باشه یعنی به مدل میگه خیلی سختگیر باشه، ضرایب نباید بزرگ بشن









'''
================================================
================================================
=======            KNN Algorhitm         =======
================================================
================================================
'''
# درواقع KNN هم جزو الگوریتم‌های Supervised Learning است، اما دو نسخه دارد:
    # KNeighborsRegressor → Supervised  Nonlinear Regression
    # KNeighborsClassifier → Supervised Classification → این مدلش معروف تره

# سایر مدلها یک معادله رو یاد میگیرن و درواقع train میشن:
    # y=ax+b

#اما KNN اصلاً هیچ معادله‌ای یاد نمی‌گیرد. به همین دلیل فرمول Loss Function یا Regularization ندارد
# درواقع KNN فقط داده‌های آموزشی را ذخیره می‌کند و هنگام پیش‌بینی، نزدیک‌ترین نمونه‌ها را پیدا می‌کند

"what is K?"
# باید یک عدد K انتخاب کنیم و براساس اون عدد میره نزدیک ترین همسایه هارو پیدا میکنه
# K=1 نزدیک ترین همسایه
# K=3 نزدیک ترین 3 همسایه
# K=10 نزدیک ترین 10 همسایه


"KNN Regression"
# یک دیتاست داریم که دما و فشار رو اندازه گرفته
#   Temp | UTS
#  ------------
#    20  | 400
#    40  | 540
#    80  | 860
# حالا یه دمای 50 درجه وارد میشه و میخوایم با KNN حساب کنیم فشار چقد میشه
# میاد از توی دیتاست نزدیک ترین دماها به 50 رو پیدا میکنه که 40 و 80 هستن
# سپس فشارهارو درمیاره و میگه میانگین فشارهای این دو دما، میشه پیشبینی فشار در دمای 26 درجه
# temp 26   (640+860)/2 = 500


"KNN Classification"
# دیتاست ما اینه
# Apple
# Apple
# Orange
# Orange
# Apple
# یه میوه جدید اومد و 3 همسایه نزدیکش اینا میشن:
# Apple
# Apple
# Orange
#و چونکه Apple دو رای داره مدل میگه Apple


"Difference"
# در Regression از همسایه ها میانگین میگیره
# در Classification بر اساس رای‌گیری نظر میده

"What happens when we fit KNN?"
# وقتی با model.fit(X,y) میایم مدل KNN رو فیت میکنیم در واقع آموزشی اتفاق نمیوفته
# فقط میاد دیتاهارو ذخیره میکنه
# اینجا هیچ معادله‌ای ساخته نمی‌شود و هیچ وزن (Weight) یاد گرفته نمی‌شود

"What happens when we predict with KNN?"
# model.predict(...)
# با predict میاد براساس K نزدیک ترین همسایه(ها) رو انتخاب میکنه
# حالا براساس اینکه Regression هست یا Classification یا میانگین میگیره یا رای‌گیری میکنه

"Euclidean Distance"
# حالا KNN چطوری فاصله دو نقطه از همدیگه رو محاسبه میکنه؟
# معروف ترین رابطه محاسبه فاصله دو نقطه از هم، فاصله اقلیدوسی هست
# d=radical(x1​−x2​)²+(y1​−y2​)²


"KNN regression scikit-learn"
from sklearn.neighbors import KNeighborsRegressor
model = KNeighborsRegressor(n_neighbors=5, weights="uniform", metric="euclidean")
# اینجا n_neighbors=5 یعنی 5 همسایه نزدیک رو پیدا کن
# وقتی وزن میذاریم روی uniform یعنی همه همسایه ها وزن مساوی دارن
# این "weights="distance یعنی نمونه نزدیکتر اهمیت بیشتری دارد
# با پارامتر metric میتونیم نحوه محاسبه فاصله رو برای مدل مشخص کنیم
# metric="euclidean"  | metric="manhattan"


"KNN classification scikit-learn"
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=5, weights="uniform", metric="euclidean")


"KNN doesnt calculate these parameters ❌"
# Loss Function
# Gradient Descent
# Regularization










'''
=====================================================================
=====================================================================
=======            Parametric & Non-Parametric Models         =======
=====================================================================
=====================================================================
'''
# Regression models can be devided into two groups:

"Parametric Models"
# این مدلها پارامتر(وزن) یاد میگیرن:
    # LinearRegression
    # Ridge
    # Lasso
    # ElasticNet
    # SGDRegressor
# در این مدلها Loss Function و optimization algorithm داریم

"Non-parametric Models"
# یکی از معروف تریناش KNN هست
# هیچ وزنی یاد گرفته نمی‌شود و هیچ تابع هزینه‌ای کمینه نمی‌شود
# فقط داده‌های آموزشی ذخیره می‌شوند و هنگام پیش‌بینی،
# نزدیک‌ترین همسایه‌ها بر اساس یک معیار فاصله (مثل Euclidean Distance) پیدا می‌شوند











'''
=====================================================================
=====================================================================
=======        Decision Tree (Non-linear regression)          =======
=====================================================================
=====================================================================
'''

# درواقع Decision Tree اصلاً معادله پیدا نمی‌کند بلکه مجموعه‌ای از سؤال‌های پشت سر هم می‌سازد
# کل مدل از سوال های yes/no تشکیل شده
# داده -> جدا کردن feature موردنظر با بهترین Split -> ساخت Root -> ساختن شاخه ها -> ساخت Leaf -> ذخیره کردن درخت

# این مدل معادله y=ax+b یاد نمیگیره و weight آموزش نمیبینه
# همچنین برای Regression و Classification دو نسخه داره

"Decision Tree Regression"
# براساس دیتاستی که داریم اینقد درخت تصمیم گیری رو ادامه میده و سوالات yes/no میسازه
# تا درنهایت به یه جواب number به عنوان prediction برسه

# Temperature<80?
#  ┌────┴────┐
# Yes       No
#  │         │
# UTS=600  Temperature<150?
#       ┌────┴─────┐
#      Yes         No
#       │          │
#    UTS=450     UTS=300


"Decision Tree Classification"
# مثلا میخوایم بگیم میوه چیست؟
# خروجی number نیست و یک Class هست

#  color=red?
#  ┌────┴────────┐
# Yes           No
#  │             │
# Strawberry    round?
#           ┌────┴─────┐
#          Yes         No
#           │          │
#          ...       Orange


"Split Criterion"
# مدل چطوری تصمیم میگیره اولین سوال چی باشه؟
# با معیارهایی مثل "معیار تقسیم" میاد تصمیم میگیره
# اگه مثلا اول روی فلان Feature تقسیم کنم، چقدر داده‌ها بهتر از هم جدا میشن

# در معیار تقسیم، Regression و Classification با هم فرق دارند

#==============
#  Regression
#==============
# اینجا هدف اینه که هر شاخه تا جای ممکن اعداد مشابهی داشته باشه
# یعنی با هربار تقسیم میخواد تا جای ممکن پراکندگی داده هارو کمتر کنه تا زودتر به جواب برسه
# برای اندازه گیری این موضوع در Regression از Variance Reduction استفاده میشه
# یا در پیاده‌سازی sklearn از کاهش Mean Squared Error (MSE) استفاده می‌شود

#=================
#  Classification
#=================
# اینجا هدف خالص شدن کلاس ها در هر تقسیم است
# برای اینکار در Classification از معیارهایی مثل Gini Impurity یا Entropy استفاده میشه



"DT Regression in scikit-learn"
#--------------------------------------------------------
X = data[['distance', 'prep_time', 'traffic', 'speed']]
y = data['delivery_time']
from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor(criterion="squared_error", max_depth=3, min_samples_split=2, min_samples_leaf=5, random_state=42)
# این criterion="squared_error" یعنی از MSE برای انتخاب بهترین split استفاده کن
# Criterion="absolute_error"
# این max_depth=3 یعنی درخت بیشتر از 3 لایه رشد نکنه و مهمترین پارامتر برای جلوگیری از overfitting هست
# این min_samples_split=2 یعنی برای تقسیم هر گره حداقل 2 نمونه وجود داشته باشه
# هرچی min_samples_split=2 عددش بیشتر باشه درخت کمتر شاخه دار میشه
# این min_samples_leaf=5 یعنی هر برگ حداقل 5 برگ داشته باشه (جلوگیری از overfitting)
# این random_state برای اینه که هربارنتیجه یکسان باشه
# این max_depth=None یعنی درخت تا جایی که بتواند رشد میکن
model.fit(X, y)
new_data = [[4, 12, 3, 40]]
prediction = model.predict(new_data)
print(prediction)  # e.g. 25


"DT Classification in scikit-learn"
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(criterion="gini", max_depth=None, min_samples_split=2, min_samples_leaf=5, random_state=42)
# criterion="entropy"
model.fit(X, y)
prediction = model.predict(new_data)
print(prediction)  #e.g. Apple



"Decision Tree doesnt calculate these parameters ❌"
# Loss Function  ->  instead chooses the best split
# Gradient Descent
# Regularization


"Tree rules"
# برای مشاهده قوانینی که مدل روی درخت گذاشته به این ترتیب عمل میکنیم
from sklearn.tree import export_text
rules = export_text(model, feature_names=list(x.columns))
print(rules)


"Draw matplotlib"
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
plt.figure(figsize=(12,6))
plot_tree(model, feature_names= x.columns, class_names=("Apple","Orange"), filled=True)
plt.show()











'''
===============================================
===============================================
=======        Ensemble Models          =======
===============================================
===============================================
'''

# درکل Ensemble یعنی ترکیب چند مدل یادگیری برای ساختن یک مدل قوی‌تر
# به جای اینکه به تصمیم یک مدل اعتماد کنیم، از تصمیم چند مدل استفاده کنیم

# مدل‌های معمولی مثل:  Linear Regression - Decision Tree - KNN - SVM هر کدام به تنهایی پیش‌بینی می‌کنند
# اما مدل‌های Ensemble از چند مدل پایه (Base Learner) استفاده می‌کنند و خروجی آن‌ها را ترکیب می‌کنند

# Ensemble Models
# │
# ├── Bagging
# │   ├── Bagging Regressor
# │   ├── Bagging Classifier
# │   └── Random Forest    معروف ترین مدل این گروه
# │
# ├── Boosting
# │   ├── AdaBoost
# │   ├── Gradient Boosting
# │   ├── XGBoost
# │   ├── LightGBM
# │   └── CatBoost
# │
# └── Stacking
#     ├── Stacking Regressor
#     └── Stacking Classifier

# 1- Bagging (Bootstrap Aggregating)
# چند مدل را به صورت مستقل و همزمان آموزش بده، سپس میانگین یا رأی‌گیری بگیر

# 2- Boosting
# مدل‌ها را پشت سر هم آموزش بده و هر مدل جدید روی اشتباهات مدل قبلی تمرکز می‌کند

# 3- Stacking
# چند مدل مختلف را آموزش بده
# سپس یک مدل دیگر یاد بگیرد که چگونه خروجی آن‌ها را با هم ترکیب کند




"======= Random Forest model ========"
# در واقع Random Forest از تعداد زیادی Decision Tree ساخته شده است
# یعنی بجای اینکه فقط یک Decision tree داشته باشیم، جنگلی از درخت ها میسازه
# همه این درختها با هم کار میکنن
# مشکل Decision Tree این است که خیلی راحت Overfitting می‌کند برای همین از Random Forest استفاده میکنیم
# این مدل یک الگوی کلی هست که 2 نسخه برای Regression و Classification داره

# چرا بهش میگن Random؟ چون در ساخت هر درخت 2 چیز را بصورت رندوم انتخاب میکنه:

    # 1-نمونه‌های آموزشی (Bootstrap)     
# فرض کنیم 1000 تا sample داریم. درخت شماره 1 ممکنه نمونه شماره 1 باشه یا 13 یا 800     
# درواقع هر درختی داده متفاوتی میبینه. درخت شماره 2 ممکنه مثلا داده شماره 945 رو بگیره و ...     

# 2-ویژگی یا Feature     
# فرض کنیم 6 تا Feature داریم. درخت 1 ممکنه Feature های شماره 1 و 3 رو بگیره     
# درخت شماره 2 ممکنه Feature های شماره 2 و 6 رو بگیره و غیره ...     


# ❌ این مدل هیچکدوم از موارد زیر رو نداره:
# معادله    
    # Weight
    # Gradient Descent
    # Loss Function
    

''''''''''''''''''''''''''''''''''''''''''''''''''
#===== Random Forest Regression in sklearn =======
# فرض کنیم 10 تا درخت داریم که هرکدوم یک عددی رو پیشبینی میکنه
# برای Regression در Random forest میانگین میگیریم از درختها
# Tree1 -> 20
# Tree2 -> 32        Prediction = (20+32+...+14)/10
# ...
# Tree10 -> 14

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(bootstrap=True, n_estimators=100, max_depth=5, criterion="squared_error", max_features="sqrt", min_samples_split=5, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
# وقتی bootstrap=True باشه میاد نمونه‌هارو بصورت sample sample برمیداره تا درختها باهم متفاوت بشن
# این n_estimators=100 یعنی 100 تا Decision Tree بسازه
# این max_depth=5 یعنی هر درخت بیشتر از 5 لایه نسازه
# این max_depth=None یعنی هر درخت تا جایی که بتواند رشد میکند
# criterion="squared_error" or "gini
# پارامتر max_features مهمترین تفاوت DT و RF میباشد
# این پارامتر مشخص میکند هر درخت در هر split چند feature اجازه داره بررسی کنه
# مثلا این "max_features="sqrt یعنی اگر مثلا 16 تا Feature داشته باشیم هر split فقط 4 تا feature رو بررسی میکنه
# این min_samples_split حداقل تعداد نمونه برای هر split رو مشخص میکنه
# این min_samples_leaf حداقل تعداد نمونه داخل هر leaf رو مشخص میکنه
# این random_state برای اینه که هربار همان جنگل ساخته بشه، نه جنگلهای متفاوت

import pandas as pd
importance = pd.Series(model.feature_importances_, index=x.columns)
print(importance.sort_values
importance = [0.42,0.31,0.15,0.08]
# income 0.42     this feature is the most important
# age 0.31
# city 0.15
# gender 0.08
# بعد از fit کردن میتونیم اهمیت هر feature رو ببینیم
''''''''''''''''''''''''''''''''''''''''''''''''''


''''''''''''''''''''''''''''''''''''''''''''''''''
#===== Random Forest Classification in sklearn ===
# در classification هر درخت یک رای داره و را‌ی‌گیری میشه
# در انتها هر رایی بیشتر بود همون انتخاب میشه
# Tree1 -> Apple
# Tree2 -> Orange
# Tree3 -> Apple      Prediction = Apple
# ...
# Tree10 -> Apple

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(bootstrap=True, n_estimators=100, max_depth=5, criterion="squared_error", max_features="sqrt", min_samples_split=5, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
''''''''''''''''''''''''''''''''''''''''''''''''''

    
# ______________________________________________________________
# |          Decision Tree               |   Random Forest     |
# |--------------------------------------|---------------------|
# |   یک درخت تصمیم    |       تعداد زیادی درخت تصمیم       |  
# |   مستعد Overfitting | مقاومت بیشتر در برابر Overfitting  |  
 # |         سریع‌تر      |               کمی کندتر             |  
# |  تفسیر بسیار آسان  |              تفسیر سخت‌تر            |  
# |        دقت خوب      | معمولاً دقت بالاتر و پایداری بیشتر   |  
# --------------------------------------------------------------




"========Bagging========"
from sklearn.ensemble import BaggingClassifier
model = BaggingClassifier(n_estimators=100, random_state=42)

from sklearn.ensemble import BaggingRegressor
model = BaggingRegressor(n_estimators=100, random_state=42)


"========AdaBoost========"
from sklearn.ensemble import AdaBoostClassifier, AdaBoostRegressor
model = AdaBoostClassifier(n_estimators=100, random_state=42)
model = AdaBoostRegressor(n_estimators=100, random_state=42)


"========Gradient Boosting========"
from sklearn.ensemble import GradientBoostingClassifier, GradientBoostingRegressor
model = GradientBoostingClassifier(n_estimators=100, random_state=42)
model = GradientBoostingRegressor(n_estimators=100, random_state=42)


"========XGBoost========"
from xgboost import XGBClassifier, XGBRegressor
model = XGBClassifier(n_estimators=100, random_state=42)
model = XGBRegressor(n_estimators=100, random_state=42)


"========LightGBM========"
from lightgbm import LGBMClassifier, LGBMRegressor
model = LGBMClassifier(n_estimators=100, random_state=42)
model = LGBMRegressor(n_estimators=100, random_state=42)


"========CatBoost========"
from catboost import CatBoostClassifier, CatBoostRegressor
model = CatBoostClassifier(n_estimators=100, random_state=42, verbose=0)
model = CatBoostRegressor(n_estimators=100, random_state=42, verbose=0)


"========Stacking Classifier========"
from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
model = StackingClassifier(
    estimators=[('rf', RandomForestClassifier()), ('svc', SVC())],
    final_estimator=LogisticRegression()  )


"========Stacking Regressor========"
from sklearn.ensemble import StackingRegressor
from sklearn.linear_model import LinearRegression, Ridge
model = StackingRegressor(
    estimators=[('ridge', Ridge()), ('lr', LinearRegression())],
    final_estimator=LinearRegression()  )













'''
============================================================
============================================================
=======        Support Vector Machine (SVM)          =======
============================================================
============================================================
'''

#                    AI
#                    | 
#                    ML
#                    |
#              Supervised ML
#                    |
#          ---------------------
#          |                   |
#    Classification        Regression
#          |                   |
#     SVC, linearSVC         SVR, linearSVR   

#          ____ Support Vector Classification = SVC
# SVM ----|____ Support Vector Regression = SVR

# بنابراین SVM یک الگوریتم Supervised Learning است که دو نسخه هم برای Reg هم برای Cls داره
# مهمترین مدل SVM برای classification در scikit-learn مدل SVC هست
# مهمترین مدل SVM برای Regression در scikit-learn مدل SVR هست


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"SVM Idea"
# ما در LogisticRegression میگفتیم یک خط پیدا کن که کلاسهارو از هم جدا کنه
# ولی در SVM میگیم نه تنها این خط باید کلاسهارو از هم جدا کنه، بلکه بیشترین فاصله از دیتاهارو داشته باشه
# یعنی نه تنها این خط باید خوب predict کنه بلکه باید یک margin خوب هم داشته باشه


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"Support Vector"
# این مهمترین مفهوم SVM است که میگه همه داده‌ها مهم نیستند
# فقط نزدیک‌ترین داده‌ها به مرز تصمیم مهم هستند

# در مثال زیر آن دو نقطه ● را Support Vector می‌گویند
# مدل فقط با همین نقاط مرز را تعیین می‌کند
# بقیه داده‌ها تقریباً تأثیری ندارند

# 🔴 🔴 
#   ●
# ────────────
#     ●
# 🔵 🔵


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"Margin"
# این مفهوم یعنی فاصله بین مرز تصمیم و Support Vector ها
# هدف SVM این است که این فاصله تا جای ممکن بزرگ باشد
# در مد ما پارامتری بنام C داریم که اگه عددش زیاد باشه مدل hard margin میشه
# یعنی با هر زوری شده میخواد حتما با یه خط در بهترین حالت کلاسهارو از هم جدا کنه
# برعکسش رو اگه انجام بدیم میشه soft margin

# 🔴 🔴 ●
# 
# ──────────────
#
# ● 🔵 🔵


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"Kernel"
# اگر داده ها مثل این مورد قابل جداسازی نباشن دیگه نمیشه با یه خط صاف از هم جداشون کرد
# در این مواقع SVM از kernel استفاده میکنه
# 🔴 🔴 🔵
# 🔵 🔴 🔵

# این Kernel داده‌ها را به فضای بزرگ‌تر می‌برد تا قابل جدا شدن شوند
# به همین دلیل SVM می‌تواند روابط غیرخطی را هم یاد بگیرد

# famous kernels:
    # Linear
    # Polynomial
    # RBF
    # Sigmoid

# این kernel مشخص می‌کند SVM با چه نوع مرزی داده‌ها را جدا کند
# 1- kernel='linear'
# مرز تصمیم یک خط مستقیم است -------    
# مناسب وقتی که داده‌ها تقریباً خطی هستند    
# 2- kernel='poly'
#در نوع polynominal مرز چند جمله‌ای میشود    
# مثلا ~~~~~~~~~~    
# 3- kernel='rbf'
# پرکاربردترین kernel هست که خطهای منعطف میسازه    
# اگر داده‌ها غیرخطی باشند، معمولاً اولین انتخاب است    
# 4- kernel='sigmoid'
# رفتارش شبیه یک نورون در شبکه عصبی است    


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"SVM Classification"
# ایده اصلی SVM اینه که بهترین مرز (Best Boundary) را بین داده‌ها پیدا کنه:
# مرز بین این دو کلاس را کجا رسم کنیم؟
# اینجا SVM میاد میگه من با مدل SVC بهترین خط رو برات پیدا میکنم
# بهترین خط چیه؟ SVM میگه بهترین خط، خطی هست که بیشترین فاصله را از هر دو کلاس داشته باشه

# 🔴 🔴 🔴
# 🔴 🔴              Apple 🔴

# ------------------

#        🔵 🔵       Orange 🔵
#    🔵 🔵 🔵

from sklearn.svm import SVC
model = SVC(C=1.0, kernel='rbf', gamma='scale')


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"SVM Regression"
# اینجا برعکس classification دیگه کلاس نداریم و میخوایم عدد پیشبینی کنیم
# اما برخلاف Linear Regression دیگه SVM دنبال کمترین خطا نیست
# ایده آن این است: تا وقتی خطا از یک مقدار مشخص کمتر باشد، مهم نیست
# این مقدار را ε (Epsilon) می‌نامند

# مثلا اگه داده واقعی 100 باشه و پیشبینی 101 باشه و مثلا epsilon=2 باشه SVM میگه این خطا مهم نیست
# ولی اگه مثلا پیشبینی 110 باشه خطا زیاده و مدل جریمه میشه

from sklearn.svm import SVR
model = SVR(C=1.0, kernel='rbf', gamma='scale')


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"ُSVM parameters"
# (C=1.0, kernel='...', gamma='scale', degree=2, coef0=0)

# C
# پارامتر C میزان سخت‌گیری مدل نسبت به خطاها را مشخص می‌کند
# این پارامتر مشخص میکند مدل چقدر تلاش کند همه داده‌ها را درست طبقه‌بندی کند؟
# فرض میکنیم داده های زیر رو داریم و یکی از قرمزها نزدیک آبی ها افتاده
# 🔴 🔴 🔴
#  
# 🔴
#
#  🔵 🔵 
#   🔵
# 🔵 🔵 🔵
# اگر C خیلی بزرگ باشه مثلا C=1000 مدل می‌گوید باید حتی همین یک نقطه را هم درست طبقه‌بندی کنم
# در نتیجه مرز تصمیم پیچیده‌تر می‌شود، خطای train کم میشود، احتمال overfitting زیاد میشود

# اگر مقدار C خیلی کوچک باشد مثلا C=0.01 مدل می‌گوید اشکالی ندارد چند نقطه اشتباه شوند
# در نتیجه مرز ساده‌تر می‌شود، Generalization بهتر میشود و ممکن است کمی underfitting اتفاق بیوفتد


# kernel
kernel='linear'
kernel='rfb'
kernel='poly'
kernel='sigmoid'


# gamma
# این پارامتر فقط برای Kernelهای غیرخطی مثل: RBF - Polynomial - Sigmoid استفاده می‌شود
# این پارامتر مشخص می‌کند هر Support Vector تا چه فاصله‌ای روی مرز تصمیم اثر بگذارد
# فرض کن یک Support Vector داریم. اگر gamma کوچک باشد مثلا gamma=0.01
# اثر این نقطه تا فاصله زیادی ادامه پیدا می‌کند
# در نتیجه مرز نرم و صاف تر میشه و Generalization  بهتر اتفاق میوفته
# اگر gamma بزرگ باشد مثلا gamma=100
# اثر نقطه فقط اطراف خودش است
# در نتیجه مرز پیچیده میشه و ممکنه overfitting اتفاق بیوفته
# این مقدار 'gamma='scale بصورت پیش فرض انتخاب مناسبی هست
# و scikit-learn خودش مقدار مناسبی را از روی داده‌ها حساب می‌کند

 
# ❌ kernel=linear
# اگر kernel=linear باشه نه gamma داره و نه degree
# چون مرز تصمیم فقط یک خط (یا هایپرپلین) است و چیزی برای خم شدن وجود ندارد


# kernel=poly
# در کرنل polynomial علاوه بر c و gamma، پارامتر degree و coef هم داریم
# حالا Degree یعنی چی؟ درجه چندجمله‌ای را مشخص می‌کند
# مثلا اگه degree=2 باشه مدل رابطه درجه 2 رو یاد میگیره مثل x²
# هرچه degree بیشتر شود، مرز تصمیم پیچیده‌تر می‌شود و احتمال Overfitting بیشتر می‌شود
# polynomial formula  -->  K(x,x′)=(γxTx′+coef0)**degree
# در این فرمول gamma (γ) تعیین می‌کند ورودی‌ها قبل از اعمال توان چقدر مقیاس شوند
# و degree تعیین می‌کند توان چند باشد
# همچنین coef0 یک مقدار ثابت است که به حاصل ضرب اضافه می‌شود


# kernel=sigmoid
# اصلا degree نداره چون اصلاً چندجمله‌ای نیست


# coef0
# یک عدد ثابت است که به فرمول Kernel اضافه می‌شود و روی شکل مرز تصمیم اثر می‌گذارد
# در Polynomial، مقدار آن مشخص می‌کند جمله ثابت در چندجمله‌ای چقدر تأثیر داشته باشد
# در Sigmoid، مانند مقدار بایاس (Bias) در تابع سیگموید عمل می‌کند
# در بیشتر پروژه‌های معمولی، مقدار پیش‌فرض (coef0=0) کافی است و کمتر نیاز به تغییر آن پیدا می‌شود


# __________________________________________
# | Kernel  |  C  | gamma | degree | coef0 |
# |---------|-----|-------|--------|-------|
# | linear  | ✅ |  ❌   |  ❌    |  ❌  |
# | rbf     | ✅ |  ✅   |  ❌    |  ❌  |
# | poly    | ✅ |  ✅   |  ✅    |  ✅  |
# | sigmoid | ✅ |  ✅   |  ❌    |  ✅  |
# ------------------------------------------


#  ✅ relationship between C and gamma
# __________________________________________________________________
# |                    result                     | gamma | C      |
# |-----------------------------------------------|----------------|
# |   کوچک | کوچک  |  مدل ساده (ممکن است Underfitting شود)       |  
# |   بزرگ | کوچک  |  مرز نسبتاً صاف ولی تلاش زیاد برای کاهش خطا  |  
# |   کوچک | بزرگ  | مرز نسبتاً پیچیده ولی جریمه خطا کم          |  
# |  بزرگ | بزرگ  |  مرز بسیار پیچیده (احتمال Overfitting زیاد) |  
# ------------------------------------------------------------------





''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"SVC - linearSVC"

# خیلی‌ها فکر می‌کنند LinearSVC فقط نسخه سریع‌تر SVC است، اما تفاوت‌های مهم‌تری هم دارند

# Support Vector Machine (SVM)

# Classification
# ├── SVC ⭐
# ├── LinearSVC
# └── NuSVC

# Regression
# ├── SVR ⭐
# ├── LinearSVR
# └── NuSVR

# درکل SVC میتونه هم خطی باشه هم غیر خطی و در این زمینه خیلی منعطفه
from sklearn.svm import SVC
model = SVC(kernel="linear")
model = SVC(kernel="rbf")
model = SVC(kernel="poly")
model = SVC(kernel="sigmoid")

# درحالیکه lienarSVC فقط خطی را پشتیبانی میکند
# اصلا پارامتر kernel نداره و فقط روی linear تنظیم شده
from sklearn.svm import LinearSVC
model = LinearSVC()

# اگر داده ها اینجوری باشن هردوتا یعنی SVC و linearSVC میتونن انجان بدن
# 🔴 🔴 🔴
# ------------------   linear
# 🔵 🔵 🔵

# ولی اگر داده ها اینجوری باشه فقط SVC میتونه با kernel=rbf یک منحنی رسم کنه و یادگیری داشته باشه
#    _______
# 🔴/ 🔵   \ 🔴
#  /   ___   \
# /🔵 /🔴|🔵\
# |___|   |___|

# چرا LinearSVC وجود دارد؟
# چون اگر مطمئن باشیم داده‌ها تقریباً خطی هستند، استفاده از Kernel اضافی فقط سرعت را کم می‌کند
# پس LinearSVC  برای داده‌های بزرگ خیلی سریع‌تر از SVC است
# در عوض اگه SVC روی دیتاستهای بزرگ سرعتش کمتر باشه، انعطاف بیشتری در یادگیری داره



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"SVR - linearSVR"
from sklearn.svm import SVR
model = SVR(kernel="linear")
model = SVR(kernel="rbf")
model = SVR(kernel="poly")
model = SVR(kernel="sigmoid")


from sklearn.svm import LinearSVR
model = LinearSVR()  #no kernel - only linear


# اگر رابطه مثلا بین temperature و UTS خطی باشه و دیتا بزرگ باشه از lienarSVR استفاده میشه
# اگر رابطه غیر خطی باشه میتونیم از SVR استفاده کنیم











'''
========================================================================
========================================================================
=======        Hyperparameter tuning in machine learning         =======
=======               overfitting - underfitting                 =======
========================================================================
========================================================================
'''

#==========================
"Machine Learning Protocol"
#==========================

"Regressor models"
# در کل مدلهای Regressor میخوان رابطه a و b رو پیدا کنن و در انتها y رو پیشبینی کنن
# همچنین میخوان با استفاده از متریک ها (MAE , MSE , RMSE, MAPE) فاصله بین پیشبینی و واقعیت رو بصورت عددی نشون بدن
# بوسیله این متریک‌ها هم evaluation انجام میشه و هم loss function بدست میاد
# وقتی در این مدلها میگیم دقت فلان مدل 90% هست یعنی هر پیشبینی باهاش انجام بدیم، 10% بالا پایین (خطا) ممکنه داشته باشه


"Classifier models"
# مدلهای Classifier میخوان دو یا چند گروه رو از هم تقسیم کنن
# در این مدلها هم متریک‌ها برای Evaluation استفاده میشه و هم loss function بدست میاد
# در این مدلها میخوایم در انتها درصد دقت رو محاسبه کنیم
# مثلا اگه بگیم فلان مدل 90% دقت داره یعنی یه خطی رسم کرده که از بین مثلا 2 گروه 9 تا از 10 تارو تونسته درست جدا کنه


"in common"
# هردو گروه این مدلها میان a و b رو بصورت رندوم initialize میکردن
# سپس با استفاده از روشهای هوشمند پارامترهای مختلف رو جوری تغییر میدادن که کمترین loss function محاسبه بشه


"models"
# Regressors : 
    # Linearregression , SGDRegressor
    # Ridge , Lasso , ElasticNet
    # KNeighborsRegressor
    # DecisionTreeRegressor
    # RandomForestRegressor
    # SVR

# Classifier:
    # Logisticregression 
    # SGDClassifier 
    # KNeighborsClassifier  
    # DecisionTreeClassifier
    # RandomForestClassifier
    # SVC



#===================
"Important Concepts"
#===================

"Parameter"
# چیزی هست که مدل یاد میگیره مثل model._coef یا model._intercept

"Hyperparameter"
# همون تنظیمات مدل هست که مقادیری بصورت پیش‌فرض داره
# اگه این مقادیر پیش‌فرض رو تغییر بدیم، کلا یادگیری مدل تغییر میکنه
# مثلا learning rate یا loss و ...



"overfitting vs underfitting"

#===============
# Underfitting |
#===============
# مدل های ماشین لرنینگ کارشون اینه که یه چیزی رو پیشبینی کنن
# هدفش این نیست که داده‌های آموزشی را حفظ کند، بلکه باید بتواند روی داده‌های جدید و ندیده هم درست پیش‌بینی کند
# مثلا در یک مدل ساده، در مثال زیر یک خط صاف میکشه و پیشبینی میکنه
# اگه خط خوب باشه پیشبینی هم خوب انجام میشه
# ●●●   ●● 
#  ●  ●  ●
# ──────────────
#    *    *
# **   *    *          

# اما اگه مدل خیلی ساده باشه با خط صاف نمیشه پیشبینی انجام داد
# در مثال زیر مشخصه که مدل با خط صاف نتونسته درست داده هارو یاد بگیره و آموزش ببینیه
# یعنی نتونسته به اندازه کافی fit بشه با دیتاها و میگن مدل underfitting شده

#     ●● /   * 
#   ● * /*  *  
# ● ● */ * ● *  *
#   ● / *   *  *

# بطور کلی underfitting یعنی مدل آن‌قدر ساده است که حتی الگوی اصلی داده را هم یاد نگرفته است
# مثلا معلم ریاضی 10 جلسه درس داده ولی دانش‌آموز فقط 1 جلسه رو خونده. قطعا نمیتونه درست آزمون بده چون کم یاد گرفته
# از ویژگی های underfitting اینه که هم Train error و هم Test error زیادی داره

# دلایل اتفاق افتادن underfitting:
# مدل بیش از حد ساده است    
# داده کافی آموزش ندیده است    
# تعداد Featureها کم است    
# آموزش خیلی زود متوقف شده است    

# چطور تشخیص بدیم؟ مثلا accuracy رو اندازه گرفتیم و این شده:
# میبینیم که هر دو ضعیف هستن پس underfitting اتفاق افتاده    
    # Train = 55%
    # Test = 52%

# چگونه underfitting را برطرف کنیم؟
# مدل پیچیده‌تر انتخاب کنیم
# بیایم Featureهای مفید بیشتری اضافه کنیم
# مدت آموزش را بیشتر کنیم (در مدل‌هایی که آموزش تکراری دارند)
# محدودیت‌های بیش از حد مدل را کاهش دهیم



#==============
# Overfitting |
#==============
# حالا اگه مدل خیلی پیچیده باشه میاد تک تک نقاط رو حفظ میکنه
# پس overfitting یعنی مدل علاوه بر الگوی اصلی، Noise و جزئیات تصادفی داده‌های آموزشی را هم یاد گرفته است
# مثلا دانش آموز بجای اینکه مفهوم را یاد بگیرد، تمام سوالهای سال قبل رو حفظ کرده
# اگر سر امتحان همان سوالها بیاد 20 میگیره ولی اگه سوال جدید بیاد 0 میگیره
# در Overfitting ما Train error کمی داریم ولی Test error زیاده

# مهمترین دلایل اتفاق افتادن overfitting:
    # مدل خیلی پیچیده است    
# داده آموزشی کم است    
# ویژگی‌های (Features) زیادی داریم    
# مدت آموزش زیاد است (مثلاً در شبکه‌های عصبی)    
# نویز زیادی در داده‌ها وجود دارد    

#     ●●    ●    ●●
#   ●  ______ ● ●
#   ●  | **  |__ ●●
#     ●| * * *  | ●
#  ●● / *  * ** /   ●
#  ● / ** _____/ ●
# ●  |____| ● ●

# از کجا بفهمیم overfitting اتفاق افتاده؟ فرض کنیم Accuracy رو حساب کردیم و این شده:
# اینجا Train خیلی قویه ولی Test ضعیف پس overfitting اتفاق افتاده    
    # Train = 99%
    # Test = 65%

# چگونه از overfitting جلوگیری کنیم؟
# داده آموزشی بیشتر جمع کنیم    
# مدل را ساده‌تر کنیم    
# از Cross Validation استفاده کنیم    
# از Regularization (مثل Ridge، Lasso، ElasticNet) استفاده کنیم    
# در Decision Tree بیایم max_depth را محدود کنیم    
# در Random Forest تعداد درخت‌ها و عمق را تنظیم کنیم    
# در Neural Network از Early Stopping و Dropout استفاده کنیم    



#============
# Good fit  | 
#============
# در این حالت مدل الگوی اصلی رو یاد گرفته
# فرض میکنیم Accuracy رو اندازه گرفتیم و شده این:
    # Train = 93%
    # Test = 91%
# هر دو مناسب هستن پس مدل خوب fit شده    



# __________________________________________________________________________
# |               ویژگی            | Underfitting | Good Fit | Overfitting |  
# |-------------------------|-------------|--------------------------------|
# |           پیچیدگی مدل         |  خیلی ساده |  متعادل  | خیلی پیچیده |  
# |       یادگیری الگوی اصلی     |      ❌     |    ✅    |     ✅      |  
# |          یادگیری نویز        |      ❌     |    ❌    |     ✅      |  
# |       پارامتر Train error     |     زیاد    |    کم    |  خیلی زیاد  |  
# |        پارامتر Test error     |     زیاد    |    کم    |     زیاد    |  
# |   قدرت تعمیم (Generalization) |     ضعیف    |   عالی   |     ضعیف    |  
# --------------------------------------------------------------------------

# __________________________________________________________________________________________________________________
# |            Model               |             Overfitting ↑             |             Underfitting ↑            |
# |--------------------------------|---------------------------------------|---------------------------------------|
# |      Linear Regression         |           Too many features           |             Nonlinear data            |
# |   Ridge / Lasso / ElasticNet   |               alpha↓                  |                 alpha ↑               |
# |        SGDRegressor            |       alpha ↓   max_iter ↑            |           alpha ↑    max_iter ↓       |
# |          Decision Tree         |   max_depth ↑    min_samples_leaf ↓   |    max_depth ↓     min_samples_leaf ↑ |
# |          Random Forest         |             max_depth ↑               |    max_depth ↓     n_estimators ↓     |
# |               KNN              |                 k ↓                   |                  k ↑                  |
# |         SVM (SVC / SVR)        |            C ↑   gamma ↑              |              C ↓    gamma ↓           |
# |      Polynomial Regression     |               degree ↑                |                degree ↓               |
# ------------------------------------------------------------------------------------------------------------------

# _____________________________________________________________________________
# |       Increase this...              |      Usually leads to...            |
# |-------------------------------------|-------------------------------------|
# |  max_depth, degree, C, gamma        |   More complex model → Overfitting  |
# |  alpha, k, min_samples_leaf         |   Simpler model → Underfitting      |
# -----------------------------------------------------------------------------




#======================================
"Overfitting/Underfitting in practical"
#======================================

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

x = np.arange(0,200,20)
y = 4 * x + np.random.randn(10)*73


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)


plt.scatter(x_train, y_train, label="train")
plt.scatter(x_test, y_test, label="test")
plt.legend()
plt.show()


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train.reshape(-1,1), y_train)
y_train_pred = model.predict(x_train.reshape(-1,1))
y_test_pred = model.predict(x_test.reshape(-1,1))


plt.scatter(x_train, y_train, label="true")
plt.plot(x_train, y_train_pred, label="prediction")    # این خط مدل ماست که با این دیتا آموزش دیده
plt.scatter(x_train, y_train_pred, label="prediction")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()


# محاسبه فاصله نقاطی که مدل پیشبینی کرده (نقاط نارنجی) با نقاطی که true هست
# یعنی میخوایم فاصله y_train با y_train_pred رو محاسبه کنیم

from sklearn.metrics import mean_absolute_error
mae_train_score = mean_absolute_error(y_train, y_train_pred)     # 61.30187192500656
# این مدل روی 8 عدد دیتا (نقاط نارنجی) train شده و +-60 خطا داره
# این خطا درواقع خطای train هست و این عدد نشونه میزان دقت مدل در پیشبینی نیست
# درواقع این 60 میگه که مدل کمترین میزان برای loss function که میتونست محاسبه کنه همینه
# این Train_score نشون میده که مدل در fit شدن با دیتایی که دیده، چقد موفق بوده


# تا الان روی دیتاهای train اومدیم مدل رو آموزش دادیم
# حالا میخوایم دیتاهای تست یعنی x_test و y_test رو رسم کنیم
# یعنی حالا ما مدل رو آوردیم که دیتای test رو پیشبینی کنه تا ببینیم چقد آموزش دیده
y_test_pred = model.predict(x_test.reshape(-1,1))
plt.scatter(x_test, y_test, label="true test")
plt.scatter(x_test, y_test_pred, label="prediction test")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()


# حالا میایم برای مقادیر test که مدل تاحالا ندیده بود و پیشبینی انجام داد،
# میخوایم مقدار خطا رو محاسبه کنیم تا ببینیم مدل برای پیشبینی دیتایی که تاحالا ندیده چیکار میکنه
mae_test_score = mean_absolute_error(y_test, y_test_pred)    # 108.1024310903997
# همانطور که میبینیم ایندفعه مقدار mae یعنی خطای test_score خیلی بیشتر از حالت train شد


# پس نتیجه شد این
# y_train , y_train_pred --> train_score = 61
# y_test , y_train_pred = 108
# همیشه توی مرحله evaluation باید این دو Score رو در کنار هم محاسبه کنیم


# حالا میخوایم خط پیشبینی مدل، مقدار دیتای واقعی که مدل باهاش Train دیده
# و مقدار دیتای test که مدل پیشبینی کرده رو در کنار هم رسم کنیم
# توی همین رسم میتونیم ببینیم که mae و خطای پیشبینی در دیتای test از دیتای train بیشتره
plt.scatter(x_test, y_test, label="true test")
plt.scatter(x_train, y_train, label="true train")
plt.plot(x_train, y_train_pred, label="prediction")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
#===============================================================



#====================
"Concept Explanation"
#====================
# آیا train_score زیاد بشه، Test_score هم زیاد میشه همیشه؟
# یعنی اگه مدل زیاد یاد گرفته باشه یعنی 100% قراره خوب پیشبینی کنه؟
# خیر، همیشه اینجوری نیست. در مثال بالا این قضیه نقض شد

# ببین اگه train_score بالا بود که هیچ، یعنی مدل خوب یاد گرفته
# اگه بالا نبود یعنی مدل خوب یاد نگرفته، یعنی hyperparameter هامون ساده محاسبه کردن
# در نتیجه Training_score پایین میاد و خطا میره بالا

# هرچی مدل از simple به سمت complexity میره، train_score افزایش پیدا میکنه، مدل بهتر یاد میگیره، error میاد پایین
# آیا این تضمین میکنه که مدل در آینده خوب پیشبینی کنه؟ نه
# چرا؟ چون دیتایی که مدل روش آموزش دیده، 100% توش ایراداتی وجود داشته
# یعنی دیتای 100% pure و درست نیست، ممکنه خطای انسانی، خطای دستگاه اندازه گیری یا هرچیز دیگه توش باشه
# پس وقتی یک مدل complex با شدت بالا داره روی این دیتا آموزش میبینه، پس همه این خطاها رو هم داره یاد میگیره
# ولی نمیدونه که اینا اشتباهه فکر میکنه درسته همش. واسه همین generalization اتفاق نیوفتاده
# یعنی ممکنه اگه یه روزی یه دیتایی جدید بیاد، از روی الگوریتم اشتباهی که از دیتای اشتباه یاد گرفته، یک پیشبینی اشتباه انجام بده
# پس در نتیجه، Training_score خیلی خیلی بالا هم خوب نیست، چون همه اشتباهات دیتا رو یاد میگیره و test_score میاد پایین

# پس وقتی مدل خیلی پیچیده باشه و زیادی آموزش ببینه ولی test_score کم باشه یعنی overfitting شده
# یا باید مدل رو با یه مدل ساده تر جایگزین کنیم یا huperparameter هارو کمتر کنیم

# حالا اگه مدل train_score خوبی نداشته باشه یعنی خوب یاد نگرفته در نتیجه خوب پیشبینی نمیکنه
# به این میگن underfitting یعنی مدل خوب یاد نگرفته و پیشبینی دیتای جدید رو درست محاسبه نمیکنه
# حالا یا باید کلا مدل رو با یه مدل complex تر جایگزین کنیم
# یا اینکه همون مدل رو بوسیله hyperparameter هاش پیچیده ترش کنیم تا بهتر یاد بگیره

# برای درک بهتر مثال زرافه رو میزنیم
# فرض کنیم 50 تا زرافه داریم و یه مدل میخواد از روی این دیتا یاد بگیره زرافه چیه
# مدلی خوبه که بیاد ازین 50 تا زرافه، مثلا 35 تاشو درست یاد بگیره
# این 35 تا درواقع sweet spot ما هست که باعث میشه مدل پیشبینی معقولی داشته باشه
# اگه بیاد همه این 50 تارو یاد بگیره و همه این 50 تا عین همدیگه باشن، مدل bias و متعصب میشه
# مثلا اگه قد همشون خیلی بلند باشه، اگه یه روزی یه زرافه بیاد که فقط یکم از اون 50تا کوچکتر باشه
# مدل درست تشخیص نمیده و میگه این زرافه نیست. میگه من هرچی زرافه یاد گرفتم همشون خیلی بلند بودن این کوتاهه پس زرافه نیست
# یا توی این 50 تا، مثلا ممکنه 5 تا زرافه باشه که مشکل دارن و قدشون کوتاهه و مدل این 5 تا که مشکل دارن رو هم یاد میگیره
# اگه یه روزی یه حیوان دیگه شبیه زرافه بیاد ولی قدش کوتاه باشه (ولی هم قد اون 5 تا زرافه کوتوله هست)، مدل میگه اینم زرافه هست
# پس Generalization اتفاق نیوفتاده و خطای پیشبینی بالاست و علتش overfitting هست. نباید اون 5تارو یاد میگرفت

# پس ما باید از هر مدل استفاده میکنیم، hyperparameter هاشو طوری تنظیم کنیم
# که complexity و generalization مدل در حدس وسط قرار بگیره، نه خیلی زیاد بشه نه خیلی کم بشه
# به این کار میگن hyperparameter tuning

# همیشه حالت وسط در یاد گیری مدل، بهترین حالته
# اینو میشه در مدلهای مختلف مثال زد
# مثلا در KNN اگه بگیم 1 همسایه رو در نظر بگیر، یعنی خیلی complex داریم نگاه میکنیم
# پس generalization رو از دست میدیم و مدل سعی میکنه همه دیتاهارو با complexity بررسی کنه
# الان تو شکل زیر میبینیم که بخاطر یک دیتای * رفته تو دل دیتاهای ● چون complexity خیلی زیادی داره
# در این حالت fitting خیلی خوبی داره، ولی شاید خطاها و اشتباهات رو هم یاد گرفته باشه
# شاید اون 1 نمونه‌ی * یک مورد نادر باشه، شاید یک دیتای اشتباه باشه، ولی مدل یادش گرفته
# ●●●  ●●   ___ ●● 
# ●●  ●● ● |  *|● ●●
#  ________|   |  ●
# |   *      * |
# | ****  *  **|
# | ** *   **  |

# حالا اگه مثلا neighbor رو 3 بزاریم، مدل خیلی smooth تر خط رسم میکنه و general تر یاد میگیره
# در نتیجه از اون نمونه‌ی اشتباه دوری میکنه و یادش نمیگیره
# ●●●  ●●       ●● 
# ●●  ●● ●  [*] ● ●●
#  ____________  ●
# |   *      * |__
# | ****  *     **|
# | ** *   **   * |

# حالا اگه neighbor مثلا برابر 9 باشه، کلا فقط میاد یه خط کلی اون وسط میکشه و دیگه هیچی درست یاد نمیگیره
# ●●●  ●●       ●● 
# ●●  ●● ●  [*] ● ●●
# __________________
#    *      * 
#  ****  *     **
#  ** *   **   * 


# در مدل decisiion tree هم میتونیم اینجوری توضیح بدیم
# اگر depth مثلا بزاریم 1 همینطوری 2 گروه میکنه و میره و دیگه خیلی زیادی smooth تصمیم میگیره و چیز خاصی یاد نمیگیره
# ●●●  ●●       ●● 
# ● **  ●● ●  * ● ●●
# __________________
#    *      * 
#  ****  ●●●   **
#  ** *   **   * 

# اگر مثلا depth=9 بذاریم، دیگه اگه دیتایی اشتباه باشه هم یاد میگیره
# ●●●  ●●       ●● 
#    __        ___ 
# ● |**|  ●● ●|  *| ● ●●
# __|  |______|   |_______
#    *      * 
#        ___
#  **** |●●●|   **
#  ** * |   | *

# بهترین حالت مثلا depth=2 هست که یک یادگیری general داره
# ●●●  ●●  ●● ________
#   ●   ●● ● / * **
# __________/  **  *
#    *      ●  *
#  ****   **  *
#  ** *   **   * 




" Generalization "

# هدف اصلی Machine Learning رسیدن به Generalization است، نه فقط یاد گرفتن داده‌های آموزشی
# مدل روی تعداد محدودی دیتا آموزش میبینه، بعدا یه دیتای جدید میاد و باید براش پیشبینی انجام بده
# اگه بتونه کار پیشبینی برای دیتای جدید رو خوب انجام بده میگیم مد تونسته generalize کنه
# پس Generalization یعنی مدل بتواند روی داده‌هایی که هرگز در زمان آموزش ندیده است
# تقریباً به همان خوبی که روی داده‌های آموزشی عمل می‌کند، پیش‌بینی انجام دهد
# به همین دلیل، در Machine Learning هدف اصلی کم کردن خطای داده‌های آموزشی نیست؛ هدف اصلی ساختن مدلی است که
# روی داده‌های جدید هم عملکرد خوبی داشته باشد. این همان چیزی است که کیفیت یک مدل را مشخص می‌کند

# معنی Generalization یعنی توانایی مدل برای پیش‌بینی صحیح روی داده‌های جدید و ندیده (Unseen Data)
# مدل نباید فقط داده‌های آموزشی را بلد باشد. باید بتواند روی داده‌هایی که هیچ‌وقت در آموزش ندیده هم درست عمل کند

# یک دانش آموز تمام کتاب رو فقط حفظ کرده، اگه روز آزمون سوال جدید بیاد نمیتونه جواب بده یعنی generalization ضعیفی داشته
# یه دانش آموز دیگه بجای فقط حفظ کردن میاد مفهوم رو یاد میگیره و هر سوالی باد میتونه جواب بده پس generalization خوبی داره


#===== ارتباط Generalization با Overfitting =====
# مدل بجای اینکه الگوی بین دیتاهارو متوجه بشه فقط دیتایی که بهش دادن رو حفظ کرده
# یعنی train_score بالایی داره مثلا 100% ولی ولی روی test پیشبینی خیلی ضعیفی داره مثلا 60%
# اینجا generalization ضعیف انجام شده


#===== ارتباط Generalization با Underfitting =====
# حالا مدل خیلی ساده هست و نه روی train خوبه نه روی test و الگوهارو اصلا خوب یاد نگرفته
# پس اینجا هم generalization خیلی ضعیفی انجام شده


#===== good generalization =====
# هر موقع  Train Accuracy≈Test Accuracy  و هر دو مقدار بالا باشن یعنی generalization خوبی داریم


#              Generalization
#                    ▲
#                    │
      #   بهترین تعمیم روی داده‌های جدید 
#                    │
#    ──────────────────────────────
#    Underfitting       Overfitting
#    complex model      simple model
#    Train ❌           Train ✅
#    Test ❌            Test ❌



# چگونه Generalization را بهتر کنیم؟
# داده‌ی آموزشی بیشتر جمع کنیم    
# از Train / Validation / Test Split استفاده کنیم    
# از Cross Validation برای انتخاب بهتر مدل و پارامترها استفاده کنیم    
# از Regularization (Ridge، Lasso، ElasticNet) بهره ببریم    
# پیچیدگی مدل را کنترل کنیم (مثل max_depth در درخت تصمیم یا C و gamma در SVM)    
# ویژگی‌های (Features) مفید انتخاب کنیم و ویژگی‌های نامرتبط را حذف کنیم    












'''
===============================================================================
==============================   Models Review   ==============================
===============================================================================
'''
# There are 2 types of ML Models: 1-Regressor models  2-Classifier models


"=============================== Regression ==================================="

# y = a*x + b
# y = ax1 + bx2 + c*x3 + .... + z

# train-test-split
from sklearn.model_selection import train_test_split 
x_trian,y_train,x_test,y_test = train_test_split(x,y,0.2, shuffle=True , random_state = 42)


# Model selection
from sklearn.linear_model import LinearRegression     #direct mathematical solution. No Gradient Descent
from sklearn.linear_model import SGDRegressor      #Stochastic Gradient Descent
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR


# configuration
model = VSR(c=10, gamma=0.001, kernel="poly", degree=3)
model = RandomForestRegressor(n_estimators=200, max_depth=4)


# fit
model.fit(x_train,y_train)


# Prediction
y_pred_train = model.predict(x_train)
y_pred_test = model.prediction(x_test)
# y_test_true = y_test


# Evaluation - test_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import explained_variance_score
from sklearn.metrics import r2_score
import math

MAE_test_score = mean_absolute_error(y_test, y_pred_test)
MSE_test_score = mean_squared_error(y_test, y_pred_test)
RMSE_test_score = math.sqrt(MSE_test_score) #roote MSE ro begir
MAPE_test_score = mean_absolute_percentage_error(y_test, y_pred_test)
EVE_test_score = explained_variance_score(y_test, y_pred_test)
r2_test_score = r2_score(y_test, y_pred_test)


# Evaluation - train_score
MAE_train_score = mean_absolute_error(y_train, y_pred_train)


#draw
import matplotlib.pyplot as plt
model.predict(x,y)




"============================ Classification ================================="

from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC


# Evaluation - test_score
from sklearn.metrics import accuracy_score 
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score
#y_pred_test = [1 , 0 , 0 , 0 , 1 , 1]
#y_train --> [1,0,1,1,1]

accuracy_test_score = accuracy_score(y_test, y_pred_test)




















































































