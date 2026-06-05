
    # Name: Khashayar Alipour
    # Year: 2025
    # License: MIT
    # Subject: Numpy library basics





# راه های import کردن از یه فایل دیگه:

#1------ 
# کل فایل رو میاری اینجا
import calculator

# واسه دسترسی به توابعش:
calculator.jam(10,20) #Out[6]: 30


#2------
from calculator import jam
jam(10,20)


#3------
from calcualtor import jam_zarb_tafrigh
jam_zarb_tafrigh(10,20)


from calculator import jam_zarb_tafrigh as jzt
jzt(10,20,2,4) #Out[9]: 56



#-----------------------------------------------------------------
#PEDAR-----
        #myfolder
             #pesar
             #dokhtar
        #BROTHER
        
        #brother.py


#agar toye file myfolder chizi hast .py 
#from . import oon chizo
#from .pesar import oon chizo
#from ..brother import ....


#. hamoon khdoesh
#.esm -->foldere tooye in folder
#.. biay brioon


#from felan import * -->hamechizo 


#-----------------------------------------------------------------



''' Library '''    # کتابخوانه


# download and install   =>   PIP

#pip install numpy      نصب نسخه استیبل ورژن که فیچرهای اصلی رو داره
#pip install numpy==1.2.1      نصب یک نسخه خاص
#pip install numpy --upgrade    نصب اخرین نسخه


#requirements folder  => for ex. after installing django,  skilearn= دیگه کار نمیکنه
# how to solve this problem??   make a virtual enviroment
#python -m venv FANAVARI2021     ساخت محیط مجازی
#mac => source FANAVARI2021/bin/activate       اجرا کردن کد در محیط مجازی (فعال کردن محیط)
#windows =>  . FANAVARI2021\Scripts\activate   یا   source FANAVARI2021\Scripts\activate
#(FANAVARI2026) CPC@khashayar MINGW64 ~/desktop    بعد از ورود به محیط مجازیت گیت اینجوری میشه
#deactivate    خروج از محیط مجازی
#pip list    وقتی توی یک محیط مجازی هستیم میشه با این دستور کتابخونه های نصب شده داخلش رو ببینیم
# pip freeze > requirements.txt    و با این دستور، لیست کتابخونه‌ها رو توی یه فایل ذخیره کنی
# pip install -r requirements.txt   بعداً هر کی پروژه تو رو بگیره، با یه دستور می‌تونه همه کتابخونه‌های لازم رو نصب کنه



#مشکلات لیست در پایتون:   
#1-   1D hast va nmishe bahash 3D kar kard
#2-   Pythonic (rooye python neveshte shode) => [name, size, type, value]= low speed
#____________  حل مشکل بالا با کتابخوانه numpy ___________
# معرفی کردن numpy array بجای لیست که ویژگی های زیر رو داره:   
   # 1- میشه ازش حتی 3 بعدی استفاده کرد                                         
    # 2- چون core روی زبان سی نوشته شده => 60 برابر سرعت بیشتر در محاسبه و ... 


#--- ویژگی های توابع در numpy:
    #1- array => very fast (C based)
    #2- matrix => multi dimentional
    #3- wide range of functions for generating all types of numbers =>   np.linespace - np.arrange
    #4- easily shaped functions with fixed values =>  np.zeros((shape)) - np.ones
    #5- making random numbers
    #6- nparrays are objects, they belong to ndarray class

# با ویژگی های بالا و متدهای بسیار زیادی که این کتابخونه داره، تبدیل شده به requirement برای خیلی از کتابخونه ها
# از جمله این کتابخونه ها مواردی هستند که برای محاسبات از numpy استفاده میکنن: (sklearn, pandas, matplotlib,....)
# از کتابخانه numpy دو کتابخانه scipy , sympy اومدن و تخصصی روی معادلات دیفرانسیل هم کار کردند (تخصصی تر)



#____________ استفاده از numpy در محیط مجازی _______
# بعد از ساخت محیط مجازیمون میزنیم PIP install numpy و نصبش میکنیم
# حالا باید توی این محیط همیشه باشیم تا بتونیم از numpy استفاده کنیم


import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
print(np.__version__)  #2.1.3


a = np.array([10,20,30,40])    #ساخت آرایه در نامپای
b= [10,20,30,40]     #ساخت لیست به روش معمولی پایتون

type(a) #Out[14]: numpy.ndarray n-dimentional-array --> آرایه های چند بعدی
type(b) #Out[15]: list


'''
#___________________________________________________________________
#                                                                   |
#                  Array attributes in numpy                        |
#___________________________________________________________________|
'''
import numpy as np

a = np.array([10,20,30,40,50])

print(type(a))     # <class 'numpy.ndarray'>
print(a)           # [10 20 30 40 50]
a.ndim             # 1  =>  (number of dimention) لیست یک بعد داره
a.size             # 5
a.shape            # (5,)
a[0]               # 10     گرفتن با عدد ایندکس
b = a[0]           # b=10   =>  ریختن یک المنت داخل یک متغیر دیگه      
a[0:2]             # array([10, 20])    خروجی یک آرایه برمیگردونه
a[0]=100           # a=[100  20  30  40  50]       mutation


'''
#____________________
#|                   |
#|   Dimentions      |
#|___________________|
'''

# 1)  0 Dimention:    صفر بعدی
a= np.array(0)
a.ndim
#0 bod

# 2)  1D:   مدل یک بعدی یک لیست از اعداد داره
a = np.array([10,20,30,40,50,60])

# 3)  2D:   ردیف و ستون داره

'''
     col1 col2 col3 col4
row1 10   20   30   40
row2 50   60   70   80    '''

# [ [row1], [row2] ]

#1d -----
a=np.array([10,20,30])


#2d -----
b=np.array([ [10,20,30,40] , [50,60,70,80]  ])
b.ndim               #2  دو بعدی
b.size               #8
b.shape              #(2, 4)   (row, column)
print(b)
'''
[[10 20 30 40]
 [50 60 70 80]]   '''
