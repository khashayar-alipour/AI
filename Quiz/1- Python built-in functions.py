

     #|=========================================|
     #|    Quiz 1                               |
     #|    Python - Built-in functions          |
     #|    Written by: Khashayar Alipour        |
     #|    2026                                 |
     #|=========================================|


#________________________________________________________________________________________________________________________


'''abs(number, /):
Return the absolute value of a number. The argument may be an integer, a floating-point number, or 
an object implementing __abs__(). If the argument is a complex number, its magnitude is returned. '''
# برگرداندن مقدار مطلق (absolute value) یک عدد (عدد بدون در نظر گرفتن علامت منفی).

# اعداد صحیح
print(abs(-5))   # 5
print(abs(3))    # 3

# اعداد اعشاری
print(abs(-3.14))  # 3.14
print(abs(2.5))    # 2.5

# اعداد مختلط (Complex numbers)
print(abs(3 + 4j))  # 5.0 (بزرگی عدد مختلط)


# _______________________________________________________________________________________________________________________


aiter()
'''aiter(async_iterable, /):
Return an asynchronous iterator for an asynchronous iterable. Equivalent to calling x.__aiter__(). '''
# دریافت یک iterator ناهمگام (asynchronous) از یک شیء تکرارپذیر ناهمگام.
# این تابع نسخه‌ی ناهمگام تابع iter() است و معمولاً برای کار با حلقه‌های async for استفاده می‌شود.

import asyncio

# یک تکرارگر ناهمگام ساده
class AsyncCounter:
    def __init__(self, stop):
        self.stop = stop
        self.current = 0
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.current >= self.stop:
            raise StopAsyncIteration
        await asyncio.sleep(0.1)  # شبیه‌سازی عملیات ناهمگام
        self.current += 1
        return self.current - 1

async def main():
    # استفاده مستقیم از aiter و anext
    counter = AsyncCounter(3)
    it = aiter(counter)
    
    print(await anext(it))  # 0
    print(await anext(it))  # 1
    print(await anext(it))  # 2

asyncio.run(main())



# _______________________________________________________________________________________________________________________


'''all(iterable, /)
Return True if all elements of the iterable are true (or if the iterable is empty). '''
# بررسی می‌کند که آیا همه عناصر یک iterable (مانند لیست) مقدار True دارند یا نه.
# اگر همه True باشند، True برمی‌گرداند، در غیر این صورت False.

# همه اعداد مثبت هستند
print(all([1, 2, 3, 4]))     # True
print(all([1, 0, 3, 4]))     # False (چون 0 معادل False است)

# بررسی شرط روی لیست
numbers = [2, 4, 6, 8]
print(all(n % 2 == 0 for n in numbers))  # True (همه زوج هستند)

# لیست خالی
print(all([]))  # True (لیست خالی همیشه True برمی‌گرداند)

# ترکیب با مقادیر مختلف
print(all([True, True, True]))    # True
print(all([True, False, True]))   # False


# _______________________________________________________________________________________________________________________


'''any(iterable, /)
Return True if any element of the iterable is true. If the iterable is empty, return False. '''
# آیا حداقل یکی از عناصر یک iterable مقدار True دارد یا نه. اگر حداقل یکی True باشد، True برمی‌گرداند، وگرنه False.

# حداقل یک عدد مثبت وجود دارد؟
print(any([0, 0, 5, 0]))     # True (چون 5 معادل True است)
print(any([0, 0, 0, 0]))     # False (همه صفر هستند)

# بررسی وجود عدد زوج در لیست
numbers = [1, 3, 5, 7, 8]
print(any(n % 2 == 0 for n in numbers))  # True (چون 8 زوج است)

# لیست خالی
print(any([]))  # False

# ترکیب با مقادیر مختلف
print(any([False, False, True]))   # True
print(any([False, False, False]))  # False


# _______________________________________________________________________________________________________________________



'''ascii(object, /):
As repr(), return a string containing a printable representation of an object, but escape the non-ASCII characters
 in the string returned by repr() using \ x, \ u, or \ U escapes. '''
# برگرداندن یک رشته که نمایش قابل چاپ اشیاء را با کاراکترهای غیر ASCII به صورت escaped (با \x, \u, \U) نشان می‌دهد.

# متن فارسی (کاراکترهای غیر ASCII)
text = "سلام دنیا!"
print(ascii(text))  # '\u0633\u0644\u0627\u0645 \u062f\u0646\u06cc\u0627!'

# مقایسه با repr
print(repr(text))   # 'سلام دنیا!'
print(ascii(text))  # '\u0633\u0644\u0627\u0645 \u062f\u0646\u06cc\u0627!'

# کاراکترهای خاص
print(ascii("😊"))  # '\U0001f60a'
print(ascii(" café "))  # ' caf\xe9 '



# _______________________________________________________________________________________________________________________



