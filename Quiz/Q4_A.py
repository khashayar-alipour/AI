

     #|=========================================|
     #|    Quiz 4                               |
     #|    Part A                               |
     #|    matplotlib                           |
     #|    Author: Khashayar Alipour            |
     #|=========================================|

#________________________________________________________________________________________________________________________

# رسم تمام نمودارهای matplotlib

# import matplotlib as mpl



'''     ===========================
        ===========================
        ======      plot     ======
        ===========================
        ===========================
'''


import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,21)
y = 3 * x
#0 ,.....20
#0 ,,,,,,,60

plt.plot(x,y)
plt.show()

#=====================================
import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5,6,7,8,9,10]
y = [3,6,9,12,15,18,21,24,27,30]
plt.plot(x,y,'o')
plt.show()

#=====================================
import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5,6,7,8,9,10]
y = [3,6,9,12,15,18,21,24,27,30]
plt.plot(x,y,'*')
plt.show()

#=====================================
import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5,6,7,8,9,10]
y = [3,6,9,12,15,18,21,24,27,30]
plt.plot(x,y,'d')
plt.show()

#=====================================
import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5,6,7,8,9,10]
y = [3,6,9,12,15,18,21,24,27,30]
plt.plot(x,y,'+')
plt.show()

#=====================================
import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5,6,7,8,9,10]
y = [3,6,9,12,15,18,21,24,27,30]
plt.plot(x,y,'.')
plt.show()

#=====================================
import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5,6,7,8,9,10]
y = [3,6,9,12,15,18,21,24,27,30]
plt.plot(x,y,'x')
plt.show()

#=====================================
import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5,6,7,8,9,10]
y = [3,6,9,12,15,18,21,24,27,30]
plt.plot(x,y,'p')
plt.show()

#=====================================
import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5,6,7,8,9,10]
y = [3,6,9,12,15,18,21,24,27,30]
plt.plot(x,y,'h')
plt.show()

#=====================================
import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5,6,7,8,9,10]
y = [3,6,9,12,15,18,21,24,27,30]
plt.plot(x,y,'v')
plt.show()

#=====================================
import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5,6,7,8,9,10]
y = [3,6,9,12,15,18,21,24,27,30]
plt.plot(x,y,'1')
plt.show()

#=====================================
import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5,6,7,8,9,10]
y = [3,6,9,12,15,18,21,24,27,30]
plt.plot(x,y,'|')
plt.show()




#=====================================
#=====================================
import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5,6,7,8,9,10]
y = [3,6,9,12,15,18,21,24,27,30]
plt.plot(x,y, marker='o' , ms=20 , mec='r' , mfc='g')
# marker= نقاط با خط بهم متصل میشن  | marker size | marker edge color | marker fill color
plt.show()



#=====================================
#=====================================
import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5,6,7,8,9,10]
y = [3,6,9,12,15,18,21,24,27,30]
# line style .  ..  -.  --  :   فقط خط
plt.plot(x,y,ls=':')
plt.show()

#=====================================
import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5,6,7,8,9,10]
y = [3,6,9,12,15,18,21,24,27,30]
plt.plot(x,y,ls='--', lw=10, color="r")
# linewidth
plt.show()



#=====================================
#=====================================
import numpy as np
import matplotlib.pyplot as plt
x= np.linspace(0,np.pi , 100)
y = np.sin(x)

plt.plot(x,y,ls=':',c='r')
# نمودار منحنی
plt.show()





#=====================================

#   |==========================|
#   |    some other settings   |
#   |==========================|

# این تنظیمات در همه فانشکنها کاربرد داره


import numpy as np
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6]
y = [10,20,30,40,50,60]

plt.plot(x,y)

# تنظیمات مهم
plt.title('my table')  # عنوان بالای نمودار
plt.xlabel('X axis')   # اسم محور x
plt.ylabel('Y axis')   # اسم محور y
plt.xlim(1,10)   # عدد محور x
plt.ylim(1,70)   # عدد محور y

plt.show()













'''     ==============================
        ==============================
        ======      scatter     ======
        ==============================
        ==============================
'''

#=====================================
# only points
# no lines
# color bar
# رنگهای شدتی
# color maps (cmaps)
# color list (cl)
# size list
# alpha list
# font | location | padding | grid
#=====================================


import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(0,10,30)    # از 0 تا 10 تقسیم به 30 قسمت مساوی
y= np.sin(x)    # سینوسی

plt.scatter(x, y, marker='*',color='r')
plt.show()



#=====================================
import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y= [10,20,30,40,50]
color_list=['r','r','b','g', 'b']     # (5 dots == 5 colors)

plt.scatter(x,y,marker='*',color=color_list)
plt.show()


#=====================================
import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y= [10,20,30,40,50]
color_list=[10,20,30,40,50]   # درجه شدت رنگ

plt.scatter(x,y,marker='*',c=color_list,cmap='viridis')
plt.show()


#=====================================
import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y= [10,20,30,40,50]
color_list=[10,20,30,40,50]

