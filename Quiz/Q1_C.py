


        #|=========================================|
        #|    Quiz 1                               |
        #|    Part C                               |
        #|    Python Error-Types                   |
        #|    Author: Khashayar Alipour            |
        #|=========================================|
        

#___________________________________________________________________________________________________________


AssertionError

'''Raised when the assert statement fails. '''
# وقتی دستور assert با شکست مواجه می‌شود (شرط آن False باشد) این خطا رخ می‌دهد.
# از assert برای بررسی مفروضات در کد استفاده می‌کنیم.


def divide(a, b):
    assert b != 0, "مقسوم‌علیه نمی‌تواند صفر باشد"
    return a / b

# این خطا می‌دهد
print(divide(10, 0))  # AssertionError: مقسوم‌علیه نمی‌تواند صفر باشد

# مثال دیگر
age = -5
assert age >= 0, "سن نمی‌تواند منفی باشد"  # AssertionError: سن نمی‌تواند منفی باشد


#___________________________________________________________________________________________________________



AttributeError

'''Raised on the attribute assignment or reference fails.'''
# وقتی سعی می‌کنید به ویژگی (attribute) یا متدی که یک شیء ندارد دسترسی پیدا کنید، این خطا رخ میدهد. 

# تلاش برای دسترسی به ویژگی ناموجود
my_list = [1, 2, 3]
print(my_list.name)  # AttributeError: 'list' object has no attribute 'name'

# فراخوانی متد ناموجود روی یک شیء
text = "hello"
text.append("!")  # AttributeError: 'str' object has no attribute 'append'

# اشتباه در نام ویژگی
class Person:
    def __init__(self, name):
        self.name = name

p = Person("ali")
print(p.nam)  # AttributeError: 'Person' object has no attribute 'nam' (اشتباه تایپی)


#___________________________________________________________________________________________________________


EOFError

'''Raised when the input() function hits the end-of-file condition.'''
# وقتی تابع input() به انتهای فایل (EOF) برسد و نتواند ورودی بیشتری بخواند، این خطا رخ می‌دهد. 
# معمولاً در موقعیت‌هایی که ورودی از فایل یا پایپ خوانده می‌شود.


# وقتی فایل ورودی تمام شده باشد
with open("input.txt", "w") as f:
    f.write("ali\nreza")  # فقط دو خط

with open("input.txt", "r") as f:
    import sys
    sys.stdin = f
    try:
        name1 = input()  # "ali"
        name2 = input()  # "reza"
        name3 = input()  # EOFError! (دیگر خطی باقی نمانده)
    except EOFError:
        print("به انتهای فایل رسیدیم")



#___________________________________________________________________________________________________________



FloatingPointError 

'''Raised when a floating point operation fails.'''
# وقتی یک عملیات روی اعداد اعشاری (float) با شکست مواجه شود، این خطا رخ می‌دهد. 


# در پایتون استاندارد، این خطا معمولاً رخ نمی‌دهد
# برای فعال کردن آن باید از ماژول fpectl استفاده کرد

import math
try:
    # محاسبات خیلی کوچک
    result = math.exp(1000)  # خیلی بزرگ می‌شود
    print(result)  # این Infinity برمی‌گرداند نه خطا
except FloatingPointError:
    print("خطای ممیز شناور رخ داد")

# در شرایط عادی پایتون، این عملیات به جای خطا، Infinity برمی‌گرداند
print(1e308 * 2)  # inf (بینهایت)
print(1e-324 / 2) # 0.0 (صفر)

# در برخی کتابخانه‌ها مثل numpy ممکن است این خطا را ببینید
import numpy as np
np.seterr(divide='raise')  # تنظیم برای ایجاد خطا
# result = np.array([1.0]) / 0.0  # FloatingPointError


#___________________________________________________________________________________________________________


GeneratorExit 

''''Raised when a generator's close() method is called.'''
# وقتی متد close() روی یک ژنراتور صدا زده می‌شود، این خطا در داخل ژنراتور ایجاد می‌شود تا آن را متوقف کند.

def my_generator():
    try:
        yield 1
        yield 2
        yield 3
    except GeneratorExit:
        print("ژنراتور در حال بسته شدن است!")

# ساخت ژنراتور
gen = my_generator()
print(next(gen))  # 1
print(next(gen))  # 2