'''bin(integer, /):
Convert an integer number to a binary string prefixed with “0b”. '''
# تبدیل یک عدد صحیح به رشته‌ی باینری (مبنای ۲) که با '0b' شروع می‌شود.

# تبدیل اعداد به باینری
print(bin(5))    # '0b101'  (5 در مبنای ۲ = 101)
print(bin(10))   # '0b1010' (10 در مبنای ۲ = 1010)
print(bin(16))   # '0b10000'

# کاربرد در عملیات بیتی
x = 5  # 0b101
y = 3  # 0b011
print(bin(x & y))  # '0b1' (AND بیتی: 001)
print(bin(x | y))  # '0b111' (OR بیتی: 111)


# _______________________________________________________________________________________________________________________


'''class bool(object=False, /):
Return a Boolean value, i.e. one of True or False. The bool class is a subclass of int. '''
# تبدیل یک مقدار به بولین (True یا False) بر اساس truthiness آن مقدار در پایتون.

# مقادیری که False می‌شوند
print(bool(0))       # False
print(bool(""))      # False (رشته خالی)
print(bool([]))      # False (لیست خالی)
print(bool(None))    # False

# مقادیری که True می‌شوند
print(bool(1))       # True
print(bool("hello")) # True (رشته غیرخالی)
print(bool([1,2]))   # True (لیست غیرخالی)
print(bool(-5))      # True (اعداد غیرصفر)

# استفاده در شرط‌ها
name = "ali"
if bool(name):  # معادل if name:
    print("نام وجود دارد")



# _______________________________________________________________________________________________________________________



'''callable(object, /):
Return True if the object argument appears callable, False if not. If this returns True, it is still possible that a call
 fails, but if it is False, calling object will never succeed.'''
 # بررسی می‌کند که آیا یک شیء قابل فراخوانی (callable) است یا نه (یعنی می‌توان آن را مثل تابع صدا زد).

# توابع قابل فراخوانی هستند
def my_func():
    pass

print(callable(my_func))      # True
print(callable(print))        # True

# کلاس‌ها قابل فراخوانی هستند (برای ساخت نمونه)
class MyClass:
    pass

print(callable(MyClass))      # True

# اشیای معمولی قابل فراخوانی نیستند
x = 5
print(callable(x))            # False
text = "hello"
print(callable(text))         # False

# اشیایی که متد __call__ دارند قابل فراخوانی هستند
class CallableClass:
    def __call__(self):
        print("من قابل فراخوانی هستم")

obj = CallableClass()
print(callable(obj))           # True


# _______________________________________________________________________________________________________________________


'''chr(codepoint, /):
Return the string representing a character with the specified Unicode code point. For example, chr(97) returns the
 string 'a', while chr(8364) returns the string '€'. '''
# برگرداندن کاراکتر متناظر با یک کد یونیکد (عدد صحیح). این تابع برعکس ord() عمل می‌کند.

# تبدیل کد یونیکد به کاراکتر
print(chr(97))     # 'a'
print(chr(65))     # 'A'
print(chr(48))     # '0'
print(chr(1593))   # 'ع' (کد یونیکد حرف عربی)

# کاراکترهای خاص
print(chr(8364))   # '€' (یورو)
print(chr(169))    # '©' (کپی‌رایت)
print(chr(9829))   # '♥' (قلب)


# _______________________________________________________________________________________________________________________



'''@classmethod:
Transform a method into a class method. A class method receives the class as an implicit first argument, just like
 an instance method receives the instance. To declare a class method, use this idiom:  '''
# تبدیل یک متد به class method که به جای instance، خود کلاس را به عنوان اولین آرگومان دریافت می‌کند (معمولاً با نام cls).


class Person:
    species = "human"
    
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def get_species(cls):
        return cls.species
    
    @classmethod
    def create_anonymous(cls):
        return cls("ناشناس")

# فراخوانی متد کلاس
print(Person.get_species())  # "human"

# ساخت نمونه با متد کلاس
anonymous = Person.create_anonymous()
print(anonymous.name)  # "ناشناس"

# از طریق نمونه هم می‌شود فراخوانی کرد
p = Person("ali")
print(p.get_species())  # "human"



# _______________________________________________________________________________________________________________________



'''
class complex(number=0, /)
class complex(string, /)
class complex(real=0, imag=0)
Convert a single string or number to a complex number, or create a complex number from real and imaginary parts. If the 
argument is a string, it must contain either a real part (in the same format as for float()) or an imaginary 
part (in the same format but with a 'j' or 'J' suffix), or both real and imaginary parts (the sign of the imaginary part
is mandatory in this case). '''
# ساخت یک عدد مختلط (complex number) با بخش حقیقی و موهومی.

# ساخت عدد مختلط با دو بخش
c1 = complex(3, 4)     # 3 + 4j
print(c1)              # (3+4j)

# از روی رشته
c2 = complex("2+5j")
print(c2)              # (2+5j)

