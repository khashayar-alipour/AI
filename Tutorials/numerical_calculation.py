

#   ==========================================================================
#   =============       Created on Thu Jun  4 12:00:59 2026      =============
#   =============            Author: KhashayarAlipour            =============
#   =============                 License: MIT                   =============
#   =============                                                =============
#   =============           AI numerical calculation             =============
#   ==========================================================================


'''
    _________________________________
   |       Numerical Modeling       |
   =================================
'''


# اکثر مواقع ما یک تابع داریم که میخوایم حلش کنیم
# مثلا ما میخوایم بدونیم در تابع x**2 + 4*x = 8 چه عددی جای x بزاریم تا معادله درست در بیاد؟؟

# پس کلا میشه گفت برای حل این معادلات 3 روش وجود داره:
    # 1-Analythical --> exact number --> دقیق حل میشه
    # 2- Numerical --> با تقریب عددی حل میشه
    # 3- Graphically --> با استفاده از تصویر و نمودار حل میشه



# در دنیای کامپیوتر و همچنین ماشین لرنینگ ما داریم دائما معادله حل میکنیم
# پس مهمه که اول بیایم همه معادلات یا equation هارو دسته بندی کنیم:

    


'''
    _____________________________________
   |    1- Linear algebric equation     |
   =====================================
'''
# اینجا algebric یعنی دیفرانسیل نداره
# و همچنین linear یعنی خطی
# این معادلات با analythical و بدست آوردن عدد دقیق حل میشه
# نیازی به تقریب و numerical و اینچیزا نداره


# الان این معادله رو به روش analythical حل کردیم
# و چون در انتها پاسخ عدد دقیق شد، پس میشه با sympy هم حلش کرد
    # ax + b =0
    # 4*x -8 =0
    # 4*x = 8
    # x = 8/4 = 2 

    import sympy
    x=sympy.symbols('x')
    eq = 4*x - 8   # ساخت معادله
    
    # اینجا میگیم آقای sympy بیا برای من solve کن معادله‌ی eq رو و x رو بدست بیار:    
    sol = sympy.solve(eq,x)
    print(sol)  # [2]


# برای ساختن x در sympy میشه این کارهارو هم کرد:
    x = Symbol('x' , real= True)
    x = Symbol('x' , positive = True)
    x = rational(4,5)


# ---- گاهی میخوایم یک symbolic رو به numerical تبدیل کنیم ----

# همچنین در انتها میخوایم نمودار تابع رو با استفاده از matplotlib رسم کنیم
    import numpy as np 
    import sympy
    x = sympy.symbols('x')
    f_symb = (x + sympy.pi)**2
    f=sympy.lambdify([x],f_symb,'numpy')
    print(type(f))    # <class 'function'>
    
    x_vec = np.linspace(0, 10,100)
    f_vec = f(x_vec)
    print(f_vec)
    
    
    import matplotlib.pyplot as plt
    plt.scatter(x_vec,f_vec,s=5)
    plt.ylabel('f nmpy')
    plt.xlabel('x')
    plt.title('Symbolic to Numpy visualization')
    plt.grid()
    plt.show()


# ____________________________
# |  some sympy capabilities |

# ---- expand ----
    sympy.expand((x+1)*(x+2)*(x+3))    # x**3 + 6*x**2 + 11*x + 6


# ---- apart ----
    f1 = 1/ ((x+1)*(x+2))
    sympy.apart(f1)   # -1/(x + 2) + 1/(x + 1)


# ---- together ----
    f2 = 1/(x+1) + 1/(x+3)
    sympy.together(f2)    # 2*(x + 2)/((x + 1)*(x + 3))


