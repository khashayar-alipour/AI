
"""
        ====================================================================
        ===========      Created on Mon Jun  8 20:28:45 2026     ===========
        ===========         Author: Khashayar Alipour            ===========
        ===========                 Pandas                       ===========
        ====================================================================
"""

# pandas --> 1 step before machine learning
# با استفاده ازین کتابخوانه هر نوع دیتایی رو میتونیم Clean کنیم یا filter کنیم

# pip install pandas
# import pandas as pd


# در numpy دیتا بوسیله ابزاری که numpy بهمون میده یعنی ndarray ساخته میشه
# ولی برای تحلیل آماری در دیتای واقعی باید از pandas استفاده کنیم
# برای اینکار pandas دوتا ابزار بهمون میده:
    # pandas.Series() -  pandas.DataFrame()

# توابع pandas همشون Case_sensetive هستن و حرف اولشون بزرگه




'''  ==========================
     ====    ___________   ====
     ====   |   Serie  |   ====
     ====   -----------    ====
     ====                  ====
     ==========================
'''

# مثل یک 1d array هست
# مثل یک ستون توی یک جدول هست
# برای دیتاهای 1D کاربرد داره

'''
case      Temperature   Pressure     power
1              20         1           30
2              30         2           40
3              40         3           50     
'''


#=========================================
# تفاوتهای لیست عادی، لیست numpy و لیست pandas

import pandas as pd
import numpy as np


l1= list([10,20,30])            #[10, 20, 30]
n1 = np.array([10,20,30])       #[10 20 30]
s1 = pd.Series([30,40,50])
#0    30
#1    40
#2    50
#dtype: int64

type(l1) #<class 'list'>
type(n1) #<class 'numpy.ndarray'>
type(s1) #<class 'pandas.core.series.Series'>

n1.ndim #1
l1.ndim #AttributeError: 'list' object has no attribute 'ndim'

'''
1D
List  --> simple list is useful for easy tasks, like a simple loop
np Array -->  Fast (speed) tasks ,useful for calculation 
pd series --> working with real data
'''


# =========================================
# میشه انواع عملیات روی تک تک المنتهای Series انجام داد. مثلا جمع، تفریق، تقسیم، مقایسه و ...

s1 = pd.Series([30,40,50])
'''
0    30
1    40
2    50
dtype: int64
'''


s1 + [10,20,30]    # خروجی میده و میشه توی متغیر ریخت و ذخیره کرد
'''
0    40 (30+10)
1    60 (40+20)
2    80 (50+30)
dtype: int64
'''


s1 + 100    # همه المنت‌ها دونه دونه با 100 جمع میشن
'''
0    130
1    140
2    150
dtype: int64
'''


s1 <35
'''
0     True
1    False
2    False
dtype: bool
'''


# ==================[ index ]=======================
# حتی میشه یک numpy array رو به یک Series تبدیل کرد

import numpy as np
a = np.array([30,40,50])


import pandas as pd
s2= pd.Series(a)

print(a) #[30 40 50]
print(s2)
'''
0    30
1    40
2    50
dtype: int64
'''



# میشه یک dictionary رو به series تبدیل کرد:

    d1= {'bob' : 50 , 'ali' : 80 , 'vahid':90 , 'reza':100}     # <class 'dict'>
    
    s3 = pd.Series(d1)
    '''
    bob       50
    ali       80
    vahid     90
    reza     100
    dtype: int64
    '''



# میشه برای series خودمون index مشخص کنیم:

    s4 = pd.Series([50,80,90,100])
    '''
    0     50
    1     80
    2     90
    3    100
    dtype: int64
    '''
    
    s5 = pd.Series([50,80,90,100],index=['bob','ali','vahid','reza'])
    '''
    bob       50
    ali       80
    vahid     90
    reza     100
    dtype: int64
    '''


# ==================[ element access ]=======================
# برای دسترسی به یک المنت در series میشه از روشهای زیر استفاده کرد:
    
s5 = pd.Series([50,80,90,100],index=['bob','ali','vahid','reza'])
'''
bob       50
ali       80
vahid     90
reza     100
dtype: int64
'''