# فقط بخش حقیقی
c3 = complex(5)        # 5 + 0j
print(c3)              # (5+0j)

# بدون آرگومان
c4 = complex()         # 0j
print(c4)              # 0j

# دسترسی به بخش‌ها
print(c1.real)         # 3.0 (بخش حقیقی)
print(c1.imag)         # 4.0 (بخش موهومی)



# _______________________________________________________________________________________________________________________



e = 'string'
dir(e)  # str functions
'''dir(object, /):
Without arguments, return the list of names in the current local scope. With an argument, attempt to return a list of valid
 attributes for that object. '''


# _______________________________________________________________________________________________________________________



'''divmod(a, b, /):
Take two (non-complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when
 using integer division. '''
# برگرداندن یک تاپل شامل (خارج قسمت، باقیمانده) از تقسیم دو عدد.

# تقسیم اعداد صحیح
result = divmod(10, 3)
print(result)       # (3, 1)  یعنی 10 = 3*3 + 1

# دسترسی به خارج قسمت و باقیمانده
quotient, remainder = divmod(17, 5)
print(quotient)     # 3
print(remainder)    # 2

# اعداد اعشاری
print(divmod(10.5, 3))  # (3.0, 1.5)

# کاربرد: تبدیل ثانیه به دقیقه و ثانیه
total_seconds = 125
minutes, seconds = divmod(total_seconds, 60)
print(f"{minutes} دقیقه و {seconds} ثانیه")  # "2 دقیقه و 5 ثانیه"


# _______________________________________________________________________________________________________________________



'''enumerate(iterable, start=0):
Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration.'''
# اضافه کردن شمارنده (اندیس) به یک iterable و برگرداندن تاپل‌های (اندیس, مقدار) برای پیمایش آسان‌تر.

# پیمایش لیست با اندیس
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry

# شروع شمارنده از عدد دلخواه
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
# 1: apple
# 2: banana
# 3: cherry

# تبدیل به لیست تاپل‌ها
print(list(enumerate(fruits)))  # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]




# _______________________________________________________________________________________________________________________



'''eval(source, /, globals=None, locals=None):
Parameters:
source (str | code object) – A Python expression.
globals (dict | None) – The global namespace (default: None).
locals (mapping | None) – The local namespace (default: None).

Returns:
The result of the evaluated expression.'''
# اجرای یک رشته به عنوان کد پایتون و برگرداندن نتیجه.

# ارزیابی عبارات ریاضی
print(eval("2 + 3 * 4"))      # 14

# استفاده از متغیرها
x = 10
print(eval("x * 2"))          # 20

# اجرای توابع
print(eval("len('hello')"))   # 5

# ساختن اشیا
print(eval("[1, 2, 3, 4]"))   # [1, 2, 3, 4]

# هشدار: eval می‌تواند خطرناک باشد!
user_input = "__import__('os').system('ls')"  # این می‌تواند دستورات خطرناک اجرا کند!
# eval(user_input)  # هرگز eval را روی ورودی کاربر اجرا نکنید!


# _______________________________________________________________________________________________________________________



filter()
# در پایتون، تابع filter() برای فیلتر کردن عناصر یک iterable (مانند لیست، تاپل و غیره) بر اساس یک شرط استفاده
# لیستی از اسامی
names = ["ali", "reza", "sara", "mohammad", "neda"]

# تابعی برای انتخاب نام‌های ۳ حرفی


def is_three_letter(name):
    return len(name) == 3


# فیلتر کردن
three_letter_names = list(filter(is_three_letter, names))

print(three_letter_names)  # ['ali']
'''filter(function, iterable, /):
Construct an iterator from those elements of iterable for which function is true. If function is None, the identity
 function is assumed, that is, all elements of iterable that are false are removed.'''


# _______________________________________________________________________________________________________________________


float('+1.23')  # 1.23
float('   -12345\n')  # -12345.0
float('1e-003')  # 0.001
float('+1E6')  # 1000000.0
float('-Infinity')  # -inf

'''class float(number=0.0, /)
   class float(string, /):
Return a floating-point number constructed from a number or a string. '''


# _______________________________________________________________________________________________________________________


''''class frozenset(iterable=(), /)'''
# ایجاد یک مجموعه(set) که mutable نیست - بعد از ساخته شدن نمی‌توان عنصری به آن اضافه یا از آن حذف کرد.

# ساختن یک frozenset از لیست اعداد
my_set = frozenset([1, 2, 3, 2, 1])
print(my_set)  # frozenset({1, 2, 3})

# این خطا می‌دهد چون frozenset قابل تغییر نیست
my_set.add(4)  # AttributeError!


# _______________________________________________________________________________________________________________________


globals()
'''Return the dictionary implementing the current module namespace. For code within functions, this is set when the 
function is defined and remains the same regardless of where the function is called. '''
# برگرداندن یک دیکشنری از همه متغیرهای global که در حال حاضر تعریف شده‌اند.

