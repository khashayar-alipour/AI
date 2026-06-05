
#   ==========================================================================
#   =============       Created on wed Jun  3 17:31:30 2026      =============
#   =============            Author: KhashayarAlipour            =============
#   =============                 License: MIT                   =============
#   =============                                                =============
#   =============                 AI-Calculs                     =============
#   ==========================================================================



'''
   __________________________________
   |                                |
   |     Differential calculus      |
   |________________________________|
'''

# what is the meaning of calculus? --> Study of a continous change
# برای اینکه یک تغییر پیوسته رو مطالعه و بررسی کنیم ما توابعی داریم که تغییراتش رو مطالعه میکنیم
# رفتار هرچیزی در جهان رو میشه با استفاده از یک تابع شبیه سازی کرد
# این توابع اکثرا یک curve دارن مثل نمودار تابع زیر

#                y
#                |
#                |     f(x)=x**2
#          \     |     /
#           \    |    /
#            \   |   /
#             \  |  /
#              \ | /
# -x ___________\|/_______________  x
#                |
#                |
#                |
#               -y



#   ___________________________
#   |    Derivative (مشتق)    |
#   ===========================

# مشتق چیه؟  یعنی یک نقطه ای داریم روی نمودار تابع و میخوایم شیب(slope) اون نقطه رو بدست بیاریم
# برای بدست آوردن شیب یک نقطه، لازمه که یک نقطه دیگه هم داشته باشیم و از نقطه اول به نقطه دوم یک خط بکشیم
# سپس شیب اون خط رو حساب میکنیم که میشه مشتق نقطه موردنظر
# slope between point "a" and point "b" --> ya-yb / xa-xb = Delta y / Delta x
# ya=f(xa) --> f(xa)-f(xb) / xa - xb

# نقطه b باید خیلی خیلی نزدیک باشه به نقطه‌ای که میخوایم مشتق اون رو بگیریم (تقریبا روی هم افتاده باشن)
# یعنی تقریبا بشه گفت xb - xa =~ 0 باشه یعنی خیلی خیلی بهم نزدیک باشن
# پس از a به b یک خط رسم میکنیم و شیب اون خط میشه مشتق نقطه xa موردنظر ما
# پس فرمول مشتق در نقطه a میشه این:
'''
    f(xa)`= Lim f(xa) - f(xb) / xa - xb
            xa-->xb
            
yejoor dg ham mishe formul bala ro nevesht:
    e = xa - xb
    f(xa)`= lim f(xa+e) - f(xb) / e
            e-->0
'''

# در تعریف مشتق ممکنه به اصطلاحات و علائم زیر برخورد داشته باشیم که معنی همشون میشه همون مشتق:
    # f` = lagrange notation
    # df/dx = leibniz notation
    # y. = newtonian notation
    # Df = euler notation





#   __________________________________
#   |     higher order derivative    |
#   ==================================

f(x)= x**3
f(x)` = df/dx = y. = 3*x**2
f(x)`` = df2/dx2 = y.. = 6*x
f(x)``` = df3/dx3 = y... = 6
f(x)```` = df4/dx4 = y.... = 0
f(x)````` =0
f(x)````` = 0





#   _____________________________
#   |     partial derivative    |
#   =============================

f(x,y) 
z = 4x + 2y

df/dx -->4
df/dy -->2
df/dxdy -->




#   ____________________
#   |     Lim rules    |
#   ====================

# lim(c) = c
# lim[f(x) +- g(x)] = lim f(x) +- lim g(x)
# lim[f(x) * g(x)] = lim f(x) * lim g(x)





#   ________________________________
#   |     differentiation Rules    |
#   ================================

# قوانین زیر در مواردی که نقطه به نقطه پشت سر هم مشتق روی نمودار رو میخوایم حساب کنیم کمک میکنن

# f(x) =c                 f'(x)=0
# f(x)=g(x) + h(x)        f'(x) = g'(x) + h'(x)
# f(x)=g(x)h(x)           f'(x)=g(x)h'(x) + h(x)g'(x)
# f(x)=g(x)/h(x)          f'(x) = g'(x)h(x) - g(x)h'(x)/h**2(x)
# f(x)=x**r               f'(x)=r*x**(r-1)
# f(x)=ln(x)              f'(x)=1/x
# f(x)=sin(x)             f'(x)=cos(x)
# f(x)=cos(x)             f'(x)=-sin(x)
# f(x)=tan(x)             f'(x)=1/cos(x)**2
# f(x)=g(h(x))            f'(x)=g'(h(x))h'(x)




#   _______________________
#   |     optimization    |
#   =======================

