
'''
===============================================================================
===============================================================================
================       Created on Tue Jul  7 18:24:55 2026     ================
================                IDE: Spyder                    ================
================         Author: Khashayar Alipour             ================
================              Statistical models               ================
================                 ML intro                      ================
===============================================================================
===============================================================================
'''


# SGDRegressor()
# SGDRegressor class
# Scaling in SGDRegressor - StandardScaler / MinMaxScaler
# LogisticRegression()
# model validation
# train_test_split()


#                                                         ------  model=LinearRegression()
#                         ----- statistical regression ---|
#                         |                               ------  model=SGDRegressor()
# Statistical models -----|
#                         ----- statistical classification --- model = LogisticRegression()

# step 0.0 --> cleaning data
# step 0.1 --> x,y تبدیل به
# step 1 --> train, test, split
# step 2 --> training phase (fit) - model
# step 3 --> evaluation => MAE , MSE , RMSE , MAPE







'''
=====================================
=======   linear regression   =======
=====================================
'''

# در درسنامه regression.py گفتیم که برای پیدا کردن رابطه بین دو چیز باید از رگراسیون استفاده کرد
# چرا باید از رگراسیون استفاده کرد؟
# چون در عمل منابع زمانی و مالی محدوده و امتحان کردن تمام حالتهای ممکن بین دو چیز عملا امکان پذیر نیست

# فرض کنیم بین x و y رابطه وجود دارد و این رابطه خطی هست
# رگراسیون خطی میاد رابطه y = a*x + b رو بین اون دو چیز حساب میکنه
# مولفه هایی مثل MSE و loss value و ... رو حساب میکرد و در نهایت رابطه رو پیدا میکرد

# در مثال زیر، با استفاده از رگراسیون خطی رابطه بین استحکام و دما رو پیدا کردیم

import numpy as np
import matplotlib.pyplot as plt

temperature = np.array([10,20,30,40,50])
estehkam = np.array([105,210,290,405,487])


def linear_regression(x,y):
    best_loss = 10000000000000000000
    best_a = 0
    best_b = 0

    all_parameters = []
    

    for a in range(100):
        for b in range(100):
            y_pred = a*x + b
            loss = np.mean((y_pred - y )**2)
            if loss < best_loss:
                best_loss = loss
                best_a = a
                best_b = b

                all_parameters.append({'a':a, 'b':b, 'loss':loss})

                plt.scatter(x,y)
                plt.plot(x, y_pred, color='red',label=f'a={a}, b={b}, loss={loss}')
                
                plt.xlabel('Temperature')
                plt.ylabel('Estehkam')
                plt.title('Estehkam vs Temperature')
                plt.xlim(0,70)
                plt.ylim(100,500)
                plt.legend()
                plt.grid()
                plt.show()
            
    return best_a, best_b

linear_regression(temperature,estehkam)









'''
===========================================================================
=======    SGDRegressor (schotastic gradient descent regression)    =======
===========================================================================
'''

# همچنین در رگراسیون خطی از روشی بنام گرادیان نزولی هم برای پیدا کردن رابطه بین دو چیز میشه استفاده کرد
# در این روش بصورت رندوم a و b یک مقدار حدس میزنه و خودش یک خط اولیه میکشه
# سپس ازین خط مشتق میگیره و شیبش رو حساب میکنه
# سپس با یک learning rate به سمت شیب منفی حرکت میکنه
# اینقد اینکار رو ادامه میده تا به پایین ترین loss value برسه
# در همون نقطه رابطه y= a*x + b محاسبه میشه


import numpy as np
import matplotlib.pyplot as plt


#pip install scikit-learn
from sklearn.linear_model import LinearRegression
model = LinearRegression()


from sklearn.linear_model import SGDRegressor
model = SGDRegressor()

# حالا این SGDRegressor چیه؟
# زیر مجموعه رگراسیون خطی هست و روش کارش بر اساس همون گرادیان نزولی هست
# یک روش آماری هست که پارامترهای داخلی داره، این پارامترها اینقد تغییر میکنن تا loss function محاسبه بشه