x = 10
y = "hi"

my_dict = globals()
print(my_dict["x"])  # 10
print(my_dict["y"])  # "hi"


# _______________________________________________________________________________________________________________________


'''getattr(object, name, /)
getattr(object, name, default, /)'''
# دریافت مقدار یک ویژگی (attribute) از یک شیء با استفاده از نام آن ویژگی (به صورت رشته).
'''Return the value of the named attribute of object. name must be a string. If the string is the name of one of the
 object’s attributes, the result is the value of that attribute. If the named attribute does not exist, default is returned
 if provided, otherwise AttributeError is raised.'''


class Person:
    name = "ali"
    age = 25


p = Person()
# دسترسی به ویژگی با نام آن
print(getattr(p, "name"))  # "ali"
print(getattr(p, "age"))   # 25
print(getattr(p, "city", "tehran"))  # "tehran" (مقدار پیش‌فرض)


# _______________________________________________________________________________________________________________________



''''hasattr(object, name, /)'''
'''The arguments are an object and a string. The result is True if the string is the name of one of the object’s 
attributes, False if not. '''
# بررسی میکند که آیا یک شیء ویژگی (attribute) مشخصی دارد یا نه (خروجی True یا False).

class Car:
    color = "red"
    year = 2020

my_car = Car()
print(hasattr(my_car, "color"))  # True
print(hasattr(my_car, "model"))   # False

if hasattr(my_car, "year"):
    print("این ماشین سال ساخت دارد!")
    
    
# _______________________________________________________________________________________________________________________



'''hash(object, /):
Return the hash value of the object (if it has one).'''
# مقدار hash یک شیء را برمی‌گرداند. از این مقدار برای مقایسه سریع کلیدها در دیکشنری و مجموعه‌ها استفاده می‌شود.

# محاسبه هش برای اشیای غیرقابل تغییر (immutable)
print(hash("hello"))     # یک عدد صحیح (مثلاً -8103489041116869005)
print(hash(42))          # 42
print(hash((1, 2, 3)))   # یک عدد صحیح

# اشیای قابل تغییر مثل لیست هش ندارند
print(hash([1, 2, 3]))  # TypeError! 


#_______________________________________________________________________________________________________________________


'''hex(integer, /):
Convert an integer number to a lowercase hexadecimal string prefixed with “0x”. '''
# تبدیل یک عدد صحیح به رشته‌ی hexadecimal (مبنای ۱۶) که با '0x' شروع می‌شود.

print(hex(10))    # '0xa'
print(hex(255))   # '0xff'
print(hex(16))    # '0x10'

# کاربرد عملی: نمایش رنگ‌ها در HTML/CSS
color_rgb = 255
color_hex = hex(color_rgb)[2:]  # حذف '0x'
print(f"#{color_hex}00ff")      # #ff00ff



#_______________________________________________________________________________________________________________________


'''id(object, /):
Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant for this object
 during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value. '''
# برگرداندن یک شماره منحصربه‌فرد (آدرس حافظه) برای هر شیء در طول عمر آن. 

x = 10
y = x
z = 20

print(id(x))  # مثلاً 140735869395632
print(id(y))  # همان عدد بالا (چون به یک شیء اشاره می‌کنند)
print(id(z))  # یک عدد متفاوت

# بررسی اینکه دو متغیر به یک شیء اشاره می‌کنند
print(id(x) == id(y))  # True 
 

#_______________________________________________________________________________________________________________________



'''class int(number=0, /)
class int(string, /, base=10):
Return an integer object constructed from a number or a string, or return 0 if no arguments are given.'''

int(123.45)   #123
int('123')   #123
int('   -12_345\n')   #-12345
int('FACE', 16)   #64206
int('0xface', 0)   #64206
int('01110011', base=2)   #115


#_______________________________________________________________________________________________________________________



'''isinstance(object, classinfo, /)
Return True if the object argument is an instance of the classinfo argument. If object is not an object of the given 
type, the function always returns False.'''
# بررسی می‌کند که آیا یک شیء از نوع مشخص‌شده (یا یکی از زیرنوع‌های آن) است یا نه.

# بررسی انواع مختلف داده
print(isinstance(5, int))        # True
print(isinstance("hello", str))  # True
print(isinstance([1, 2], list))  # True
print(isinstance(5, str))        # False

# بررسی با چند نوع همزمان
print(isinstance(5, (int, str)))  # True (چون int است)
print(isinstance("hi", (int, str)))  # True (چون str است)



#_______________________________________________________________________________________________________________________



'''issubclass(class, classinfo, /)
Return True if class is a subclass of classinfo. A class is considered a subclass of itself. classinfo may be a tuple 
of class objects or a Union Type, in which case return True if class is a subclass of any entry in classinfo. In any other 
case, a TypeError exception is raised. '''