s5[0]       # 50 ->  دسترسی بوسیله عدد اندیس
s5['bob']   # 50 -> دسترسی بوسیله کلید

# دسترسی بوسیله توابع مخصوص series: 
    # .loc[] -> location
    # .iloc[]  -> index location
    s5.loc['bob'] #50
    s5.iloc[0] #50




# ==================[ keywords ]=======================

s5.keys() #Index(['bob', 'ali', 'vahid', 'reza'], dtype='object')



# ==================[ series functions ]=======================

s2.abs() #ghadre motlagh
s2.add()  #add mikoni y adad
s2.div() #divide
s2.divide() #divide
s2.divmod() #divide integer (gerd mikone)
s2.multiply() #zarb
s2.mul() #zarb
s2.pow() #b tavan

s2.pop() #remove
s2.clip()  #thresholding


s2.all() #shart --> baraye hame True bud --> True return mikone
s2.any()  #shart --> baraye hadeaghal yeki az element ha true bud -->true return mikone
s2.max() #max
s2.min() #min
s2.argmax() #indexe elementi ke max hast
s2.argmin() #indexe elementi ke min hast
s2.astype() #dtype taghir bedi , as type 
s2.view() # copy deep
s2.copy() #copy deep
s2.keys()  #kilid vazhe haro 
s2.items() #index , value --> for i,j in ...

s2.apply() 
s2.filter()
s2.isin()
s2.isna()
s2.isnull()
s2.fillna()
s2.drop()
s2.drop_duplicates()
s2.dropna()
s2.ffill()
s2.bfill()






'''  ==============================
     ====    _______________   ====
     ====   |   DataFrame  |   ====
     ====   ---------------    ====
     ====                      ====
     ==============================
'''

# همانطور که برای 1D از Series استفاده میشه
# برای 2D از DataFrame استفاده میشه


n2 = np.array([[10,20,30],[40,50,60]])
type(n2)    # <class 'numpy.ndarray'>
'''
[[10 20 30]
 [40 50 60]]
'''

df1 = pd.DataFrame([[10,20,30],[40,50,60]])
type(df1)    # 'pandas.core.frame.DataFrame'>
'''
    0   1   2
0  10  20  30
1  40  50  60
'''



# ==================[ label gozari ]=======================
# استاندارد ترین حالت اینه که index عددی باشه و column رو label گذاری کنیم

df2 = pd.DataFrame([[10,20,30],[40,50,60]],columns=['dama','feshar','estehkam'])
'''
   dama  feshar  estehkam
0    10      20        30
1    40      50        60
'''

df3 = pd.DataFrame([[10,20,30],[40,50,60]],index=['case1','case2'])
'''
        0   1   2
case1  10  20  30
case2  40  50  60
'''


df4 = pd.DataFrame([[10,20,30],[40,50,60]],index=['case1','case2'],columns=['dama','feshar','estehkam'])
'''
       dama  feshar  estehkam
case1    10      20        30
case2    40      50        60
'''



# =======================[ access ]============================

# برعکس numpy که اولویت همیشه با ردیف بود، در pandas همیشه column در اولویت هست

'''
   dama  feshar  esthekam
0    25       1       500
1    28       2       600
2    30       3       700
'''

df.columns     # Index(['dama', 'feshar', 'esthekam'], dtype='object')


a = df['dama']
'''
0    25
1    28
2    30
Name: dama, dtype: int64
'''

type(a)   # <class 'pandas.core.series.Series'>
# در DataFrame هر ستون در واقع یک Series هست
# پس در معماری pandas واحد اصلی Series هست
# از کنار هم قرار گرفتن چند Series در ستونها، یک DataFrame تشکیل میشه



# ==== دسترسی به ردیف ====
# برای دسترسی به ردیف باید از loc و iloc استفاده بشه

df.loc[0]    # ردیف 0
'''
dama         25
feshar        1
esthekam    500
Name: 0, dtype: int64
'''

df.iloc[0]    # ردیف با اندیس 0
'''
dama         25
feshar        1
esthekam    500
Name: 0, dtype: int64
'''


