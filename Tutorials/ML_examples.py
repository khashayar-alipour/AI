
'''
===============================================================================
===============================================================================
================       Created on Tue Aug  4 14:15:05 2026     ================
================                IDE: Spyder                    ================
================         Author: Khashayar Alipour             ================
================                Real Examples                  ================
===============================================================================
===============================================================================
'''

# حل مثال‌های واقعی با دیتاهای کتابخوانه sklearn با استفاده از انواع مدلهای ماشین لرنینگ
# در مثال california housing dataset درمورد correlation matrix آموزش داده شده

# Supervised regression  - California housing dataset
#       |____correlation matrix

# Supervised classification  - load_breast_cancer
#       |____ confusion matrix

# Unsupervised clustering  - load wine dataset






#===============================================================
#===============================================================
"ُ     Supervised regression  - California housing dataset    "
#===============================================================
#===============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing(as_frame=True)

# دیتاست California Housing از کجا آمده؟
# این دیتاست مربوط به قیمت خانه‌های ایالت کالیفرنیا است.
# اصل این داده‌ها از سرشماری آمریکا (1990 U.S. Census) استخراج شده‌اند و بعداً برای آموزش ماشین لرنینگ آماده شده‌اند.
# هر سطر نشان‌دهنده‌ی یک منطقه (district) در کالیفرنیاست، نه یک خانه‌ی منفرد
# این دیتاست که داخل کتابخوانه sklearn وجود داره یکی از معروف‌ترین دیتاست‌های آموزشی دنیاست

# متغیر housing یک  DataFrame نیست بلکه یک شیء از نوع sklearn.utils.Bunch هست
# می‌توانی آن را شبیه یک دیکشنری در نظر بگیری که داخل آن چند چیز مختلف وجود دارد

print(housing.keys())
# dict_keys([
# 'data',
# 'target',
# 'frame',
# 'target_names',
# 'feature_names',
# 'DESCR'
# ])

"features (x)"
print(housing.data[:1])
#    MedInc  HouseAge  AveRooms  ...  AveOccup  Latitude  Longitude    # هر ردیف یک منطقه در کالیفرنیا هست نه یک خانه منفرد
# 0  8.3252      41.0  6.984127  ...  2.555556     37.88    -122.23
# [1 rows x 8 columns]
print(housing.feature_names)
# ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']


"Output (y)"
print(housing.target[:1])
# 0    4.526
# Name: MedHouseVal, dtype: float64
print(housing.target_names)   #['MedHouseVal']


"Full description of this dataset"
print(housing.DESCR)
# California Housing dataset
# --------------------------
# **Data Set Characteristics:**
# :Number of Instances: 20640 --> تعداد نمونه
# :Number of Attributes: 8 numeric, predictive attributes and the target
# :Attribute Information:   --> ستونها
#     - MedInc        median income in block group
#     - HouseAge      median house age in block group
#     - AveRooms      average number of rooms per household
#     - AveBedrms     average number of bedrooms per household
#     - Population    block group population
#     - AveOccup      average number of household members
#     - Latitude      block group latitude
#     - Longitude     block group longitude
# :Missing Attribute Values: None  --> یعنی دیتا نیاز به پاکسازی نداره

# The target variable is the median house value for California districts,
# expressed in hundreds of thousands of dollars ($100,000).   --> یعنی 100 هزار دلار رو بصورت 100$ مینویسه

# This dataset can be downloaded/loaded using the
# :func:`sklearn.datasets.fetch_california_housing` function.


"Creating a dataframe"
# با استفاده از کلید frame میشه همزمان به feature(x) و y دسترسی پیدا کرد
# وقتی as_frame=True باشه آنگاه sklearn خودش یک DataFrame برامون می‌سازد که هم features و هم Target داخل آن هستند
print(housing.frame)  # 8+1 columns

# با دستور copy یک dataframe جدید از روی Dataframe دیتای اصلی میسازیم و توی متغیر df میریزیم
df = housing.frame.copy()   # <class 'pandas.core.frame.DataFrame'>