plt.scatter(x,y,marker='*',c=color_list,cmap='inferno')
plt.colorbar()
plt.show()


#=====================================
import numpy as np
import matplotlib.pyplot as plt

# همزمان 3 متغیر در یک نمودار

sample = [1,2,3,4,5]                    # x
height =[180 , 160 , 175 , 178 , 190]   # y

weight = [80 , 60 , 70 , 100 , 95]

plt.scatter(sample, height , c=weight , s=100 ,cmap='inferno')
plt.xlabel('person')       # c = color  s=size
plt.ylabel('height (cm)')
plt.colorbar()
plt.show()


#=====================================
import numpy as np
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[10,20,30,40,50]

size_list=[150,180,200,30,50]

plt.scatter(x,y,s=size_list)
plt.show()


#=====================================
import numpy as np
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[10,20,30,40,50]

# 1  میشه پررنگ

plt.scatter(x,y,s=200,alpha=0.3)
plt.show()


#=====================================
import numpy as np
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[10,20,30,40,50]

alpha_list = [0.2 , 0.3 , 1 , 1 ,0.5]

plt.scatter(x ,y ,s=200 ,alpha=alpha_list)
plt.show()


#=====================================
import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0,10,(100,))
y = np.random.uniform(10,20,(100,))

color_list=np.random.uniform(0,100,(100,))
size_list =np.random.uniform(20,50,(100,))
alpha_list=np.random.uniform(0,1,(100,))

plt.scatter(x ,y ,c=color_list ,s=size_list ,alpha = alpha_list ,cmap='inferno' )
plt.title('cool scatter')
plt.xlabel('random x')
plt.ylabel('random y')
plt.colorbar()

plt.show()


#=====================================
import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0,10,(100,))
y = np.random.uniform(10,20,(100,))

title_font={  'family' : 'serif' , 'color' : 'red' , 'size' : 20}
x_font={  'family' : 'serif' , 'color' : 'green' , 'size' : 20}
y_font={  'family' : 'serif' , 'color' : 'blue' , 'size' : 20}

plt.scatter(x, y,)

plt.title('cool scatter' ,fontdict=title_font ,loc='left' ,pad=30)
plt.xlabel('random x' ,fontdict=x_font)      # loc = location
plt.ylabel('random y' ,fontdict=y_font)
plt.grid()

plt.show()


#=====================================
import numpy as np
import matplotlib.pyplot as plt

x= [1,2,3,4,5]
y = [10,20,30,40,50]

plt.scatter(x,y)
plt.grid(color='green',linestyle='--',linewidth=0.5 ,axis="x")
plt.show()









'''     ==========================
        ==========================
        ======      pie     ======
        ==========================
        ==========================
'''

# label + percentage


#=====================================
import numpy as np
import matplotlib.pyplot as plt

lab = ['apple' , 'banana','cherry','orange']

#percentage
size = [50,30,10,10]     # -> apple=50% - banana=30% - cherry=10% - orange=10%

mycolor=['green','red','blue','black']     # -> apple=green - banana=red - cherry=blue - orange=black

ex=[0,0,0,0.2]      # -> apple=0 - banana=0 - cherry=0 - orange=0.2

plt.pie(size,labels=lab,colors=mycolor,explode=ex)
plt.show()










'''     ==========================
        ==========================
        ======      bar     ======
        ==========================
        ==========================
'''

# label + number


#=====================================
import numpy as np
import matplotlib.pyplot as plt

x = ['A','B','C','D']
y = [3 , 7 , 1 , 10]

plt.bar(x,y,color='g',width=0.7)

plt.title('cool bar chart')
plt.ylabel('population')
plt.xlabel('group')

plt.grid(axis='y')

plt.show()









'''     ===========================
        ===========================
        ======      hist     ======
        ===========================
        ===========================
'''

# بررسی فراوانی و انواع توزیع


#=====================================
import numpy as np
import matplotlib.pyplot as plt

data = np.random.uniform(0,10,(100,))   # تعداد 100 عدد رندوم بین 0 و 10 انتخاب کن که توزیع همسان دارن

plt.hist(data, width=0.8)

plt.show()

# X axis -> data
# Y axis -> فراوانی


#=====================================
import numpy as np
import matplotlib.pyplot as plt

data = np.random.uniform(0,10, (10000))

plt.hist(data, width=0.5)

plt.show()


#=====================================
import numpy as np
import matplotlib.pyplot as plt

#mean=5 , variance=1 , shape
data = np.random.normal(5,1,(1000,))

plt.hist(data, color='g',alpha=0.5)

plt.show()


#=====================================
import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(5,1,(10000,))

plt.hist(data,color='g',alpha=0.75,bins=50)

plt.show()


#=====================================
import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(5,1,(10000,))
plt.hist(data,color='g',alpha=0.75,bins=500)
plt.title('random data distribition')
plt.xlabel('data')
plt.ylabel('faravani')
plt.grid()
plt.show()