# ==== دسترسی به یک element خاص ====
# کدوم ستون - کدوم ردیف
df['estehkam'].loc[0]   #500
df['estehkam'].iloc[0]  #500

# تغییر دادن مقدار یک المنت
df['dama'].loc[1]  = 28.5








'''     _________________________
       |    Pandas Functions    |
       -------------------------
'''


# ===============================[ important ]=================================

# در پایتون توابع Str روی داده‌ی اصلی تغییر اعمال نمیکرد، فقط یک خروجی میداد
# ولی در متدهای لیست برعکس بود و روی هر متغیری متدهای لیست اعمال میشد، خود متغیر هم تغییر میکرد

# تمام فانکشن‌های کتابخوانه pandas مثل متدهای Str در پایتون هستن و فقط خروجی میدن
# پس روی هر دیتایی متدهای pandas رو بزنی، دیتای اصلی دست نخورده میمونه

# حالا چیکار کنیم که در مواقع مورد نیاز بتونیم دیتای اصلی رو تغییر بدیم؟
# همه متدهای pandas یک آپشن inplace دارن که در حالت پیش‌فرض False هست
# اگر بخوایم که متد مورد استفاده روی دیتای اصلی تغییر اعمال کنه inplace=True میذاریم

# وقتی تغییر روی دیتای اصلی اعمال بشه، اصلا نیازی نیست که چیزی در یک متغیر جدید ذخیره کنیم
# ولی اگه فقط خروجی بده، برای مشاهده نتیجه باید توی یک متغیر جدید ذخیره کنیم

data.drop(columns="jadid", inplace=True)
print(data)
# =============================================================================






df = pd.DataFrame([[25,1,500],[28,2,600],[30,3,700],
                   [35,4,800],[40,5,900],[45,6,1000],
                   [50,7,1100],[55,8,1200],[60,9,1300]],columns=['dama','feshar','estehkam'])
'''
   dama  feshar  estehkam
0    25       1       500
1    28       2       600
2    30       3       700
3    35       4       800
4    40       5       900
5    45       6      1000
6    50       7      1100
7    55       8      1200
8    60       9      1300
'''


# =======================[ comparison ]============================

# >= > < <= == != and ...
# موارد بالارو برای همه المنت‌ها چک میکنه و True و False میده

df['estehkam'] >600
'''
0    False
1    False
2     True
3     True
4     True
5     True
6     True
7     True
8     True
Name: estehkam, dtype: bool
'''



# =======================[ filtering ]============================

# در filtering میایم یا بصورت دستی یا با استفاده از حالات مقایسه‌ای یک Filtering list درست میکنیم
# سپس این filtering list رو میدیم به df
# میاد میبینه توی filtering list ما کجاهاش True هست، بر اساس همون df رو فیلتر میکنه
# در نهایت هرچی True هست رو برمیگردونه


filtering_list=[True,False,True,False,False,False,False,False,False]
# طبق filtering list فقط اندیس 0 و 2 اینجا True هستن، پس همین ردیف هارو برمیگردونه

df[filtering_list]
'''
   dama  feshar  estehkam
0    25       1       500
2    30       3       700
'''


#df['estehkam']>600 --> این حالت مقایسه‌ای نتیجش یک فیلترینگ لیست میشه
#df[filtering ] --> filter

df[df['estehkam']>600]
'''
   dama  feshar  estehkam
2    30       3       700
3    35       4       800
4    40       5       900
5    45       6      1000
6    50       7      1100
7    55       8      1200
8    60       9      1300
'''


df_high_strength = df[df['estehkam']>1100]

'''
   dama  feshar  estehkam
7    55       8      1200
8    60       9      1300
'''


df_low_temperature = df[df['dama']<30]
'''
   dama  feshar  estehkam
0    25       1       500
1    28       2       600
'''


specific_df = df[df['dama']==25]    # اگه دوجا داشتیم که دما 25 بود جفتش رو میداد
'''
   dama  feshar  estehkam
0    25       1       500
'''




new_df = pd.DataFrame([[25,1,500],[25,2,600],[30,3,700],
                   [35,4,800],[40,5,900],[45,6,1000],
                   [50,7,1100],[55,8,1200],[60,9,1300]],columns=['dama','feshar','estehkam'])