#===================================================================================
model = SGDRegressor(loss = 'squared_error',learning_rate='constant',eta0=0.0001 , max_iter=10000,random_state=42)
# اگر این مقداری که به learning rate دادیم خیلی زیاد باشه برای پیدا کردن min loss خیلی اینور اونور میپره و unstabel هست
# اگر مقدارش خیلی کم باشه با سرعت خیلی کمی پارامترها تغییر میکنن و min خیلی طول میکشه پیدا بشه
# اینجا max iter میشه اون range که توش باید a و b رو حدس بزنه تا به min برسه
#===================================================================================



''' ========================= SGDRegressor class =============================== '''
# داخل کتابخوانه sklearn یک پوشه بنام linear_model هست
# که داخلش یک فایل بنام SGD.py هست که کلاس SGDRegressor داخلش به صورت زیر تعریف شده
# این کلاس چند تابع مهم داره که اینجا توضیح داده شده

class SGDRegressor:

    def __init__(self,loss='squared_error',learning_rate='constant',eta0=0.0001 , max_iter=10000,random_state=42):
        self.loss = loss
        self.learning_rate = learning_rate
        self.eta0 = eta0
        self.max_iter = max_iter
        self.random_state = random_state


    def fit(self,X,y):
        # در این تابع یک حلقه for اجرا میشه و a و b رو تغییر میده        
        #for range (0, self.max_iter)
        
    # این تابع دوتا ورودی میگیره و با روش gradient descent نقاط رو پیدا میکنه        
    
    # یک قانون این تابع اینه که اگه x که ورودی میدیم 1 بعدی باشه باید reshape کنیم وگرنه ValueError میده        
        # x=1D --> reshape(-1,1)   تبدیل به آرایه 2 بعدی میشه
    
        initial_a , intiial_b = _initialize_parameters(X.shape[1])    # nesbat be x miad a,b hads mizane
        gradient_a , gradient_b = _gradient(X,y,initial_a,initial_b,self.learning_rate,self.max_iter,self.random_state)    # moshtaghe a , b ro migire 
        new_a , new_b = _update_parameters(a,b,gradient_a,gradient_b,self.learning_rate,self.max_iter,self.random_state)
        all_parameters = _loss(new_a,new_b,X,y)
        _record_information(new_a,new_b,loss)
        best_a , best_b , best_loss = _find_best_parameters(self.all_parameters)

# در انتهای این تابع بهترین a و بهترین b که پیدا کرده رو به اینصورت ذخیره میکنه:        
    # اسم a رو میذاره coef که مخفف coefficient هست که همون ضریب با شیب خط ما هست        
        self.coef_ = best_a
# اسم b رو میذاره intercept که همون عرض از مبدا ما هست        
        self.intercept_ = best_b


# در این تابع یک نقطه حدس زده میشه    
    def predict(self,X):
        # x=1D --> reshape(-1,1)  قانون این تابع
        y_pred = self.coef_ * X + self.intercept_       #y_pred = a * x + b
        return y_pred


# در این تابع نقطه‌ای که در تابع بالایی حدس زده شد با y واقعی از نظر فاصله مقایسه میشه    
    def score(self,X , y):
        # x=1D --> reshape(-1,1)  قانون این تابع
        y_pred = self.predict(X)
        return self._loss(y_pred,y)


    def _loss(self,y_pred,y_true):
        if self.loss == 'squared_error':
            return np.mean((y_pred - y_true)**2)
        elif self.loss == 'absolute_error':
            return np.mean(np.abs(y_pred - y_true))
    
    
    def _initialize_parameters(self,n_features):
        pass

    def _gradient(self,x,y,initial_a,initial_b,learning_rate,max_iter,random_state):
        pass

    def _update_parameters(self,a,b,gradient_a,gradient_b,learning_rate,max_iter,random_state):
        pass

    def _find_best_parameters(self,all_parameters):
        pass

    def _record_information(self,new_a,new_b,loss):
        pass
'''==============================================================================='''





