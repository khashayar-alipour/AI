


     #|=========================================|
     #|    Quiz 6                               |
     #|    Part C                               |
     #|    delivery_time_dataset.csv            |
     #|    Author: Khashayar Alipour            |
     #|=========================================|

#________________________________________________________________________________________________________________________

# دیتای مربوط به ارسال بسته توسط uber در شهر Vancouver
# تخمین زمان رسیدن بسته، برای 2300 بسته رو توی دیتا آورده
# دیتا clean هست و نیاز به پاکسازی نیست، مدل انتخاب کن و پیشبینی انجام بده


import pandas as pd

data = pd.read_csv("C:/Users/C P C/Desktop/delivery_time_dataset.csv")

data.columns
# Index(['distance', 'items', 'traffic', 'prep_time', 'courier_speed', 'delivery_time'], dtype='object')

data.head()
#     distance  items   traffic  prep_time  courier_speed  delivery_time
# 0  10.823249     18  0.911573  48.134486      29.312917      80.489224
# 1  22.364597     16  0.009994  20.072629      23.531980      66.862832
# 2   3.390687     15  0.782506  27.089022      58.616715      38.816909
# 3  17.862776     11  0.057527  27.728805      47.546690      56.541215
# 4   9.030875     13  0.478222  32.020010      52.279925      46.480209

data.tail()
#        distance  items   traffic  prep_time  courier_speed  delivery_time
# 2295  17.941850     18  0.238214  25.530324      67.021058      54.182698
# 2296   8.363905     18  0.769664  52.059629      31.792588      78.745015
# 2297  17.625107      5  0.264285  32.409333      50.275774      64.014790
# 2298  13.406402     14  0.727216  58.063107      24.593095      87.463284
# 2299  16.975759     11  0.837286  32.699184      36.981217      72.701143


data.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 2300 entries, 0 to 2299
# Data columns (total 6 columns):
#       Column         Non-Null Count  Dtype  
# ---  ------         --------------  -----  
#  0   distance       2300 non-null   float64
#  1   items          2300 non-null   int64  
#  2   traffic        2300 non-null   float64
#  3   prep_time      2300 non-null   float64
#  4   courier_speed  2300 non-null   float64
#  5   delivery_time  2300 non-null   float64
# dtypes: float64(5), int64(1)
# memory usage: 107.9 KB


data.isnull().sum()
# distance         0
# items            0
# traffic          0
# prep_time        0
# courier_speed    0
# delivery_time    0
# dtype: int64


data.describe()
#           distance        items  ...  courier_speed  delivery_time
# count  2300.000000  2300.000000  ...    2300.000000    2300.000000
# mean     12.547974     9.981739  ...      44.544259      57.157140
# std       7.111210     5.406215  ...      20.105648      18.991136
# min       0.500228     1.000000  ...      10.007716       1.652226
# 25%       6.313633     5.000000  ...      27.096619      43.281137
# 50%      12.578500    10.000000  ...      44.892358      57.597291
# 75%      18.667394    15.000000  ...      61.518015      70.074478
# max      24.992523    19.000000  ...      79.978693     112.329318





'''==============================[ x , y]==================================='''

x = data.drop(columns="delivery_time")    #all columns except "delivery_time"
print(x.shape)    #(2300, 5) -> no need to reshape

y = data["delivery_time"]




'''=================================[ Model ]==============================='''
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x,y)




'''===============================[a,b]====================================='''
a=model.coef_
b=model.intercept_
print(a)    #[ 1.79467868  0.50177496 19.89185063  0.69781051 -0.29420113]
print(b)    #9.828680469264462




'''=============================[predict]==================================='''
y_pred=model.predict(x)




'''================================[matplotlib]============================='''
import matplotlib.pyplot as plt


#========= y vs y_pred ==============
y = data["delivery_time"]
y_pred = model.predict(x)

plt.figure(figsize=(9,6), dpi=300)
plt.scatter(y,y_pred)
plt.xlabel("Actual delivery_time")
plt.ylabel("Predicted delivery_time")
plt.title("Real vs Predicted delivery time")
plt.tight_layout()
plt.show()