# ---- sigma ----   -> Sum,s and products
    n = sympy.symbols('n')
    # sigma 1/n**2   n 1-->10
    #1/1**2 + 1/2**2 + 1/3**2 + 1/4**2 +....+ 1/10**2
    
    sympy.Sum(1/n**2,(n,1,10))
    #Sum(n**(-2), (n, 1, 10))
    
    sympy.Sum(1/n**2,(n,1,10)).evalf()    # 1.54976773116654
    
    sympy.Sum(1/n**2,(n,1,sympy.oo)).evalf()    # 1.64493406684823


#--> + Sum , zarb she beynesh ---> product
    #n -->  1 ta 10 
    #1 * 2 * 3 * 4 ..* 10 -->10!
    #1/x 
    #1/sx**2
    
    sympy.Product(n,(n,1,10))    # Product(n, (n, 1, 10))
    sympy.Product(n,(n,1,10)).evalf()    # 3628800.00000000


#---- Limits ----
    sympy.limit(sympy.sin(x)/x , x,0)    # 1


#---- series ----
    # e*x -- 1 + x + x**2/2 + x**3/6 + ...
    sympy.series(sympy.exp(x),x)   # 1 + x + x**2/2 + x**3/6 + x**4/24 + x**5/120 + O(x**6)
    
    sympy.series(sympy.exp(x),x,1)
    '''
    E + E*(x - 1) + E*(x - 1)**2/2 + E*(x - 1)**3/6 + E*(x - 1)**4/24 + E*(x - 1)**5/120 + O((x - 1)**6, (x, 1))
    '''
    
    sympy.series(sympy.exp(x), x, 1, 10)
    '''
    E + E*(x - 1) + E*(x - 1)**2/2 + E*(x - 1)**3/6 + E*(x - 1)**4/24 + E*(x - 1)**5/120 + E*(x - 1)**6/720 + E*(x - 1)**7/5040 + E*(x - 1)**8/40320 + E*(x - 1)**9/362880 + O((x - 1)**10, (x, 1))
    '''
    
#---- special function ----
    from scipy.special import jn , yn 
    #jn, yn bassel function hastan
    
    
    
    
'''
    _________________________________________
   |    2- Non-Linear algebric equation     |
   =========================================
'''
# در Non-linear برعکس linear ما نمیتونم فقط با analythical همه معادلات رو حل کنیم

# معادلات non-linear چند نوع هستن:
    # qudratic --> ax**2 + bx + c =0
    # cubic --> ax**3 + bx**2 + c*x + d =0
    # exponential --> e**x - felan
    # logarithmic --> log , ln ... 
    # trigonometric --> sin(x) = 1.05

    
# خلاصه‌ای از analythical
    #ax**2 + bx + c =0   این معادلمون هست مثلا

    #b*2 - 4ac --> delta
    #delta + - 0 
    
# حالا جواب 3 حالت داشت:    
    #delta < 0 --> no answer
    #delta = 0 --> -b/2a
    #delta > 0 --> 2 answers:  x1 = -b + radical delta / 2a     x2 = -b - radical delta / 2a
    
    # حتی میشه تابعش رو هم همینجوری نوشت:    
    import math
    def solve_quadratic(a,b,c):
        delta = b**2 - 4 * a *c
        if delta<0:
            print('javab nadarad')
            return None
        elif delta==0:
            x = -1 * b  / 2*a
            return x
        else:
            x1= (-b + math.sqrt(delta))/2*a
            x2= (-b - math.sqrt(delta))/2*a
            return x1,x2
    
    # حالا یه مثال با تابع بالا حل میکنیم:    
    # x**2 -3x + 2 = 0
    # delta --> 9 - 8  = 1 
    
    # r1= - -3 + 1 / 2 = 2
    # r2= - - 3 - 1 / 2 = 1
    # (x-1)(x-2) = 0 
    
    solve_quadratic(1,-3,2)    # (2.0, 1.0)



