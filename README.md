# AI Engineering Tutorial

**Author:** Khashayar Alipour

**Credit:** [Ali Pilehvar Meibody](https://github.com/APMaii) 

**License:** MIT

**Year:** 2026


<p align="center">
  <img src="Pictures/AI.png" alt="AI Engineering" width="400"/>
</p>


---

## Introduction

This repo contains Tutorial files for professional AI Engineering: numerical computing, data science, visualization, ML/DL pipelines, AI agents, databases, and DevOps tooling (Linux, CLI, Git).

---

## Curriculum

| Module | Topic | Description | File |
|--------|-------|-------------|------|
| **01** | Python | Variables, types, control flow, functions, classes, iterables, advanced OOP |  |
| **02** | Markdown | A guideline for Markdown language | [MDguide.md](Tutorials/MDguide.md) |
| **03** | CLI & Shell | Bash, navigation, file management, text editors (vim/nano), networking tools | [CLI.md](Tutorials/CLI.py) |
| **04** | Linux | Shell, navigation, file management, Commands, Streams, Pipelines | [Linux.py](Tutorials/Linux.py) |
| **05** | Git & Version Control | Local versioning, staging, commits, GitHub, project supervision | [Git.md](Tutorials/Git.md) |
| **06** | Telegram Bots | Bot setup, handlers (command, message, callback), inline keyboards, conversation flow | [Telegram_tutorial/](Telegram_tutorial/README.md) |
| **07** | NumPy | Arrays, indexing, slicing, broadcasting, linear algebra, numerical computation | [Numpy.py](Tutorials/numpy.py) |
| **08** | Matplotlib | Visualization and graphics with matplotlib | [Matplotlib.ipynb](Tutorials/matplotlib.ipynb) |
| **09** | Linear Algebra | Vectors, matrices, transformations, eigenvalues, and core algebra for AI | [Linear_Algebra.py](Tutorials/linear_algebra.py) |
| **10** | Calculus | Derivatives, gradients, optimization intuition, and calculus essentials for ML | [Calculus.py](Tutorials/calculus.py) |
| **11** | Numerical Methods | Numerical stability, approximation, and computational techniques | [Numerical.py](Tutorials/numerical_calculation.py) |
| **12** | Pandas | Library for data analysis and work with data | [pandas.py](Tutorials/pandas.py) |
| **13** | Data cleaning | Data Cleaning before Machine learning (With Pandas) | [pre_processing.py](Tutorials/pre_processing.py) |
| **14** | Statistics | Statistics Overview required for Machine learning | [statistics.py](Tutorials/statistics.py) |
| **15** | Linear Regression | Types of Machine learning - Intro of regression, Intro of linear regression concepts, Intro of scikit-learn, gradient descent, SGDRegressor model, Intro of loss function | [regression.py](Tutorials/regression.py) |
| **16** | ML Concepts | Machine Learning glossary | [ML_cocepts.py](Tutorials/ML_concepts.py) |
| **17** | Machine Learning Intro | linear regression, SGDRegressor model class, LinearRegression model, data Scaling, classification -> logisticRegression(), Model validity, train_test_split(), sklear metrics | [ML_intro.py](Tutorials/ML_intro.py) |
| **18** | ML Models | ✅Supervised Regression (linear/non-linear) models: Ridge, Lasso, ElasticNet, Decision Tree, Random Forest, KNN, SVM | ✅Ensemble models: Random forest | ✅Hyperparameter Tuning (overfitting, underfitting, generalization)    | [ML_models.py](Tutorials/ML-models.py) |
| **19** | GridSearchCV | GridSearch and Hyperparameter tuning with cross validation | [ML_GridSearchCV.py](Tutorials/ML_GridSearchCV.py) |
| **20** | Feature Engineering | Preparing data before ML Pipelines - Data Scaling - PolynomialFeatures - Feature encoding (Label encoding,  One hot encoding, Ordinal encoding) - Feature Selection (SelectKBest, RFE, PCA ) | [feature_engineering.py](Tutorials/feature_engineering.py) |
| **21** | Machine Learning Pipeline | Complete Pipeline for preprocessing and Modeling, ColumnTransformer concepts | [pipelines.py](Tutorials/pipelines.py) |
| **22** | Unsupervised ML | Intro on Clustering (KMeans, Hierarchial, DBSCAN, Gaussian Mixture) and Dimentional reduction (PCA, KernelPCA, t-SNE, UMAP) | [unsupervised_ML.py](Tutorials/unsupervised_ML.py) |


---

## Quiz


| Quiz | Focus | File |
|------|-------|------|
| **Q1** | Advanced Python, class methods, and errors | [Q1_A.py](Quiz/Q1_A.py) - [Q1_B.py](Quiz/Q1_B.py) - [Q1_C.py](Quiz/Q1_C.py) |
| **Q2** | CLI and Git workflow practice | [Q2_A.py](Quiz/Q2_A.py) - [Q2_B.py](Quiz/Q2_B.py) |
| **Q3** | NumPy quiz | [Q3_A.py](Quiz/Q3_A.py) - [Q3_B.py](Quiz/Q3_B.py) - [Q3_C.py](Quiz/Q3_C.py) |
| **Q4** | Matplotlib quiz | [Q4_A.py](Quiz/Q4_A.py) - [Q4_B.py](Quiz/Q4_B.py) - [Q4_C.py](Quiz/Q4_C.py) - [Q4_D.py](Quiz/Q4_D.py) |
| **Q5** | Pandas quiz | [Q5_A.py](Quiz/Q5_A.py) - [Q5_B.py](Quiz/Q5_B.py) |
| **Q6** | ML practices, We have 4 data in these Quizes (data cleaning, train model with data, prediction, matplotlib)| [Q6_A.py](Quiz/Q6_A.py) - [Q6_B.py](Quiz/Q6_B.py) - [Q6_C.py](Quiz/Q6_C.py) - [Q6_D.py](Quiz/Q6_D.py) |
| **Q7** |


---

## Repository Structure

```
AI/
│
├── README.md
├── LICENSE
│
│
├── pictures/
│   └── AI.png
│
│
├── Telegram_tutorial/         # How to make a telegram bot
│   ├── README.md
│   ├── steps.py
│   ├── telegram_server.py
│   └── telegram_test1.py … telegram_test6.py
│
│
├── Tutorials/
│   ├── README.md              # Study guide
│   ├── CLI.md                 # Command Line Interface & Shell
│   ├── GIT.md                 # Git, GitHub, version control
│   ├── numpy.py               # NumPy
│   ├── matplotlib.ipynb       # Matplotlib
│   ├── Linux.md               # Linux & DevOps
│   ├── linear_Algebra.py      # statistics
│   ├── calculus.py
│   ├── numerical.py
│   ├── pandas.py
│   ├── pre_processing.py
│   ├── statistics.py
│   ├── regression.py         # start of machine learning
│   ├── ML_concepts.py
│   ├── ML_intro.py
│   ├── ML_Models.py
│   ├── ML_GridSearchCV.py
│   ├── feature_engineering.py
│   ├── pipelines.py
│   ├── unsupervised_ML.py
│   ├──
│   ├──
│   └── 
│
│
└── Quiz/
    ├── README.md
    ├── Q1.md
    ├── Q2.md
    ├── Q3.md
    ├── Q4.md
    ├── Q5.md
    ├── Q6.md
    ├── Q7.md
    └── 

```

---

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/khashayar-alipour/AI.git
   cd AI
   ```

2. **Dependencies** (recommended: Conda or venv)
   ```bash
   conda create -n ai_eng python=3.10
   conda activate ai_eng
   pip install numpy pandas matplotlib scikit-learn sympy scipy sqlalchemy
   ```
---


## Contact

[Gmail](khashayar.alipour111@gmail.com)

[linkedin](https://www.linkedin.com/in/khashayar-alipour-99543b414/)