b[0]                 # array([10, 20, 30, 40])   دسترسی به ردیف صفر
b[1,2]               # 70   دسترسی به ردیف 1 ستون 2
                    # در نامپای اندیس گذاری ردیف و ستون از 0 شروع میشه                     
b[1,2]=1000          # تغییر دادن یک المنت خاص در ردیف 1 و ستون 2
'''
[[   10    20    30 10000]
 [   50    60    70    80]]   '''
b[:,1]               # array([20, 60])    دسترسی به تمام ردیف ها، ستون 1


# 3D ------
'''
10 20 30
40 50 60

1  2  3
4  5  6

9 99 999
8 88 888
'''

c = np.array([ [ [10,20,30],[40,50,60]   ] , 
              [  [1,2,3] ,[4,5,6] ] ,
              [ [9,99,999],[8,88,888]  ]  ])


c.ndim                # 3
c.size                # 18
c.shape               #(3, 2, 3)   این ینی 3 تا جدول داره، هر جدول 2 ردیف و هر ردیف 3 تا ستون داره

# دسترسی به یک المنت خاص، مثلا عدد 3
# کدوم جدول؟ = 1
# کدوم ردیف؟ = 0
# کدوم ستون؟ = 2

c[1,0,2]    # 3


'''
#____________________
#|                   |
#|   Assignment      |
#|___________________|
'''

zarf = np.array([10,20,30,40],dtype='float32')         #[10. 20. 30. 40.]

# np.arange(#start , stop , step)
a= np.arange(10)     #[0 1 2 3 4 5 6 7 8 9]

b= np.linspace(0,1,10)     # اعداد بین 0 تا 1 رو به 10 قسمت مساوی تقسیم کن
'''
[0.         0.11111111 0.22222222 0.33333333 0.44444444 0.55555556
 0.66666667 0.77777778 0.88888889 1.        ]       '''


c = np.logspace(0,10,10 )     # از 0 تا 10 به توان 10 رو بساز
'''
[1.00000000e+00 1.29154967e+01 1.66810054e+02 2.15443469e+03
 2.78255940e+04 3.59381366e+05 4.64158883e+06 5.99484250e+07
 7.74263683e+08 1.00000000e+10]      '''


'''
#____________________
#|                   |
#|      Matrix       |
#|___________________|
'''

# در توابع بالا باید value رو تعیین میکردیم. بعضی متدها value مشخص دارن فقط باید shape آنها تعیین بشه:
# باید shape داخل پرانتز تعیین بشه:
#np.empty(2,3) غلطه
#np.empty((shape))  درست

np.zeros(10)     # بیا 10 تا صفر بساز
'''array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])    '''

np.zeros((2,5))   # بیا 2 ردیف و 5 ستون صفر بساز
'''array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])   '''


np.ones((3,5))    # بیا 3 ردیف و 5 ستون 1 بساز
'''array([[1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.]])     '''


np.empty(10)     # بیا 10 تا خالی بساز
'''array([1.00000000e+00, 1.29154967e+01, 1.66810054e+02, 2.15443469e+03,
       2.78255940e+04, 3.59381366e+05, 4.64158883e+06, 5.99484250e+07,
       7.74263683e+08, 1.00000000e+10])     '''


np.empty((2,3))   # بیا 2 ردیف و 3 ستون خالی بساز
'''array([[0.00e+000, 4.94e-324, 9.88e-324],
       [4.84e-322, 4.89e-322, 4.94e-322]])     '''


# np.full((shape) , full by which value?)
np.full((2,3),3.14)    # بیا 2 ردیف و 3 ستون رو با مقداری که من میگم فول کن
'''array([[3.14, 3.14, 3.14],
       [3.14, 3.14, 3.14]])  '''


    
#---Identity matrix---
#i x i --> وتر برابر 1 و بقیه المنت ها صفر هستند

np.eye(3)    # ماتریس 3 در 3
'''array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])    '''


#4 x 4 --> ماتریس 4 در 4
np.eye(4)
'''array([[1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.]])    '''


    
#---diagonal Matrix---
# وتر به ترتیب اعداد داخل لیست ماست و بقیه المنت ها صفر هستند

np.diag([1,2,3])
'''array([[1, 0, 0],
          [0, 2, 0],
          [0, 0, 3]])   '''


np.diag([1,2,3,4])
'''array([[1, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 3, 0],
          [0, 0, 0, 4]])  '''


#offset
#مقدار پیش فرض برابر 0 و به مقدار عددی که به K میدیم به همون اندازه وتر ماتریکس رو بالا و پایین میشه

np.diag([1,2,3,4],k=0) 
'''
array([[1, 0, 0, 0],
       [0, 2, 0, 0],
       [0, 0, 3, 0],
       [0, 0, 0, 4]])  '''


np.diag([1,2,3,4],k=1) 
'''
array([[0, 1, 0, 0, 0],
       [0, 0, 2, 0, 0],
       [0, 0, 0, 3, 0],
       [0, 0, 0, 0, 4],
       [0, 0, 0, 0, 0]])   '''


np.diag([1,2,3,4],k=2)
'''
array([[0, 0, 1, 0, 0, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 0, 0, 3, 0],
       [0, 0, 0, 0, 0, 4],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]])   '''


np.diag([1,2,3,4],k=-1)
'''
array([[0, 0, 0, 0, 0],
       [1, 0, 0, 0, 0],
       [0, 2, 0, 0, 0],
       [0, 0, 3, 0, 0],
       [0, 0, 0, 4, 0]])   '''



data = np.genfromtxt('felan.dat') 

a_array= np.diag([1,2,3,4],k=-1)
#savetxt(name , numpy array)
np.savetxt('random_matrix.csv',a_array)


'''
#____________________
#|                   |
#|      Random       |
#|___________________|
'''

#a default python library (random):
    
import random

random.random() # 0.3978211326844082   #0.7111013979063225

random.randint(10, 20) #18  # 12


# numpy random:
# یک آرایه میده که ردیف و ستونهاش اعداد تصادفی float بین 0 و 1 هستن
# میشه به توابعش shape داد

