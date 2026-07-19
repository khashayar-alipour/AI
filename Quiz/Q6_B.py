


     #|=========================================|
     #|    Quiz 6                               |
     #|    Part B                               |
     #|    taxi_fare_dataset.xlsx               |
     #|    Author: Khashayar Alipour            |
     #|=========================================|

#________________________________________________________________________________________________________________________

# دیتای مربوط به مولفه‌های تصمیم گیرنده برای هزینه کرایه تاکسی اینترنتی در شهر نیویورک
# دیتارو وارد کن، Clean کن، یک مدل انتخاب کن و پیشبینی و رسم انجام بده


import pandas as pd

data = pd.read_excel("C:/Users/C P C/Desktop/taxi_fare_dataset.xlsx")

data.columns
# Index(['distance', 'duration', 'traffic', 'speed', 'rain', 'fare'], dtype='object')

data.head()
#     distance   duration   traffic      speed      rain        fare
# 0  11.548934  63.438231  0.185133  67.098996  0.261706   84.395736
# 1  28.546072  49.176480  0.541901  62.710007  0.246979  121.224703
# 2  22.093821  29.238430  0.872946  12.820627  0.906255   99.720935
# 3  18.160425  73.613962  0.732225  47.537261  0.249546  117.325635
# 4   5.102550  62.256343  0.806561  51.821518  0.271950   76.033862

data.tail()
#       distance   duration   traffic       speed      rain        fare
# 495  10.923891  10.059222  0.668213   82.265067  0.492325   47.207480
# 496  17.717855  82.723595  0.619490  115.227608  0.577279  120.890254
# 497   2.793172  14.040040  0.463494   17.585382  0.865577   32.559993
# 498  29.244647  85.620887  0.379786   16.276019  0.980739  154.546920
# 499  29.593217  41.248508  0.863334   41.040578  0.407584  124.403111

data.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 500 entries, 0 to 499
# Data columns (total 6 columns):
#      Column    Non-Null Count  Dtype  
# ---  ------    --------------  -----  
#  0   distance  499 non-null    float64
#  1   duration  499 non-null    float64
#  2   traffic   500 non-null    float64
#  3   speed     499 non-null    float64
#  4   rain      500 non-null    float64
#  5   fare      500 non-null    float64
# dtypes: float64(6)
# memory usage: 23.6 KB

data.describe()
#         distance    duration     traffic       speed        rain        fare
# count  499.000000  499.000000  500.000000  499.000000  500.000000  500.000000
# mean    15.186410   44.433057    0.517558   64.607830    0.499844   83.562537
# std      8.807425   25.144102    0.297193   31.602600    0.285809   30.591845
# min      0.649317    2.407618    0.004940   10.354009    0.001565   16.027666
# 25%      7.600859   22.147345    0.241228   36.504179    0.268112   62.099775
# 50%     15.606745   43.541891    0.539738   65.919660    0.496012   84.284857
# 75%     22.773887   65.971964    0.777344   91.113497    0.743293  105.194153
# max     29.792461   89.975155    0.999414  119.818226    0.995438  156.945863



'''============================[ Data cleaning ]============================'''

''' empty cell '''
data.isnull().sum()
# distance    1
# duration    1
# traffic     0
# speed       1
# rain        0
# fare        0
# dtype: int64

data.dropna(inplace=True)

data.isnull().sum()
# distance    0
# duration    0
# traffic     0
# speed       0
# rain        0
# fare        0
# dtype: int64



''' type '''
data.info()
# <class 'pandas.core.frame.DataFrame'>
# Index: 497 entries, 0 to 499
# Data columns (total 6 columns):
#      Column    Non-Null Count  Dtype  
# ---  ------    --------------  -----  
#  0   distance  497 non-null    float64
#  1   duration  497 non-null    float64
#  2   traffic   497 non-null    float64
#  3   speed     497 non-null    float64
#  4   rain      497 non-null    float64
#  5   fare      497 non-null    float64
# dtypes: float64(6)
# memory usage: 27.2 KB



''' logical '''
data.describe()
#        distance    duration     traffic       speed        rain        fare
# count  497.000000  497.000000  497.000000  497.000000  497.000000  497.000000
# mean    15.161762   44.469077    0.517947   64.480688    0.499386   83.500922
# std      8.804914   25.103544    0.297660   31.601570    0.285932   30.604261
# min      0.649317    2.407618    0.004940   10.354009    0.001565   16.027666
# 25%      7.567076   22.174123    0.242045   36.476198    0.261706   61.710921
# 50%     15.606745   43.541891    0.539491   65.675605    0.494212   84.308449
# 75%     22.759015   65.863317    0.779584   91.056112    0.743193  105.175236
# max     29.792461   89.975155    0.999414  119.818226    0.995438  156.945863



