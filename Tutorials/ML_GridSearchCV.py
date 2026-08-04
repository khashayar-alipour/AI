
'''
===============================================================================
===============================================================================
================       Created on Sun Jul 26 22:05:48 2026     ================
================                IDE: Spyder                    ================
================         Author: Khashayar Alipour             ================
================              Statistical models               ================
================                 ML GridSearchCV               ================
===============================================================================
===============================================================================
'''


# Model Tuning --> GridSearch - CrossValidation





'''
=================================================================
=================================================================
=======   Model Tuning - GridSearch - Cross validation  =======
=================================================================
=================================================================
'''


"===== GridSearch ====="

# از کجا بفهمیم بهترین مقدار C یا max_depth یا k یا alpha چیست؟
# برای اینکار از ابزارهای model tuning مثل GridSearchCV استفاده میکنیم

# ما هر مدلی بخوایم انتخاب کنیم، مثلا SVM یا KNN یا RandomForest و ... ، اینا همشون یه سری hyperparametr دارن
# حالا مثلا موقع استفاده از مدل SVC مقدار C رو روی چند بزاریم تا بهترین حالت generalization برای مدل بدست بیاد؟

# یه راهش اینه که بصورت دستی مثلا c رو دونه دونه بزاریم 1 یا 10 یا 100
# بعد واسه هر کدوم بیایم مثلا MAE رو حساب کنیم تا ببینیم کدومش از همه بهتره
# بعد بیایم همون مقدار c رو انتخاب کنیم برای این مدل

# راه دیگش اینه همه hyperparameter هارو بدیم به ابزاری بنام GridSearchCV که بیاد تو دل خودش تمام این حالات رو محاسبه کنه
# این ابزار میاد نه تنها مثلا مقدار c و gamma رو جدا جدا، بلکه بصورت ترکیبی باهم هم محاسبه میکنه

# کارکرد grid search اینجوریه. مثلا میخوایم بهترین مقدار c و gamma رو برای یک مدل پیدا کنیم:
# | C   | gamma | Accuracy |
# | --- | ----- | -------- |
# | 0.1 | 0.01  | 81%      |
# | 0.1 | 0.1   | 84%      |
# | 1   | 0.01  | 89%      |
# | 1   | 0.1   | 93% ✅   |
# | 10  | 0.1   | 91%      |

# طبق محاسبات Grid search بهترین مقادیر برای فلان مدل برای پردازش فلان دیتا c=1 و gamma=0.1 هست
# این مقادیر توی یه مدل و با یک دیتای دیگه ممکنه متفاوت باشه



#=================
"Behind the scene"
#=================

# حالا grid search در دل خودش چطوری مثلا بهترین مقدار برای C رو حساب میکنه؟

x_train, x_test , y_train,y_test = train_test_split(x,y,test_size=0.25,shuffle=True, random_state=42 )

from skelarn.svm import SVR
from sklearn.metrics import mean_absolute_error

# اول میاد یه حلقه میزنه و دونه دونه مقادیر مختلف برای C رو تست میکنه
# و مقدار test_score و train_score رو برای هر کدوم حساب میکنه
# همه این مقادیر رو میریزه توی یک متغیر

gridsearch_results= []

for c_value in [0.0001,0.001,0.01,0.1,1,10]:
    model = SVR(kernel='linear', C= c_value)
    model.fit(x_train,y_train)

    y_pred_train= model.predict(x_train)
    y_pred_test = model.predict(x_test)

    train_score= mean_absolute_error(y_train,y_pred_train)
    test_score = mean_absolute_error(y_test , y_pred_test)

    gridsearch = {'C':c_value , 'train_score' :train_score , 'test_score' : test_score}
    gridsearch_results.append(gridsearch)


# سپس میاد از دل این متغیر، test_score هارو میکشه بیرون و اون C که کمترین test_score رو داره پیدا میکنه

minimum_mae = 10000000000
best_c = None

for results in gridsearch_results:

    test_score = results['test_score']

    if test_score < minimum_mae:
        minimum_mae = test_score
        best_c = results['C']

print(f'the best model in the range of [0.0001 , 10 ] best C is {best_c} with MAE of {minimum_mae}')



#=======================
"grid search in sklearn"
#=======================

from sklearn.svm import SVC
model = SVC()

# اینا مقادیری هست که میخوایم gridSearch برای این hyperparametr ها تست کنه و بهترینش رو انتخاب کنه
param_grid = { "C":[0.1,1,10], "gamma":[0.01,0.1,1], "kernel":["rbf"]   }

from sklearn.model_selection import GridSearchCV
grid = GridSearchCV( estimator=model, param_grid=param_grid, cv=5, scoring="accuracy"  )   #cv=cross validation

grid.fit(X_train,y_train)

# برای گرفتن بهترین hyperparameter ها
print(grid.best_params_)      #{'C':1, 'gamma':0.1, 'kernel':'rbf'}

# برای گرفتن بهترین accuracy
# بهترین امتیاز Cross validation رو میده
print(grid.best_score_)    # 0.94

cv_results = grid.cv_results_
print(cv_results)    # نتیجه تمااام محاسباتش توی یک دیکشنری قابل مشاهده هست

# گرفتن بهترین مدل
# دیگر لازم نیست دوباره مدل بسازی. یعنی نیاز نیست از اول با hyperparametr های جدید بنویسی model=SVC(c=..., gamma=...)
# بلکه خود Gridsearch میاد به کمک این خروجی، بهترین Trained Model رو خودش با بهترین مقادیر hyperparametr بهمون میده
best_model = grid.best_estimator_
y_pred = best_model.predict(X_test)