# حالا میخوایم در عمل بیایم با این SGDRegressor رابطه بین دما و استحکام رو حساب کنیم

# هردو 1 بعدی هستن و x باید reshape بشه
temperature = np.array([10,20,30,40,50])
estehkam = np.array([105,210,290,405,487])


from sklearn.linear_model import SGDRegressor

# از کلاس SGDRegressor یک آبجکت (model) میسازیم که بتونیم از متودهاش استفاده کنیم
model = SGDRegressor(loss = 'squared_error',learning_rate='constant',eta0=0.0001 , max_iter=10000,random_state=42)

temperature = temperature.reshape(-1,1)    # تبدیل به دو بعدی
model.fit(temperature, estehkam)


# حالا بعد از fit شدن از دل آبجکتی که ساختیم a و b رو خارج میکنیم که به ترتیب coef و intercept هست
# و زمانیکه a و b محاسبه بشه دیگه میتونیم معادله خودمون رو بدست بیاریم

a = model.coef_
b = model.intercept_

print(a)    #[9.88053609]
print(b)    #[0.28367049]
print(f'y = {a} * x + {b}')   #y = [9.88053609] * x + [0.28367049]



# حالا که معادله ما بدست آمده میتونیم هر عددی که بخوایم رو پیش بینی کنیم
# دما به اینصورت بود: [10,20,30,40,50]
# میخوایم مثلا ببینیم استحکام در دمای 15 چقدر هست
# استفاده از معادله به اینصورت غلطه:
res = a * 15 + b 
# باید از تابع predict استفاده بشه که از دل کلاس SGDRegressor میاد
# این تابع هم اگه x یک بعدی بهش بدیم ارور میده پس باید reshape بشه:
model.predict(np.array([15]).reshape(-1,1))    #array([148.49171184])

# برای دماهای 15 و 20 و 30 و 40
model.predict(np.array([15,20,30,40]).reshape(-1,1))    #array([148.49171184, 197.89439229, 296.69975319, 395.50511409])





'''======================= SGDRegressor  1D =================================='''
x= temperature
y = estehkam 

from sklearn.linear_model import SGDRegressor
model = SGDRegressor()

model.fit(x,y)

model.coef_
model.intercept_

print('a = ',model.coef_)
print('b = ',model.intercept_)
print(f'y = {model.coef_} * x + {model.intercept_}')

new_x = np.array([15]).reshape(-1,1)
y_pred = model.predict(new_x)
'''==========================================================================='''








'''
============================================================================
=======   Scaling in SGDRegressor - StandardScaler / MinMaxScaler    =======
============================================================================
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


# برای scale کردن از روشهای مختلفی استفاده میشه:

'''1-StandardScaler'''
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
X_scaled = scaler.fit_transform(X)

# تابع fit_transform همزمان 2 کار انجام میده
# اول قسمت scaler.fit(x) میاد میانگین و انحراف معیار رو حساب میکنه
# سپس قسمت transform(X) میاد اعداد رو تبدیل میکنه    



'''2-MinMaxScaler'''
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
X_scaled = scaler.fit_transform(X)


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
=========================================================
=======   classification - logisticRegression()   =======
=========================================================
'''

# تا اینجا رگراسیون خطی رو یاد گرفتیم
# حالا میخوایم ببینیم Classification چیه

# اینجا هم x ورودی و y خروجی داریم
# ولی دیگه دنبال y= a*x + b نیستیم
# بلکه دنبال اینیم که X ورودی بدیم و بگه براساس X توی کدوم دسته هست
# یعنی بجای مقایسه x و y برای پیدا کردن رابطشون، میاد بین x ها بررسی میکنه تا بتونه دسته بندی کنه

# مثلا ما دو نوع گل داریم (رز و یاسمن) و طول و عرض هر گل رو حساب کردیم و تمام نمونه ها label گذاری شدن
# براساس طول و عرض جدول بندی میکنیم
# میخوایم یه سیستمی درست کنیم که اگه طول و عرض گل بهش بدیم نوع و دسته بندی گل رو برامون مشخص کنه
# دنبال عدد نیستیم دنبال دسته بندی هستیم