# بررسی می‌کند که آیا یک کلاس، زیرکلاس (subclass) کلاس دیگری است یا نه.
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

print(issubclass(Dog, Animal))  # True
print(issubclass(Cat, Animal))  # True
print(issubclass(Dog, Cat))     # False

# بررسی با چند کلاس همزمان
print(issubclass(Dog, (Animal, Cat)))  # True (چون Animal را شامل می‌شود)



#_______________________________________________________________________________________________________________________




'''iter(callable, sentinel, /)'''
# ایجاد یک iterator که تا رسیدن به مقدار sentinel به فراخوانی یک تابع ادامه می‌دهد.

import random

# اعداد تصادفی تولید کن تا به عدد 5 برسی
def random_number():
    return random.randint(1, 10)

for num in iter(random_number, 5):
    print(f"عدد {num} آمد (هنوز 5 نیامده)")
    
print("به 5 رسیدیم!")


#_______________________________________________________________________________________________________________________



'''len(object, /)
Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, 
tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).'''

print(len("سلام"))        # 4
print(len([1, 2, 3, 4]))  # 4
print(len({"a":1, "b":2}))  # 2
print(len((5, 6, 7)))     # 3



#_______________________________________________________________________________________________________________________



'''locals()
Return a mapping object representing the current local symbol table, with variable names as the keys, and their currently 
bound references as the values.'''

def my_function():
    name = "ali"
    age = 30
    city = "tehran"
    
    locals_dict = locals()
    print(locals_dict)
    # {'name': 'ali', 'age': 30, 'city': 'tehran'}
    
    # دسترسی به متغیرها از طریق دیکشنری
    print(locals_dict["name"])  # ali

my_function()


#_______________________________________________________________________________________________________________________



'''map(function, iterable, /, *iterables, strict=False)
Return an iterator that applies function to every item of iterable, yielding the results. If additional iterables arguments 
are passed, function must take that many arguments and is applied to the items from all iterables in parallel. With multiple 
iterables, the iterator stops when the shortest iterable is exhausted. If strict is True and one of the iterables is 
exhausted before the others, a ValueError is raised.'''
# اعمال یک تابع به تمام عناصر یک یا چند iterable و برگرداندن یک iterator از نتایج.

# اعمال تابع به یک لیست
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16]

# اعمال تابع به دو لیست (جمع عناصر متناظر)
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print(sums)  # [11, 22, 33]


#_______________________________________________________________________________________________________________________


'''max(iterable, /, *, key=None)
max(iterable, /, *, default, key=None)
max(arg1, arg2, /, *args, key=None)
Return the largest item in an iterable or the largest of two or more arguments.'''

# برگرداندن بزرگترین عنصر در یک iterable یا بزرگترین بین چند آرگومان.

# بزرگترین عدد در لیست
print(max([3, 7, 2, 9, 1]))        # 9

# بزرگترین بین چند عدد
print(max(5, 2, 8, 1))              # 8

# بزرگترین رشته (بر اساس حروف الفبا)
print(max(["ali", "reza", "sara"]))  # "sara"

# با key برای معیار سفارشی
words = ["python", "java", "c++", "javascript"]
print(max(words, key=len))           # "javascript" (بلندترین کلمه)

# با default برای iterable خالی
empty_list = []
print(max(empty_list, default="خالی است"))  # "خالی است"


#_______________________________________________________________________________________________________________________



'''min(iterable, /, *, key=None)
min(iterable, /, *, default, key=None)
min(arg1, arg2, /, *args, key=None)
Return the smallest item in an iterable or the smallest of two or more arguments.'''
# برگرداندن کوچکترین عنصر در یک iterable یا کوچکترین بین چند آرگومان.

# کوچکترین عدد در لیست
print(min([3, 7, 2, 9, 1]))        # 1

# کوچکترین بین چند عدد
print(min(5, 2, 8, 1))              # 1

# کوچکترین رشته (بر اساس حروف الفبا)
print(min(["ali", "reza", "sara"]))  # "ali"

# با key برای معیار سفارشی
words = ["python", "java", "c++", "javascript"]
print(min(words, key=len))           # "c++" (کوتاهترین کلمه)

# با default برای iterable خالی
empty_list = []
print(min(empty_list, default="خالی است"))  # "خالی است"


#_______________________________________________________________________________________________________________________



'''next(iterator, /)
next(iterator, default, /)
Retrieve the next item from the iterator by calling its __next__() method. If default is given, it is returned if the 
iterator is exhausted, otherwise StopIteration is raised.'''
# دریافت عنصر بعدی از یک iterator. اگر iterator تمام شده باشد، مقدار پیش‌فرض برمی‌گرداند یا خطای StopIteration می‌دهد.

# کار با iterator یک لیست
my_list = [10, 20, 30]
it = iter(my_list)

print(next(it))        # 10
print(next(it))        # 20
print(next(it))        # 30
# print(next(it))      # StopIteration! (خطا)