#np.random.random( ,(shape)) => 0-1
np.random.random() #0.016036791252807436

np.random.random((2,3))

'''
array([[0.01302821, 0.32131125, 0.11003532],
       [0.08975113, 0.08635853, 0.72005935]])   '''


#--- انتخاب عدد تصادفی در numpy بر اساس انواع توزیع آماری
# بخوایم عدد تصادفی برداریم میشه انتخاب کنیم که uniformly باشه یا gaussian way (normal) باشه.

# 1- توزیع همگن یا uniform distribution:
    # شانس انتخاب هر عدد رندوم مثلا بین 0 تا 10 یکسان باشه


# 2- توزیع میانگین یا normal distribution:
# شانس انتخاب تمرکز داره روی یک عدد (حول محور یک عدد خاص)
# هرچی ازین عدد خاص دورتر میشیم شانس انتخاب کمتر میشه
# واریانس (variance) یعنی تا چه حد اعداد تصادفی حول محور عدد میانگین خاص باشه


#--- توابع زیر اعداد تصادفی float تولید میکنن

#np.random.uniform(a, b, (shape))  => float
np.random.uniform(0,10)
#7.121615786798342
#2.849058582400794

np.random.uniform(0,10,(2,3))
'''
array([[5.71142564, 6.91424201, 0.27549855],
       [3.61827544, 5.71250762, 6.08274449]])    '''


# انتخاب اعداد تصادفی حول محور 20 و فقط 5 عدد اینور یا اونور باشه:
np.random.normal(20,5)
#17.03996522106831
#20.60846555217081
#28.32151614349159

#np.random.normal( ,variance ,(shape)) => float    حول محور میانگین، با فاصله واریانس
np.random.normal(20,5,(2,3))
'''
array([[18.18839678, 17.19648441, 16.78172775],
       [19.48670663, 22.56325968, 23.14233308]])   '''



#--- تابع زیر اعداد تصادفی integer تولید میکنن

#np.random.randint(a, b, (shape)) => 1-10 integer
np.random.randint(0,10)   # 9

np.random.randint(12,18,(2,3))
'''
array([[12, 12, 16],
       [14, 12, 12]])   '''




#_______________________________
#|                              |
#|      advanced on dtype       |
#|______________________________|

# dtype = data type
# میشه به نامپای بگی که عناصر داخل آرایه رو با چه نوعی داخل حافظه ذخیره کنه
# مثلا dtype="float32 یعنی همه اعداد رو به صورت عدد اعشاری 32 بیتی ذخیره کنی
# a=np.array([10,20,30,40], dtype="float32")
# پس مثلا آرایه بالا اینشکلی میشه  [10.0, 20.0, 30.0, 40.0]
# print(a.dtype) => float32

# int32 => عدد صحیح
# float32 => عدد اعشاری
# bool => true/false
# complex64 => اعداد مختلط

# ذخیره کردن دیتا با نوع دلخواه میتونه توی بعضی چیزا تاثیر داشته باشه
# مثلا ازونجایی که حجم هر دیتای float32 برابر 4byte و هر دیتای float64 برابر 8byte هست
# در مصرف حافظه، سرعت پردازش float32 بهتره
# حالا float64 از 32 دقت بیشتری داره



'''
PYTHON TYPE --> INT, FLOAT, COMPLEX, BOOL

DTYPE------ only for numpy --> C


bool_ Boolean stored as a byte
int_   default integer type ( same as C long: normally int64 or int32)
intc    identical to C int (normally int32 or int64)
intp    integer used for indexing ( C ssize_t , int32 or int64)
int8    byte(-128 , 127)
int16   integer ( -32768 to 32767)
int 32
int64

unit8    unsigned integer (0 to 255)
unit16 
unit32
unit64

float_   shorthand for float64
float16
float32 
float 64

complex_ shorthand for complex128
complex64
complex128
'''




'''
#__________________________
#|                         |
#|    Magic Functions      |
#|_________________________|
'''

#===================
#    reshaping     |
#===================

#.reshape()
grid = np.arange(1, 10).reshape((3, 3))
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''

#==================
#    .astype()    |
#==================
#changing the type

M = np.array([10,20,30,40])   # M=[10 20 30 40]
# M.dtype =>  int64
 
M2 = M.astype(float)    #[10. 20. 30. 40.]

M3 = M.astype(bool)     #[ True  True  True  True]



#=================
#    flatten     |
#=================

a = np.random.uniform(1,10,(5,2))
'''
[[9.63260924 5.67090252]
 [7.73690271 3.86751571]
 [1.54304279 7.2368842 ]
 [3.31023339 9.34176159]
 [8.68903823 4.33071184]]  '''


b = a.flatten()
'''
[9.63260924 5.67090252 7.73690271 3.86751571 1.54304279 7.2368842 3.31023339 9.34176159 8.68903823 4.33071184]
'''



'''
#======================
#    copy and view    |
#======================
'''
# هر تغییری روی متغیر copy یا view بدیم، متغیر اصلی اولیه تغییر نمیکنه.
# اگر از متغیر اصلی copy بگیریم و روی کپی تغییری اعمال بشه، متغیر اصلی (arr) بدون تغییر میمونه.
# اگر از متغیر اصلی view بگیریم و روی view تغییری اعمال بشه، متغیر اصلی (arr) هم مثل view تغییر میکنه.

arr = np.arange(0,10)   #[0 1 2 3 4 5 6 7 8 9]

arr2=arr.copy()         #[0 1 2 3 4 5 6 7 8 9]
arr3=arr.view()         #[0 1 2 3 4 5 6 7 8 9]


arr2=arr2.reshape(2,5)
'''
[[0 1 2 3 4]
 [5 6 7 8 9]]
'''



'''
#==========================
#     fancy indeexing     |
#=========================
'''

# یک نوع filtering هست و میشه هرچی خواستیم از دل array بیرون بکشیم

''' row_index '''
arr=np.array([11,22,33,44,55,66,77,88,99])
row_index = [1,2,3]