# arz  |  tool  | noe gol
#-------------------------
# 5        10     yasaman  
# 6        12     yasaman  
# 5        18     yasaman  
# 8        9      yasaman 
# 9        14     yasaman 
# 10       20     yasaman 

# 15       15      roz 
# 20       18      roz 
# 23       17      roz 
# 18       16      roz 
# 17       20      roz 
# 16       22      roz 
# 20       24      roz 


# دیتاهای ما از قبل همشون جمع آوری شده‌اند -> RL نیست
# حجم دیتاها کمه -> Deep Learning نیست
# هم ورودی داریم و هم خروجی، خروجی‌ها لیبل خورده -> unsupervised نیست
# خروجی‌ دسته بندی هست -> پس supervised classification هست


# ====== رسم نمودار دیتاهامون ======

import numpy as np
import matplotlib.pyplot as plt

# x1 = arz column
x1 = np.array([5, 6, 5, 8, 9, 10,        # yasaman
               15, 20, 23, 18, 17, 16, 20]) # roz

# x2 = tool column
x2 = np.array([10, 12, 18, 9, 14, 20,      # yasaman
               15, 18, 17, 16, 20, 22, 24]) # roz

# label: yasaman = 0, roz = 1
label = np.array([0, 0, 0, 0, 0, 0,         # yasaman (6 samples)
                  1, 1, 1, 1, 1, 1, 1])      # roz     (7 samples)

c_label = ['blue','blue','blue','blue','blue','blue','red','red','red','red','red','red','red']


x_range = np.linspace(0,25,100)
a= -1.1
b=31.5
y_range = a * x_range + b
plt.plot(x_range,y_range,color='black')

plt.scatter(x1,x2,c=c_label)
plt.xlabel('arz')
plt.ylabel('tool')
plt.title('arz va tool')
plt.show()



# ما در این نمودار دیگه دنبال این نیستیم که خطی رسم کنیم  که نقطه‌هارو بهم وصل کنه (y= a*x +b)
# بلکه دنبال خطی هستیم که در نمودار گلهای رز و یاسمن از همدیگه جدا کنه کلا
# که اگه یروزی یه گل جدید اومد با گرفتن طول و عرضش تشخیص بدیم که این تو کدوم دسته قرار میگیره

# حالا این خط از کجا بفهمیم چه خطی هست؟ باید حداقل ممکن برای loss function رو داشته باشه
# اینجا loss function ما میشه تعداد گلهایی که واقعا در دسته‌ی خودشون قرار گرفتن
# یعنی مثلا اگه یه خط فرضی رسم کردیم که از 7 تا گل رز (کلا 13تا گل)، هیچکدوم واقعا توی دسته خودش قرار نداده
# یعنی از 13تا گل 6تاشو درست تشخیص نداده
# اینجا loss function اینجوری حساب میشه ->  6 تقسیم بر 13 ضرب در 100 که میشه 46
# اینقد خط رسم میکنیم تا به بهترین نتیجه برسیم و خطی پیدا کنیم که در بهترین حالت دسته بندی هارو جدا کنه
# بهترین loss function اونی میشه که درصدش از همه پایین تره (ممکنه به 0 برسیم ممکنه نرسیم)

# مثلا در مثال بالا ما چند خط رسم کردیم و همش a و b رو تغییر دادیم تا به درست ترین خط با کمترین loss function برسیم
# a=-1 , b=10 --> 48 % خطا
# a= -1 , b=20 --> 25 % خطا
# a= -1 , b=25 --> 1/13 --> 5 % خطا
# a=-1.1 , b = 31.5 --> 0/13 خطا

# به زبان ساده: در رگراسیون خطی میگفتیم loss_function = y_pred - y_true ولی اینجا میشه: چندتا درست تشخیص داده شده؟



