
'''
===============================================================================
===============================================================================
================       Created on Mon Jul 27 22:01:51 2026     ================
================                IDE: Spyder                    ================
================         Author: Khashayar Alipour             ================
================              Statistical models               ================
================           AI feature engineering              ================
===============================================================================
===============================================================================
'''

# مباحث این قسمت همه برای data processing هستن. یعنی مرحله قبل از دادن دیتا به مدل

# Data scaling --> StandardScaler / MinMaxScaler

# PolynomialFeatures

# Feature Encoding
#       ├── Label Encoding (Ordinal feature)
#       ├── One-Hot Encoding (Categorical feature)
#       ├── Ordinal Encoding
#       └── ...

# Feature Selection
#        ├── SelectKBest
#        ├── RFE
#        └── PCA (در واقع Feature Extraction)





'''
==================================================
=======   StandardScaler / MinMaxScaler    =======
==================================================
'''

# فرض میکنیم دیتایی به شکل زیر داریم

# | Height(cm) | Income(toman) |
# | ---------- | ------------- |
# | 170        | 20,000,000    |
# | 180        | 35,000,000    |
# | 175        | 18,000,000    |

# اختلاف دیتا در height در حد صدها هست ولی بین income در حدل میلیون‌ها هست
# در الگوریتم‌هایی که با Gradient Descent کار می‌کنند (مثلا مدل SGDRegressor) مدل وقتی گرادیان را حساب می‌کند، به این اعداد نگاه می‌کند
# در نتیجه ستون income تقریباً تمام تصمیم مدل را کنترل می‌کند چون وزنش زیاده
# ستون height تقریباً بی‌اثر می‌شود در حالی که شاید هر دو مهم باشند


# مدل SGDRegressor با Gradient Descent آموزش می‌بیند
# و Gradient Descent در هر مرحله تقریباً این کار را انجام می‌دهد:
# w=w−η×gradient
# w = وزن مدل
# η (eta0) = Learning Rate
# gradient = گرادیان

# وقتی اعداد Feature بزرگ باشند، مقدار گرادیان نیز بزرگ می‌شود
# در نتیجه وزن‌ها خیلی سریع به سمت مقادیر بسیار بزرگ یا بسیار منفی حرکت می‌کنند
# در نهایت مدل به جای اینکه به بهترین خط برسد، واگرا (Diverge) می‌شود
# در نتیجه مدل a و b رو خیلی غیرمنطقی بدست میاره و نمیتونه درست پیشبینی کنه و کارامد نیست


# پس قبل از آموزش مدل، کاری می‌کنیم که همه ستون‌ها تقریباً در یک مقیاس قرار بگیرند که به اینکار میگن Feature scaling
# بعد از Scale کردن همه دیتاها تقریبا در یک محدوده قرار میگیرن و اینجوری مدل به همه دیتاها توجه میکنه



# کدوم مدلها نیازه از Scaler استفاده کنن؟
# LogisticRegression, KNN, SVM, NeuralNetwork
# چون این مدلها داخلشون از الگوریتم distance استفاده میکنن
# یعنی فاصله بین نمونه ها براش مهمه، پس نیازه که نمونه ها Scale بشن

# مدلهایی مثل ensemble models از الگوریتم split کردن نمونه ها استفاده میکنه
# برای این مدلها distance بین نمونه ها مهم نیست پس نیازی به Scale کردن ندارن



# برای scale کردن از روشهای مختلفی استفاده میشه:

"StandardScaler"
# z= (x−μ) / σ​     فرمول آن
# x مقدار اصلی
# μ میانگین
# σ انحراف معیار

# الان میخوایم با روش StandardScaler این دادههارو scale کنیم:
# 20  --> (20−40)/28.3=−1.41
# 40  --> (40−40)=0
# 60  --> (100−60)/28.3=1.41
# میانگین اینا میشه 40

# بعد از Sclae کردن
# -1.41
# 0
# 1.41


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# تابع fit_transform همزمان 2 کار انجام میده
# اول قسمت scaler.fit(x) میاد میانگین و انحراف معیار رو حساب میکنه
# سپس قسمت transform(X) میاد اعداد رو تبدیل میکنه    