#index 1 , 2, 3
arr[row_index]     #array([22, 33, 44])



''' row_mask => can be used for filtering '''
row_mask = np.array([True,True,False,False,False,False,False,False, False])
row_mask = np.array([1,1,0,0,0,0,0,0,0])

arr[row_mask]   #returns only True values
#array([11, 22])



''' other filtering features '''
x = np.array([1, 2, 3, 4, 5])
x < 3 # less than               =>  array([ True, True, False, False, False], dtype=bool)
x > 3 # greater than            =>  array([False, False, False, True, True], dtype=bool)
x <= 3 # less than or equal     =>  array([ True, True, True, False, False], dtype=bool)
x >= 3 # greater than or equal  =>  array([False, False, True, True, True], dtype=bool)
x != 3 # not equal              =>  array([ True, True, False, True, True], dtype=bool)
x == 3 # equal                  =>  array([False, False, True, False, False], dtype=bool)



x = np.arange(0,10)

row_mask = x>5   #[False False False False False False  True  True  True  True]
x[row_mask ]     # array([6, 7, 8, 9])
x[x>5]           #array([6, 7, 8, 9])
x[x==4]          #array([4])




''' where '''
# میگه فلان چیز کجاست؟ برامون با عدد ایندکس پیدا میکنه

a = np.arange(10,40)
'''
[10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33
 34 35 36 37 38 39]
'''

a11=np.where(a==12)   # array([2]) --> ایندکس 2
a[2] #12

b11=np.where(a==5)    # array([])   --> همچین چیزی نداریم

c11=np.where(a>30)    # array([21, 22, 23, 24, 25, 26, 27, 28, 29])



''' counting '''
# میایم تعداد چیزی که میخوایم پیدا میکنیم.
# میگه چنتا المنت فلان شرایط براشون محققه؟

x = np.arange(0,10)   #[0 1 2 3 4 5 6 7 8 9]

np.count_nonzero(x < 6) #6   چندتا زیر 6 داریم؟
np.sum(x < 6) #6   اونایی که زیر 6 هستن باهم جمع کن




'''
#=====================
#     conditions     |
#=====================
'''

#.any() -->  اگر حتی یکی (حداقل یکی) از المنت‌ها مطابق با شرط باشه 
#.all() -->  همه المنت‌ها باید مطابق با شرط باشن

M = np.arange(5,10)   #[5 6 7 8 9]

(M>8).any() #9 --> True
(M>8).all() #False


# اینجا any و all در شرط گذاری ها کاربرد دارن

if (M>5).any():     #اگر حداقل یکی بیشتر از 5 بود فلان کارو بکن
    pass

if (M>5).all():     # اگر همه بیشتر از 5 بودن فلان کارو بکن
    pass




'''
    ==============================
   |       Array arithemic       |
   ==============================
'''