'''
   dama  feshar  estehkam
0    25       1       500
1    25       2       600
2    30       3       700
3    35       4       800
4    40       5       900
5    45       6      1000
6    50       7      1100
7    55       8      1200
8    60       9      1300
'''

pecific_new_df = new_df[new_df['dama']==25]    # دوتا دما برابر 25 داریم
'''
   dama  feshar  estehkam
0    25       1       500
1    25       2       600
'''


very_specific_new_df = new_df[ (new_df['dama']==25) & (new_df['estehkam']>550) ]
'''
   dama  feshar  estehkam
1    25       2       600
'''


new_df[new_df['dama'].isin([25,30])]     # دما تو بازه 25 تا 30
'''
   dama  feshar  estehkam
0    25       1       500
1    25       2       600
2    30       3       700
'''



# =======================[ adding new column ]============================

print(new_df)
'''
   dama  feshar  estehkam
0    25       1       500
1    25       2       600
2    30       3       700
3    35       4       800
4    40       5       900
5    45       6      1000
6    50       7      1100
7    55       8      1200
8    60       9      1300
'''


# افزودن ستون جدید به نام "jadid" و مقدارش هم 0 هست

new_df['jadid'] = 0 
print(new_df)
'''
   dama  feshar  estehkam  jadid
0    25       1       500      0
1    25       2       600      0
2    30       3       700      0
3    35       4       800      0
4    40       5       900      0
5    45       6      1000      0
6    50       7      1100      0
7    55       8      1200      0
8    60       9      1300      0
'''


# راه مرسوم برای اضافه کردن ستون اینجوریه
# دیتاهای موجود در یکی از ستونها رو با یک عدد ضرب یا جمع یا ... میکنیم
# و دیتاهای ستون جدید بدست میاد

new_df['jadid'] = new_df['dama'] +100
print(new_df)
'''
   dama  feshar  estehkam  jadid
0    25       1       500    125
1    25       2       600    125
2    30       3       700    130
3    35       4       800    135
4    40       5       900    140
5    45       6      1000    145
6    50       7      1100    150
7    55       8      1200    155
8    60       9      1300    160
'''


# روش دیگه با استفاده از متود apply هست
# روی ستون "dama" میره و فقط یک چیزی رو پس میده و چیزی apply نمیکنه
# میگه برو روی ستون 'dama' و به هر x رسیدی اگر بالای 30 بود اسمش بزار high temp وگرنه بزار low temp

df['dama'].apply(lambda x: 'high temp' if x>30 else 'low temp' )
print(new_df)

'''
   dama  feshar  estehkam  jadid   category
0    25       1       500    125   low temp
1    25       2       600    125   low temp
2    30       3       700    130   low temp
3    35       4       800    135  high temp
4    40       5       900    140  high temp
5    45       6      1000    145  high temp
6    50       7      1100    150  high temp
7    55       8      1200    155  high temp
8    60       9      1300    160  high temp
'''



# روش دیگه استفاده از loc هست

new_df.loc[new_df['dama']>30,'category 2'] = 'high temp'
new_df.loc[new_df['dama']<=30,'category 2'] = 'low temp'
print(new_df)

'''
   dama  feshar  estehkam  jadid   category category 2
0    25       1       500    125   low temp   low temp
1    25       2       600    125   low temp   low temp
2    30       3       700    130   low temp   low temp
3    35       4       800    135  high temp  high temp
4    40       5       900    140  high temp  high temp
5    45       6      1000    145  high temp  high temp
6    50       7      1100    150  high temp  high temp
7    55       8      1200    155  high temp  high temp
8    60       9      1300    160  high temp  high temp
'''




# =======================[ delete a column ]============================

# میشه از متدهای .pop یا del هم استفاده کرد. ولی روش اصلی اینه:

    
# استفاده از متد drop

new_df.drop(columns='jadid')
'''
   dama  feshar  estehkam   category category 2
0    25       1       500   low temp   low temp
1    25       2       600   low temp   low temp
2    30       3       700   low temp   low temp
3    35       4       800  high temp  high temp
4    40       5       900  high temp  high temp
5    45       6      1000  high temp  high temp
6    50       7      1100  high temp  high temp
7    55       8      1200  high temp  high temp
8    60       9      1300  high temp  high temp
'''


