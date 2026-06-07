



     #|=========================================|
     #|    Quiz 3                               |
     #|    Part A                               |
     #|    Numpy summary                        |
     #|    Author: Khashayar Alipour            |
     #|=========================================|

#________________________________________________________________________________________________________________________

# خلاصه ای از کل متودهای کتابخوانه numpy



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






