# استفاده از مقدار پیش‌فرض
it2 = iter([1, 2, 3])
print(next(it2, "تموم شد"))  # 1
print(next(it2, "تموم شد"))  # 2
print(next(it2, "تموم شد"))  # 3
print(next(it2, "تموم شد"))  # "تموم شد" (بدون خطا)


#_______________________________________________________________________________________________________________________



'''oct(integer, /)
Convert an integer number to an octal string prefixed with “0o”. '''
#  تبدیل یک عدد صحیح به رشته‌ی octal (مبنای ۸) که با '0o' شروع می‌شود.

# تبدیل اعداد به مبنای ۸
print(oct(8))    # '0o10'  (چون 8 در مبنای ۸ میشود 10)
print(oct(10))   # '0o12'
print(oct(16))   # '0o20'


#_______________________________________________________________________________________________________________________



'''open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
Open file and return a corresponding file object. If the file cannot be opened, an OSError is raised.'''
# باز کردن یک فایل و برگرداندن یک شیء فایل برای خواندن، نوشتن یا ویرایش آن.

# نوشتن در فایل
with open("test.txt", "w", encoding="utf-8") as file:
    file.write("سلام دنیا!")

# خواندن از فایل
with open("test.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)  # "سلام دنیا!"

# اضافه کردن به انتهای فایل
with open("test.txt", "a", encoding="utf-8") as file:
    file.write("\nخط جدید")


#_______________________________________________________________________________________________________________________



'''ord(character, /):
Return the ordinal value of a character.'''
# برگرداندن کد یونیکد (عدد صحیح) متناظر با یک کاراکتر.

# تبدیل کاراکتر به کد یونیکد
print(ord('a'))     # 97
print(ord('A'))     # 65
print(ord('1'))     # 49
print(ord('&'))     # 38
print(ord('ع'))     # 1593 (کد یونیکد حرف عربی)

# کاربرد: بررسی حروف کوچک و بزرگ
print(ord('b') - ord('a'))  # 1



#_______________________________________________________________________________________________________________________




'''pow(base, exp, mod=None)
Return base to the power exp; if mod is present, return base to the power exp, modulo mod (computed more efficiently 
than pow(base, exp) % mod). The two-argument form pow(base, exp) is equivalent to using the power operator: base**exp. '''
# محاسبه توان (base به توان exp) و optionally محاسبه باقیمانده (modulo) که بهینه‌تر از حالت عادی است.

# توان معمولی
print(pow(2, 3))      # 8 (2 به توان 3)
print(pow(5, 2))      # 25 (5 به توان 2)

# توان با mod (محاسبه باقیمانده)
print(pow(2, 3, 5))   # 3 (چون 2^3=8 و 8 % 5 = 3)
print(pow(10, 2, 7))  # 2 (چون 10^2=100 و 100 % 7 = 2)


#_______________________________________________________________________________________________________________________



'''print(*objects, sep=' ', end='\n', file=None, flush=False):
Print objects to the text stream file, separated by sep and followed by end. sep, end, file, and flush, if 
present, must be given as keyword arguments. '''
# چاپ اشیا در خروجی با امکان تنظیم جداکننده، پایان‌دهنده و مقصد.

# چاپ ساده
print("سلام", "دنیا")  # سلام دنیا

# تغییر جداکننده (sep)
print("apple", "banana", "orange", sep=", ")  # apple, banana, orange

# تغییر پایان‌دهنده (end)
print("Hello", end=" ")
print("World")  # Hello World

# نوشتن در فایل
with open("output.txt", "w") as f:
    print("این در فایل ذخیره می‌شود", file=f)

# چاپ لیست با جداکننده دلخواه
numbers = [1, 2, 3, 4]
print(*numbers, sep=" - ")  # 1 - 2 - 3 - 4



#_______________________________________________________________________________________________________________________



'''class property(fget=None, fset=None, fdel=None, doc=None):
Return a property attribute. fget is a function for getting an attribute value. fset is a function for setting an 
attribute value. fdel is a function for deleting an attribute value. And doc creates a docstring for the attribute.'''
# ایجاد managed attributes که امکان تعریف getter، setter و deleter برای دسترسی به یک ویژگی را فراهم می‌کند.

class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        """Getter برای name"""
        return self._name
    
    @name.setter
    def name(self, value):
        """Setter با اعتبارسنجی"""
        if not isinstance(value, str):
            raise ValueError("نام باید رشته باشد")
        self._name = value
    
    @name.deleter
    def name(self):
        """Deleter"""
        del self._name

# استفاده
p = Person("ali")
print(p.name)     # ali (getter)
p.name = "reza"   # setter
# del p.name       # deleter



#_______________________________________________________________________________________________________________________




'''class range(stop, /)
class range(start, stop, step=1, /):
Rather than being a function, range is actually an immutable sequence type. '''
# تولید یک sequence از اعداد صحیح که immutable است و معمولاً برای حلقه‌های for استفاده می‌شود.

# فقط stop (از 0 تا stop-1)
print(list(range(5)))      # [0, 1, 2, 3, 4]

# start و stop
print(list(range(2, 7)))   # [2, 3, 4, 5, 6]

# start، stop و step
print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]
print(list(range(10, 0, -2))) # [10, 8, 6, 4, 2]

