


     #|=========================================|
     #|    Quiz 6                               |
     #|    Part D                               |
     #|    home_energy_consumption_dataset.xlsx |
     #|    Author: Khashayar Alipour            |
     #|=========================================|

#________________________________________________________________________________________________________________________

# این دیتا درمورد مصرف ماهیانه انرژی 11300 خانه در ژاپن میباشد
# دیتا نیاز به پاکسازی ندارد
# پیشبینی با مدل انجام شود



import pandas as pd
data = pd.read_excel("c:/Users/C P C/Desktop/home_energy_consumption_dataset.xlsx")

data.columns
# temperature
# house_size
# people -> تعداد افراد داخل هر خانه
# ac_hours -> ساعت روشن بودن سیستم تهویه
# heater_hours
# efficiency -> میزان کارامدی برق‌کشی خانه
# energy_consumption


data.head()
#    temperature  house_size  ...  efficiency  energy_consumption
# 0    36.286664  230.891624  ...    0.604524          183.092506
# 1    37.185926  125.656955  ...    0.889281           43.262531
# 2     5.397596  223.469312  ...    0.842110          131.340794
# 3    20.806207  238.991548  ...    0.705291          149.069933
# 4    14.190455   89.951958  ...    0.859180           45.770136
# [5 rows x 7 columns]


data.tail()
# temperature  house_size  ...  efficiency  energy_consumption
# 11295    35.536287  138.758217  ...    0.906347          109.456675
# 11296    -9.700708  188.762005  ...    0.804694          104.101898
# 11297     9.331590  146.946124  ...    0.966198           87.312936
# 11298    -9.680574  172.077905  ...    0.599810           79.678103
# 11299    17.924326  243.845820  ...    0.681053          155.016198
# [5 rows x 7 columns]


data.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 11300 entries, 0 to 11299
# Data columns (total 7 columns):
#      Column              Non-Null Count  Dtype  
# ---  ------              --------------  -----  
#  0   temperature         11300 non-null  float64
#  1   house_size          11300 non-null  float64
#  2   people              11300 non-null  int64  
#  3   ac_hours            11300 non-null  float64
#  4   heater_hours        11300 non-null  float64
#  5   efficiency          11300 non-null  float64
#  6   energy_consumption  11300 non-null  float64
# dtypes: float64(6), int64(1)
# memory usage: 618.1 KB

data.isnull().sum()
# temperature           0
# house_size            0
# people                0
# ac_hours              0
# heater_hours          0
# efficiency            0
# energy_consumption    0


data.describe()
# temperature    house_size  ...    efficiency  energy_consumption
# count  11300.000000  11300.000000  ...  11300.000000        11300.000000
# mean      17.753174    145.509389  ...      0.750299          103.340534
# std       15.857629     60.782403  ...      0.144061           29.818382
# min       -9.992908     40.009983  ...      0.500114           10.221707
# 25%        4.069822     93.144472  ...      0.625036           82.783054
# 50%       17.761608    144.853789  ...      0.751477          103.491832
# 75%       31.633782    198.992363  ...      0.873311          123.951956
# max       44.992384    249.977959  ...      0.999958          196.836937
# [8 rows x 7 columns]




'''==============================[ x , y]==================================='''

x=data.drop(columns=("energy_consumption"))
y=data["energy_consumption"]



'''=================================[ model ]==============================='''
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x,y)


'''===============================[a,b]====================================='''
a=model.coef_
b=model.intercept_
print(a)    #[ 1.09472358e+09 -1.79222222e+09 -6.28609234e+08  5.61267626e+09  -3.45700852e+07 -4.32635334e+09]
print(b)    #[-2.73594402e+09]


'''=============================[predict]==================================='''
y_pred=model.predict(x)



'''=============================[scaling]==================================='''
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)



'''================================[matplotlib]============================='''
import matplotlib.pyplot as plt


#========= y vs y_pred ==============
y=data["energy_consumption"]
y_pred=model.predict(x)

plt.scatter(y,y_pred, c="red", alpha=0.4)
plt.xlabel("real energy_cons")
plt.ylabel("predicted energy_cons")
plt.title("real vs predicted energy_cons")
plt.show()



#========= data[...] vs y_pred ============
x_temperater = data["temperature"]
y = data["energy_consumption"]
y_pred = model.predict(x)

plt.figure(figsize=(8,5), dpi=300)
plt.scatter(x_temperater, y, label="data")
plt.plot(x_temperater, y_pred, label="Prediction", color="red", alpha=0.6)
plt.xlabel("temperature")
plt.ylabel("energy_consumtion")
plt.title("temperature vs energy_consumtion")
plt.legend()
plt.tight_layout()
plt.show()



#======== loop for all columns ===========
for column in data.columns:
    if column != 'energy_consumption':    # غیر از فلان ستون، بقیه ستونهارو لحاظ کن
        plt.figure(figsize=(10,6))
        plt.scatter(data[column], data['energy_consumption'], s=5)   #s=size
        plt.xlabel(column)
        plt.ylabel('energy_consumption')
        plt.title(f"{column} vs energy_consumption")
        plt.show()



#======== seaborn pairplot ===========
import seaborn as sns
sns.pairplot(data)
plt.show()



#========= 3D =========================
x1=data["house_size"]    # x مختصات محور
x2=data["ac_hours"]    # y مختصات محور
y=data["energy_consumption"]   # z مختصات محور

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection="3d")

scatter = ax.scatter(x1,x2,y, c=y, cmap="plasma", alpha=0.5)

ax.set_xlabel("house_size")
ax.set_ylabel("ac_hours")
ax.set_zlabel("energy_consumption")
ax.set_title("house_size, ac_hours vs energy_consumption")

fig.colorbar(scatter, ax=ax, label="energy_consumption")
plt.tight_layout()
plt.show()