# این classification هم یک کلاس واسه خودش توی sklearn داره که مثل همون کلاس SGDRegressor و LinearRegression هست
# با چندتا تفاوت جزئی توی بعضی توابعش
# مثال بالارو اول دستی حل کردیم حالا میخوایم با یک مدل classification که اسمش LogisticRegression هست انجام بدیم

import numpy as np

# x1 = arz column
x1 = np.array([5, 6, 5, 8, 9, 10,        # yasaman
               15, 20, 23, 18, 17, 16, 20]) # roz

# x2 = tool column
x2 = np.array([10, 12, 18, 9, 14, 20,      # yasaman
               15, 18, 17, 16, 20, 22, 24]) # roz

# label: yasaman = 0, roz = 1
label = np.array([0, 0, 0, 0, 0, 0,         # yasaman (6 samples)
                  1, 1, 1, 1, 1, 1, 1])      # roz     (7 samples)


# برای استفاده از مدلها باید همه چیز به یک x و یک y تبدیل بشه
# اینجا 2تا x داریم که ستونهاشو میذاریم کنار هم و به یک X تبدیلش میکنیم
x = np.array([x1,x2]).reshape(-1,2)    # گفتیم 2 تا ستون بشه و ردیف هاشو خودت مشخص کن هرچی هست
y = label


from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

model.fit(x,y)



# حالا که مدل رو fit کردیم میایم با تابع predict پیشبینی انجام میدیم

model.predict(np.array([10,15]).reshape(1,-1))   # array([0])   تو دسته یاسمن رفت
model.predict(np.array([20,30]).reshape(1,-1))   # array([1])   تو دسته رز رفت












'''
==========================================
=======   classification metrics   =======
==========================================
'''

from sklearn.metrics import accuracy_score
# این متریک میاد میسنجه که مدل چند درصد دقت داره

#y_test_pred = [1,0,0,0,1,1]
#y_test = [1,0,1,1,1,0]

test_score_accuracy = accuracy_score(y_test_pred - y_true)

#balanced_accuracy_score
#top_k_accuracy_score
#recall_score
#f1_score











'''
===============================================
=======   Statistical models validity   =======
===============================================
'''

# حالا وقتی یه مدل پیشبینی انجام میده از کجا بفهمیم که این پیشبینی درسته؟
# از کجا بفهمیم این model که ازش استفاده میکنیم reliable هست؟
# به پروسه سنجش کیفیت یک مدل میگن model validation

''' difference of loss and validation? '''
# کلا loss برای آموزش یک مدل کاربرد داره ولی Validation برای سنجیدن یک مدل هست
# فرض کنیم هنگام درس خوندن بعد از فصل از خودمون یک امتحان بگیریم --> loss
# در پایان سال معلم از کل فصلها یک آزمون میگیره --> Validation
# Data gathering --> model training --> loss calculation --> parameter optimzation --> validation --> Test


''' regression evaluation metrics '''
# این معیارها بهمون کمک میکنن بفهمیم عملکرد مدل را با چه معیاری اندازه بگیرم؟
# بعد ازینکه با متودهای validation تقسیم داده ها انجام شد، با معیارهای Evaluation میایم از عملکرد مدل test میگیریم
Regression Metrics
    ├── MAE
    ├── MSE
    ├── RMSE
    ├── R² Score
    └── Adjusted R²


''' regression validation methods '''
# این متودها بهمون کمک میکنن بفهمیم روی کدام داده‌ها مدل را ارزیابی کنم؟
# روشهایی هستند که هرکدوم با فرمول خاص خودشون دیتاهارو به دو گروه Train و test تقسیم میکنن
Validation Methods
    ├── Train/Test Split
    ├── K-Fold Cross Validation
    ├── Leave-One-Out
    └── Stratified K-Fold




# در مثال زیر مثلا در یک شرکت هستیم و به رئیس شرکت میگیم بیا من یک مدل ساختم که رابطه بین دما و استحکام رو پیشبینی میکنه
# ولی رئیس شرکت میگه از کجا بفهمم این مدل قابل اعتماد هست؟

temperature = [10,20,40,60,80,100]
estehkam = [105, 197, 401, 605, 809, 1013]