# بستن ژنراتور
gen.close()  # "ژنراتور در حال بسته شدن است!" چاپ می‌شود

# بعد از close، دیگر نمی‌توان از ژنراتور استفاده کرد
print(next(gen))  # StopIteration




#___________________________________________________________________________________________________________


IndexError	

'''Raised when the index of a sequence is out of range.'''
# وقتی سعی می‌کنید با اندیسی به عنصری از یک sequence (مانند لیست، رشته، تاپل) دسترسی پیدا کنید که خارج از محدوده آن است، این خطا رخ می‌دهد.

# لیست با ۳ عنصر
my_list = [10, 20, 30]
print(my_list[0])   # 10
print(my_list[2])   # 30
print(my_list[3])   # IndexError: list index out of range

# رشته
text = "python"
print(text[6])      # IndexError: string index out of range

# حلقه با اندیس اشتباه
numbers = [1, 2, 3, 4]
for i in range(len(numbers) + 1):  # اشتباه: +1 اضافی
    print(numbers[i])  # IndexError در آخرین تکرار

# دسترسی با اندیس منفی فراتر از محدوده
print(my_list[-4])  # IndexError: list index out of range



#___________________________________________________________________________________________________________


KeyboardInterrupt	

'''Raised when the user hits the interrupt key (Ctrl+c or delete).'''
# وقتی کاربر برنامه را با کلیدهای میانبر قطع کند (معمولاً Ctrl+C در ترمینال)، این خطا رخ می‌دهد. 
# این راهی برای توقف برنامه در حال اجراست.


# یک حلقه بی‌نهایت
try:
    counter = 0
    while True:
        print(f"شمارنده: {counter}")
        counter += 1
        # برای دیدن خطا، برنامه را اجرا کن و Ctrl+C بزن
except KeyboardInterrupt:
    print("\nبرنامه توسط کاربر متوقف شد!")



#___________________________________________________________________________________________________________



MemoryError	

'''Raised when an operation runs out of memory.'''
# وقتی برنامه حافظه بیشتری از آنچه در دسترس است مصرف کند، این خطا رخ می‌دهد. 
# معمولاً هنگام کار با داده‌های خیلی بزرگ یا ایجاد ساختارهای حجیم.


# ایجاد لیست خیلی بزرگ (ممکن است MemoryError بدهد)
try:
    huge_list = [0] * (10**10)  # لیستی با ۱۰ میلیارد عنصر
except MemoryError:
    print("حافظه کافی نیست!")

# حلقه بی‌نهایت با اضافه کردن به لیست
data = []
try:
    while True:
        data.append("x" * 10**6)  # هر بار ۱ مگابایت اضافه کن
except MemoryError:
    print(f"حافظه پر شد! {len(data)} آیتم ساخته شد")



#___________________________________________________________________________________________________________



NameError	

'''Raised when a variable is not found in the local or global scope.'''
# وقتی سعی می‌کنید از متغیری استفاده کنید که تعریف نشده یا در دسترس نیست، این خطا رخ می‌دهد.


print(x)  # NameError: name 'x' is not defined

name = "ali"
print(nam)  # NameError: name 'nam' is not defined


# استفاده از متغیر قبل از تعریف
print(counter)  # NameError
counter = 10

# متغیر محلی خارج از محدوده
def my_func():
    y = 20
    return y

my_func()
print(y)  # NameError: name 'y' is not defined (y فقط داخل تابع است)



#___________________________________________________________________________________________________________



NotImplementedError

'''Raised by abstract methods.'''
# وقتی متدی را صدا می‌زنید که باید در کلاس فرزند پیاده‌سازی (override) شود ولی هنوز پیاده‌سازی نشده، این خطا رخ می‌دهد.


# کلاس پایه با متدی که باید در کلاس فرزند پیاده‌سازی شود
class Animal:
    def make_sound(self):
        raise NotImplementedError("زیرکلاس‌ها باید این متد را پیاده‌سازی کنند")

# کلاس فرزند که متد را پیاده‌سازی کرده
class Dog(Animal):
    def make_sound(self):
        return "واق واق!"

# کلاس فرزند که متد را پیاده‌سازی نکرده
class Cat(Animal):
    pass

