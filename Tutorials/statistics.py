
"""
           =============================================================================
           =============================================================================
           =============        Created on Fri Jun 19 20:58:52 2026        =============
           =============        Author: Khashayar Alipour                  =============
           =============        Subject: AI Statistics                     =============
           =============================================================================
           =============================================================================
"""


# Study of data
# به ما کمک میکنه دیتاهارو آنالیز و درک کنیم


# ما در کل 2 نوع آمار داریم:
    # 1- Descriptive statitics (amare tosifi) - summarize data (min , max , count , mode , median , standard deviation)
    # 2- Inferential statistics (amare estenbati) - making prediction from data 



#   ============================================================
#   ============================================================
#   ==========     Generating Data, Data analysis     ==========
#   ============================================================
#   ============================================================

# در ادامه یه سری دیتا میسازیم، از نظر آمار توصیفی بررسیشون میکنیم و نمودارشون رو رسم میکنیم


import numpy as np
import pandas as pd
import scipy.stats as stats

a = np.arange(1,401)  # 1 to 400
b = a.reshape(100,4)  # az a ye matrix besaz 100 ta radif dashte bashe 4 ta soton
b[0:4,:]   # az radife 0 ta 4, hame soton ha, ro neshun bede

'''
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12],
       [13, 14, 15, 16]])
'''


data = pd.DataFrame(b,columns=['feshar','dama','time','estehkam'])
data.columns    # Index(['feshar', 'dama', 'time', 'estehkam'], dtype='object')

data.head()
'''
   feshar  dama  time  estehkam
0       1     2     3         4
1       5     6     7         8
2       9    10    11        12
3      13    14    15        16
4      17    18    19        20
'''


data.tail()
'''
    feshar  dama  time  estehkam
95     381   382   383       384
96     385   386   387       388
97     389   390   391       392
98     393   394   395       396
99     397   398   399       400
'''

data.describe()
'''
           feshar        dama        time    estehkam
count  100.000000  100.000000  100.000000  100.000000
mean   199.000000  200.000000  201.000000  202.000000
std    116.045968  116.045968  116.045968  116.045968
min      1.000000    2.000000    3.000000    4.000000
25%    100.000000  101.000000  102.000000  103.000000
50%    199.000000  200.000000  201.000000  202.000000
75%    298.000000  299.000000  300.000000  301.000000
max    397.000000  398.000000  399.000000  400.000000
'''

np.mean(data)   # 200.5   میانگین در کل دیتا
np.mean(data['feshar'])    # 199.0   میانگین در ستون فشار

#[1 , 4 , 5 , 6 , 7]  --> median=5
np.median(data['feshar'])     # 199.0   مدیان یعنی عدد وسط

stats.mode(data['feshar'])   #ModeResult(mode=1, count=1)   مد میشه عددی که بیشترین تکرار رو داره

#range
max(data['feshar'])  # 397
min(data['feshar'])  # 1
data_range = max(data['feshar']) - min(data['feshar'])
print(data_range)  # 396


# variance , standard deviation  -> یعنی پراکندگی دیتاهای ما از میانگین به چه صورت هست
# range = az 1 ta 397
# mean  = 199
# Variance = Standard deviation **2
# Standard deviation -> جهت سهولت در محاسبات انسانی استفاده میشه
variance_value = np.var(data['feshar'], ddof=1)   # 13466.666666666666   این یعنی پراکندگی دیتا از میانگین خیلی زیاده و دیتا متمرکز نیست
np.std(data['feshar'],ddof=1)    # 116.04596790352807

generated_good_focused_data = np.random.normal(199,5,(100,))
np.var(generated_good_focused_data,ddof=1)   # 25.646069656108594    یعنی پراکندگی از میانگین کم هست و دیتای ما متمرکز هست

import matplotlib.pyplot as plt
plt.hist(data['feshar'],bins=100 , color='blue')
plt.title('histogram of dsata')
plt.xlabel('values')
plt.ylabel('frequency')
plt.show()

import matplotlib.pyplot as plt
plt.hist(generated_good_focused_data,bins=100 , color='blue')
plt.title('histogram of dsata')
plt.xlabel('values')
plt.ylabel('frequency')
plt.show()





#   ============================================================
#   ============================================================
#   ==========        Probability - احتمالات          ==========
#   ============================================================
#   ============================================================

# در کل مفاهیم این مبحث بررسی میکنن که چقدر احتمال داره یک رویداد اتفاق بیوفته
# این احتمال از 0 (غیرممکن) تا 1 (قطعی) وجود داره