#========= data[...] vs y_pred =============
x_distance = data["distance"]
y = data["delivery_time"]
y_pred = model.predict(x)

plt.figure(figsize=(8,5), dpi=300)
plt.scatter(x_distance, y, label="data")
plt.plot(x_distance, y_pred, label="Prediction", color="red", alpha=0.6)
plt.xlabel("distance")
plt.ylabel("delivery_time")
plt.title("distance vs delivery_time")
plt.legend()
plt.tight_layout()
plt.show()


#======== loop for all columns ===========
for column in data.columns:
    if column != 'delivery_time':    # غیر از فلان ستون، بقیه ستونهارو لحاظ کن
        plt.figure(figsize=(10,6))
        plt.scatter(data[column], data['delivery_time'], s=5)   #s=size
        plt.xlabel(column)
        plt.ylabel('delivery_time')
        plt.title(f"{column} vs delivery_time")
        plt.show()


#======== seaborn pairplot ===========
import seaborn as sns
sns.pairplot(data)
plt.show()


#======== 3D ===========
x1=data["distance"]    # x مختصات محور
x2=data["prep_time"]    # y مختصات محور
y=data["delivery_time"]   # z مختصات محور

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection="3d")

scatter = ax.scatter(x1,x2,y, c=y, cmap="plasma", alpha=0.5)

ax.set_xlabel("distance")
ax.set_ylabel("prep_time")
ax.set_zlabel("delivery_time")
ax.set_title("Distance, prep_time vs delivery_time")

fig.colorbar(scatter, ax=ax, label="delivery_time")
plt.tight_layout()
plt.show()



#================ آموزشی ================
# اینجا fig مخفف Figure هست که همون صفحه‌ای هست که نمودار توش رسم میشه
# اینجا ax یعنی Axes که میشه محلی داخل Figure که نمودار روی آن رسم می‌شود

# Figure
# ┌────────────┐
# │ ┌───────┐  │
# │ │  Axes │  │
# │ └───────┘  │
# └────────────┘

# هر Figure می‌تواند چند تا Axes داشته باشد
# ┌───────────────────────┐
# │ ┌────────┐ ┌────────┐ │
# │ │ Axes1  │ │ Axes2  │ │
# │ └────────┘ └────────┘ │
# │ ┌────────┐ ┌────────┐ │
# │ │ Axes3  │ │ Axes4  │ │
# │ └────────┘ └────────┘ │
# └───────────────────────┘


# این add_subplot(111) یعنی چی؟
# از سه عدد تشکیل شده
# 1row - 1column - subplot number 1

# اگر مینوشتم 221 این میشد:
# 2 سطر - 2 ستون
# ┌─────┬─────┐
# │  1  │  2  │
# ├─────┼─────┤
# │  3  │  4  │
# └─────┴─────┘


# این projection="3d" یعنی چی؟
# وقتی اینو بنویسیم خود matplotlib میاد هر 3 محور x,y,z رو رسم میکنه


# چرا مینویسیم ax.scatter ؟ 
# چون حالا نمودار داره داخل Axes رسم میشه نه مستقیم داخل Figure


# وقتی مینویسیم c=red یعنی رنگ هر نقطه قرمز بشه
# وقتی میگیم c=y یعنی رنگ هر نقطه براساس مقادیر متغیر y که میشه ستون Delivery_time بشه
# در این پالت cmap="viridis" یعنی پالت virdis کمترین مقدار رنگش 🟣 و بعدش 🔵 و بعد 🟢 و بیشترین مقدار 🟡 هست
# در پالت plasma ترکیب رنگی متفاوتی هست


# اینجا fig.colorbar(scatter, ax=ax) وقتی نوشتیم Scatter یعنی رنگهارو از روی نمودار Scatter بخوان
# وقتی نوشیتیم ax=ax یعنی این Colorbar برای همین axes هست (برای مواردی که چند axes داریم)










