"SUMMARY" #____________________________________________________________________________
# پس ما از کتابخوانه sklearn یک دیتای واقعی دانلود کردیم
# از دل این دیتا یک dataframe بیرون کشیدیم
# این دیتافریم 9 تا ستون داره که 8 تاش میشه feature یا X و یکیش میشه target یا y
# پس با استفاده از ویژگی های یک خانه میخوایم قیمت خانه رو پیشبینی کنیم
# چون که هم X داریم و هم y پس از supervised regression استفاده میکنیم
#______________________________________________________________________________________



#----------------------------------
"         Data Cleaning           "
#----------------------------------

# 1- Empty cell (dropna, fillna)
# 2- Type (.as_type())
# 3- Logical Error
# 4- Duplicated

df.head()
   MedInc  HouseAge  AveRooms  ...  Latitude  Longitude  MedHouseVal
0  8.3252      41.0  6.984127  ...     37.88    -122.23        4.526
1  8.3014      21.0  6.238137  ...     37.86    -122.22        3.585
2  7.2574      52.0  8.288136  ...     37.85    -122.24        3.521
3  5.6431      52.0  5.817352  ...     37.85    -122.25        3.413
4  3.8462      52.0  6.281853  ...     37.85    -122.25        3.422
[5 rows x 9 columns]


df.tail()
       MedInc  HouseAge  AveRooms  ...  Latitude  Longitude  MedHouseVal
20635  1.5603      25.0  5.045455  ...     39.48    -121.09        0.781
20636  2.5568      18.0  6.114035  ...     39.49    -121.21        0.771
20637  1.7000      17.0  5.205543  ...     39.43    -121.22        0.923
20638  1.8672      18.0  5.329513  ...     39.43    -121.32        0.847
20639  2.3886      16.0  5.254717  ...     39.37    -121.24        0.894
[5 rows x 9 columns]


df.isnull().sum()
MedInc         0
HouseAge       0
AveRooms       0
AveBedrms      0
Population     0
AveOccup       0
Latitude       0
Longitude      0
MedHouseVal    0


df.describe()
             MedInc      HouseAge  ...     Longitude   MedHouseVal
count  20640.000000  20640.000000  ...  20640.000000  20640.000000
mean       3.870671     28.639486  ...   -119.569704      2.068558
std        1.899822     12.585558  ...      2.003532      1.153956
min        0.499900      1.000000  ...   -124.350000      0.149990
25%        2.563400     18.000000  ...   -121.800000      1.196000
50%        3.534800     29.000000  ...   -118.490000      1.797000
75%        4.743250     37.000000  ...   -118.010000      2.647250
max       15.000100     52.000000  ...   -114.310000      5.000010
[8 rows x 9 columns]


df.duplicated().sum()
# np.int64(0)



#---------------------
"        EDA        "
#---------------------

# Histogram
df.hist(figsize=(14,10), bins=30)
plt.show()

# Box plot
df.plot(kind="box", subplots=True, layout=(3,3), figsize=(15,10))
plt.show()


#Scatter
plt.scatter(df["MedInc"], df["MedHouseVal"], alpha=0.5, color="green")
plt.xlabel("Median Income")
plt.ylabel("Median House Value")
plt.title("Median income VS Median house value")
plt.show()
# این نمودار نشون میده این دو ویژگی تقریبا باهم رابطه مستقیم دارن



"Pearson Correlation Matrix"

# Simple correlation matrix for begginers   🟡🟣
correlation_matrix = df.corr(numeric_only=True, )
fig, ax = plt.subplots(figsize=(10,8))
image = ax.imshow(correlation_matrix)  
ax.set_xticks(range(len(correlation_matrix.columns)))
ax.set_yticks(range(len(correlation_matrix.columns)))
ax.set_yticklabels(correlation_matrix.columns)
ax.set_xticklabels(correlation_matrix.columns)
fig.colorbar(image)
ax.set_title("correlation matrix")
plt.tight_layout()
plt.show()


# Complex correlation matrix for professional using seaborn heatmap
import seaborn as sns
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
correlation_matrix = df.corr(numeric_only=True, )
fig, ax = plt.subplots(figsize=(10,8))
ax.set_xticks(range(len(correlation_matrix.columns)))
ax.set_yticks(range(len(correlation_matrix.columns)))
ax.set_yticklabels(correlation_matrix.columns)
ax.set_xticklabels(correlation_matrix.columns)
fig.colorbar(image)
ax.set_title("correlation matrix")
plt.tight_layout()
plt.show()