"MinMaxScaler"
# روشی دیگر برای Sclae کردن داده هاست که میاد همه دیتاهارو بین 0 و 1 میاره
# x′ = (x-min) / (max-min)

# 20  --> min value
# 40
# 60
# 80
# 100  --> max value

# 0     --> (20-20)/(100-20) = 0
# 0.25  --> (40-20)/(100-20) = 0.25
# 0.50  --> (60-20)/(100-20) = 0.50
# 0.75  --> (80-20)/(100-20) = 0.75
# 1     --> (100-20)/(100-20) = 1


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)


# فرض کنیم مدل رو آموزش دادیم و بعد یک دمای جدید (new_Data) میاد. نباید بنویسیم:
scaler.fit_transform(new_data)
# چون دوباره کوچک‌ترین و بزرگ‌ترین مقدار را حساب می‌کند و مقیاس تغییر می‌کند. باید بنویسیم:
new_scaled = scaler.transform(new_data)
# از همان min و max که روی داده آموزشی یاد گرفته‌ای استفاده کن
    


'''when to use each?'''
# |          model      |          Scaler              |
# | ------------------- | ---------------------------- |
# | SGDRegressor        | ✅ StandardScaler            |
# | Logistic Regression | ✅ StandardScaler            |
# | SVM                 | ✅ StandardScaler            |
# | Neural Network      | ✅ StandardScaler            |
# | KNN                 | ✅ StandardScaler یا MinMax  |
# | KMeans              | ✅ StandardScaler            |
# | Decision Tree       | ❌ لازم نیست                 |
# | Random Forest       | ❌ لازم نیست                 |
# | XGBoost             | ❌ لازم نیست                 |
'''==========================================================================='''









'''
=======================================
=======   PolynomialFeatures    =======
=======================================
'''
# این یکی از مهم‌ترین ابزارهای Feature Engineering است
# یک Feature Engineering Transformer است که قبل از مدل استفاده می‌شود و کارش تغییر دادن feature هاست

# گاهی دیتا طوری هست که وقتی نمودارش رو رسم میکنیم خط صاف نمیشه و درواقع رابطه خطی ندارن (منحنی میشه)
# | Temperature | Strength |
# | ----------- | -------- |
# | 100         | 400      |
# | 200         | 390      |
# | 300         | 360      |
# | 400         | 310      |
# | 500         | 240      |

# Strength
# 400 ●
# 380   ●
# 340      ●
# 300         ●
# 240             ●
#           Temperature

# در این مواقع دیگه نمیشه از مدلهای linear مثل LinearRegression استفاده کرد چون فقط بلده خط راست رسم کنه
# اگر برای دیتاهای بالا از linearRegression استفاده کنیم همچین چیزی رسم میکنه که بدرد نمیخوره:
#   y |
#     |
#     |  _________
#     |
#     |____________  x
# ولی ما میدونیم نمودار داده ها خط صاف نیست و منحنی هست
# پس مدل underfitting شده و نتونسته رابطه رو یاد بگیره


# حالا اولین راهی که به ذهن میرسه اینه که مدل رو عوض کنیم تا رابطه رو بتونه پیدا کنه
#ولی بجای تغییر مدل بیایید داده را طوری تغییر بدهیم که همان Linear Regression بتواند منحنی بسازد
# بجای تغییر دادن مدل، ویژگی‌ها (Features) را تغییر می‌دهیم

# قبلا دیتاست ما این بود:
# Temperature
# 100
# 200
# 300
# 400
# 500
# حالا PolynomialFeatures می‌آید و می‌گوید: "با استفاده از این ستون، من یک ستون جدید می‌سازم"
# Temperature
# Temperature²

# | Temp | Temp²  |
# | ---- | ------ |
# | 100  | 10000  |
# | 200  | 40000  |
# | 300  | 90000  |
# | 400  | 160000 |