# با استفاده از sympy میشه مسائل analythical رو که معمولا ساده هستن حل کرد:
    from sympy import symbols, solve
    x = symbols('x')
    eq = x**2 - 3*x +2 
    solution = solve(eq,x)
    print(solution)   # [1, 2]


    eq = sympy.sin(x) - 0.5
    solution = solve(eq,x)
    print(solution)    # [0.523598775598299, 2.61799387799149]


    eq = sympy.log(x) -100
    solution = solve(eq,x)
    print(solution)    # [exp(100)]




# حالا اگه یک معادله non-algebric سخت داشته باشیم چی؟
# روشهای analythic اصلا نمیتونه اینها رو حل کنه
# فقط باید از روشهای numerical و تقریبی استفاده کرد:
    
    # 1- iteration methods---> g(x) = x with intiial guess and .....
    
    
    # 2- wegeshtain method ---> more speed up because we have x1=g(x0) so
        # x m+1 = xm-1 g(x) .....
    
    
    # 3- Newton Method --> first we have initial guess (x0) and then we havederivatiev f'(x0) and 
        # we must know each cross y=0 at which point and this is our new x and .......
        # f'(x0) = f(x0) / x0 - x1
        # X m+1 = xm - f(xm)/f'(xm)
    
        from scipy.optimize import newton
    
        def f(x):
            return x**3 - x - 2
        
        def df(x):     # Derivative
            return 3*x**2 - 1
        
        root = newton(f, x0=1.5, fprime=df)     # Starts at x0=1.5
        print(root)
    
    
    
    # 4- secant method --> instead of f'() we use the approixmated of that 
    
    
       
    # 5- Bisection method --> f(a) and f(b) must be non same sign and ..
        # c= a+b/2 --> f(c) and then ....
    
        from scipy.optimize import bisect
    
        def f(x):
            return x**3 - x - 2      # Example function
    
        root = bisect(f, 1, 2)      # Bracketing between 1 and 2
        print(root)
    
    


    # 6- fixed point
    
        from scipy.optimize import fixed_point
    
        def g(x):
            return (x + 2/x)**0.5     # Example transformation
        
        root = fixed_point(g, x0=1.5)
        print(root)




    # 7- ROOT
        #Uses various numerical solvers (Newton, Broyden, Hybr, LM, etc.).
    
        from scipy.optimize import root
        
        def f(x):
            return x**3 - x - 2
        
        x0 = 1.5     # Initial guess
        
        sol = root(f, x0, method='hybr')     # Hybrid method (default)
        print(sol.x)     # Root found
        '''
        hybr	Trust Region	General Problems (Default)
        lm (Levenberg-Marquardt)	Trust Region	Nonlinear Least Squares
        broyden1	Quasi-Newton	Large Sparse Problems
        broyden2	Quasi-Newton	Large Sparse Problems
        anderson	Iterative	Fixed-Point Problems
        krylov	Iterative	Large Systems
        diagbroyden	Quasi-Newton	Diagonal Jacobians
        excitingmixing	Iterative	Physics & Engineering
        linearmixing	Iterative	Fixed-Point Equations
        '''


    # 8- ---sympy --> solve --> nsolve (numerical solve) --> newton raphson
        import sympy
        
        x = sympy.symbols('x')
        eq = x**3 - x - 2
        
        #solution = sympy.solve(eq,x)
        
        root = sympy.nsolve(eq,x,1.5) #intiial guess
        print(root)





'''
    _____________________________________________
   |    3- Linear algebric system queations     |
   =============================================
'''

# 1-Linear Algebric equations --> can be solved with analytical
# 2-Non-Linear Algebric Equations --> can be solved with analytical  + Numerical (various method)

# algberic (lin, non-lin) --> این دو گروه همشون معادلات یک خطی هستن
# equation systems --> مخصوص معادلات چند خطی


# مثلا مورد زیر یک سیستم از 2تا معادله هست:
    2*x + y = 5
    x - y = 1
    
    # حل بصورت دستی:    
        3*x = 6
        x = 2
        
        2*2 + y = 5
        y=1