#           Build Model
#               ▼
#      Define Hyperparameters
#               ▼
#         Create Grid
#               ▼
#      Try Every Combination
#               ▼
#     Cross Validation (CV)
#               ▼
#      Calculate Mean Score
#               ▼
#     Select Best Parameters 🎯
#               ▼
#      Return Best Model


# پارامتر scoring چیه؟
# برای gridSearch باید مشخص کنیم وقتی 2 حالت مختلف رو برای یک مدل محاسبه کرد
# بر اساس چه معیاری بیاد از بین این دوتا انتخاب کنه
# مثلا در Classification اگر بذاریم scoring=accuracy میاد هر مدلی که Accuracy بیشتری داشت انتخاب میکنه
# | Model | Accuracy |
# | ----- | -------- |
# | A     | 91%      |
# | B     | 94% ✅   |
# | C     | 90%      |

scoring = "accuracy"
scoring = "precision"
scoring = "recall"
scoring = "f1"
scoring = "roc_acu"

# حالا مثلا در Regression برای scoring میتونیم از این مقادیر استفاده کنیم:
scoring="neg_mean_squared_error"
scoring="neg_mean_absolute_error"
scoring="neg_root_mean_squared_error"
scoring="r2"



"===== Cross Validation ====="
# ما میومدیم با train-test-split دیتاهای خودمون رو به دو دسته train dataset و test dataset تقسیم میکردیم
# مدل روی train dataset آموزش میدید و روی test dataset بصورت آزمایشی پیشبینی میکرد و میزان Accuracy اندازه گیری میشد
# اینکه در پروسه train-test-split کدوم دیتاها به عنوان test dataset انتخاب بشه بصورت رندوم اتفاق میوفته
# مثلا ما در دیتای temperature=[10,20,30,40,80,100] بصورت رندوم اومدیم test هارو گرفتیم و 80 و 100 درومد (2تای آخر)
# یعنی test dataset ممکنه بصورت رندوم یه دیتای خیلی ساده یا خیلی سخت انتخاب بشه پس در نتیجه Accuracy واقعی نیست
# حالا زمانیکه میخوایم gridSearch بزنیم، بیاد hyperparametr هارو روی این test dataset انجام بده
# و نتیجه gridSearch این بشه که مثلا بهترین مقدار c برابر 0.001 هست
# حالا ما با این اوصاف، میتونیم مطمئن باشیم که این مقداری که برای c توسط gridSearch بدست اومده،
#  بهترین مقدار C برای همممه دیتاهایی جدیدی هست که ممکنه برای prediction به مدل داده بشه؟

# در اینجا از روشی بنام Cross validation یا GridSearchCV استفاده میشه
# میاد به جای اینکه فقط یک بار Train/Test انجام بده چند بار این کار را انجام میده
# مثلا وقتی میگیم cv=5 داده ها به 5 قسمت تقسیم میشه:
    # Fold1
    # Fold2
    # Fold3
    # Fold4
    # Fold5
    
# در مرحله بعد میاد به تعداد Fold ها آموزش رو انجام میده و هر سری یک Fold رو برای test انتخاب میکنه:
    # اینجوری هر sample یکبار test میشه و 4 بار train میشه    
    # Fold1 Fold2 Fold3 Fold4  |||  Fold5=test
    # Fold1 Fold2 Fold3 Fold5  |||  Fold4=test
    # Fold1 Fold2 Fold5 Fold4  |||  Fold3=test
    # Fold1 Fold5 Fold3 Fold4  |||  Fold2=test
    # Fold5 Fold2 Fold3 Fold4  |||  Fold1=test

# حالا هر سری accuracy هارو حساب میکنه:
    # | Fold | Accuracy |
    # | ---- | -------- |
    # | 1    | 94%      |
    # | 2    | 92%      |
    # | 3    | 95%      |
    # | 4    | 93%      |
    # | 5    | 91%      |

# حالا ازشون میانگین میگیره:
    # 94+92+95+93+91​ / 5 = 93%  --> Cross Validation Score
    

#===== sklearn =====
from sklearn.model_selection import cross_val_score
scores = cross_val_score( model, X, y, cv=5 )
print(scores)
# [0.94
# 0.92
# 0.95
# 0.93
# 0.91]
scores.mean()   # 93%



# پس GridSearch در داخل خودش از CrossValidation بهره میبره
# در کل تعریف CV میشه تقسیم داده به چند Fold، آموزش و ارزیابی چندباره برای به‌دست آوردن برآورد قابل اعتمادتر از عملکرد مدل
# با CV میایم چند دور مدل رو آموزش میدیم و هر دیتا حداقل یکبار به عنوان test dataset انتخاب شده
# در نتیجه دیگه مدل روی دیتای خاصی تعصب و bias نداره و Accuracy کاذب نداریم

#                     🤖 Build Model
#                           ▼
#                Define Hyperparameters
#                           ▼
#                  Grid Search starts
#       ┌───────────────────┴───────────────────┐
#       ▼                                       ▼
#  Try Combination #1                    Try Combination #2
# (C=1, γ=0.1)                          (C=10, γ=0.01)
#       ▼                                       ▼
#    5-Fold CV                              5-Fold CV
#       ▼                                       ▼
#  Average Score                         Average Score
#       └──────────────┬────────────────────────┘
#                      ▼
#             🎯 Select Best Combination
#                      ▼
#             `best_estimator_`
#                      ▼
#            Predict on New Data

















