# همبستگی یا correlation عددی است که نشان می‌دهد دو ویژگی (Feature) چقدر با هم رابطه دارند
# مثلا وقتی ویژگی قد همزمان با ویژگی وزن افزایش پیدا میکنه، میگیم همبستگی این دو باهم +1 هست
# با افزایش سن، ساعت خواب کم میشه پس correlation بین این دو ویژگی -1 هست
# وقتی دو ویژگی هیچ رابطه ای باهم نداشته باشن Correlation بین آنها برابر 0 هست

# در آمار، رایج‌ترین معیار همبستگی ضریب همبستگی پیرسون (Pearson Correlation Coefficient) است
# فرمول آن بر پایه‌ی کوواریانس (Covariance) و انحراف معیار (Standard Deviation) ساخته شده است
# نتیجه آن همیشه بین +1 تا -1 هست
# در کتابخوانه pandas با دستور df.corr() بصورت پیش فرض از Pearson Correlation استفاده میشه

# چرا Matrix؟
# در این مثال مثلا 8 تا ویژگی داریم. رابطه بین هر دو ویژگی باید بررسی بشه
# پس میشه یک جدول 8*8 که به این جدول میگن Correlation Matrix
# در قطر اصلی همیشه نمره +1 هست چون هر ویژگی با خوش مقایسه شده مثلا Age با Age پس Correlation = 1
# جدول همیشه نسبت به قطر اصلی متقارن است چون corr(A,B)=corr(B,A)

# با استفاده از heatmap میتونیم بجای اینکه یک جدول عددی شلوغ رو بخونیم
# با نگاه کردن به رنگها میزان correlation بین ویژگی های مختلف رو متوجه بشیم
# 🟡 زرد = همبستگی زیاد      🟣 بنفش = همبستگی کم

# کاربردهای Correlation Matrix؟؟؟
# 1- feature selection
# اگر دو ستون مختلف همبستگی = تقریبا 1 داشته باشن باید یکیش حذف بشه    
# چون نگه داشتن 2 ستون شبیه به هم فایده نداره    
# 2- Finding Multicollinearity
# در Linear Regression وجود ویژگی‌های بسیار مشابه مشکل ایجاد می‌کند    
# 3- Before PCA
# اگر ویژگی‌ها خیلی به هم وابسته باشند،PCA بسیار مفید خواهد بود    
# 4- EDA(تحلیل داده)
# تقریباً اولین نموداری است که Data Scientist رسم می‌کند    




#---------------------------
"        Pipeline         "
#---------------------------

# x, y
x = df.drop(columns="MedHouseVal")
y = df["MedHouseVal"]

print(x.shape)   #(20640, 8)
print(y.shape)   #(20640,)


# train-test-split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, shuffle=True, random_state=42)
print("Training samples", x_train.shape[0])    # 16512
print("Test samples", x_test.shape[0])    # 4128


# Making Pipeline
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge

scaler = StandardScaler()
model = Ridge()

ridge_pipeline = Pipeline([
    ("scaler", scaler),
    ("model", model) ])


# Making parameter grid for GridSearchCV
ridge_param_grid = {
    # 'scaler': [None, StandardScaler(), MinMaxScaler()],
    # 'scaler__n_components: [2,3,4,5],
    'model__alpha': [0.001, 0.01, 0.1, 1, 10, 100]  }

from sklearn.model_selection import GridSearchCV
grid = GridSearchCV(
        estimator= ridge_pipeline, 
        param_grid= ridge_param_grid,
        scoring = 'neg_mean_absolute_percentage_error',
        cv=5,
        n_jobs=1  )


# Model fit
grid.fit(x_train, y_train)

# Score
grid.best_score_     #-0.3151441974454266

# Parameters
grid.best_params_    # {'model__alpha': 100}




















#===============================================================
#===============================================================
"ُ     Supervised clustering  - load_breast_cancer    "
#===============================================================
#===============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer(as_frame=True)
print(cancer.keys())
# dict_keys([
# 'data'
# 'target' 
# 'frame' 
# 'target_names'
# 'DESCR'
# 'feature_names'
# 'filename'
# 'data_module'])