# حالا اگه مثلا 3تا یا 4تا یا 5تا بشه چی؟ چجوری حلش میکنیم؟
    # اولین چیز میگن اینو بصورت ماتریکس بنویس    
        # A*x = B
        # A --> ماتریکس ضرایب
        # x --> مجهول
        # B --> ماتریکس جواب

        #  |2    1|   |x|      |5|
        #  |1   -1|   |y|   =  |1|
        
        #  A = |2    1|   
        #      |1   -1|
        
        #      |x|
        #  x = |y|

        #     |5|
        #  b =|1|


    # روشهای زیادی وجود داره برای حل کردن اینجور مسائل. مثلا:    
        # Cramer’s rule  --> X = | | / | | --> not efficient
        # Gussian Elimination ---> Can have numerical instability
        # Gauss Jordan 
        # Matrix Inversion:--->Ax=B  A-1 Ax=A-1 b  Ix=x=A-1b
        # LU Decomposition --> analytical
        # Cholesky Decomposition --> analytical


# مهمترین روش این مورد هست    
# اینقد با معادله بازی میکنه تا یکی از مجهول‌ها رو حذف کنه و بقیه مسئله رو حل کنه:    
        # Gussian Elimination / Substitution
        # analytically --> روش حل مسائل در این متود
        # در این روش اصلا نیازی به ماتریکس کردن معادلات نیست        
        import  sympy
        x , y = sympy.symbols('x,y')
        eq1 = sympy.Eq(2*x + 3*y , 7)
        eq2 = sympy.Eq(4*x +y , 5 )
        solution = sympy.solve((eq1,eq2),(x,y))
        
        solution[x]   # 4/5
        solution[y]   # 9/5



    # Iteration method
# استفاده از این روش باعث میشه سریع به جواب برسیم        
        
        #4*x + 1y = 1
        #1*x + 3*y = 2
        import numpy
        a = np.array([[4,1],[1,3]])
        print(a)
        
        # matrix zarayeb
        # [[4 1]
        #  [1 3]]
        
        b= np.array([1,2])
        print(b)
        #[1 2]
        
        #A * x = B
        
        from scipy.sparse.linalg import cg
        x,info = cg(a,b)
        print(x)    # [x=0.09090909  y=0.63636364]



    # generalized minimal residual method
    # این روش تقریبا برای همه کار میکنه ولی slow هست        
        from scipy.sparse.linalg import gmres

        x , info = gmres(a,b) 
        print(x)   # [0.09090909 0.63636364]





'''
    _________________________________________________
   |    4- Non-Linear algebric system queations     |
   =================================================
'''
# در کل این روش خیلی کم استفاده میشه چون معادلات خیلی سنگینی داره

# analytically 
    import sympy
    
    x,y= sympy.symbols('x,y')
    
    eq1= sympy.Eq(x**2 + y**2 , 4)
    eq2 = sympy.Eq(4*x+3*y , 2)
    
    solution = sympy.solve((eq1,eq2),(x,y))



# numerical
# Grober basis روش
    from sympy import nonlinsolve
    x,y= sympy.symbols('x,y')
    solutions = nonlinsolve([x**2 + y**2-4 ,4*x+3*y-2 ], (x,y))








#   ============================================
#   =============                ===============
#   ==========      Total Summary    ===========
#   =============                ===============
#   ============================================


# Algebric (جبری)
    1-linear algebric equation -> analytical (sympy)
    2- Non-linear algebric equation --> analytical (sympy) numerical (scipy)
    3- Linear algebric system equations --> ** most important
    4- Non-linear algberic system equations --> rare


# Non-Algebric (غیر جبری)
    # این مورد در علم کامپیوتر خیلی کاربرد نداره    
                                    ________ Ordinary Differential Equations (ODE)
    5- Differential Equations  ----|________ Partial Differential Equations (PDE)
    6- Differential System Equations
    
    


