# ===============
# چند تعریف:
    # Experiment --> انداختن تاس
    # sample space (s) --> all possible outcomes {1,2,3,4,5,6}
    # event (e) -->  مسئله‌ای که مدنظر ما هست و انتظار داریم اتفاق بیوفته
    # probability of event --> P(e) - چقد احتمال داره که یک رویداد اتفاق بیوفته
    # P(e) : Favorable outcomes / all events


# ===============
# distributions- انواع توزیع آماری در دیتاها:
    # توزیع یعنی تکرار (frequency) یک داده در بین بقیه داده‌ها چقد هست؟    
    
    #=== 1-Uniform distribution
    # دیتاها در این نوع توزیع هر کدوم تعداد یکسانی دارن        
    # اگه از بین این دیتاها هر کدوم رو بخوای رندوم انتخاب کنی احتمال انتخاب شدن هر دیتا برابر 1 هست        
# مثلا عددی که از انداختن تاس بدست میاد یک توزیع یونیفرم دارم        
# یعنی اگه از 1 تا 6 ما تاس بندازیم، احتمال اینکه هر عدد بیاد باهم برابره        
# اگه مثلا 10000 بار تاس بندازیم، تعداد دفعاتی که 1 میاد تقریبا با تعداد دفعاتی که بقیه اعداد میاد توی یک range مشخص هست        

data = np.random.uniform(1,6,size=(10000,))
plt.hist(data,bins=6)
plt.title('uniform distributions')
plt.xlabel('data')
plt.ylabel('frequency (probability)')
plt.show()

    #=== 2-Normal (gaussian) distribution
    # احتمال اتفاق افتادن این نوع توزیع در رویدادهای طبیعی محتمل تر هست        
# مثلا در یک جامعه میانگین قد 175 هست و بقیه افراد حول این عدد پراکنده شده‌اند        
# مثلا حدود 50% جامعه قد حدود 175 دارن، ولی این وسط کسایی هستند که مثلا ممکنه قد 190 یا 140 داشته باشن        
# نمودار این نوع توزیع بصورت زنگوله‌ای (bell shape) هست        
# این نوع توزیع از همه مهمتره به چند دلیل:        
    # 1- در طبیعت اکثر دیتاها توزیع نرمال دارن            
    # 2-بعضی تستهای آماری مهم ( Z-test, t-test , Anova) فقط روی دیتاهای نرمال جواب میده            
    # 3-در بحث ماشین لرنینگ، آنالیز آماری روی دیتاهای نرمال فقط انجام میشه            

mu = 175  #miangin
sigma = 15 
normal_data = np.random.normal(mu,sigma,10000)
plt.hist(normal_data,bins=30)
plt.title('normal distribution')
plt.xlabel('value')
plt.ylabel('density')
plt.show()

    #=== 3-Binominal distribution
    # برای رویدادهای که دوحالت بیشتر نداره، یا میشه یا نمیشه        
    # نمودار این نوع توزیع هم بصورت زنگوله هست        

n, p = 10, 0.5    # 10 trials, 50% success chance
binom_data = np.random.binomial(n, p, 1000)
plt.hist(binom_data, bins=10, edgecolor='black', density=True)
plt.title("Binomial Distribution (n=10, p=0.5)")
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.show()

    #=== 4-Poisson distribution
    # برای رویدادهای خیلی نادر کاربرد داره. مثلا پیشبینی زلزله و ...        
    
lambda_ = 2   #Average 2 events per time period
poisson_data = np.random.poisson(lambda_, 10000)
plt.hist(poisson_data, bins=15, edgecolor='black', density=True)
plt.title("Poisson Distribution (λ=3)")
plt.xlabel("Number of Events")
plt.ylabel("Probability")
plt.show()








#   ============================================================
#   ============================================================
#   ==========           Normality test               ==========
#   ============================================================
#   ============================================================

# تست هایی برای اینکه بفهمیم توزیع یک دیتا نرمال هست یا نه



'''     ___________
       | 1-visual |
       -----------
'''           
# در این روش با نگاه کردن به نمودار متوجه بشیم دیتا نرماله


import numpy as np
import matplotlib.pyplot as plt

# Generate normal data
data = np.random.normal(50, 10, 1000)