# حالا با اینکار چی تغییر کرد؟
# مدل قبلا که فقط یک ستون داشت، فقط میتونست این رابطه رو یاد بگیره یعنی از یک ستون استفاده میکرد:   y = ax+b
# حالا دوتا ستون Temp و Temp² داره پس معادله این میشه:   y = a₁T + a₂T² + b
# پس هنوز از Linear Regression استفاده می‌کنیم اما چون Featureهای جدید اضافه کرده‌ایم، خروجی مدل می‌تواند منحنی باشد
# در واقع مدل هنوز همون خط رو میکشه ولی با این درجه=2 که بهش دادیم میتونه خمیدگی منحنی رو یاد بگیره

# خطی بودن به ضرایب (Weights) مربوطه نه به توان x
# a₁  a₂    ضرایب همگی توان یک دارن
# پس مدل هنوز خطی هست


# کاربرد polynominal وقتی هست که رابطه بین Featureها و Target غیرخطی باشد
# در واقع در مواردی که ما احتمال این رو میدیم که در آینده و دیتاهای بالاتر امکان منحنی شدن نمودار باشه
# در این موارد میایم feature های بیشتری با استفاده از توان میدیم که مدل بتونه تغییر رفتار رو یاد بگیره
# در واقع میایم کاری میکنیم که مدل خطی بتونه روابط غیرخطی هم یاد بگیره و در جایی که نمودار غیرخطی شد Fail نشه


#====== degree ======
# کلا degree یعنی تا چه توانی Feature تولید کنم
# x -> degree=2 --> X X²
# x -> degree=3 --> X X² X³
# x -> degree=5 --> X X² X³ X⁴ X⁵

# هر چی درجه کمتر باشه مدل فقط یک خط صاف میکشه و underfit میشه
# هرچی درجه بیشتر باشه مدل پیچیده تر میشه و همه نقاط رو حفظ میکنه و احتمال overfit هست

# از کجا بفهمیم Degree رو باید چند بزاریم؟ هیچکی نمیدونه
# در اینجا میتونیم از gridSearch استفاده کنیم تا خودش حساب کنه کدام درجه بیشترین Score رو داره
param_grid = {"poly__degree":[1,2,3,4]}



X = [[2], [3], [4]]
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)
# همین یک خط تمام Featureهای جدید را می‌سازد

# [[1 2 4]
#  [1 3 9]
#  [1 4 16]]

model = LinearRegression()
model.fit(X_poly,y)
y_pred = model.predict(X_poly)










'''
=============================================================================================
=======   Feature encoding --> Label encoding / One hot encoding / Ordinal encoding   =======
=============================================================================================
'''

# فرض کنیم دیتاست زیر رو داریم:
# | Age | Salary | Gender | Purchased |
# | --- | ------ | ------ | --------- |
# | 25  | 4000   | Male   | Yes       |
# | 30  | 5000   | Female | No        |
# | 28  | 4500   | Male   | Yes       |


# حالا یک مدل رو با دیتاهای بالا آموزش دادیم model.fit(x,y) و اگر x رو چاپ کنیم این میشه:
# Age   Salary   Gender
# 25    4000     Male
# 30    5000     Female
# 28    4500     Male


# problem?
# مشکل اینه که مدل معنی کلمه male یا Female رو نمیفهمه
# چون مدل‌های Machine Learning فقط با اعداد کار می‌کنند مثلا 10  100  2.5  -12
# ولی مثلا اینارو نمیفهمه:  male  female  apple  red  blue


# به پروسه تبدیل داده های متنی به عدد، میگن Feature Encoding
# یعنی تبدیل داده‌های دسته‌ای (Categorical Data) به داده‌های عددی، تا مدل‌ها بتوانند آن‌ها را پردازش کنند
# پس Feature encoding یک مفهوم کلی هست که چندین روش داره


"Types of data"
# Numeric
    # e.g. Age, Salary, Weight, ...
    # This data needs no encoding
    
# Categorical
    # e.g. Red, Blue, Male, Female, Apple, ...
    # This data needs to be encoded
    


"✅ Label encoding"
#ساده ترین روش هست. میاد برای هر دسته یک شماره میذاره
# یعد از شماره گذاری، مدل دیگه بجای دیتای categorical با عدد کار میکنه (0,1,2,3 ...)
#  color
# ------
#  Red
#  Blue
#  Green