x = np.arange(4)
print(x)              # x = [0 1 2 3]
print(x + 5)          # x + 5 = [5 6 7 8]
print(x - 5)          # x - 5 = [-5 -4 -3 -2]
print(x * 2)          # x * 2 = [0 2 4 6]
print(x / 2)          # x / 2 = [0.  0.5 1.  1.5]
print(x // 2)         # x // 2 = [0 0 1 1]  floor division
print(-x)             # -x =  [ 0 -1 -2 -3]
print(x ** 2)         # x ** 2 =  [0 1 4 9]
print(x % 2)          # x % 2 =  [0 1 0 1]
print(x%2==0).all()   # True   همه اعداد ذوج هستند


#------------
np.add() #+
np.substract() #-
np.negative() #-
np.multiply() #*
np.divide() #/
np.floor_divide() #//
np.power() #**
np.mod() #%
np.absolute()
#or
np.abs()


arr1= np.array([1,2,3,4])
arr2= np.array([5,6,7,8])
arr3= np.add(arr1,arr2)
print(arr3)   #[ 6  8 10 12]


#-------------
x = [1.3 , 2.8]

np.floor(x)    # [1., 2.]     به پایین گرد میکنه 
np.ceil(x)     # [2., 3.]     به بالا گرد میکنه


#-------------
x = np.arange(1,6)           # [1 2 3 4 5]

np.add.reduce(x)             # 15    1+2+3+4+5
np.multiply.reduce(x)        # 120   1*2*3*4*5
np.multiply.accumulate(x)    # [1, 2, 6, 24, 120]     1*2-> 2   2*3-> 6   6*4-> 24  24*5-> 120






'''
    ==============================
   |         STATISTICS          |
   ==============================
'''

L = np.random.random(100)
'''
[0.80222959 0.07894942 0.42059851 0.14907542 0.92798877 0.4627912
 0.15475565 0.6618435  0.58784648 0.79115779 0.79679832 0.82835395
 0.27187584 0.94472923 0.82823702 0.05262717 0.25835695 0.23485167
 0.28794714 0.64314675 0.28543144 0.98198517 0.95435668 0.39978538
 0.64350983 0.9038329  0.87394201 0.05311214 0.44752308 0.5632728
 0.87768612 0.56330696 0.22700284 0.9595241  0.39681074 0.26616065
 0.84900794 0.09536302 0.25160383 0.35014525 0.07026135 0.53923212
 0.22258151 0.83657879 0.74637742 0.055037   0.42623499 0.18821141
 0.61706252 0.2260063  0.36686731 0.71682258 0.49024109 0.72943461
 0.39890948 0.99632125 0.23251807 0.40410719 0.97754344 0.15903533
 0.04841419 0.20072715 0.84943721 0.75394774 0.32030464 0.31632382
 0.51085874 0.86815641 0.99309322 0.63717269 0.99114754 0.64017088
 0.74736605 0.45354721 0.36277059 0.23193163 0.53842361 0.45841963
 0.14566935 0.11710003 0.37977044 0.510686   0.64120124 0.25801337
 0.09051514 0.87961482 0.41199003 0.25997485 0.25409784 0.64055371
 0.33407954 0.24135215 0.32952643 0.95307759 0.03870667 0.40867981
 0.42284081 0.71306972 0.23503463 0.04614364]   '''

# اینا توابع بیرونی هستن و توشون باید آرایه بزاریم: 
np.sum(L) #48.76081779543432
np.min(L) #0.038706672983148116
np.max(L) #0.9963212462513072

# اینا توابع درونی هستن و باید . بزاریم تا بتونیم ازشون استفاده کنیم: 
L.sum() #48.76081779543432
L.min() #0.038706672983148116
L.max() #0.9963212462513072



L2 = np.random.random((2,3))
'''
            soton0      soton1       soton2
radif0  [[0.43123905   0.11408909   0.32224427]
radif1 [0.71701833    0.80749121    0.53378818]]   '''

L2.sum()            # 2.925870129555811                       جمع همه المنت‌ها
L2.sum(axis=0)      # [1.14825738, 0.9215803 , 0.85603246]    جمع همه المنت های هر ستون
L2.sum(axis=1)      # [0.86757241, 2.05829772]                جمع همه المنت های هر ردیف 


L2.min()           # 0.11408908790960137                     کمترین عدد بین همه المنت ها
L2.min(axis=0)     # [0.43123905, 0.11408909, 0.32224427]    کمترین عدد بین المنت‌های هر ستون
L2.min(axis=1)     # [0.11408909, 0.53378818]                کمترین عدد بین کل المنت‌های هر ردیف 



# ------------ سایر توابع -------------
a=np.arange(0,10)
np.var()         # sum of elements
np.prod()        # product of elemnts
np.std()         # compute standad deviation
np.var()         # variance
np.min()
np.max()
np.argmin()      # find the index of min
np.argmax()      # find the index o max
np.mean(a)       # 4.5   میانگین
np.median()
np.percentile()
np.any()
np.all()



#------ sort ---------

x=np.arange(15)
np.sort(x)          # مرتب کردن المنت‌ها     
np.sort(x,axis=0)   # مرتب کردن المنت‌های فلان متغیر، فقط ستونها





'''
#========================================================
#                 Trigonometric functions               |
#========================================================
'''
# توابع هندسی

theta = np.linspace(0, np.pi, 3)

print(theta)             # theta =  [0., 1.57079633, 3.14159265]
print(np.sin(theta))     # sin(theta) =  [0.0000000e+00  1.0000000e+00  1.2246468e-16]
print(np.cos(theta))     # cos(theta) =  [1.000000e+00   6.123234e-17  -1.000000e+00]
print(np.tan(theta))     # tan(theta) =  [0.00000000e+00  1.63312394e+16  -1.22464680e-16]


x = [-1, 0, 1]
print(x)                # x =  [-1, 0, 1]
print(np.arcsin(x))     # arcsin(x) =  [-1.57079633  0.            1.57079633 ]
print(np.arccos(x))     # arccos(x) =  [3.14159265   1.57079633    0.         ]
print(np.arctan(x))     # arctan(x) =  [-0.78539816  0.            0.78539816 ]




'''
#================================
#           Comparison          |
#================================
'''

arr1=np.array([10,20,30])

print(arr1)      # [10 20 30]
print(arr1>3)    # [ True,  True,  True]
print(arr1>=3)   # [ True  True  True]
print(arr1<3)    # [False False False]
print(arr1<=3)   # [False False False]
print(arr1==3)   # [False False False]
print(arr1!=3)   # [ True  True  True]


# ------ مقایسه دونه دونه المنت ها-------
np.equal() #==
np.not_equal() #!=
np.less() #<
np.less_equal() #<=
np.greater() #>
np.greater_equal() #>=


# آیا آرایه 1 با آرایه 2 برابر هست؟
arr1=np.array([10,20,30])
arr2=np.array([10,20,40])
np.equal(arr1,arr2)  # [ True,  True, False]

# آیا آرایه 1 از آرایه 2 کوچکتر هست؟
arr1=np.array([10,20,30])
arr2=np.array([100,200,1])
np.less(arr1,arr2) # [ True,  True, False]

# آیا آرایه 1 از آیاره 2 کوچکتره؟
arr1=np.array([10,20,30])
arr2=np.array([100,200,1])

np.less(arr1,arr2)          # [ True  True False]
np.less(arr1,arr2).any()    # True
np.less(arr1,arr2).all()    # False





'''
   =============================================
  |          Exponents and logarithms          |
  =============================================    
'''

# e=۲.۷۱۸۲۸۱۸۲۸۴۵۹۰۴۵...
# عدد e یک عدد خاص تو ریاضی هست مثل عدد پی.
# اگه بخوای بیشترین رشد ممکن رو داشته باشی، از عدد e استفاده می‌کنی.
# توابع زیر یه nd.array جدید برامون میسازه و متغیر خودمون رو باید توش بزاریم.
# تغییر روی دونه دونه المنت ها اعمال میشه.


x = [1, 2, 3]
print("x =", x)                  # x = [1, 2, 3]
#e**
print("e^x =", np.exp(x))        # e^x = [ 2.71828183  7.3890561  20.08553692]
print("2^x =", np.exp2(x))       # 2^x = [2. 4. 8.]
print("3^x =", np.power(3, x))   # 3^x = [ 3  9 27]


x = [1, 2, 4, 10]
print(x)                 # x = [1, 2, 4, 10]
print(np.log(x))         # ln(x) = [0.  0.69314718   1.38629436   2.30258509]
print(np.log2(x))        # log2(x) = [0.   1.    2.   3.32192809]
print(np.log10(x))       # log10(x) = [0.    0.30103    0.60205999 1.  ]






'''
   =============================================
  |            specialized functions           |
  =============================================    
'''
  
from scipy import special
x = [1, 5, 10]
print("gamma(x) =", special.gamma(x))
print("ln|gamma(x)| =", special.gammaln(x))
print("beta(x, 2) =", special.beta(x, 2))
x = np.array([0, 0.3, 0.7, 1.0])
print("erf(x) =", special.erf(x))
print("erfc(x) =", special.erfc(x))
print("erfinv(x) =", special.erfinv(x))







'''
    ========================================
   |     Iterating over array elements     |
   ========================================
'''

#----- 1D
v = np.array([1,2,3,4])

for element in v:
    print(element)
'''
1
2
3
4
'''


#------2D

M = np.array([[1,2],[3,4]])
print(M)
'''
radif 0 --> [[1 2]
radif1 --> [3 4]]
'''

# برای دسترسی به یک المنت خاص در آرایه 2 بعدی اول باید بگیم کدوم ردیف؟
for row in M:
    print(row)
    for element in row:
        print(element)

'''
1
2
3
4
'''


#-------3D

C3 = np.array([[[1,2,3],[4,5,6]] , 
               [[7,8,9],[10,11,12]] ,
               [[13,14,15],[16,17,18]] ])
C3.ndim #3
C3.shape #(3,2,3)

for matrix in C3:
    for row in matrix:
        for element in row:
            print(element)

        
'''
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
'''


#-------4D

#d4[kodom 3d , kodom table, kodom radif, kodom soton]

#for 3d in 4d:
    #for matrix in 2d:
        #for row in matrix:
            #for element in row:
                #print(element)



'''---- Faster ways ----'''
M[2,1]       # ردیف 2، ستون 1
C3[1,2,2]    # کدوم جدول، کدوم ردیفو کدوم ستون


#____________________________________________
Matrix = np.random.uniform(10,20,(4,5))
print(Matrix)
'''
[[10.7101504  10.9931878  19.36326489 12.57765563 10.40385527]
 [11.30634037 18.09112736 18.75921809 19.03509636 19.2634681 ]
 [19.5841465  19.01956689 18.80846765 13.94746962 10.35346747]
 [17.65658903 12.38961262 19.73570548 11.68273099 19.60990709]]   '''

mylist=[]
for row in Matrix:
    for element in row:
        if element>15:
            mylist.append(element)
            
print(mylist)
'''
[19.363264891938712, 18.091127363963125, 18.759218093195543, 19.035096363034956, 19.263468102884477, 19.584146501415404, 19.019566889061757, 18.808467650353343, 17.656589025143113, 19.73570547891891, 19.609907091633232]
'''
#_______________Faster way__________________

Matrix>19
'''
array([[False, False,  True, False, False],
       [False, False, False,  True,  True],
       [ True,  True, False, False, False],
       [False, False,  True, False,  True]])   '''

if (Matrix>19).any():
    print('failed')     #failed


Matrix[Matrix>15]
'''
array([19.36326489, 18.09112736, 18.75921809, 19.03509636, 19.2634681 ,
       19.5841465 , 19.01956689, 18.80846765, 17.65658903, 19.73570548,
       19.60990709])   '''









'''
    ========================================
   |         JOINING ANS SPLITTING         |
   ========================================
'''

a=np.array([10,20,30,40])
b= np.array([100,200,300,400])


# np.concatenate(a,b) --> wrong!

c= np.concatenate((a,b))
print(c)    #[ 10  20  30  40 100 200 300 400]

c= np.concatenate((a,b),axis=0)
print(c)    #[ 10  20  30  40 100 200 300 400]

c=np.concatenate((a,b),axis=1)
print(c)    #AxisError: axis 1 is out of bounds for array of dimension 1


#reshape()

c.reshape(2,4)
'''
array([[ 10,  20,  30,  40],
       [100, 200, 300, 400]])    '''

c.reshape(4,2)
'''
array([[ 10,  20],
       [ 30,  40],
       [100, 200],
       [300, 400]])    '''



#-----------3D---------

a=np.array([10,20,30,40]).reshape(2,2)
b= np.array([100,200,300,400]).reshape(2,2)

print(a)
'''
[[10 20]
 [30 40]]   '''

print(b)
'''
[[100 200]
 [300 400]]  '''


c = np.concatenate((a,b))
# در طول ردیفها concat میکنه.
print(c)
'''
[[ 10  20]
 [ 30  40]
 [100 200]
 [300 400]]  '''


c = np.concatenate((a,b),axis=0)
print(c)
'''
[[ 10  20]
 [ 30  40]
 [100 200]
 [300 400]]
'''



c = np.concatenate((a,b),axis=1)
print(c)
'''
[[ 10  20]
 [ 30  40]
 [100 200]
 [300 400]]

'''


#-----------vstack--------------
# vertical stack    عمودی

x = np.array([1, 2, 3])    #[1 2 3]

grid = np.array([[9, 8, 7], [6, 5, 4]])
print(grid)
'''
[[9 8 7]
 [6 5 4]]
'''

np.vstack([x, grid])
'''
[[1, 2, 3],
 [9, 8, 7],
 [6, 5, 4]]
'''


#---------- hstack -------------
# horizontal stack

np.hstack((x,grid)) #errror

a=np.array([10,20,30,40]).reshape(2,2)
b= np.array([100,200,300,400]).reshape(2,2)

np.hstack((a,b))
'''
array([[ 10,  20, 100, 200],
       [ 30,  40, 300, 400]])
'''


#------------ split -------------

x = [1, 2, 3, 99, 99, 3, 2, 1]

a = np.split(x,(3,5))

print(a)    #[array([1, 2, 3]), array([99, 99]), array([3, 2, 1])]



#------------ repeat -------------

a= np.array([[1,2],[3,4]])

np.repeat(a,3)

#array([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4])



#------------ BLOCK -------------

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(a)
'''
[[1 2]
 [3 4]]
'''

print(b)
'''
[[5 6]
 [7 8]]
'''

result = np.block([
    [a, np.zeros((2,2))],
    [np.zeros((2,2)), b] ])

print(result)
'''
[[1. 2. 0. 0.]
 [3. 4. 0. 0.]
 [0. 0. 5. 6.]
 [0. 0. 7. 8.]]
'''



#------------ reshape -------------
# تابع reshape یک عدد -1 داره که هرجا نمیدونیم برای ستون یا ردیف چه عددی وارد کنیم بجاش -1 میذاریم که خودش حساب کنه.

a= np.arange(10,410,10)
print(a)
'''
[ 10  20  30  40  50  60  70  80  90 100 110 120 130 140 150 160 170 180
 190 200 210 220 230 240 250 260 270 280 290 300 310 320 330 340 350 360
 370 380 390 400]   '''

a.shape # (40,)

#size = radif x soton
# اگه a رو بخوایم 4 ردیف تبدیل کنیم طبیعتا تنها حالتی که میمونه انه که 10 تا ستون داشته باشه و برعکس.
# پس میایم تعداد ستون یا ردیفی که میخوایم میذاریم، بجای اونی که نمیدونیم -1 میذاریم خودش حساب کنه.


#1----usage

b=a.reshape(4,-1)
b.shape # (4, 10)

c= a.reshape(-1,4)
c.shape # (10, 4)



#2----usage

# بعضی از توابع روی shape آرایه هایی که بهشون میدیم محدودیت shape دارن.
# مثلا بعضی جاها مجبور میشیم تابع 1 بعدی رو به 2 بعدی تبدیل کنیم.


a = np.array([1,2,3,4,5,6,7,8,9,10])
a.shape # (10,)
a.ndim  # 1

a.reshape(1,-1)   # یک ردیف، ستون هارو خودت حساب کن
a.reshape(-1,1)   # یک ستون، ردیف هارو خودت حساب کن

# 10 ردیف یک ستون
'''
1
2
3
4
5
6
7
8
9
10
'''












#   =====================================================================
#   =====================================================================
#   ==============           Review of all codes           ==============
#   =====================================================================
#   =====================================================================


'''
a = np.array([1,2,3,4])
print(a)
print(type(a))
print(a.ndim)
print(a.shape)
print(a.size)
print(b[1,2])
print(b[0,:])
a= np.arange(10)   0-10
a=np.linspace(0,1,100)    0-1 taghsim be 100 ghesmate mosavi
c = np.logspace(0,10,10 )   tavane 10

(shape)
    np.empty((2,3))
    np.empty(10)  10 ta khali besaz
    np.zeros(10)   10 ta 0
    np.zeros((2,5))  2row, 5col => 0
    np.ones((3,5))  3row, 5col => 1
    np.full((2,3),3.14)   2row, 3col => ba adade 3.14 ke behet dadam por kon

Identity matrix
    i x i --> vatar=1, baghie=0
    np.eye(3)   3*3 matrix   
    [1., 0., 0.],
    [0., 1., 0.],
    [0., 0., 1.]
    
    np.eye(4)  4*4 matrix
    [1., 0., 0., 0.],
    [0., 1., 0., 0.],
    [0., 0., 1., 0.],
    [0., 0., 0., 1.]
    
    
Diagonal matrix
    vatar=adade dakhele list, baghie=0
    np.diag([1,2,3])
    [1, 0, 0],
    [0, 2, 0],
    [0, 0, 3]
offset:
    meghdare pishfarz(k) =0
    be andaze adadi le be k midim, vatar bala payin mire
    np.diag([1,2,3,4],k=0) 
    [1, 0, 0, 0],
    [0, 2, 0, 0],
    [0, 0, 3, 0],
    [0, 0, 0, 4]

    np.diag([1,2,3,4],k=1) 
    [0, 1, 0, 0, 0],
    [0, 0, 2, 0, 0],
    [0, 0, 0, 3, 0],
    [0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0]


random.random()
random.randint(10, 20)
np.random.random( ,(shape)) => 0-1
np.random.random()   #0.016036791252807436
np.random.random((2,3))
    [0.01302821, 0.32131125, 0.11003532],
    [0.08975113, 0.08635853, 0.72005935]
random distribution |----- uniformly => a-b
                    |_____ gausian (normal) => variance
np.random.uniform(0,10,(2,3))
    [5.71142564, 6.91424201, 0.27549855],
    [3.61827544, 5.71250762, 6.08274449]
np.random.normal(20,5)  => adade tasadofi hole mehvare 20, variance=5
    17.03996522106831
    20.60846555217081
    28.32151614349159

np.random.randint(12,18,(2,3))
    [12, 12, 16],
    [14, 12, 12]
    
    
dtype = data type
    int32
    int64
    float32
    float64




 _______________________
|                      |
|  Magic functions     |
-----------------------

reshape()
    a = np.arange(1, 10).reshape((3, 3))
    [[1 2 3]
     [4 5 6]
     [7 8 9]]

.astype() => changing data type
    M = np.array([10,20,30,40])   M.dtype=int64   # M=[10 20 30 40]
    M2 = M.astype(float)    #[10. 20. 30. 40.]
    M3 = M.astype(bool)     #[ True  True  True  True]

flatten()
    a = np.random.uniform(1,10,(5,2))
    b = a.flatten()   => [9.63260924 5.67090252 7.73690271 ...]





 _____________________________________
|                                    |
|  Fancy editting  => filtering      |
-------------------------------------

row_index
    arr=np.array([11,22,33,44,55,66,77,88,99])
    row_index = [1,2,3]
    arr[row_index]   => array([22, 33, 44])

row_mask -> only returns true values
    row_mask = np.array([True,True,False,False,False,False,False,False, False])
    row_mask = np.array([1,1,0,0,0,0,0,0,0])

other filtering features
    x = np.array([1, 2, 3, 4, 5])
    x < 3 # less than 
    x > 3 # greater than
    x <= 3 # less than or equal
    x >= 3 # greater than or equal
    x != 3 # not equal
    x == 3 # equal

where => folan chiz kojast? ba adade index mige
    a = np.arange(10,40)
    np.where(a==12)   array([2]) --> a[2]
    np.where(a==5)    array([])   --> no such thing
    np.where(a>30)    array([21, 22, 23, 24, 25, 26, 27, 28, 29])

counting => tedad chizi ke mikhaym peyda mikone - chanta element folan sharayet dare?
    x = np.arange(0,10)   #[0 1 2 3 4 5 6 7 8 9]
    np.count_nonzero(x < 6)    6؟
    np.sum(x < 6)    6




 __________________
|                 |
|  conditions     |
------------------

    if-else
    
    M = np.arange(5,10)   #[5 6 7 8 9]
    (M>8).any() #9 --> True
    (M>8).all() #False




 ______________________
|                     |
|  Array arithemic    |
----------------------

    np.add() #+
    np.substract() #-
    np.negative() #-
    np.multiply() #*
    np.divide() #/
    np.floor_divide() #//
    np.power() #**
    np.mod() #%
    np.absolute()
    #or
    np.abs()
    
    np.floor(x)
    np.ceil(x)
    
    x = np.arange(1,6)           # [1 2 3 4 5]
    np.add.reduce(x)             # 15    1+2+3+4+5
    np.multiply.reduce(x)        # 120   1*2*3*4*5
    np.multiply.accumulate(x)    # [1, 2, 6, 24, 120]




 _________________
|                |
|  Statistics    |
-----------------

    L = np.random.random(100)
    np.sum(L) #48.76081779543432
    np.min(L) #0.038706672983148116
    np.max(L) #0.9963212462513072
    
    L.sum() #48.76081779543432
    L.min() #0.038706672983148116
    L.max() #0.9963212462513072
    
    L2 = np.random.random((2,3))
                soton0      soton1       soton2
    radif0  [[0.43123905   0.11408909   0.32224427]
    radif1 [0.71701833    0.80749121    0.53378818]]
    
    L2.sum()            # 2.925870129555811   jame hame element ha
    L2.sum(axis=0)      # [1.14825738, 0.9215803 , 0.85603246]   jame hame element haye har soton
    L2.sum(axis=1)      # [0.86757241, 2.05829772]      jame hame, har radif
    
    L2.min()           # 0.11408908790960137  
    L2.min(axis=0)     # [0.43123905, 0.11408909, 0.32224427]    min dar har soton
    L2.min(axis=1)     # [0.11408909, 0.53378818]    min dar har radif 
    
    
    a=np.arange(0,10)
    np.var()         # sum of elements
    np.prod()        # product of elemnts
    np.std()         # compute standad deviation
    np.var()         # variance
    np.min()
    np.max()
    np.argmin()      # find the index of min
    np.argmax()      # find the index o max
    np.mean(a)       # 4.5   miangin
    np.median()
    np.percentile()
    np.any()
    np.all()





 __________________
|                 | 
|  Comparison     |
------------------

    moghayese dune dune element ha
    np.equal() #==
    np.not_equal() #!=
    np.less() #<
    np.less_equal() #<=
    np.greater() #>
    np.greater_equal() #>=
    
    arr1=np.array([10,20,30])
    arr2=np.array([10,20,40])
    np.equal(arr1,arr2)  # [ True,  True, False]




 _____________________________________
|                                    |
|  iterating over array elements     |
-------------------------------------

1D
    v = np.array([1,2,3,4])
    for element in v:
        print(element)     # 1 2 3 4
    
2D
    M = np.array([[1,2],[3,4]])
    for row in M:
        print(row)
        for element in row:
            print(element)    # 1 2 3 4

3D
    C3 = np.array([[[1,2,3],[4,5,6]] , 
                   [[7,8,9],[10,11,12]] ,
                   [[13,14,15],[16,17,18]] ])
    for matrix in C3:
        for row in matrix:
            for element in row:
                print(element)
 
    
 
 _____________________________
|                            |
|  Joining and Splitting     |
-----------------------------

    a=np.array([10,20,30,40])
    b= np.array([100,200,300,400])
    # np.concatenate(a,b) --> wrong!
    c= np.concatenate((a,b))     #[ 10  20  30  40 100 200 300 400]
    c= np.concatenate((a,b),axis=0)    #[ 10  20  30  40 100 200 300 400]


3D
    a=np.array([10,20,30,40]).reshape(2,2)
    b= np.array([100,200,300,400]).reshape(2,2)
    [[10 20]        [[100 200]
     [30 40]]       [300 400]]
    
    c = np.concatenate((a,b))  => dar tule radif ha concat mikone
    c = np.concatenate((a,b),axis=0)
    [[ 10  20]
     [ 30  40]
     [100 200]
     [300 400]]
    
    c = np.concatenate((a,b),axis=1)
    [[ 10  20]
     [ 30  40]
     [100 200]
     [300 400]]


VERTICAL STACK
    x = np.array([1, 2, 3])
    grid = np.array([[9, 8, 7], [6, 5, 4]])       [[9 8 7]
                                                   [6 5 4]]
    np.vstack([x, grid])
    [[1, 2, 3],
     [9, 8, 7],
     [6, 5, 4]]
    np.hstack((x,grid)) #errror


HORIZONTAL STACK
    a=np.array([10,20,30,40]).reshape(2,2)
    b= np.array([100,200,300,400]).reshape(2,2)
    np.hstack((a,b))
          [[ 10,  20, 100, 200],
           [ 30,  40, 300, 400]]


SPLIT
    x = [1, 2, 3, 99, 99, 3, 2, 1]
    a = np.split(x,(3,5))      #[array([1, 2, 3]), array([99, 99]), array([3, 2, 1])]


REPEAT
    a= np.array([[1,2],[3,4]])
    np.repeat(a,3)     #array([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4])


BLOCK
    a = np.array([[1,2],[3,4]])
    b = np.array([[5,6],[7,8]])
    
    result = np.block([
        [a, np.zeros((2,2))],
        [np.zeros((2,2)), b] ])
    
    [[1. 2. 0. 0.]
     [3. 4. 0. 0.]
     [0. 0. 5. 6.]
     [0. 0. 7. 8.]]


RESHAPE
    harja nmidunim baraye radif ya soton che adadi bzarim, -1 midim ke khodesh hesab kone.
    a= np.arange(10,410,10)    a.shape # (40,)
    b=a.reshape(4,-1)
    b.shape # (4, 10)
    
    c= a.reshape(-1,4)
    c.shape # (10, 4)



'''

