# استفاده در حلقه
for i in range(3):
    print(f"تکرار {i}")  # تکرار 0، تکرار 1، تکرار 2


#_______________________________________________________________________________________________________________________




'''repr(object, /):
Return a string containing a printable representation of an object. For many types, this function makes an attempt 
to return a string that would yield an object with the same value when passed to eval(); otherwise, the representation 
is a string enclosed in angle brackets that contains the name of the type of the object together with additional 
information often including the name and address of the object. '''
# برگرداندن یک رشته که formal representation یک شیء را نشان می‌دهد - معمولاً طوری که بتوان با eval() دوباره آن شیء را ساخت.

# تفاوت repr و str
text = "سلام\nدنیا"
print(str(text))   # سلام
                   # دنیا
print(repr(text))  # 'سلام\nدنیا'

# برای اعداد
num = 123.456
print(repr(num))   # '123.456'

# برای اشیا
import datetime
now = datetime.datetime.now()
print(repr(now))   # 'datetime.datetime(2024, 1, 15, 10, 30, ...)'
print(str(now))    # '2024-01-15 10:30:00'


#_______________________________________________________________________________________________________________________



'''reversed(object, /):
Return a reverse iterator.'''
# یک iterator برمی‌گرداند که عناصر یک sequence (مانند لیست، رشته، تاپل) را به ترتیب معکوس پیمایش می‌کند.

# معکوس کردن لیست
numbers = [1, 2, 3, 4]
rev = list(reversed(numbers))
print(rev)  # [4, 3, 2, 1]

# معکوس کردن رشته
text = "Python"
rev_text = ''.join(reversed(text))
print(rev_text)  # "nohtyP"

# پیمایش معکوس در حلقه
for i in reversed(range(5)):
    print(i)  # 4, 3, 2, 1, 0
    

#_______________________________________________________________________________________________________________________



'''round(number, ndigits=None):
Return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the 
nearest integer to its input.'''
# گرد کردن یک عدد اعشاری به تعداد رقم اعشار مشخص (یا به نزدیکترین عدد صحیح).

# گرد کردن به نزدیکترین عدد صحیح
print(round(3.2))    # 3
print(round(3.7))    # 4
print(round(3.5))    # 4 (در پایتون گرد کردن بانکی)

# گرد کردن با تعداد رقم اعشار
print(round(3.14159, 2))     # 3.14
print(round(3.14159, 4))     # 3.1416
print(round(1234.567, -2))   # 1200.0 (گرد کردن به 2 رقم سمت چپ)


#_______________________________________________________________________________________________________________________



'''setattr(object, name, value, /):
This is the counterpart of getattr(). The arguments are an object, a string, and an arbitrary value. The string may name 
an existing attribute or a new attribute.'''
# تنظیم مقدار یک attribute روی یک شیء با استفاده از نام آن ویژگی (به صورت رشته).

class Person:
    pass

p = Person()

# تنظیم ویژگی جدید
setattr(p, "name", "ali")
setattr(p, "age", 25)

print(p.name)  # ali
print(p.age)   # 25

# تغییر ویژگی موجود
setattr(p, "age", 30)
print(p.age)   # 30

# معادل دستور مستقیم
p.city = "tehran"  # همین کار را می‌کند
print(p.city)      # tehran


#_______________________________________________________________________________________________________________________



'''class slice(stop, /)
class slice(start, stop, step=None, /)
Return a slice object representing the set of indices specified by range(start, stop, step). The start and step arguments 
default to None.'''
# ایجاد یک شیء برش (slice) که مشخص می‌کند چه بخشی از یک sequence (مانند لیست یا رشته) انتخاب شود.

# ایجاد slice object
my_slice = slice(1, 4)  # اندیس‌های 1 تا 3
my_slice2 = slice(0, 5, 2)  # اندیس‌های 0, 2, 4

# استفاده روی لیست
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[my_slice])   # [20, 30, 40]
print(numbers[my_slice2])  # [10, 30, 50]

# معادل با برش مستقیم
print(numbers[1:4])        # [20, 30, 40]
print(numbers[0:5:2])      # [10, 30, 50]

# روی رشته
text = "python"
print(text[slice(1, 4)])   # "yth"


#_______________________________________________________________________________________________________________________