df = cancer.frame.copy()
df.shape  # (569, 31)    تعداد 569 بیمار و 31 فیچر داریم

cancer.feature_names
array(['mean radius', 'mean texture', 'mean perimeter', 'mean area',
       'mean smoothness', 'mean compactness', 'mean concavity',
       'mean concave points', 'mean symmetry', 'mean fractal dimension',
       'radius error', 'texture error', 'perimeter error', 'area error',
       'smoothness error', 'compactness error', 'concavity error',
       'concave points error', 'symmetry error',
       'fractal dimension error', 'worst radius', 'worst texture',
       'worst perimeter', 'worst area', 'worst smoothness',
       'worst compactness', 'worst concavity', 'worst concave points',
       'worst symmetry', 'worst fractal dimension'], dtype='<U23')


cancer.target_names    # ['malignant', 'benign']
"malignant --> bad khim --> 1"
"benign --> khosh khim --> 0"


cancer.data
#      mean radius  mean texture  ...  worst symmetry  worst fractal dimension
# 0          17.99         10.38  ...          0.4601                  0.11890
# 1          20.57         17.77  ...          0.2750                  0.08902
# ..           ...           ...  ...             ...                      ...
# 567        20.60         29.33  ...          0.4087                  0.12400
# 568         7.76         24.54  ...          0.2871                  0.07039
# [569 rows x 30 columns]


cancer.target
# 0      0
# 1      0
#       ..
# 567    0
# 568    1
# Name: target, Length: 569, dtype: int64


df.head()
#    mean radius  mean texture  ...  worst fractal dimension  target
# 0        17.99         10.38  ...                  0.11890       0
# 1        20.57         17.77  ...                  0.08902       0
# 2        19.69         21.25  ...                  0.08758       0
# 3        11.42         20.38  ...                  0.17300       0
# 4        20.29         14.34  ...                  0.07678       0
# [5 rows x 31 columns]


df["target"].value_counts()
target
1    357   # bad khim
0    212   # khosh khim
Name: count, dtype: int64



#---------------------
"        EDA         "
#---------------------




#---------------------------
"        Pipeline         "
#---------------------------

x = df.drop(columns="target")
y = df["target"]

x.shape  #(569, 30)
y.shape  #(569, )

# الان کل ستون target فقط 0 و 1 هست که 0 یعنی خوش‌خیم و 1 یعنی بدخیم


"---- train-test-split ----"
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42, shuffle=True, stratify=y)

# در train_test_split پارامتر stratify برای این است که Class Distribution در
#  داده‌های train و test تقریباً مشابه دیتاست اصلی باقی بماند
# مهم‌ترین کاربرد stratify زمانی است که y شامل کلاس‌های categorical باشد

# فرض کنیم 100 تا نمونه داریم
Class A → 80 نمونه
Class B → 20 نمونه

# یعنی توزیع کلاس ها اینجوریه
A = 80%
B = 20%

# اگر تقسیم داده بصورت کاملا تصادفی باشه ممکنه نتیجه این بشه
Train:
A = 67
B = 13

Test:
A = 13
B = 7

# یعنی
Train → A=83.75% ، B=16.25%
Test  → A=65%    ، B=35%
# یعنی توزیع کلاس‌ها در test خیلی متفاوت از دیتاست اصلی شده است

# ولی اگر stratify=y باشه یعنی به train_test_split میگیم هنگام تقسیم داده، نسبت کلاس‌های y را در Train و Test حفظ کن
# بنابراین مثلا همچین حالتی خواهیم داشت:
Original:
A = 80%
B = 20%

Train:
A ≈ 80%
B ≈ 20%

Test:
A ≈ 80%
B ≈ 20%

# درواقع این پارامتر میاد براساس مقادیر y تقسیم را stratified انجام میده
# و اینجوری نسبت دیتاها در Test set حفظ میشه مخصوصا زمانی که y شامل کلاس‌های categorical باشد
# در عمل Stratified split با Random split فرق داره
# فرقش اینه که stratify جلوی Random بودن تقسیم را نمی‌گیرد؛ بلکه 
# نحوه‌ی انتخاب تصادفی نمونه‌ها را محدود می‌کند تا نسبت کلاس‌ها حفظ شود


