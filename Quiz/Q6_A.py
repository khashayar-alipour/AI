


     #|=========================================|
     #|    Quiz 6                               |
     #|    Part A                               |
     #|    Material_Strength_Temperature.xlsx   |
     #|    Author: Khashayar Alipour            |
     #|=========================================|

#________________________________________________________________________________________________________________________

# در این تمرین دیتا از فایل Material_Strength_Temperature.xlsx توسط pandas وارد شد
# در مرحله pre_processing دیتا clean شد
# سپس x و y مشخص شد
# از مدل SGDRegressor استفاده کردیم
# مدل با دیتا fit شد و train انجام شد
# سپس a و b و بعد predict محاسبه شد
# در مرحله رسم مشکل داشتیم که Scaling کردیم و حل شد
# در انتها نمودار صحیح رسم شد



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



data = pd.read_excel("C:/Users/C P C/Desktop/Material_Strength_Temperature.xlsx")

data.columns   #Index(['Temperature', 'UTS'], dtype='object')

data.head()
#    Temperature    UTS
# 0         20.0  590.0
# 1         40.0  578.0
# 2         60.0  571.0
# 3         80.0  560.0
# 4        100.0  552.0

data.tail()
#     Temperature    UTS
# 32        660.0  299.0
# 33        680.0  290.0
# 34        700.0  281.0
# 35        720.0  272.0
# 36        740.0  263.0


data.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 37 entries, 0 to 36
# Data columns (total 2 columns):
#      Column       Non-Null Count  Dtype  
# ---  ------       --------------  -----  
#  0   Temperature  36 non-null     float64
#  1   UTS          36 non-null     float64
# dtypes: float64(2)
# memory usage: 724.0 bytes

# 37 entries -> یعنی 37 بار در دماها با استحکامهای مختلف آزمایش انجام شده


data.describe()
#        Temperature         UTS
# count    36.000000   36.000000
# mean    355.555556  424.722222
# std     244.627349   98.877590
# min    -320.000000  263.000000  --> negative temp!!
# 25%     175.000000  340.750000
# 50%     370.000000  426.500000
# 75%     545.000000  506.000000
# max     740.000000  590.000000



'''================ data cleaning ======================'''
#1-empty cell 
#2- Type
#3- logical
#4- duplcited


#============= 1-empty cell, type ============

data.dropna(inplace=True)
#data["Temperature"].dropna(inplace=True)
#data["UTS"].dropna(inplace=True)
data.describe()
#        Temperature         UTS
# count    35.000000   35.000000
# mean    352.571429  427.857143
# std     247.533038   98.489218
# min    -320.000000  263.000000
# 25%     170.000000  347.000000
# 50%     360.000000  430.000000
# 75%     550.000000  509.000000
# max     740.000000  590.000000

data.isnull().sum()
# Temperature    0
# UTS            0
# dtype: int64

data.info()
# <class 'pandas.core.frame.DataFrame'>
# Index: 35 entries, 0 to 36
# Data columns (total 2 columns):
#      Column       Non-Null Count  Dtype  
# ---  ------       --------------  -----  
#  0   Temperature  35 non-null     float64
#  1   UTS          35 non-null     float64
# dtypes: float64(2)
# memory usage: 840.0 bytes




#========== 2-type ====================
data.astype(float)




#============= 3-logical ==============
# temeprature can't be negative

new_data = data[data['Temperature'] > 0]
# new_data = data.apply(lambda x: x > 0)

new_data.describe()
#        Temperature         UTS
# count    34.000000   34.000000
# mean    372.352941  427.235294
# std     221.401306   99.900574
# min      20.000000  263.000000  --> negative temp removed
# 25%     185.000000  345.000000
# 50%     370.000000  426.500000
# 75%     555.000000  512.000000
# max     740.000000  590.000000




#============= 4-duplicated ==============
new_data.duplicated().sum()   #0   there are no duplicates
new_data.drop_duplicates(inplace=True)



#========================================
#============= Final touch ==============
new_data.reset_index(drop=True,inplace=True)

new_data.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 34 entries, 0 to 33
# Data columns (total 2 columns):
#      Column       Non-Null Count  Dtype  
# ---  ------       --------------  -----  
#  0   Temperature  34 non-null     float64
#  1   UTS          34 non-null     float64
# dtypes: float64(2)
# memory usage: 676.0 bytes


new_data.columns
#Index(['Temperature', 'UTS'], dtype='object')


new_data.head()
#Temperature	UTS
#0	20.0	590.0
#1	40.0	578.0
#2	60.0	571.0
#3	80.0	560.0
#4	100.0	552.0


new_data.tail()
#Temperature	UTS
#29	660.0	299.0
#30	680.0	290.0
#31	700.0	281.0
#32	720.0	272.0
#33	740.0	263.0







'''
================================= x , y =======================================
'''

#======== pd.column ==========

temperature = new_data["Temperature"]
print(temperature)
# 0      20.0
# 1      40.0
# 2      60.0
# ..     ...
# 33    740.0
# Name: Temperature, dtype: float64