x  = np.array(temperature).reshape(-1,1)
y = np.array(estehkam)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x,y)
new_x = np.arange(0,150,1).reshape(-1,1)
y_pred = model.predict(new_x)

plt.scatter(x,y,label='experimental data')
plt.plot(new_x,y_pred,color='red',label='linear regression')
plt.title('temperature va estehkam')
plt.xlabel('temperature')
plt.ylabel('estehkam')
plt.xlim(0,150)
plt.ylim(0,1500)
plt.grid()
plt.legend()
plt.show()


print(model.coef_)    # [10.13150685] --> a
print(model.intercept_)   # -1.7945205479452397 --> b

# estehkam = 10.1315 * dama - 1.7945   در نهایت رابطه‌ای که بدست آوردیم میشه این



# راه حل پیشنهادی شرکت برای سنجش قابل اعتماد بودن این مدل اینه که بریم 2 دمایی که اصلا در دیتاهامون نیست آزمایش کنیم
# من میذارم توی مدل خودم و شرکت میره در عمل تستش میکنه، سپس میایم این دوتارو باهم مقایسه میکنیم و ببینیم فاصلشون باهم چقدره؟
# میایم برای دمای 30 و 90 که در دیتاهامون نیست تست میکنیم

# 1- یا میتونیم از رابطه y= a*y + b که بدست آوردیم محاسبه کنیم:
temp_30 = 10.1315 * 30 - 1.7945
temp_90 = 10.1315 * 90 - 1.7945
print(temp_30)   # استحکام در دمای 30 درجه میشه 302.1505
print(temp_90)   # استحکام در دمای 90 درجه میشه 910.0405

# 2- میتونیم از تابع y_pred در مدل خودمون استفاده کنیم برای پیشبینی:
pred_30 = model.predict(np.array([30]).reshape(1,-1))
pred_90 = model.predict(np.array([90]).reshape(1,-1))
print('predicted estehkam for 30 degree: ', pred_30)     # [302.15068493]
print('predicted estehkam for 90 degree: ', pred_90)     # [910.04109589]



# حالا میخوایم دماهایی که مدل خودم تست کرده با دماهایی که در واقعیت شرکت آزمایش کرده مقایسه کنیم:
# یک راه اینه که دونه دونه از هم تفریق کنم و میانگین حساب کنم
# واقعیت منهای مدل و از نتیجه قدر مطلق میگیریم و میانگینش رو حساب میکنیم

true_30 =  np.array([310.2322])
true_90 = np.array([908.332123])
# mean(|true-prediction|)
#908-910 = -2 --> abs|| --> 2
#310-302 = 8  --> abs|| --> 8 
# 6 -->  خطای مدل من میشه این
# این یعنی میانگین خطای مدل من به ازای هر ورودی که بدم +-6 تا بالا پایین هست

# به این روش محاسبه خطا میگن Mean Absolute Error یا MAE -> میانگین خطای قدرمطلق
# ما اگر خطا رو تقسیم به خودش کنیم میتونیم درصد خطا رو محاسبه کنیم که بهش میگن Mean absolute percentage error یا MAPE
# یا میتونیم خطا رو به توان 2 برسونیم که بهش میگن mean squared error یا MSE
# یا میتونیم خطا رو به توان 2 برسونیم و میانگین بگیریم و سپس روش رادیکال بگیریم که بهش میگن Root Mean Squared Error یا RMSE


# یک راه دیگه برای سنجش معتبر بودن پیشبینی های مدلمون اینه:
# مثلا ما توی پوشه دیتاهامون اینجا 6 تا دیتا (x) داشتیم
# بجای اینکه مدل رو روی هر 6تا x بیایم fit کنیم و train کنیم میایم مثلا روی 4تا x فقط train میکنیم
# حالا 2 تا پوشه داریم که یکیش 4تا x داره که مدلم روش train شده و یاد گرفته و خط رو پیدا کرده
# 2 تا X توی یک پوشه دیگه دارم، که شرکت هم از قبل در آزمایشگاه اینارو تست کرده و y رو داره
# میام این 2تا x رو میدم به مدل خودم و y رو مقایسه میکنم با y که در آزمایشگاه بدست آمده
# اینطوری بدون اینکه برم پیش رئیس شرکت خودم خطای مدلم رو بررسی میکنم
# در واقع میشه گفت از 6 دیتایی که از آزمایشگاه گرفتیم، نمایم همشو برای train کردن مدل خودمون بسوزونیم
# میایم 4 تاشو برای train میذاریم و 2تاشو برای test میذاریم