# | Color | Label |
# | ----- | ----- |
# | Red   | 0     |
# | Blue  | 1     |
# | Green | 2     |


# problem?
# مشکل این روش اینه که شماره گذاری بصورت ترتیبی انجام میشه
# برای همین ممکنه مدل فکر کنه که:  Green > Blue > Red
# یعنی ممکنه مدل فکر کنه مثلا Green از Blue بزرگتره
# پس Label Encoding ممکن است مدل را گمراه کند


# When to use Label encoding?
# وقتی دیتاها ترتیب طبیعی داشته باشند و ordinal باشن. مثلا:
# Education
# High School   0
# Bachelor      1
# Master        2
# PhD           3


from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
data["Gender"] = encoder.fit_transform(data["Gender"])
# متد fit برای یادگیری و متد transform برای تبدیل داده است و fit_transform هرد کار رو باهم انجام میده

encoder.inverse_transform()
# این متد برای برگرداندن اعداد به متن کاربرد داره
# 0  ->  Female   
# 1  ->  Male
# 0  ->  Female




"✅ Ordinal Encoding"
# از نظر خروجی، Ordinal Encoding و Label Encoding شبیه هم هستند و تفاوت اصلی در هدف و کاربرد آنهاست
# فرض کنیم این ستون دیتا رو داریم:
# | Education   |
# | ----------- |
# | Bachelor    |
# | Master      |
# | PhD         |
# | Bachelor    |
# | High School |

# میخواهیم این دیتا رو وارد مدل کنیم و مدل فقط عدد میفهمه پس باید متن به عدد تبدیل بشه
# از اونجایی که یه ترتیب و رابطه بین ردیف های این ستون وجود داره، از ordinal encoding استفاده میکنیم
# | Education   | Code |
# | ----------- | ---- |
# | High School | 0    |
# | Bachelor    | 1    |
# | Master      | 2    |
# | PhD         | 3    |

# حالا چرا از label encoding استفاده نمیکینم؟ چون کارش اینه که فقط  بصورت رندوم شماره گذاری کنه 0 و 1 و 2 و 3 و ...
# ولی شماره گذاریش به ترتیب چینش دیتاها نیست، رندومه. یعنی مثلا به PHD ممکنه عدد 0 بده یا 1 یا ...
# اما وقتی از ordinal encoding استفاده میکنیم نه تنها به ترتیب چینش دیتاها عدد میده، بلکه 0 < 1 و 1 < 2 و ...
# در واقع ordinal encoder به ما اجازه میده ترتیب رو خودمون مشخص کنیم


from sklearn.preprocessing import OrdinalEncoder
encoder = OrdinalEncoder(
    categories=[ ["High School", "Bachelor", "Master", "PhD"] ]    # با این متد ترتیب رو مشخص میکنیم
  )

x_train = encoder.fit_transform(
    data[["Education"]]
  )

# 0
# 1
# 2
# 3

# فرض کنیم 2 ستون edication و size داریم. هر ستون ترتیب خودش رو داره:
encoder = OrdinalEncoder(
    categories=[
        ["High School","Bachelor","Master","PhD"],
        ["Small","Medium","Large"]
      ]
  )

# فرض کنیم مدل در مرحله آموزش فقط small و medium رو دیده. اما موقع تست large هم یهو میاد. برای جلوگیری از ارور:
encoder = OrdinalEncoder(categories=[["small", "medium"]], handle_unknown="use_encoded_value")

# اگر یک مقدار ناشناخته جدید در مرحله تست آمد، چه عددی بهش بده؟
encoder = OrdinalEncoder(categories=[["small", "medium"]], unknown_value=-1)




"✅ One-Hot Encoding"
# مشکل ترتیبی بودن label encoding رو حل میکنه
# پس این نوع از encoding برای دیتاهای بدون ترتیب یا Nominal کاربرد داره
# چرا اسمش اینه؟ چون فقط یک ستون مقدار 1 میگیره

# اگر دیتای ما این باشه:
# Color
# -----
# Red
# Blue
# Green