new_df.drop(columns='jadid',inplace=True)
print(new_df)
'''
   dama  feshar  estehkam   category category 2
0    25       1       500   low temp   low temp
1    25       2       600   low temp   low temp
2    30       3       700   low temp   low temp
3    35       4       800  high temp  high temp
4    40       5       900  high temp  high temp
5    45       6      1000  high temp  high temp
6    50       7      1100  high temp  high temp
7    55       8      1200  high temp  high temp
8    60       9      1300  high temp  high temp
'''




# ===========================[ delete a row ]==================================

new_df.drop(index=3,inplace=True)    # ردیف 3 رو حذف میکنه
print(new_df)

'''
   dama  feshar  estehkam   category
0    25       1       500   low temp
1    25       2       600   low temp
2    30       3       700   low temp
4    40       5       900  high temp
5    45       6      1000  high temp
6    50       7      1100  high temp
7    55       8      1200  high temp
'''


# بهتره بعد از استفاده از drop برای حذف یک ردیف، از تابع reset_index استفاده بشه تا عدد ایندکس هارو درست کنه
# این متد علاوه بر اینکه عدد ایندکس هارو درست میکنه، میاد یک کپی از قبلیه هم بهمون میده که نشون بده چی بود چی شد
# حالا اگه نخوایم این ستون copy رو نشون بده چی؟
# این متد یک آرگومان بنام drop داره که در حالت پیش‌فرض False هست و باید اون رو True کنیم

new_df.reset_index(inplace=True)
print(new_df)
'''
   index  dama  feshar  estehkam   category
0      0    25       1       500   low temp
1      1    25       2       600   low temp
2      2    30       3       700   low temp
3      4    40       5       900  high temp
4      5    45       6      1000  high temp
5      6    50       7      1100  high temp
6      7    55       8      1200  high temp
'''


new_df.reset_index(drop=True,inplace=True)
print(new_df)
'''
  dama  feshar  estehkam   category
0    25       1       500   low temp
1    25       2       600   low temp
2    30       3       700   low temp
3    40       5       900  high temp
4    45       6      1000  high temp
5    50       7      1100  high temp
6    55       8      1200  high temp
'''



# ===========================[ sort a column ]==================================

# sort_values()
# این تابع میاد برای یک ستون از کم به زیاد مقادیر رو sort میکنه

new_df = pd.DataFrame([[25,1,500],[25,2,200],[30,3,100],
                   [35,4,800],[40,5,900],[45,6,50],
                   [50,7,1100],[55,8,60],[60,9,1300]],columns=['dama','feshar','estehkam'])
print(new_df)
'''
   dama  feshar  estehkam
0    25       1       500
1    25       2       200
2    30       3       100
3    35       4       800
4    40       5       900
5    45       6        50
6    50       7      1100
7    55       8        60
8    60       9      1300
'''


new_df.sort_values(by='estehkam',inplace=True)
print(new_df)
'''
   dama  feshar  estehkam
5    45       6        50
7    55       8        60
2    30       3       100
1    25       2       200
0    25       1       500
3    35       4       800
4    40       5       900
6    50       7      1100
8    60       9      1300
'''


# تابع sort_value بصورت پیشفرض از کوچک به بزرگ مرتب میکنه
# اگه برعکسش رو بخوایم آپشن Ascending=False قرار میدیم و این میشه:
    
new_df.sort_values(by='estehkam',ascending=False,inplace=True)
print(new_df)
'''
   dama  feshar  estehkam
8    60       9      1300
6    50       7      1100
4    40       5       900
3    35       4       800
0    25       1       500
1    25       2       200
2    30       3       100
7    55       8        60
5    45       6        50
'''


# حالا دوباره در انتهای هرکاری که انجام دادیم میتونیم Reset کنیم که ایندکس ها درست بشه:

new_df.reset_index(drop=True,inplace=True)
print(new_df)