#=========================================
'''     steps - train_test_split()     '''
#=========================================

# پس تا اینجای کار ما مراحلمون به اینصورت میشه

# step 0.0 --> cleaning data
# step 0.1 --> x,y تبدیل به
# step 1 --> train, test, split
# در این مرحله میایم از کل دیتاهامون بعضیارو به عنوان تست و بعضی‌هارو به عنوان train استفاده میکنیم     
# این مرحله میشه شروع machine learning     

#__________________________________________________________
# اول از همه کل دیتایی که داریم در یک نگاه اینه:

temperature = [10,20,40,60,80,100]
estehkam = [105 , 197  , 401  , 605 , 809  , 1013]
x  = np.array(temperature).reshape(-1,1)
y = np.array(estehkam)
plt.scatter(x,y)
plt.ylabel('estehkam')
plt.xlabel('temperature')
plt.legend()
plt.show()
#__________________________________________________________



# حالا میخوایم با این روش جدید مدل خودمون رو تست کنیم:

temperature = [10,20,40,60,80,100]
estehkam = [105 , 197  , 401  , 605 , 809  , 1013]

x  = np.array(temperature).reshape(-1,1)
y = np.array(estehkam)

from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2, shuffle=True,random_state= 42)

# train_test_split:
    # test_size --> یعنی چند درصد از دیتاهات رو به عنوان تست بگیرم؟ یک عدد بین 0 تا 1 و معمولا 20 یا 25 درصد میگیرن
    # shuffle --> یعنی از این ترتیبی که الان دیتات داره به اندازه تست سایز از ابتدای دیتات جدا کنم؟ یا اول دیتاهاتو هم بزنم و بعد از اولش بگیرم؟
    # random_state --> این یک عدد ثابت هست که شدت هم زدن دیتاهارو میگه، و زمانیکه یه عدد مشخص براش میذاریم دفعه بعدم که کد اجرا میشه
    # دوباره میره همونایی که دفعه پیش رندوم انتخاب کرد رو انتخاب میکنه نه اینکه بره دوباره رندوم یچیز جدید انتخاب کنه                       
    # اینجوری reproducibility کدهامون حفظ میشه - بصورت توافقی بین producerها عدد 42 رو براش انتخاب کردن                       
    # result --> پس کلی بخوایم تنظیمات این تابع رو بگیم میشه دو تا ورودی بگیر، تست سایز 20 درصد دیتاهامون هست و روی 80 درصد بقیه آموزش ببین، بصورت رندوم و با شدت مشخص دیتاهارو بردار


# x,y -->  x_train , y_train (80%)  |  x_test , y_test (20%)
# این تابع 4 تا خروجی میده و ترتیبش هم مهمه که فقط به همین صورت نوشته بشه
# x_train , x_test , y_train , y_test = train_test_split(x,y, ...)


plt.scatter(x_train,y_train,label='train data',color='blue')
plt.scatter(x_test,y_test,label='test data',color='red')
plt.xlabel('temperature')
plt.ylabel('estehkam')
plt.legend()
plt.show()


print('x_test: ', x_test)    #[[20] [40]]
print('y_test: ', y_test)    #[197 401]

print('x_train: ', x_train)    #[[ 10] [ 80] [ 60] [100]]
print('y_train: ', y_train)    #[ 105  809  605 1013]








#================================================
'''     steps - start of Machine Learning     '''
#================================================

