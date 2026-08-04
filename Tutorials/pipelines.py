
'''
===============================================================================
===============================================================================
================       Created on Fri Jul 31 17:09:44 2026     ================
================                IDE: Spyder                    ================
================         Author: Khashayar Alipour             ================
================              Statistical models               ================
================                AI Pipelines                   ================
===============================================================================
===============================================================================
'''

# Full Pipelne
# ColumnTransformer




'''
============================
=======   Pipeline   =======
============================
'''


# در پروسه پیشبینی با model، دو مشکل ممکنه پیش بیاد که pipeline حلش کرده
# اول اینکه ممکنه تعداد مراحل برای پردازش دیتا خیلی زیاد بشه و کد شلوغ میشه
# دوم اینکه ممکنه بصورت اشتباهی مدل رو بجای دیتای Train روی دیتای Test هم بیایم fit کنیم
# اینجوری مدل دیتای تست رو هم دیده، درواقع Data Leakage اتفاق افتاده و دیتای تست به مدل نشت کرده

# دانشمندان اومدن گفتن چه کاریه خب، میایم همه مراحل رو میذاریم توی یک pipeline
# مثلا مراحل Encoding، Scaling، Polynomial، Feature Selection و ...
# در کل Pipeline یعنی چند مرحله پردازش داده و مدل را به صورت یک زنجیره پشت سر هم قرار بدیم تا همشون با یک دستور اجرا بشن
# مراحل داخل pipeline به همون ترتیبی اجرا میشن که ما مشخص میکنیم


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import PolynomialFeatures
from sklearn.feature_selection import SelectKBest
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression

# import data
data = pd.read_csv("data.csv")

# x,y
X = data.drop("Purchased", axis=1)
y = data["Purchased"]

# train-test split
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=42 )

# columns
numeric_features = ["Age", "Salary"]
categorical_features = ["City", "Gender"]

# making ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(), categorical_features) ],
        remainder="drop"
)

# making Pipeline
pipe = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("poly", PolynomialFeatures()),
        ("selector", SelectKBest()),
        ("model",LogisticRegression())
    ]
)

# GridSearchCV
param_grid = {
    "poly__degree":[1,2,3],
    "selector__k":[3,5,7],
    "model__alpha":[0.1,1,10]
}

grid = GridSearchCV(
    estimator=pipe,
    param_grid=param_grid,
    cv=5,
    scoring="r2"
)


# Training the model
grid.fit(X_train, y_train)

# best model
best_pipe = grid.best_estimator_    # finds the best pipeline

# best parameters
print(grid.best_params_)

# best score
print(grid.best_score_)

# Prediction
y_pred = pipe.predict(X_test)

# Evaluation
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)



# ما بجای اینکه فقط روی مدل GridSearch بزنیم، روی کل پروسه pipeline میزنیم

#                      Raw Data
#                          ▼
#                   Train / Test Split
#                          ▼
#                  Build Pipeline
#                          ▼
#         ┌──────────────────────────────────────┐
#         │             GridSearchCV             │
#         │                                      │
#         │  degree=1  k=3  alpha=0.1            │
#         │  degree=1  k=3  alpha=1              │
#         │  degree=2  k=5  alpha=1              │
#         │  degree=3  k=7  alpha=10             │
#         │          ...                         │
#         └──────────────────────────────────────┘
#                          ▼
#                  Best Pipeline
#                          ▼
#                    Predict(X_test)
#                          ▼
#                      Evaluation







'''
=====================================
=======   ColumnTransformer   =======
=====================================
'''

# فرض میکنیم دیتای ما اینه:
# | Age | Salary | Gender | City   |
# | --- | ------ | ------ | ------ |
# | 25  | 4000   | Male   | Tehran |

# حالا میخوایم Age و Salary رو scale کنیم و Gender و City رو One-Hot کنیم
# اگر فقط یک pipeline خالی داشته باشیم، میاد کل جدول رو میده به StandardScaler
# در حالیکه مثلا StandardScaler نمیتونه Male رو scale کنه
# یا مثلا اگر به ترتیب، اول One-Hot بذاریم نمیتونه Age رو One-Hot کنه و اشتباه میشه

# مشکل چیست؟ ستون‌های مختلف نیاز به پردازش‌های مختلف دارند
# تعریف: ColumnTransformer یعنی برای هر گروه از ستون‌ها، پردازش متفاوتی تعریف کنیم
# و در انتها دوباره همه به هم وصل میشن

#  Age                  Gender
#  Salary               City
# --------------       --------
# StandardScaler       OneHotEncoder

#                Data
#       ┌──────────┴──────────┐
#       ▼                     ▼
# Numeric Columns      Categorical Columns
#       ▼                     ▼
# StandardScaler      OneHotEncoder
#       └──────────┬──────────┘
#                  ▼
#           Final Dataset



# در نهایت، ColumnTransformer فقط مرحله Preprocessing را انجام می‌دهد
# و همچنین Pipeline کل پروژه را مدیریت می‌کند
# پس معمولاً ColumnTransformer داخل Pipeline قرار می‌گیرد


from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), ["Age", "Salary"]),
        ("cat", OneHotEncoder(), ["City", "Gender"])
    ]
)

# این ستونهارو Scale کن:  Age, Salary
# این ستونهارو One-Hot کن: Gender, City


pipe = Pipeline([
    ("preprocessing", preprocessor),
    ("model", LogisticRegression())
])

pipe.fit(X_train, y_train)
# با اجرای این دستور fit، اول ColumnTransformer توسط pipeline اجرا میشه
# سپس مدل آموزش میبینه

y_pred = pipe.predict(X_test)




#     Raw Data
#       ▼
# ColumnTransformer
#       │
#       ├─────────────┐
#       ▼             ▼
#     Scale          One-Hot
#       └──────┬──────┘
#              ▼
#      PolynomialFeatures
#              ▼
#      Feature Selection
#              ▼
#      Random Forest



























































































































































