# کار با اشیا
dog = Dog()
print(dog.make_sound())  # "واق واق!"

cat = Cat()
cat.make_sound()  # NotImplementedError: زیرکلاس‌ها باید این متد را پیاده‌سازی کنند


#___________________________________________________________________________________________________________



OSError	

'''Raised when a system operation causes a system-related error.'''
# وقتی یک عملیات سیستمی (مثل کار با فایل، دایرکتوری یا شبکه) با خطا مواجه شود، این خطا رخ می‌دهد.
# این خطای والد برای بسیاری از خطاهای مربوط به سیستم است.

# باز کردن فایلی که وجود ندارد
try:
    with open("file_not_exists.txt", "r") as f:
        content = f.read()
except OSError as e:
    print(f"خطای سیستمی: {e}")  # [Errno 2] No such file or directory

# ایجاد دایرکتوری در مسیر غیرمجاز
import os
try:
    os.mkdir("/root/my_folder")  # نیاز به مجوز ادمین دارد
except OSError as e:
    print(f"خطا: {e}")  # Permission denied

# حذف فایلی که وجود ندارد
try:
    os.remove("nonexistent.txt")
except OSError as e:
    print(f"خطا: {e}")  # No such file or directory



#___________________________________________________________________________________________________________



OverflowError	

'''Raised when the result of an arithmetic operation is too large to be represented.'''
# وقتی نتیجه یک عملیات ریاضی آنقدر بزرگ باشد که در حافظه قابل نمایش نباشد، این خطا رخ می‌دهد.


# اعداد اعشاری خیلی بزرگ
import math

try:
    result = math.exp(1000)  # e^1000 خیلی بزرگ است
    print(result)  # در پایتون این بینهایت (inf) برمی‌گرداند نه خطا
except OverflowError:
    print("عدد خیلی بزرگ است!")

# محاسباتی که واقعاً OverflowError می‌دهند
try:
    huge_float = 1e400  # 10 به توان 400 (بسیار بزرگ)
except OverflowError:
    print("عدد اعشاری خیلی بزرگ است!")

# مثال با خروج از محدوده
x = 10.0 ** 1000  # این float است و OverflowError می‌دهد
# x = 10 ** 1000  # این int است و مشکلی ندارد (پایتون int نامحدود است)

# تشخیص در عملیات
try:
    result = 2.0 ** 10000  # خیلی بزرگ
except OverflowError:
    print("بیش از حد بزرگ!")



#___________________________________________________________________________________________________________



RuntimeError	

'''Raised when an error does not fall under any other category.'''
# وقتی خطایی رخ می‌دهد که در دسته‌بندی خطاهای دیگر قرار نمی‌گیرد، این خطا به عنوان یک خطای عمومی اجرایی صدا زده می‌شود.

# خطای عمومی در موقعیت‌های خاص
def divide_numbers(a, b):
    if b == 0:
        raise RuntimeError("تقسیم بر صفر مجاز نیست، اما این یک خطای عمومی است!")
    return a / b

try:
    result = divide_numbers(10, 0)
except RuntimeError as e:
    print(f"خطای اجرایی: {e}")



#___________________________________________________________________________________________________________



SyntaxError	

'''Raised by the parser when a syntax error is encountered.'''
# وقتی کد پایتون شما قوانین نوشتاری (گرامر) زبان را رعایت نکرده باشد، این خطا توسط مفسر در زمان خواندن کد رخ می‌دهد.

# فراموش کردن دو نقطه (:) در انتهای if
x = 10
if x > 5  # SyntaxError: expected ':'
    print("x بزرگتر است")