# step 0.0 --> cleaning data
# step 0.1 --> x,y تبدیل به
# step 1 --> train, test, split
# step 2 --> training phase (fit) - model
# step 3 --> evaluation

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# اینجا دیتای خودمون رو با pandas وارد میکنیم ...


#step 0.0 --> data cleaning    1-empty cell  2-type  3-logic  4-duplciated reset_index() .info()....
#step 0.1 --> converting to x,y (np.array)

temperature = [10,20,40,60,80,100]
estehkam = [105 , 197  , 401  , 605 , 809  , 1013]

x  = np.array(temperature).reshape(-1,1)
y = np.array(estehkam)

#step 1 --> train test split --> start of machine learning
from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2, shuffle=True,random_state= 42)


#step 2 --> model 
#Phase training (Fit)
#regression
from sklearn.linear_model import LinearRegression
model = LinearRegression()
#from sklearn.linear_model import SGDRegressor
#model = SGDRegressor(loss='squared_error',max_iter=1000,tol=1e-3,random_state=42)


# قبلا روی کل دیتا train میکردیم، الان فقط روی اون قسمت از دیتاها که در دسته بندی train هستن باید fit کنیم
model.fit(x_train,y_train)  #b raveshe khdoesh (a,b,, loss fucntion minimum ,..)


print('model.coef_: ', model.coef_)
print('model.intercept_: ', model.intercept_)

y_train_pred = model.predict(x_train)

plt.scatter(x_train,y_train,label='train data',color='blue')
plt.plot(x_train,y_train_pred,label='predict data',color='red')
plt.xlabel('temperature')
plt.ylabel('estehkam')
plt.legend()
plt.show()



# Step3 --> evaluation of x_test
# حالا میخوایم اون x_test هارو رسم کنیم ببینیم اونا چی شدن

# فقط به مدل x رو میدیم که prediction کنه
y_test_pred = model.predict(x_test)

# اینجا y_true میشه همون y_test یعنی نتیجه x_test باید با نتیجه آزمایش در آزمایشگاه باید یکی بشه
y_true_test = y_test


# حالا به کمک توابع metrics میایم y_true با y_pred مقایسه میکنیم ببینیم فاصلشون چقد هست و خطای مدل محاسبه میشه
# یعنی میایم ببینیم نتیجه عملیاتی که مدل محاسبه کرده با نتیجه عملیاتی که در آزمایشگاه محاسبه شده چقد باهم فاصله دارن
# از روشهایی مثل MAE , MSE , RMSE , MAPE میشه استفاده کنیم

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score , mean_absolute_percentage_error
# کلا توابع metrics به عنوان ورودی (y_true , y_pred) تا واقعیت رو با انداز گیری مدل مقایسه کنن


mae = mean_absolute_error(y_true_test,y_test_pred)    # میانگین قدرمطلق دونه دونه پیشبینی‌ها منهای واقعیت
mse = mean_squared_error(y_true_test,y_test_pred)     # دونه دونه پیشبینی‌ها - واقعیت| **2 --> میانگین| 
rmse = np.sqrt(mse)    #rooye miangine MSE --> radical migire
mape = mean_absolute_percentage_error(y_true_test,y_test_pred)    # دونه دونه |پیشبینی-واقعیت| تقسیم بر پیشبینی * 100 --> درصد خطا
r2 = r2_score(y_true_test,y_test_pred)    # خودش یه روش آماری هست

print('mae: ', mae)    # 6.312849162011204    یعنی مدل من +-6.31 استحکام رو اشتباه پیشبینی کرد برای اون دوتا نقطه تست
print('mse: ', mse)    # 41.22842607908657
print('rmse: ', rmse)   # 6.420936542209911
print('mape: ', mape)   # 0.025408644681578083   این درصد خطای مدل ما هست که عددش باید بصورت درصد حساب شه 0.02*100=2% که میشه درصد خطای مدل
print('r2: ', r2)      # 0.9960372523953204    عددش بین 0 تا 1 هست و هرچی بالاتر باشه یعنی تونسته بصورت آماری توضیح بده ارورهارو