''' duplicated '''
data.duplicated().sum()    #np.int64(0)  -> there are no duplicates



''' final step '''
data.reset_index(drop=True,inplace=True)







'''==============================[ x , y]==================================='''

# الان دیگر یک X نداریم؛ بلکه یک ماتریس X داریم که هر ستون آن یک ویژگی (Feature) است

# x = data.drop(columns='fare')   همه ستونها غیر از فلان ستون
x=data[['distance', 'duration', 'traffic', 'speed', 'rain']]
# distance   duration   traffic       speed      rain
# 0    11.548934  63.438231  0.185133   67.098996  0.261706
# 1    28.546072  49.176480  0.541901   62.710007  0.246979
# ...     ...        ...       ...         ...        ...
# 495  29.244647  85.620887  0.379786   16.276019  0.980739
# 496  29.593217  41.248508  0.863334   41.040578  0.407584
# [497 rows x 5 columns]


y=data["fare"]
# 0      84.395736
# 1      121.224703
# ---    ---
# 495    154.546920
# 496    124.403111
# Name: fare, Length: 497, dtype: float64






'''=================================[ Model ]==============================='''
from sklearn.linear_model import SGDRegressor
model = SGDRegressor(loss = 'squared_error',learning_rate='constant',eta0=0.0001 , max_iter=10000,random_state=42)
model.fit(x,y)





'''===============================[a,b]====================================='''
a=model.coef_
b=model.intercept_
print(a)     #[ 2.70317612  0.87100133  2.81971823 -0.05106231  1.56228414]
print(b)     #[1.60721815]

# معادله دیگر این نیست: y=a*x+b
# الان که 5 تا Feature یا ویژگی داریم: y=a1​x1​+a2​x2​+a3​x3​+a4​x4​+a5​x5​+a6​x6​+b
# یعنی هر ستون(ویژگی) یک ضریب برای خودش دارد






'''=============================[predict]==================================='''
y_pred=model.predict(x)




'''================================[matplotlib]============================='''

# برای رسم میتونیم چندتا کار انجام بدیم
# 1-میتونیم مقدار واقعی(y) و پیش‌بینی(y_pred) را با هم مقایسه کنیم

import matplotlib.pyplot as plt

y=data["fare"]
y_pred=model.predict(x)

plt.scatter(y, y_pred)
plt.xlabel("Actual Fare")
plt.ylabel("Predicted Fare")
plt.title("Y vs Y-pred")
plt.show()


# 2-میتونیم دونه دونه هر Feature رو با fare مقایسه کنیم و رابطشون رو رسم کنیم

x_distance=data[["distance"]]
y=data["fare"]
y_pred=model.predict(x)

plt.scatter(x_distance, y, label="data")
plt.plot(x_distance, y_pred, label="prediction", color="red", alpha=0.5)
plt.xlabel("distance")
plt.ylabel("Predicted Fare")
plt.title("distance vs fare")
plt.legend()
plt.show()


# 3-میتونیم یک حلقه بزنیم بیاد دونه دونه همه مولفه هارو با fare مقایسه کنه و رسمشون کنه
# الان به تعداد featureها میاد نمودار رسم میکنه

for column in data.columns:
    if column != 'fare':
        plt.figure(figsize=(10,6))
        plt.scatter(data[column], data['fare'], s=5)
        plt.xlabel(column)
        plt.ylabel('fare')
        plt.title(f"{column} vs fare")
        plt.show()



# 4-میشه همه جدول هارو با استفاده از کتابخوانه Seaborn به اینصورت کنار هم دید

import seaborn as sns
sns.pairplot(data)
plt.show()


# 5-میشه نمودار 3 بعدی هم بکشیم
# ولی باید تصمیم بگیریم کدوم دو Feature رو میخوایم با Fare مقایسه کنیم
# در نمودارهای بالا مشخصه که distance و duration تقریبا با Fare رابطه خطی دارن
# ولی بقیه مولفه ها خیلی رابطه مشخصی با fare ندارن
# پس میایم distance و duration رو با fare مقایسه میکنیم

x1=data["distance"]
x2=data["duration"]
y=data["fare"]

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection="3d")

scatter = ax.scatter(x1,x2,y, c=y, cmap="viridis", alpha=0.5)

ax.set_xlabel("distance")
ax.set_ylabel("duration")
ax.set_zlabel("fare")
ax.set_title("Distance,Duration vs Fare")

fig.colorbar(scatter, ax=ax, label="Fare")
plt.tight_layout()
plt.show()






















