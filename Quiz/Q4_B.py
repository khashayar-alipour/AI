

     #|=========================================|
     #|    Quiz 4                               |
     #|    Part B                               |
     #|    matplotlib                           |
     #|    Author: Khashayar Alipour            |
     #|=========================================|

#________________________________________________________________________________________________________________________

# برای دیتاهای زیر باید 4 تا نمودار رسم کنیم

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
sales = [120, 150, 170, 140, 200, 220, 180]
customers = [30, 45, 50, 40, 60, 65, 55]




#==========================================================
# 1- نمودار خطی برای فروش در طول هفته، با grid و title

import matplotlib.pyplot as plt
plt.plot(sales, days, "*", ms=15, mfc="red" )
plt.title("cool plot")
plt.grid(c="green")
plt.xlabel("sales")
plt.ylabel("days")
plt.show()




#==========================================================
# 2- نمودار scatter برای تعداد مشتریان در مقابل میزان فروش، استفاده از مارکر متفاوت

import matplotlib.pyplot as plt
color_list = [10,20,30,40,50,60,70]
plt.scatter(customers, sales, marker="o", c=color_list, cmap="inferno")
plt.xlabel("customers")
plt.ylabel("sales")
plt.title("customers vs sales", color="green")
plt.grid(c="blue")
plt.colorbar()
plt.show()





#==========================================================
# 3- نمودار bar برای فروش روزانه

import matplotlib.pyplot as plt

font={"family":"serif", "color": "blue", "size": 20 }

plt.bar(days, sales, color="orange", width=0.6)
plt.title("no title", loc="left", fontdict=font)
plt.xlabel("days", fontdict=font)
plt.ylabel("sales", fontdict=font)
plt.grid(axis="y")
plt.show()





#==========================================================
# 4- نمودار histogram از sales و bin=5 باشه

import matplotlib.pyplot as plt

plt.hist(sales, bins=5, color="red", alpha=0.7)
plt.xlabel("sales")
plt.ylabel("distribution")
plt.grid(axis="x")
plt.show()





