# حالا One-Hot بجای اینکه به ترتیب بیاد 0و1و2 بده به تعداد feature ها ستون میسازه و اینجوری عدد گذاری میکنه:
# | Red | Blue | Green |
# | --- | ---- | ----- |
# | 1   | 0    | 0     |
# | 0   | 1    | 0     |
# | 0   | 0    | 1     |

# یعنی اگر blue باشد 1 میگیره و بقیه 0
# اگر Red باشد 1 میگیره و بقیه 0
# اگر در یک ستون Green باشد 1 میگیره و بقیه 0


# Gender
# ------
#  Male
#  Female

# | Male | Female |
# | ---- | ------ |
# | 1    | 0      |
# | 0    | 1      |
# | 1    | 0      |

from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder()
x_train = encoder.fit_transform(data[["Gender"]])
x_test = encoder.transform()
# [[1 0]
#  [0 1]
#  [1 0]]

# اگر بخواهی خروجی به جای Sparse Matrix یک آرایه NumPy باشد:
encoder = OneHotEncoder(sparse_output=False)
# خروجی sparse matrix برای داده های بزرگ حافظه کمتری مصرف میکند

# فرض کنیم در train دیتاها بصورت male female بوده ولی در مرجله تست other هم میاد.
# برای اینکه مدل ارور نده از این پارامتر استفاده میشه:
encoder = OneHotEncoder(handle_unknown="ignore")









'''
=================================================================
=======   Feature Selection -->  SelectKBest | RFE | PCA  =======
=================================================================
'''
# معمولاً بعد از Encoding، Scaling و قبل از آموزش مدل یاد گرفته می‌شود
# گاهی ممکنه در دیتاست ما تعداد زیادی feture داشته باشیم. ولی برای کارمون خیلی از آنهارو نیاز نداریم
# مثلا اگه ستون House color داشته باشیم، برای پیشبینی قیمت خانه این ستون اهمیتی نداره
# پس اگه این ستون هارو وارد مدل کنیم مجبوره الکی چیزهای بی اهمیت یاد بگیره که هیچوقت ازش استفاده نمیشه

# نتیجه؟
# آموزش کندتر 🐢
# حافظه بیشتر 💾
# احتمال Overfitting بیشتر 🚨
# دقت کمتر 📉

# پس Feature Selection یعنی انتخاب مهم‌ترین Featureها و حذف Featureهای غیرضروری
# بعد از عملیات Feture selection فقط ستون های مفید باقی میمونن و بقیه حذف میشن


# در sklearn سه روش معروف برای Feature selection وجود داره
# Feature Selection
#         ├── SelectKBest
#         ├── RFE
#         └── PCA (در واقع Feature Extraction)
# نکته مهم اینه که PCA در واقع Feature Selection نیست. بلکه Feature Extraction است. ولی کاربرد مشابهی دارد



"✅ SelectKBest"

# ساده ترین روش feature selection هست
# فرض میکنیم 10 تا feature داریم و 3 تاشو میخوایم
# اینجا SelectKBest میگه من به هر Feature یک امتیاز می‌دهم و بهترین K تا را نگه می‌دارم

# | Feature    | Score |
# | ---------- | ----- |
# | Area       | 98    |
# | Garage     | 84    |
# | Age        | 76    |
# | Color      | 15    |
# | Owner Name | 3     |

# مثلا اگه k=3 باشه خروجی این میشه:
# Area
# Garage
# Age


# مزایای این روش اینه که ساده و سریع هست
# معایبش اینه که feature هارو تکی بررسی میکنه و رابطه بین اونهارو باهم نمیبینه


# در این روش Score چجوری محاسبه میشه؟
# برای regression از f_regression استفاده میشه
# برای classification از f_classif استفاده میشه

#====== Regression =========
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression

selector = SelectKBest(score_func=f_regression, k=3 )
X_train = selector.fit_transform(x_train, y_train)

# اینجا fit به همه feature ها Score میده و transform فقط بهترین هارو نگه میداره
# اگر بگیم k=3 یعنی 3 تا Feature رو نگه دار


#======= classification =======
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

selector = SelectKBest(score_func = f_classif, k=4)

x_train = selector.fit_transform(x_train, y_train)
x_test = selector.transform(x_test)