# پرانتز ناقص
print("سلام دنیا!"  # SyntaxError: unexpected EOF while parsing

# استفاده از علامت مساوی اشتباه در شرط
if x = 5:  # SyntaxError: invalid syntax (باید == باشد)
    print("x برابر 5 است")

# رشته بدون بسته شدن
text = "سلام  # SyntaxError: EOL while scanning string literal

# کلیدواژه اشتباه
fonction my_function():  # SyntaxError: invalid syntax (fonction باید def باشد)
    pass


#___________________________________________________________________________________________________________


IndentationError	

'''Raised when there is an incorrect indentation.'''


# مخلوط کردن تب و فاصله (space)
def calculate():
    x = 5
	y = 10  # این تب است در حالی که بقیه فاصله هستند
    # IndentationError: inconsistent use of tabs and spaces in indentation

# بلوک بدون تورفتگی
if 5 > 3:
print("پنج بزرگتر است")  # IndentationError: expected an indented block


#___________________________________________________________________________________________________________



TabError	

'''Raised when the indentation consists of inconsistent tabs and spaces.'''

# ترکیب تب و فاصله در یک بلوک
def calculate():
    x = 5      # اینجا از ۴ فاصله استفاده شده
	x = 10     # اینجا از تب استفاده شده (معادل ۸ فاصله)
    # TabError: inconsistent use of tabs and spaces in indentation



#___________________________________________________________________________________________________________



SystemError	

'''Raised when the interpreter detects internal error.'''
# وقتی مفسر پایتون خودش با یک مشکل داخلی مواجه شود، این خطا رخ می‌دهد.
# این خطا معمولاً نشان‌دهنده یک باگ در خود پایتون است، نه در کد شما.


# وقتی یک ماژول توسعه‌یافته با C/C++ مشکل داشته باشد
try:
    # فرض کنید یک ماژول خارجی نصب شده
    import some_broken_extension
except SystemError:
    print("ماژول توسعه‌دهنده باعث خطای داخلی شده")



#___________________________________________________________________________________________________________



SystemExit	

'''Raised by the sys.exit() function.'''
# وقتی تابع sys.exit() صدا زده می‌شود، این خطا برای خروج از برنامه ایجاد می‌شود.

import sys

# خروج ساده از برنامه
def check_age(age):
    if age < 0:
        print("سن نمی‌تواند منفی باشد")
        sys.exit(1)  # خروج با کد خطا
    print(f"سن شما: {age}")

check_age(-5)  # برنامه اینجا متوقف می‌شود



#___________________________________________________________________________________________________________



TypeError	

'''Raised when a function or operation is applied to an object of an incorrect type.'''
# وقتی عملیاتی را روی شیء با نوع (type) اشتباه انجام می‌دهید، این خطا رخ می‌دهد. مثلاً جمع کردن عدد با رشته یا فراخوانی متدی که آن شیء ندارد.

# جمع عدد و رشته
x = 5
y = "10"
print(x + y)  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# فراخوانی تابع با آرگومان اشتباه
len(123)  # TypeError: object of type 'int' has no len()

# استفاده از متد رشته روی عدد
name = 123
name.upper()  # TypeError: 'int' object has no attribute 'upper'

# اندیس‌گذاری روی عدد
numbers = 12345
print(numbers[0])  # TypeError: 'int' object is not subscriptable

# تابعی که نوع خاصی انتظار دارد
def double(x):
    return x * 2

print(double(5))     # 10 (int)
print(double("hi"))  # "hihi" (str - این کار می‌کند)
print(double([1,2])) # [1,2,1,2] (list - این هم کار می‌کند)
# اما:
def greet(names):
    return "سلام " + names  # انتظار رشته دارد

greet(["ali", "sara"])  # TypeError: can only concatenate str (not "list") to str



#___________________________________________________________________________________________________________



ValueError	

'''Raised when a function gets an argument of correct type but improper value.'''
# وقتی تابعی آرگومانی با نوع درست (مثلاً عدد) دریافت کند اما مقدار آن نامناسب باشد (مثلاً عدد منفی جایی که نباید)، این خطا رخ می‌دهد.


# تبدیل رشته به عدد - رشته عددی نیست
int("abc")  # ValueError: invalid literal for int() with base 10: 'abc'

# ریشه دوم عدد منفی
import math
math.sqrt(-4)  # ValueError: math domain error

# اندیس در رشته - شروع بزرگتر از پایان
text = "python"
text[5:1]  # این خطا نمی‌دهد (رشته خالی)
text[10]   # IndexError (نوع دیگر)

# متد find با مقدار نامناسب
[1, 2, 3].index(10)  # ValueError: 10 is not in list

# تابع سفارشی با مقدار نامناسب
def set_age(age):
    if age < 0 or age > 150:
        raise ValueError("سن باید بین ۰ تا ۱۵۰ باشد")
    print(f"سن: {age}")

set_age(25)   # "سن: 25"
set_age(-5)   # ValueError: سن باید بین ۰ تا ۱۵۰ باشد


#___________________________________________________________________________________________________________



ZeroDivisionError	

'''Raised when the second operand of a division or module operation is zero.'''
# وقتی سعی می‌کنید عددی را بر صفر تقسیم کنید یا از صفر باقیمانده (modulo) بگیرید، این خطا رخ می‌دهد.

# تقسیم بر صفر
x = 10
y = 0
result = x / y  # ZeroDivisionError: division by zero

# باقیمانده بر صفر
result = 10 % 0  # ZeroDivisionError: integer modulo by zero

# تقسیم صحیح بر صفر
result = 10 // 0  # ZeroDivisionError: integer division or modulo by zero

# مدیریت خطا
try:
    result = 10 / 0
except ZeroDivisionError:
    print("تقسیم بر صفر مجاز نیست!")


#___________________________________________________________________________________________________________


IndexError

'''The IndexError is thrown when trying to access an item at an invalid index.'''
# وقتی سعی می‌کنید با اندیسی به عنصری از یک sequence (مانند لیست، رشته، تاپل) دسترسی پیدا کنید که خارج از محدوده آن است، این خطا رخ می‌دهد.

# لیست با ۳ عنصر
my_list = [10, 20, 30]
print(my_list[0])   # 10
print(my_list[2])   # 30
print(my_list[3])   # IndexError: list index out of range

# دسترسی با اندیس منفی فراتر از محدوده
print(my_list[-4])  # IndexError: list index out of range



#___________________________________________________________________________________________________________



ModuleNotFoundError

''''The ModuleNotFoundError is thrown when a module could not be found.'''
# وقتی پایتون نمی‌تواند ماژولی را که می‌خواهید (import) کنید پیدا کند، این خطا رخ می‌دهد.

# ماژولی که در سیستم نصب نیست
import pandas as pd  # ModuleNotFoundError: No module named 'pandas'

# ماژولی با نام اشتباه
import numpy as np  # اگر اشتباهاً بنویسیم:
import nump  # ModuleNotFoundError: No module named 'nump'

# ماژول شخصی که در مسیر نیست
# فرض کنید فایل mymodule.py در پوشه فعلی نیست
import mymodule  # ModuleNotFoundError: No module named 'mymodule'



#___________________________________________________________________________________________________________



KeyError

'''The KeyError is thrown when a key is not found.'''
# وقتی سعی می‌کنید با یک کلید به مقدار در دیکشنری دسترسی پیدا کنید که آن کلید وجود ندارد، این خطا رخ می‌دهد.


person = {"name": "ali", "age": 25, "city": "tehran"}
print(person["name"])  # "ali"
print(person["job"])   # KeyError: 'job'


users = {
    "user1": {"name": "ali", "age": 25},
    "user2": {"name": "sara", "age": 30}
}
print(users["user3"])  # KeyError: 'user3'




#___________________________________________________________________________________________________________


ImportError

'''The ImportError is thrown when a specified function can not be found.'''
# وقتی ماژولی پیدا می‌شود اما یک تابع یا متغیر خاص در آن ماژول وجود ندارد، این خطا رخ می‌دهد.
# همچنین زمانی که ماژول کلی پیدا نشود هم می‌تواند رخ دهد.


# ماژول وجود دارد اما تابع درخواستی در آن نیست
import math
from math import square_root  # ImportError: cannot import name 'square_root' from 'math'

# متغیری که در ماژول وجود ندارد
from os import not_existing_variable  # ImportError: cannot import name 'not_existing_variable'

# سعی در import از ماژولی که اصلاً وجود ندارد
import pandas as pd  # اگر pandas نصب نباشد: ModuleNotFoundError (زیرمجموعه ImportError)




#___________________________________________________________________________________________________________



StopIteration

'''The StopIteration is thrown when the next() function goes beyond the iterator items.'''
# وقتی تابع next() فراتر از آخرین عنصر یک (iterator) برود و عنصر دیگری برای برگرداندن نباشد، این خطا رخ می‌دهد. این خطا نشان‌دهنده پایان یافتن iterator است.

# یک لیست ساده
my_list = [1, 2, 3]
it = iter(my_list)

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
print(next(it))  # StopIteration (عنصری باقی نمانده)



#___________________________________________________________________________________________________________