"--- pipeline ----"
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression    # a classification model
model = LogisticRegression(max_iter=5000, random_state=42)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

classification_pipeline = Pipeline([
    ("scaler", scaler),
    ("model", model)])


"---- parameter grid ----"
classification_param_grid = {
    'model__C':[0.001,0.01,0.1,1,10,100],
    'model__penalty': ['l1', 'l2']}

from sklearn.model_selection import GridSearchCV
grid = GridSearchCV(estimator = classification_pipeline, 
                    param_grid = classification_param_grid,
                    cv=5,
                    scoring= 'accuracy')


"---- fit ----"
grid.fit(x_train, y_train)


"--- train scores ---"
grid.best_score_   #0.98
grid.best_params_   #{'model__C': 0.1, 'model__penalty': 'l2'}
best_model = grid.best_estimator_


"---- predict ----"
y_pred = best_model.predict(x_test)


"---- test score ----"
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)   #0.97


#--------------------------
"    Confusion Matrix     "
#--------------------------
from sklearn.metrics import confusion_matrix
conf_mat = confusion_matrix(y_test, y_pred)
print(conf_mat)
# [[40  2]
#  [ 1 71]]

# اصلا confusion matrix چیه؟
# یکی از مهم‌ترین ابزارها برای ارزیابی مدل‌های Classification است، چون به جای اینکه
# فقط بگوید «مدل چند درصد درست پیش‌بینی کرده»، دقیقاً نشان می‌دهد چه نوع اشتباهاتی انجام داده است

# مثلا در این دیتا، 140 تا نمونه تست داریم که مدل test score رو 97 درصد حساب کرده
# اینجا 97% مثلا یعنی 135 مورد رو درست پیشبینی کرده و 5 مورد اشتباه بوده
# درواقع conf mat میاد اون 5 موردی که اشتباه بوده رو بررسی میکنه

# این ماتریکس بصورت زیر نتیجه رو نشون میده که 4 حالت داره:
               Pred Positive   Pred Negative
                 ┌───────────┬───────────┐
Actual Positive  │    TP     │    FN     │
                 ├───────────┼───────────┤
Actual Negative  │    FP     │    TN     │
                 └───────────┴───────────┘

# ✅ TP — True Positive
# یعنی واقعا Positive بوده و مدل Positive تشخیص داده
# مثلا واقعا=بیمار / مدل=بیمار

# ✅ TN — True Negative
# واقعاً Negative بوده و مدل هم Negative تشخیص داده
# مثلا واقعا=سالم / مدل=سالم

# ❌ FP — False Positive
# واقعاً Negative بوده، ولی مدل اشتباهاً Positive تشخیص داده
# به این حالت میگیم False Positive / Type I Error
# مثلا واقعا=بیمار / مدل=سالم

# ❌ FN — False Negative
# واقعاً Positive بوده، ولی مدل اشتباهاً Negative تشخیص داده
# مثلا واقعا=بیمار / مدل=سالم
# به این حالت میگیم False Negative / Type II Error


# چرا اسمش Confusion Matrix است؟ چون نشان می‌دهد مدل کجاها گیج شده است
#                      | Predicted Healthy | Predicted Cancer |
# | ------------------ | ----------------- | ---------------- |
# | **Actual Healthy** |          90       |         10       |
# | **Actual Cancer**  |           5       |         95       |
# 90 سالم را درست تشخیص داده
# 10 سرطان را با سالم اشتباه گرفته
# 5 سالم را با سرطان اشتباه گرفته
# 95 سرطان را درست تشخیص داده

# پس صرفا گفتن Accuracy = 97% به تنهایی همیشه کافی نیست
# در این موارد Confusion Matrix به ما می‌گوید این 3٪ خطا دقیقاً از کجا آمده است


حالا ارتباط Confusion Matrix با Classification Metrics چیه؟
# 4 مقدار اصلی TP,TN,FP,FN پایه محاسبه چند معیار مهم هستند
Accuracy:
# چه درصدی از کل پیش‌بینی‌ها درست بوده‌اند؟
# Accuracy=(TP+TN) / (FP+FN+TP+TN)