selector.get_support()  # --> True, False




"✅ RFE(Recursive Feature Elimination)"

# ما این دیتاست رو داریم که 6 تا feature داره
# و RFE میاد اول روی این دیتا مدل رو آموزش میده و به همه Feature ها یک Score میده
# سپس میاد کم اهمیت ترین feature رو که اینجا F باشه حذف میکنه

# | Feature | Importance |
# | ------- | ---------- |
# | A       | 0.9        |
# | B       | 0.8        |
# | C       | 0.7        |
# | D       | 0.2        |
# | E       | 0.1        |
# | F       | 0.05       |

# سپس دوباره مدل رو آموزش میده و دوباره کم اهمیت ترین رو حذف میکنه
# اینقد این کار رو تکرار میکنه تا فقط مثلا 3 feature باقی بمونه
# به همین دلیل اسمش recursive یا تکراری هست


# مزایای این روش اینه که دقیق‌تر از SelectKBest چون Featureها را با هم بررسی می‌کند
# معایبش اینه که کندتر است. چون چندین بار مدل را آموزش می‌دهد


from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression

model = LinearRegression()
selector = RFE(estimator=model, n_features_to_select=3, step=1)

x_train = selector.fit_transform(x_train, y_train)
x_test = selector.transform(x_test)

# پارامتر estimator مشخص میکنه چه مدلی اهمیت Feature هارو بررسی کنه
# پارامتر n_features_to_select مشخص میکنه چند feature باقی بمونه
# پارامتر step مشخص میکنه هر بار چند feature حذف بشه




"✅ PCA (Principal Component Analysis)"

# فرض کن 50 تا Feature داری که بعضی از آنها تقریبا 1 چیز رو اندازه میگیرن. اینها اطلاعات تکراری دارن
# Weight (kg)     Height(cm)      Income
# Weight (lb)     Height(m)       Salary

# حالا PCA میاد میگه من بجای 50 تا، 5 تا feature جدید میسازم که که همون اطلاعات رو داشته باشه
# before            after
# ------            -----
# Height            PC1
# Weight  --PCA-->  PC2
# BMI

# فرض کنیم 3 دوربین از یک ماشین عکس گرفتن و PCA میاد میگه من بجای اینها، یک عکس میسازم که خلاصه هر 3 باشد


from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_new = pca.fit_transform(X)
# پارامتر n_components یعنی چند component بسازه


# ❌ کلا PCA به y نگاه نمیکنه بلکه فقط به x نگاه میکنه
# به همین دلیل یک روش unsupervised هست

# Original Features
#        ▼
#       PCA
#        ▼
#   New Features
#        ▼
#      Model

# چه زمانی PCA خوب است؟
# وقتی Featureهای خیلی زیادی داری
# مثلاً:
# تصویر    
# متن    
# داده‌های ژنتیکی    
# صدها Feature    



"✅ SUMMARY"

#                   Many Features
#                        │
#         ┌──────────────┴──────────────┐
#         │                             │
#    Want to keep                Want new compact
#  original features?               features?
#         │                             │
#       Yes                           No
#         │                             │
#    ┌────┴─────┐                       ▼
#    │          │                      PCA
#  Fast?      Accurate?
#    │          │
#    ▼          ▼
# SelectKBest   RFE

# _______________________________________________________________________________________________________
# |          ویژگی         |         SelectKBest        |           RFE          |          PCA         |  
# |----------------------------|------------------------|----------------------|------------------------|
# |     حذف Feature       |          ✅          |          ✅            |             ❌            |  
# |   ساخت Feature جدید   |          ❌          |          ❌            |             ✅            |  
# |   به y نگاه می‌کند؟    |          ✅          |          ✅            |             ❌            |  
# |         نوع           |     Supervised          |         Supervised     |      Unsupervised        |  
# |         سرعت          |        🚀 زیاد       |       🐢 کمتر         |          🚀 زیاد          |  
# |    مناسب برای        |  حذف Featureهای ضعیف | انتخاب دقیق Featureها | کاهش ابعاد و حذف همبستگی |  
# ------------------------------------------------------------------------------------------------------









































