'''
   dama  feshar  estehkam
0    60       9      1300
1    50       7      1100
2    40       5       900
3    35       4       800
4    25       1       500
5    25       2       200
6    30       3       100
7    55       8        60
8    45       6        50
'''


# با استفاده از متد Rank() میشه بر اساس یک ستون که ما مشخص میکنیم، rank بندی کنیم:

new_df['rank'] = new_df['estehkam'].rank()
print(new_df)

'''
   dama  feshar  estehkam  rank
0    60       9      1300   9.0
1    50       7      1100   8.0
2    40       5       900   7.0
3    35       4       800   6.0
4    25       1       500   5.0
5    25       2       200   4.0
6    30       3       100   3.0
7    55       8        60   2.0
8    45       6        50   1.0
'''


new_df['rank'] = new_df['estehkam'].rank(ascending=False)
new_df

'''
   dama  feshar  estehkam  rank
0    60       9      1300   1.0
1    50       7      1100   2.0
2    40       5       900   3.0
3    35       4       800   4.0
4    25       1       500   5.0
5    25       2       200   6.0
6    30       3       100   7.0
7    55       8        60   8.0
8    45       6        50   9.0
'''



# ===========================[ drawing a plot ]==================================

# میشه برای دیتایی که داریم نمودار بکشیم
# برای اینکار هم میشه از matplotlib استفاده کنیم و هم از توابع مخصوص pandas


import matplotlib.pyplot as plt
x=new_df['dama']
y= new_df['estehkam']
plt.scatter(x,y)
plt.title('Strenght vs temeprature ')
plt.ylabel('Strnegth (MG)')
plt.xlabel('Temp C')
plt.grid()
plt.show()


# ---- با استفاده از توابع خود pandas ----

new_df.plot(kind='line',x='dama',y=['estehkam'])    # line -> plt.plot()
plt.show()



new_df.plot(kind='scatter',x='dama',y=['estehkam'])
plt.grid()
plt.show()





# ===========================[ mathematical ]==================================

new_df.mean()    # میانگین کلی برای هر ستون
'''
dama         40.555556
feshar        5.000000
estehkam    556.666667
rank          5.000000
dtype: float64
'''

# میانگین یک ستون
new_df['dama'].mean() # 40.55555555555556
new_df['dama'].median() # 40.0


# تمام متدهای زیر رو هم میشه روی کل ستون‌ها یا هر ستون جدا اعمال کرد

s2.abs() #ghadre motlagh
s2.add()  #add mikoni y adad
s2.div() #divide
s2.divide() #divide
s2.divmod() #divide integer (gerd mikone)
s2.multiply() #zarb
s2.mul() #zarb
s2.pow() #b tavan

s2.pop() #remove
s2.clip()  #thresholding

s2.all() #shart --> baraye hame True bud --> True return mikone
s2.any()  #shart --> baraye hadeaghal yeki az element ha true bud -->true return mikone
s2.max() #max
s2.min() #min





# ===========================[ import data ]==================================

# در دنیای واقعی معمولا دیتا بصورت فایل csv یا excel هست و باید اینجا import بشه
# با استفاده از تابع read میشه هرررر نوع دیتاتایپی رو خوند

# داده های جدولی معمولا:
    # .docs .doc .docx --> word
    # .csv      ----- > CSV
    # .xls .xlsx  -----> Excell


import pandas as pd

df = pd.DataFrame()

# آدرس فایل رو با کلیک راست روی فایل و بعد از طریق properties میشه بدست آورد
# اینجا با read دیتای موجود در اون فایل رو میخونیم و بعد میریزیم توی یک dataFrame که نتیجش میشه یک dataFrame
df = pd.read_excel('C://user//apm//desktop/...../esme_data.xls')
df = pd.read_csv('......./ name dade .csv')



# در کامپیوتر وقتی اسپایدر بسته بشه یا سیستم خاموش بشه دیتا از RAM پاک میشه
# چون دیتای موجود در RAM دیتای volatile هست
# برای اینکه دیتایی که بدست آوردیم پاک نشه میشه با روش زیر در آدرسی که میخوایم با فرمتی که میخوایم ذخیرش میکنیم:
    
df.to_csv('addresss')
df.to_excel('addresss')