uts = new_data["UTS"]
print(uts)
# 0     590.0
# 1     578.0
# 2     571.0
# 33    263.0
# Name: UTS, dtype: float64



#======= np.array =========

x = np.array(new_data["Temperature"])
print(x)
x.ndim()   #1
# [ 20.  40.  60.  80. 100. 120. 140. 160. 180. 200. 220. 240. 260. 280.
#  300. 340. 360. 380. 400. 420. 440. 480. 500. 520. 540. 560. 580. 600.
#  640. 660. 680. 700. 720. 740.]

y = np.array(new_data["UTS"])
print(y)
y.ndim()   #1
# [590. 578. 571. 560. 552. 541. 533. 522. 515. 503. 497. 485. 476. 468.
#  458. 441. 430. 423. 412. 404. 395. 378. 368. 360. 351. 343. 334. 326.
#  307. 299. 290. 281. 272. 263.]






'''
================================= model =======================================
'''
from sklearn.linear_model import SGDRegressor

model = SGDRegressor(loss = 'squared_error',learning_rate='constant',eta0=0.0001 , max_iter=10000,random_state=42)





'''
============================= model.fit =======================================
'''

model.fit(x.reshape(-1,1), y)    #fit shod





'''
================================= a , b =======================================
'''
a = model.coef_
b = model.intercept_
print("a: ", a)    #[-4.00665527e+10]
print("b: ", b)    #[-1.22056113e+09]  

y_line = a*x + b
print(y_line)    # y=[-4.00665527e+10]*x + [-1.22056113e+09]




'''
================================= predict =====================================
'''


y_pred = model.predict([760].reshape(-1,1))
print(y_pred)

# pred_temp    pred_uts
# 760
# 780
# 800
# 820






'''
================================= matplotlib =====================================
'''

x = np.array(new_data["Temperature"])
print(x)
x.ndim()   #1
# [ 20.  40.  60.  80. 100. 120. 140. 160. 180. 200. 220. 240. 260. 280.
#  300. 340. 360. 380. 400. 420. 440. 480. 500. 520. 540. 560. 580. 600.
#  640. 660. 680. 700. 720. 740.]

y = np.array(new_data["UTS"])
print(y)
y.ndim()   #1
# [590. 578. 571. 560. 552. 541. 533. 522. 515. 503. 497. 485. 476. 468.
#  458. 441. 430. 423. 412. 404. 395. 378. 368. 360. 351. 343. 334. 326.
#  307. 299. 290. 281. 272. 263.]

y_pred = model.predict(x)
x = x.reshape(-1,1)

plt.scatter(x, y, label="new_data")    # رسم نقاط واقعی آزمایش
plt.plot(x,y_pred, label="prediction", color="red")     # خطی که از پیشبینی مدل رسم میشه
plt.xlabel("Temperature")
plt.ylabel("UTS")
plt.title("Temp vs UTS")
plt.grid()
plt.legend()
plt.show()




'''
=============================== problem - scaling =============================
'''

# بعد از فیت کردن و train شدن مدل اومدیم نمودارش رو رسم کردیم ولی اون چیزی که میخواستیم نشد
# و همچنین ضرایب a و b اعدادی غیرطبیعی و بسیار بزرگ هستند


# مشکل اینجاست که temperature بین 20 تا 730 هست در دیتا
# وقتی اعداد Feature بزرگ باشند، مقدار گرادیان نیز بزرگ می‌شود
# در نتیجه وزن‌ها خیلی سریع به سمت مقادیر بسیار بزرگ یا بسیار منفی حرکت می‌کنند
# در نهایت مدل به جای اینکه به بهترین خط برسد، واگرا (Diverge) می‌شود
# به همین دلیل شیب خط (a) تقریباً شده است: 40,000,000,000-
# که اصلاً منطقی نیست


# در واقع آموزش SGD به دلیل مقیاس داده‌ها دچار مشکل شده است
# در این دیتاهایی که داریم تغییر learning rate تاثیری نداره
# در واقع حتی اگه کوچکش کنیم بازم مدل به جواب درست نمیرسه
# در چنین مواردی که feature ما بسیار بزرگ هست اگر Featureها Scale نشده باشند
# حتی با Learning Rate کوچک هم ممکن است گرادیان آن‌قدر بزرگ باشد که مدل نتواند به جواب مناسبی برسد


''' Scaling'''

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor

#===== x,y
scaler = StandardScaler()
x = np.array(new_data["Temperature"])
x_scaled = scaler.fit_transform(x)
print(x_scaled)

y = np.array(new_data["UTS"])
print(y)

#====== fit
model.fit(x_scaled, y)


#====== a,b
a = model.coef_
b = model.intercept_
print(a)   #[-98.27807391]
print(b)   #[426.71759548]
# y = -98.27807391 * x + 426.71759548


#====== pred
y_pred = model.predict(x_scaled)


#====== matplotlib
import matplotlib.pyplot as plt

plt.scatter(x,y,label="Real Data")
plt.plot(x,y_pred,color="red",label="Prediction")
plt.legend()
plt.show()