# وقتی مشتق یک تابع برابر 0 بشه یعنی شیب 0 میشه
# اکثر توابع یک مینیمم یا ماکسیمم دارن
# هرجایی از تابع که به min یا max رسیدیم اونجا مشتق برابر 0 هست
# برای بهینه سازی یا optimization برای اینکه بدونن یک تابع max یا min کجا قرار داره
# میان مشتق اون تابع رو برابر 0 میذارن و مشخص میشه min و max کجاست









'''
=========================================================================================
=====================================[ Part 2 ]==========================================
'''




'''
    ___________________________
   |                          |
   |     Differentiation      |
   |__________________________|
'''

#   ______________________
#   |    Dependencies    |
#   ======================

# در این درسنامه از کتابخوانه های numpy، sympy و scipy استفاده شده

#pip install numpy
#pip install sympy
#pip install scipy

#sympy --> symbol + python --> سمبلیک
#scipy --> scientific + python --> علمی- دانشی 
# هر دوتای این کتابخوانه ها بر اساس numpy نوشته شدن



#   _________________________
#   |    Sympy - symbolic   |
#   =========================

import sympy
# import sympy as sp

# کلا symbolic یعنی عدد دقیق داریم (اعشاری نیست)
# با تابع symbol که از دل کتابخوانه Sympy خارج میکنیم
# یک متغیر میسازیم که این متغیر تبدیل به یک symbol object خواهد شد
# این تابع یک object از دل sympy میسازه دقیقا مثل ndarray از دل numpy

x= sympy.symbols('x')
print(type(x))    # <class 'sympy.core.symbol.Symbol'>


# ------ Derivative(مشتق) --------
# حالا میخوایم با استفاده از sympy مشتق بگیریم
# ما موارد زیر رو در کتابخوانه های دیگه داشتیم:
    #math --> math.sin() math.cos() , ...
    #numpy --> np.sin() np.cos() , ...
    #sympy --> sp.sin() sp.cos() , ...
    #exponential --> e** felan
    
    f = sympy.sin(x) * sympy.exp(x)    # f = sin(x)*e**x
    print(type(f))    # <class 'sympy.core.mul.Mul'>

# برای اینکه یک تابع بسازیم که مشتق میگیره میشه اسمهای زیر رو واسش گذاشت:
    # df/dx
    # df_dx
    # dfdx  مرسوم

    dfdx = sympy.diff(f,x)
    print(type(dfdx))    # <class 'sympy.core.add.Add'>
    print(f'derivative: {dfdx}')    # derivative: exp(x)*sin(x) + exp(x)*cos(x)


# حالا مشتق درجه 2
    dfdx2 = sympy.diff(f,x,2)    # 2*exp(x)*cos(x)