'''sorted(iterable, /, *, key=None, reverse=False):
Return a new sorted list from the items in iterable. Has two optional arguments which must be specified as 
keyword arguments.
1- key specifies a function of one argument that is used to extract a comparison key from each element in 
iterable (for example, key=str.lower). The default value is None (compare the elements directly).
2- reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed. '''
# مرتب‌سازی عناصر یک iterable و برگرداندن یک لیست جدید مرتب‌شده (بدون تغییر iterable اصلی).

# مرتب‌سازی اعداد
numbers = [4, 1, 8, 3, 9]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 3, 4, 8, 9]
print(numbers)         # [4, 1, 8, 3, 9] (تغییر نکرده)

# مرتب‌سازی نزولی
print(sorted(numbers, reverse=True))  # [9, 8, 4, 3, 1]

# مرتب‌سازی رشته‌ها
fruits = ["banana", "apple", "cherry", "date"]
print(sorted(fruits))  # ['apple', 'banana', 'cherry', 'date']

# مرتب‌سازی بر اساس طول کلمه
words = ["python", "java", "c++", "javascript"]
print(sorted(words, key=len))  # ['c++', 'java', 'python', 'javascript']



#_______________________________________________________________________________________________________________________



'''@staticmethod:
Transform a method into a static method. A static method does not receive an implicit first argument. To declare a 
static method, use this idiom: 
class C:
    @staticmethod
    def f(arg1, arg2, argN): ...'''
# تبدیل یک متد به متد static که بدون نیاز به instance از کلاس قابل فراخوانی است و به self یا cls دسترسی ندارد.

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b

# فراخوانی بدون ساختن نمونه از کلاس
print(Calculator.add(5, 3))        # 8
print(Calculator.multiply(4, 2))   # 8

# همچنین می‌توان با نمونه هم صدا زد
calc = Calculator()
print(calc.add(10, 20))  # 30


#_______________________________________________________________________________________________________________________



'''sum(iterable, /, start=0):
Sums start and the items of an iterable from left to right and returns the total. The iterable’s items are normally 
numbers, and the start value is not allowed to be a string.'''
# جمع کردن تمام عناصر یک iterable (مانند لیست) به همراه یک مقدار شروع (پیش‌فرض ۰).

# جمع اعداد یک لیست
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))        # 15

# با مقدار شروع متفاوت
print(sum(numbers, 10))    # 25 (10 + 1+2+3+4+5)

# جمع اعداد یک تاپل
print(sum((10, 20, 30)))   # 60

# جمع اعداد یک range
print(sum(range(1, 6)))    # 15 (1+2+3+4+5)

# جمع اعداد اعشاری
print(sum([1.5, 2.3, 3.7]))  # 7.5


#_______________________________________________________________________________________________________________________




'''class super(type, object_or_type=None, /):
Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing 
inherited methods that have been overridden in a class.c'''
# دسترسی به متدهای کلاس والد از داخل کلاس فرزند، مخصوصاً وقتی متدی در کلاس فرزند بازنویسی (override) شده باشد.

class Parent:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"سلام من {self.name} هستم"

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # صدا زدن سازنده والد
        self.age = age
    
    def greet(self):
        parent_greet = super().greet()  # صدا زدن متد والد
        return f"{parent_greet} و {self.age} سال دارم"

child = Child("ali", 10)
print(child.greet())  # "سلام من ali هستم و 10 سال دارم"


#_______________________________________________________________________________________________________________________



'''vars(object, /)'''
# برگرداندن attributes یک شیء به صورت دیکشنری (معادل object.__dict__).

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("ali", 25)

# دریافت ویژگی‌ها به صورت دیکشنری
print(vars(p))  # {'name': 'ali', 'age': 25}

# اضافه کردن ویژگی جدید
p.city = "tehran"
print(vars(p))  # {'name': 'ali', 'age': 25, 'city': 'tehran'}

# بدون آرگومان - معادل locals() در محدوده جاری
x = 10
print(vars())  # دیکشنری متغیرهای محلی فعلی



#_______________________________________________________________________________________________________________________



'''zip(*iterables, strict=False):
Iterate over several iterables in parallel, producing tuples with an item from each one.'''
# کنار هم قرار دادن عناصر چند iterable به صورت موازی و ساختن تاپل‌هایی از عناصر متناظر.

# زیپ کردن دو لیست
names = ["ali", "sara", "reza"]
ages = [25, 30, 28]
paired = list(zip(names, ages))
print(paired)  # [('ali', 25), ('sara', 30), ('reza', 28)]

# پیمایش همزمان در حلقه
for name, age in zip(names, ages):
    print(f"{name} {age} ساله")

# سه لیست
scores = [18, 20, 17]
combined = list(zip(names, ages, scores))
print(combined)  # [('ali', 25, 18), ('sara', 30, 20), ('reza', 28, 17)]


strict=True     #برای اطمینان از هم‌اندازه بودن
list(zip([1,2], [3,4,5], strict=True))     # ValueError!


#_______________________________________________________________________________________________________________________