# Plot histogram
# نمودار هیستوگرام باید زنگوله ای باشه
plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.title("Histogram of Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


#Box Plot
# در نمودار جعبه‌ای شکل نمودار باید متقارن (symetric) باشه
# یعنی خط میانگین در وسط جعبه باشه
plt.boxplot(data, vert=False)
plt.title("Box Plot")
plt.show()


#Q-Q plot
# در این نمودار اگر منحنی theoretical quantiles بر منحنی ordered values (مقادیر خودمون) منطبق باشه نرماله
import scipy.stats as stats
import matplotlib.pyplot as plt
stats.probplot(data, dist="norm", plot=plt)
plt.title("Q-Q Plot")
plt.show()


#KDE plot
# اینجا هم شکل نمودار باید bell-shape باشه
import seaborn as sns
sns.kdeplot(data, shade=True, color="blue")
plt.title("KDE Plot")
plt.show()




'''     ______________________
       | 2-Shapiro-wilk test |
       ----------------------
'''  

from scipy.stats import shapiro
data = np.random.normal(50, 10, 1000)

stat, p = shapiro(data)
print(f"Shapiro-Wilk Test: Statistic={stat}, p-value={p}")


# ازونجایی که این تست برای سنجش این هست که دیتا نرمال هست یا نه؟
# پس فرض 0 در این تست میشه اینکه این دیتا نرمال هست یا نه
'''
H0 : data is normal
H1 : data is not normal
        
--> shapiro_state (T,Z,...) --> p 

p<0.05 --> reject H0 --> reject normal --> data is not normal
p>0.05 --> fail to reject H0 --> data is normal
'''


# p_value = 0.7820693254710884
# p_value > 0.05 ? --> Fail to reject H0 --> failed to reject normality of data
# بر اساس اعدادی که در نتیجه بدست اومد، میتونیم بپذیریم که این دیتا نرمال هست


# مثال دوم
data2 = np.random.uniform(1, 100, 1000)

from scipy.stats import shapiro
state , p_value = shapiro(data2)

print(p_value)    # 8.214666204034599e-16   این عدد یعنی 8 ضرب در 10 به توان منفی 16
#8 * 10*-16

#if p_value <0.05 --> reject H0 (normality data) --> data is not normal
#if p_value >0.05 --> failed to reject --> data is normal

if p_value<0.05:
    print('normal nist')   # normal nist
else:
    print('normal hast')






'''     __________________________
       | 3-anderson darling test |
       --------------------------
'''  
from scipy.stats import anderson

# این anderson یک فانکشن بنام Result بهمون میده:
result = anderson(data)
print(f"Anderson-Darling Test Statistic: {result.statistic}")
#Anderson-Darling Test Statistic: 0.2524234094341864


for i in range(len(result.critical_values)):
    sig_level = result.significance_level[i]
    crit_val = result.critical_values[i]    # p_value
    if result.statistic < crit_val:
        print(f"Accept normality at {sig_level}% level")
    else:
        print(f"Reject normality at {sig_level}% level")


# این تست نرمالیتی دیتا رو در چند لول بررسی میکنه
'''
Accept normality at 15.0% level
Accept normality at 10.0% level
Accept normality at 5.0% level
Accept normality at 2.5% level
Accept normality at 1.0% level
'''

# مثال دوم
from scipy.stats import anderson

result = anderson(data2)
print(f"Anderson-Darling Test Statistic: {result.statistic}")
# Anderson-Darling Test Statistic: 0.2524234094341864


for i in range(len(result.critical_values)):
    sig_level = result.significance_level[i]
    crit_val = result.critical_values[i] #p_value
    if result.statistic < crit_val:
        print(f"Accept normality at {sig_level}% level")
    else:
        print(f"Reject normality at {sig_level}% level")

'''
Anderson-Darling Test Statistic: 9.781214910060385
Reject normality at 15.0% level
Reject normality at 10.0% level
Reject normality at 5.0% level
Reject normality at 2.5% level
Reject normality at 1.0% level
'''









#   ============================================================
#   ============================================================
#   ===      WHAT CAN WE DO IF DATA IS NOT NORMALL????      ====
#   ============================================================
#   ============================================================

# کلا حالت پیش‌فرض برای دیتاها در ماشین لرنینگ روی مال بودن دیتاهاست
# اگر دیتایی با تست‌ها مشخص شد نرمال نیست باید normalize بشه

# یکی از ساده ترین راهها برای نرمال کردن دیتاها استفاده از lognormal یا ریشه دوم هست
# یعنی یا لگاریتم دیتاهارو میگیریم، یا suqare root (ریشه دوم) دیتاهارو میگیریم
# سپس روی اونها بجای دیتای اصلی normality test انجام میدیم و اگر اونها نرمال بودن، بجای دیتای اصلی با همونا کار میکنیم


# -------- 1-To log ---> Lognormal --------
import numpy as np
data_log = np.log(data)   # Apply log transformation
# data_log


# -------- 2-Square Root Transformation --------
data_sqrt = np.sqrt(data)
# Test normality --> instead of data we use data_sqrt or data_log


# -------- 3-Yeo-Johnson Transformation --------
from sklearn.preprocessing import PowerTransformer
pt = PowerTransformer(method='yeo-johnson')
data_yeo = pt.fit_transform(data.reshape(-1, 1))







#   ============================================================
#   ============================================================
#   ============   Applied Statistics - آمار کاربردی    =======
#   ============================================================
#   ============================================================

# نکاتی درمورد آمارِ کاربردی (practical) و انواع تست آماری در مبحث quality control


# ما تستهای آماری زیادی برای سنجش کیفیت داریم. مثلا:
'''
Z-test , T-test , F-test , one-smaple Z-test , two-sample z-test , one-sample  t -test
anderson-darling test, Bartlett’s Test c, Welch’s t-test ...
'''


''' ------Hypothesis Testing------ '''
# تست فرض آماری
# محاسبات ریاضی که پشت این تستها هست بسیار پیچیده و طولانیه
# ولی منطق اصلی که پشت همه این تستها هست بهش میگن "تست فرضیه"

# در این تست میایم در یک مسئله که میخوایم حالات مختلفش رو بسنجیم، یک فرض باطل رو به عنوان مبنا درنظر میگیریم
# به این فرض میگن H0
# در کنارش یک فرضیه دیگه هم داریم که مخالف H0 هست که بهش میگن H1
    # H0 : Null hypothesis : No effect / No diffeerence
    # H1` : Alternative hypothesis : There is effect/difference

# مثلا میخوایم مسئله میانگین سنی رو در یک گروهی بسنجیم
# فرض اینه که در این گروه میانگین سنی 27 هست. پس:
    # H0 : Mean_group = 27
    # H1 : Mean_group != 27

# یا مثلا در دو گروه گروه میانگین قدی رو میخوایم بررسی کنیم.
# فرض اولیه اینه که میانگین قدی توی گروه A از گروه B بیشتره. پس:
    # H0 : Mean_A_height < Mean_B_height
    # H1 : Mean_A_height > Mean_B_height
   

# تستهای آماری داخلش یه سری محاسبات انجام میشه مثلا با استفاده از ریاضی و احتمال و ...
# در نهایت هر تست یک یک خروجی (criteria) داره مثلا T-test خروجی T داره یا Z-test خروجی Z داره و ...
# مهم اینه که در نهایت همه اینها تبدیل به چیزی به اسم P تبدیل میشن


# همچنین یک حد داریم به اسم aplha
# میزان این حد میتونه 5% (0.05) باشه، میتونه 10% (0.10) باشه، میتونه 15% (0.15) باشه
# اینکه مقدار حد چقد باشه رو میتونه شرکت یا یک استاد یا حتی خودمون تعیین کنیم
# ولی مقدار استاندارد جهانیش رو 0.05 درنظر میگیرن که بهش میگن حد آستانه


# حالا چطوری فرض هارو با این تست‌ها میسنجیم؟
# بعد از انجام تست و بدست آوردن P میایم اون رو با alpha (اینجا مقدارش رو 0.05 میذاریم) مقایسه میکنیم
# در نتیجه 2 حالت داریم: یا H0 رو میپذیریم (فقط میپذیریم نه اینکه تاییدش کنیم) یا H0 رو رد میکنیم
    # P < 0.05 --> Null hypothesis (H0) will be rejected
    # P > 0.05 --> Failed to reject null hypothesis (H0)



# در ادامه چنتا ازین تستهای آماری رو بررسی میکنیم

# اگر بخوایم درمورد میانگین یک یا دو گروه فرضی رو بررسی کنی از z test یا t test استفاده میشه
# اگر یک نمونه یا دیتا داشته باشیم:
    # 1 sample Z test , 1 sample t test
# اگر دو نمونه یا دیتا داشته باشیم:
    # 2 sample z test , 2 sample t test

# زمانی از Z-test استفاده میشه که دیتاها حداقل بیشتر از 30 باشه و standard deviation رو بدونیم
# ولی اگه دیتا کمتر از 30 باشه یا standard deviation نامعلوم باشه از T-test استفاده میشه



#=========================================
'''        1- One sample Z test       '''
#=========================================

# یک گروه داریم و میانگین سنی رو میخوایم بررسی کنیم
# پس یک sample از یه سری افراد داخل این گروه (population) که سن این افراد رو نشون میده میگیریم
# یعنی اگه مثلا گروه 50 نفر باشه یک sample مثلا 8 نفره میگیریم

# Sample: نمونه ای که ما گرفتیم
# Population: کل جمعیتی که داریم

# Hypothesis :
    # H0 Null hypothtesis --> group_mean_age = 26
    # H1 Alternative hypothesis --> group_mean_age != 26


# برای انجام این تست یک سری پیش‌فرض ها باید رعایت بشه:
    # Normality: The population follows a normal distribution.   دیتا باید توزیع نرمال داشته باشه
    # Independence: Observations must be independent.   دیتاها باهم ارتباطی نداشته باشن
    # Known Population Variance    واریانس رو بدونیم
    # Random Sampling: The sample must be randomly selected.   نمونه گیری بصورت تصادفی انجام شده باشه
    # Sample >= 30    تعداد نمونه ها حداقل 30 تا باشه



from statsmodels.stats.weightstats import ztest

sample_data = [23 , 27 , 30 , 35 , 46 , 16 , 22 , 30 ]
hypothesis_population_mean = 26

z_stat, p_value = ztest(sample_data, value=hypothesis_population_mean)
# z_stat --> criteria dakheli ke khode test pas az mohasebate riazi pichide hesab mikoni
# p_value --> in baraye ma mohem hast

print(p_value)   # 0.41624721334861114    بیشتر از مقدار آلفا هست

alpha = 0.05

if p<alpha:
    print('null hypothesis is rejected')
else:
    print('fail to reject null  hypothesis')


# ما یک نمونه 8 نفره از کل گروه گرفتیم و بر اساس سن این 8 نفر راجع به کل گروه نظر دادیم
# نظرمون (H0) این بود که این گروه میانگین سنی شون 26 میشه
# طبق محاسبات این تست، P از alpha بزرگتر بود و در نتیجه این فرض نمیتونه رد بشه
# این به این معنی هست که فرضیه ما نسبت به این جامعه آماری که ما داریم، شدنی هست





#=========================================
'''        2- Two sample Z test       '''
#=========================================

# دوتا کلاس 500 نفره داریم میخوایم نمونه بگیریم و قدهاشون رو اندازه بگیریم
# ازین دو جامعه 500 نفری از هر کلاس 30 تا sample میگیریم
# یه کلاس میانگین قدش شده 170، یکی دیگه شده 174
# میخوایم بررسی کنیم که آیا این دو کلاس میانگین قدی برابر داره یا نه

'''
 class A     class B
500 nafar   500 nafar --> population
  30 nfr     30 nfr   --> sample
  170        174      --> height mean

H0 null hypothesis : mean_group_A = mean_group_B
h1 altenrative hypothesis :mean_group_A != mean_group_B 
'''

sample1 = np.random.normal(170, 5, 30)
sample2 = np.random.normal(174, 5, 30)

z_stat, p_value = ztest(sample1, sample2)
print(z_stat)    # -3.2879442325938664
print(p_value)    # 0.0010092182860184493

alpha = 0.05
if p_value<alpha:
    print('null hypothesis is rejected')
else:
    print('fail to reject null  hypothesis')
    

# با توجه به نتیجه تست، به این نتیجه رسیدیم که null hypothesis رد شده
# و میانگین قدی این دو گروه برابر نیست
# ما بر اساس 2 نمونه، راجع به کل جمعیت نظر دادیم که به این میگن استنباط (Inference)




#=========================================
'''        3- one sample T test       '''
#=========================================

#                            ____  data < 30
# When to use this test?  --|____  unknown standard deviation

from scipy.stats import ttest_1samp
sample = [22, 23, 19, 21, 25, 30, 24, 22, 27, 26]
t_stat, p_value = ttest_1samp(sample, 24)
print(t_stat)    # -0.09842680723871938
print(p_value)     # 0.9237507005577772





#=========================================
'''        4- Two sample T test       '''
#=========================================
from scipy.stats import ttest_ind

group1 = np.random.normal(50, 10, 20)
group2 = np.random.normal(55, 10, 20)

t_stat, p_value = ttest_ind(group1, group2)
print(t_stat)   # -0.405853612224562
print(p_value)    # 0.687126513753912





#============================================================
# تا الان با تست های بالا میانگین دو جامعه رو مقایسه میکردیم
# از الان به بعد پراکندگیشونو مقایسه میکنیم
#============================================================




#==================================================
'''        5- F test (variance comaprison)     '''
#==================================================

# در این تست پراکندگی نمونه بررسی میشه
# پیش‌فرض در این تست اینه که دیتا نرمال هست
# یعنی اگه دیتا نرمال نباشه این تست جوابش غلط میشه

# میخوایم بررسی کنیم واریانس نمونه1 با نمونه 2 برابره
'''
Sample1 , sample2 

H0 ---> Var1 = Var2
H1 --> Var1 != Var2
'''

# این تست یک Criteria بنام F میده که در نتیجه محاسبات پیچیده بدست میاد
# یک P_value هم میده که فقط همین P برامون مهمه
'''
F = sigma1**2 / sigma2**2 ....
F --> P_value

if p_value < 0.05 --> reject null -> variances are different
'''

from scipy.stats import f

group1 = np.random.normal(50, 10, 20)
group2 = np.random.normal(55, 10, 20)

var1 = np.var(group1,ddof=1)
var2 = np.var(group2,ddof=1)

F_stat = var1 / var2
p_value = 1 - f.cdf(F_stat, len(group1)-1, len(group2)-1)

print(F_stat)   # 1.4953974780815125
print(p_value)   # 0.19415667914948775

'''
p _value > 0.05 --> reject null  --> varianc deha barabaran
'''




#=============================================
'''     6-  Eqaulity of variances Test    '''
#=============================================
# اسم این تست هست: Levene’s Test (Less sensitive to non-normality)

'''
H0 --> V1 = V2
H1 --> V1 !=V2

P < 0.05 --> rejct null  (V1!=V2)
P > 0.05 --> failed to reject H0
'''


from scipy.stats import levene

group1 = np.random.normal(50, 10, 100)  # Mean=50, Std=10, n=100
group2 = np.random.normal(55, 15, 100)  # Mean=55, Std=15, n=100

stat, p_value = levene(group1, group2)
print(f"Levene’s Test: Statistic={stat}, P-Value={p_value}")
# Levene’s Test: Statistic=17.795925732339168, 
# P-Value=3.7410815898496045e-0

alpha = 0.05
if p_value<alpha:
    print('variance barabar nist')   # variance barabar nist
else:
    print('variance barabar hast')





#=========================================
'''     7-  Non parametric Test   '''
#=========================================

# مثالهایی از انواع این تست:

    # Z test 1 sample, 2 sample
    # T test 1 smaple , 2 sample
    # F test ,... 

# Assume we have normal data!

# If we dont have normal data we must go for non-parametric tests:
    #Bartlett’s Test
    #Welch’s t-test 
    #non-parametric test (Wilcoxon signed-rank test) --> Z test if data is not normal
    #non-parametric test (Mann-Whitney U test) --> 2 sample z test non parametric
    #1 sample t test normal nabashe-> (Wilcoxon signed-rank test)
    #2 sample test nromal nabashe --> Use Mann-Whitney U test or Permutation test






#=========================================
'''    8-  Correlation test    '''
#=========================================

# خیلی وقتها برامون مهمه که ارتباط یا correlation بین دو فاکتور بررسی بشه

# برای بررسی correlation باید چند پیش فرض اول بررسی بشن:
    # Linearity: The relationship must be linear (Check using a scatter plot).
    # Normality: Both variables should be normally distributed (Check using Shapiro-Wilk test).
    # Homoscedasticity: The variance of  Y should be similar across all X values (Check using Levene’s test).
    # Independence: Observations must be independent of each other.


import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Generate data
np.random.seed(42)
x = np.random.normal(50, 10, 100)  # Normally distributed X
y = 2*x + np.random.normal(0, 5, 100)  # Linear relationship with noise


#------linearity    بررسی خطی بودن
# اگر باهم رابطه داشته باشن، نمودار scatter محور x و y روی هم میوفتن
plt.scatter(x, y)
plt.title("Scatter Plot (Check Linearity)")
plt.show()


#------normality    بررسی نرمال بودن دیتا
from scipy.stats import shapiro

shapiro(x).pvalue   # 0.6551676754215167 > 0.05 --> Fail to reject H0 --> x is normal
shapiro(y).pvalue   # 0.9501836786075823 > 0.05 --> Fail to reject H0 --> y is normal


#------Homoscedasticity    بررسی واریانس
residuals = y - (2*x)
print("Levene’s test for Homoscedasticity:", stats.levene(x, residuals).pvalue)
# P-value = 1.3084338260012296e-07




# پس از بررسی موارد بالا حالا میریم correlation بررسی کنیم
# برای بررسی correlation از تست خطی pearson استفاده میکنیم

'''
H0 : no relationship between two variable [there is no correlation]
H1 : there is a correlation
'''

r, p_value = stats.pearsonr(x, y)
print(f"Pearson correlation: {r}, p-value: {p_value}")
# Pearson correlation: 0.9654943669720487, p-value: 4.538186359602331e-59

if p_value <0.05:
    print('reject null hypothesis')
    print('there is correlation')
else:
    print('no correlation')

# P_value < 0.05 --> there is correlation between x and y


# این تست pearson یک criteria بنام r میده
# که یک عدد بین +1 و -1 هست و اصلا - یا + بودنش هیچ معنی نداره
# هرچی به قدرمطلق 1 نزدیکتر باشه یعنی correlation قوی تره
# هرچی به 0 نزدیکتر باشه یعنی correlation ضعیف تره
# در این مثال مقدار r بدست اومده 0.9654943669720487 که خیلی به 1 نزدیکه



# یک مثال واقعی از محاسبه pearson
# در دیتاهایی که چندین ستون داریم به اینصورت correlation ستونها باهم مقایسه میشه

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame(np.random.rand(100, 5), columns=[f'Var{i+1}' for i in range(5)])

# Compute Pearson correlation matrix
corr_matrix = data.corr(method='pearson')

# Print correlation matrix
print(corr_matrix)

'''
          Var1      Var2      Var3      Var4      Var5
Var1  1.000000 -0.186608  0.207927 -0.095359 -0.011769
Var2 -0.186608  1.000000  0.013542  0.137047 -0.091873
Var3  0.207927  0.013542  1.000000  0.006958  0.018743
Var4 -0.095359  0.137047  0.006958  1.000000 -0.067341
Var5 -0.011769 -0.091873  0.018743 -0.067341  1.000000
'''

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.colormaps()
plt.title("Pearson Correlation Heatmap")
plt.show()



#--pearson -> Linear y = x**2 --> corrrelation 
#y = 2*x  , 3*x x ,....

spearman_corr = data.corr(method='spearman')

plt.figure(figsize=(10, 8))
sns.heatmap(spearman_corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Spearman Correlation Heatmap (Non-Linear)")
plt.show()



#----Pairwise Scatter Plots (Non-Linear Check)----
sns.pairplot(data)
plt.show()









#=========================================
'''    9 - Analaysis of Variance    '''
#=========================================

# در تست های قبلی نهایت تا 2 گروه رو میتونستیم باهمدیگه مقایسه کنیم
# اگه بیشتر از 2 گروه باشن چیکار کنیم؟؟؟

# مثلا میخوایم میانگین وزرن در 3 گروه رو باهم مقایسه کنیم
# در این حالت باید واریانس هاشون رو باهم مقایسه کنیم

# Analysis of Varance -->  ANOVA one-way
    # H0 Null hypothesis : mu1 = mu2 = mu3    (mu = mean)
    # h1 alternative : mu1!= mu2!= mu3!=   (at leas on of them is not equal with others)

# این ANOVA میاد یک stat بنام F حساب میکنه که میشه واریانس بین گروه‌ها تقسیم بر واریانس داخل گروه‌ها:
    # F = Variance betweeen groups / Variance within group
    
    # بعد از محاسبه F دو حالت پیش میاد:
        # مقدار F خیلی بالا هست --> فاصله بین گروه‌ها خیلی زیاده --> میانگین برابر نیست --> P_value < 0.05 --> رد کردن H0    
# مقدار F خیلی کوچیک باشه --> میانگین گروه‌ها روی هم همپوشانی دارن --> P_value < 0.05 --> نمیشه H0 رو رد کرد --> یعنی میانگین‌ها برابره    

# پس منطق پشت تست ANOVA روی همین مقدار F هست
# این تست برای مقایسه 1 میانگین بین بیشتر از 2 گروه کاربرد داره

# حالا برای انجام شدن این تست یه سری پیش‌فرض ها وجود داره:
    # 1- دیتای تمام گروه‌ها باید نرمال باشه --> shapiro    
    # 2- همگن بودن واریانس --> levene    
    # 3- استقلال داده‌ها --> pearson    


#-----One-Way ANOVA------
# مثال اول

'''
H0 --> Vazne har 3 goroh barbare mu1=mu2=mu3
H1 --> Mu!=mu2!=mu3
'''

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Generate random data for 3 groups
np.random.seed(42)
group1 = np.random.normal(50, 10, 30)   # میانگین وزن این گروه 50 
group2 = np.random.normal(55, 10, 30)   # میانگین وزن این گروه 55
group3 = np.random.normal(60, 10, 30)   # میانگین وزن این گروه 60


# ---------------------------------------------
# نمودار جعبه‌ای برای مثال بالا برای درک بهتر
df = pd.DataFrame({
    "value": np.concatenate([group1, group2, group3]),
    "group": ["G1"]*30 + ["G2"]*30 + ["G3"]*30  })

sns.boxplot(data=df, x="group", y="value")
plt.show()
# ---------------------------------------------


import scipy.stats as stats

f_stat , p_value = stats.f_oneway(group1,group2,group3)

print(f"F-statistic: {f_stat:.3f}")    # 12.210
print(f"P-value: {p_value:.3f}")    # 0.000

# با توجه به نتیجه تست، مقدار F از 0.05 بیشتره و میشه 2 جور استنباط یا inference کرد:
    # 1- میانگین وزنی 3 گروه برابر نیست (رد کردن H0 که میگفت میانگین وزنی همه برابره)    
    # 2- این 3 گروه متفاوت هستن، عامل یا فاکتور وزن باعث تفاوت این 3 گروه هست    





'''    _______________
      | 2-way ANOVA  |
      ===============
'''   
# مثلا ما سه گروه گیاه داریم، با one-way فقط میتونیم بفهمیم که رشد این 3 گیاه برابر هست یا نه
# ولی نمیتونیم بفهمیم بخاطر کودشون هست یا بخاطر نوع نوردهی هست یا ...
# یعنی در این حالت 3 گروه داریم و میخوایم 2 فاکتور رو بررسی کنیم
# با استفاده از two-way بررسی میکنیم که تاثیر کدوم فاکتور هست

import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns

import matplotlib.pyplot as plt

# Sample Data
np.random.seed(42)
df = pd.DataFrame({
    'Fertilizer': np.repeat(['Organic', 'Chemical'], 15),
    'Sunlight': np.tile(['Low', 'Medium', 'High'], 10),
    'Growth': np.random.normal(20, 5, 30) + 
              (np.repeat([2, 5], 15)) +  # Fertilizer effect
              (np.tile([1, 3, 6], 10))   # Sunlight effect
})


df.head()
'''
  Fertilizer Sunlight     Growth
0    Organic      Low  25.483571
1    Organic   Medium  24.308678
2    Organic     High  31.238443
3    Organic      Low  30.615149
4    Organic   Medium  23.829233
'''


from statsmodels.formula.api import ols
import statsmodels.api as sm
model = ols('Growth ~ C(Fertilizer) + C(Sunlight) + C(Fertilizer):C(Sunlight)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

# Show ANOVA Table
print(anova_table)


'''
                               sum_sq    df         F    PR(>F)
C(Fertilizer)                7.727385   1.0  0.453412  0.507152
C(Sunlight)                 70.483107   2.0  2.067833  0.148405
C(Fertilizer):C(Sunlight)   73.283022   2.0  2.149977  0.138390
Residual                   409.025866  24.0       NaN       NaN
'''

# بررسی جدول:
# اولین فاکتور Fertilizer هست که میریم P رو بررسی میکنیم (0.507) و میبینیم که از 0.05 بیشتره
# پس نمیتونیم null رو رد کنیم (null میگفت میانگین رشد برای این 3 گروه مختلف کود برابر هست)
# پس در نتیجه mu1=mu2=mu3 و میتونیم بگیم که فاکتور کود تاثیری در رشد نداره

# حالا در بررسی فاکتور sunlight میبینیم که P که مقدارش 0.14 هست از 0.05 بیشتره
# پس با شواهد آماری که داریم نمیتونیم فرض متفاوت بودن را رد کنیم
# پس در نتیجه فاکتور نور تاثیری در رشد ندارد

# اختلافات مشاهده شده بین نمونه‌ها از نظر آماری معنادار یا significant نیست

# در بررسی جفت فاکتورها بصورت همزمان (C(Fertilizer):C(Sunlight)) هم میبینیم که P مقدارش که 0.13 هست از 0.05 بیشتره
# پس interaction بین کود و نوردهی هم در رشد تاثیری نداره


 



#=========================================
'''           10 - Regression          '''
#=========================================





