# حالا میخوایم مشتق رو در یک نقطه حساب کنیم
    # 1- manual (روش اول)
    # این روش خیلی مرسوم نیست    
    
    f`(x)=dfdx
    print(dfdx)    # exp(x)*sin(x) + exp(x)*cos(x)
    import math
    dif_at_2= math.exp(2)*math.sin(2) + math.exp(2)*math.cos(2)
    print(dif_at_2) #3.643917376788891


    # 2- subs (روش دوم)
    # در این روش به سادگی از تابع subs استفاده میکنیم    
    value = dfdx.subs(x,2)    # this means: evaluate at x=2
    print(value)
    

    # 3- 3 symbols (ساخت 3 سمبل)
    #partial
    x,y,z = sympy.sybols('x,y,z')
    f = sympy.sin(x*y)+ sympy.sin(y*z)

    # df/x y**2
    dfdxy= sympy.diff(f,x,1,y,2)




#   ___________________________
#   |    Scipy - numerical    |
#   ===========================

# کلا symbolic میشد عدد دقیق بدون تقریب
# گاهی به عدد تقریبی و اعشاری نیاز داریم
# در این موارد به numerical نیاز داریم
# اگر دیدیم symbolic نداره و جواب نمیده از numerical استفاده میشه


# حالا میخوایم با کتابخونه scipy مشتق f رو روی x=2 حساب کنیم:
    # اینجا تابع خودمون رو اینجوری میسازیم
def f(x):
    return np.sin(x)*np.exp(x)

    
import scipy
dfx_numeric = scipy.optimize._numdiff.approx_derivative(f,2.0)
print(dfx_numeric)     # [3.64391738]






'''
    ____________________
   |                   |
   |     Integral      |
   |___________________|
'''

# انتگرال یعنی محیط زیر نمودار
# یعنی توی نمودار یک curve داریم و مساحت زیرش میشه انتگرال

# اگه از f مشتق بگیریم و بشه f(x) -> اگه بخوایم f رو برگردونیم، f میشه انتگرال f(x)
# f --> f(x)`    f --> integral f(x)`
# x**2  --> 2*x = moshtaghe x**2
#----> integral of 2*x = x**2


#______________________________
# استفاده از sympy      
#______________________________
# در روشهای زیر بصورت دقیق و symbolic محاسبه میکنیم

import sympy
x = sympy.symbols('x')
f = sympy.sin(x) * sympy.exp(x)

sympy.integrate(f,x)   # integrate = انتگرال
# exp(x)*sin(x)/2 - exp(x)*cos(x)/2

# در بحث انتگرال مهمه که limit خودمون رو مشخص کنیم
# یعنی مثلا وقتی میگیم انتگرال آیا منظور ما از منفی بی‌نهایت تا مثبت بی‌نهایت هست؟
# یا مثلا از x=1 تا x=5 منظورمونه؟
# اگه منظورمون یه محدوده مشخص باشه میشه از تابع integrate بصورت زیر استفاده کرد:
    sympy.integrate(f,(x,-1,1))    # -E*cos(1)/2 + exp(-1)*cos(1)/2 + exp(-1)*sin(1)/2 + E*sin(1)/2

# اگر از منفی تا مثبت بی‌نهایت بخوایم میتونیم از تابع oo از دل sympy استفاده کنیم:
    from sympy import oo
    #sympy.oo
    sympy.integrate(f,(x,-oo,oo))    # -oo*sign(AccumBounds(-1, 1))

# اگر در کتابخوانه scipy بخوایم در بی‌نهایت انتگرال حساب کنیم اینجوری میشه:
    #scipy --> -np.inf +np.inf
    
    
#______________________________
# استفاده از Scipy      
#______________________________
# حالا میخوایم به روش numerical و اعداد تقریبی انتگرال حساب کنیم
# برای اینکار از کتابخوانه Scipy استفاده میشه برای محاسبات

from scipy.integrate import quad ,dblquad , tplquad

'''
function    purpose
quad        1st integral
dblquad     2nd integral  --> dota integral migire (higher dimention)
tplquad     3rd integral
'''

def f(x):
    return x

x_lower =0
x_upper= 1

quad(f,x_lower,x_upper)     # (0.5, 5.551115123125783e-15) 
val , abserr = quad(f,x_lower,x_upper)
print('computed integral:', val)     # computed integral: 0.5
# اینجا val میگه در تابع x اگر بخوایم انتگرالش رو از 0 تا 1 بگیریم میشه 0.5
# پس val میشه دقیقا همون انتگرالی که دنبالش هستیم:
    # انتگرال تابع x میشه x**2 / 2    
# در نقطه 1 --> 0.5    
# در نقطه 0 --> 0    
    #0.5 - 0 --> 0.5

# حالا abserr چیه؟
# ارور تقریب ماست    
    print('numerical erropr:',abserr)     # 5.551115123125783e-15



# ----- Lambda  این چیه؟؟ -----
    # در scipy بجای توابع ساده مثل f(x) که در بالا ساختیم میتونیم از labmda استفاده کنیم
    # بجای این:    
        def f(x):
            return x**2
    # میتونیم اینو بنویسیم:    
        y = lambda x : x**2
        y(2)  # 2*2 = 4
        y(10)  # 10*10 = 100
    
    # تابعی که در بالا ساختیم هم میتونه اینجوری بشه:    
        from scipy.integrate import quad
        val , abserr = quad(lambda x : x**2,0,1)



# ----- higher dimention in scipy -----
    # این دوتا انتگرال میگیره    

    from scipy.integrate import dblquad
    
    def integrant(x,y):
        return np.exp(-x**2 -y**2)
    
    x_lower = 0
    x_upper= 10
    y_lower = 0
    y_upper=10
    
    val , abserr = dblquad(integrant,x_lower,x_upper, lambda x : y_lower , lambda x : y_upper)







#   ________________________
#   |    TOTALL SUMMARY    |
#   ========================
'''
We can calculate Differential and Integral with scipy and sympy:
_____________________________________________________
symbolic (sympy)           |    Numerical (Scipy)     
=====================================================  
Exactl result              |   approximate nmber
x --> sympy.symbols()      |   ------
f --> yek equation az x    |   func f() or lambda
.diff()                    |   .optimization._diff....
integerate()               |   quad() dblquad() 
sympy.oo                   |   np.inf
oo -oo                     |   -np.inf  np.inf
complex --> slow           |   Very fast --> lower accuracy

'''

# When sympy??
# زمانیکه ریاضی دقیق میخوایم و زمانیکه معادلات داریم
# زمانیکه داریم کار theoritical ریاضی انجام میدیم


# When scipy??
# وقتیکه analytical solution وجود نداره
# وقتیکه تابع خیلی پیچیدست و ما باید سریعا یک روش تقریبی و numerical result داشته باشیم






