Precision:
# از تمام مواردی که مدل Positive اعلام کرده، چند درصد واقعاً Positive بوده‌اند؟
# Precision=TP / (FP+TP)
​
Recall:
# از تمام Positiveهای واقعی، مدل چند مورد را پیدا کرده است؟
# Recall=TP / (FN+TP)

F1 score:
# ترکیبی از Precision و Recall است
# F1 = 2 × ( [Precision×Recall] / [Precision+Recall]​​ )


پس Accuracy کلا بدرد نمیخوره؟
# 950 سالم
# 50 بیمار
# گاهی ممکنه Accuracy=95% باشه یعنی مدل مثلا از 1000 نمونه 950 تا درست گفته
# ظاهرا مدل عالی عمل میکنه ولی:
# TP = 0
# FN = 50
# یعنی عملا هیچ بیمار واقعی‌ای را پیدا نکرده است. در مواردی مثل پزشکی FN خیلی اهمیت داره
# در چنین مواردی conf mat و معیار هایی که ازش ساخته میشه اهمیت پیدا میکنن


نمایش گرافیکی
# برای اینکه خواندن conf mat راحت تر بشه از ConfusionMatrixDisplay استفاده میشه و با plot رسم میکنه
from sklearn.metrics import ConfusionMatrixDisplay
conf_mat_display = ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
print(conf_mat_display)











#===============================================================
#===============================================================
"ُ     Unsupervised clustering  - load wine dataset    "
#===============================================================
#===============================================================

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_wine

wine = load_wine(as_frame=True)

df = wine.frame.copy()
print(df)
#      alcohol  malic_acid   ash  ...  od280/od315_of_diluted_wines  proline  target
# 0      14.23        1.71  2.43  ...                          3.92   1065.0       0
# 1      13.20        1.78  2.14  ...                          3.40   1050.0       0
# ..       ...         ...   ...  ...                           ...      ...     ...
# 177    14.13        4.10  2.74  ...                          1.60    560.0       2
# [178 rows x 14 columns]

# x
wine.feature_names
# ['alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium',
#  'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins',
#  'color_intensity', 'hue', 'od280/od315_of_diluted_wines', 'proline']

# y
wine.target_names
# ['class_0', 'class_1', 'class_2']

# اینجا دیتای ما clean هست ولی همیشه اینجوری دیتا آماده نیست
# بعضی مواقع اصلا y رو نداریم و باید از روش unsupervised استفاده کنیم
# در این مثلا فرض میکنیم که فقط x داریم و Y وجود نداره


"x"
x = df.drop(columns="target")
y_real = df["target"]


"model: Kmeans"
from sklearn.cluster import KMeans

# ازونجایی که نمیدونیم n_cluster باید چه عددی بزاریم از روش elbow برای پیدا کردن مقدار k استفاده میکنیم
# Elbow method
k_values = range(1,11)
inertia_values = []
for k in k_values:
    model = KMeans(n_clusters=k, random_state=42, n_init=200)
    elbow_pipeline = Pipeline([
        ("scaler", StandardScaler),
        ("kmeans", model)])

    elbow_pipeline.fit(x)
    inertia = (elbow_pipeline.named_steps["kmeans"].inertia)
    inertia_values.append(inertia)

# میاد روی این دیتا 11 تا kmeans محاسبه میکنه
# رسم کردن
plt.figure(figsize=(8,6))
plt.plot(list(k_values), inertia_values, marker="o")
plt.xlabel("number of cluster(k")
plt.ylabel("inertia")
plt.title("elbow method")
plt.show()

# براساس شکل نمودار میتونیم بگیم:
best_k = 3


"final clustering"
final_clustering = Pipeline([
    ("scaler", StandardScaler),
    ("kmeans", KMeans(n_clusters=best_k, random_state=42, n_init=20)])


"cluster labels"
cluster_labels = final_clustering.fit_predict(x)


"histogram"
plt.hist(cluster_labes, bins=30)
plt.show()


"Adding to dataset"
clustered_df = x.copy()
clustered_df["cluster"] = cluster_labels
clustered_df["real_class"] = y_real.values


clustered_df.head()


"plt"
plt.scatter(clustered_df["alcohol"], clustered_df["malic_acid"], c=clustered_df["cluster"])
plt.xlabel("alcohol")
plt.ybalel("malic_acid")
plt.show()









































