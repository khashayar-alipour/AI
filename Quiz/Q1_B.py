


     #|=========================================|
     #|    Quiz 2                               |
     #|    Part B                               |
     #|    Python                               |
     #|    Author: Khashayar Alipour            |
     #|=========================================|

    
# با یک مثال تفاوت بین private methods و static methods و  class methods را توضیح دهید
# _________________________________________________________________________________________________



''' ______________ [ @instancemethod ] _________________ '''
# تمام متودهایی که در تابع های کلاس تعریف میشن instance method هستن
# که همشون self میگیرن و به instance وابسته هستن
# برای دسترسی به instance method ها از نمونه خودمون استفاده میکنیم


''' ______________ [ @classmethod ] _________________ '''
# حالا class method ها مربوط به کلاس هستند و با class att ها کار میکنن و به عنوان ورودی cls میگیرن
# متدی که تبدیل به classmethod میشه روی کل کلاس عملیات انجام میده نه روی نمونه


''' ______________ [ @staticmethod ] _________________ '''
# کاربردشون تو گذاشتن validation روی یک سری مقادیر هست
# این validation ها باید قبل از ایجاد instance اعمال بشن
# برای صدازدن staticmethod ها از self استفاده میکنیم


''' ____________ [ @property - private ] ______________ '''
# متغیر score در کلاس Student رو با استفاده از __ اومدیم private کردیم
# اینجوری دیگه مقدارش غیر قابل تغییر میشه
# البته همچنان در عمل تغییر دادن مقدار این متغیر امکان پذیر هست
# میشه با استفاده از شرطی کردن متغیر private با property setter قابلیت تغییر پیدا کردن رو بهش بدیم


# _________________________________________________________________________________________________
# در مثال زیر یک کلاس داریم که اطلاعات مربوط به دانش‌آموز را میگیرد و میانگین نمره را حساب میکند.


class Student():
    
    num_of_student=0
    
    def __init__(self, name, stu_num, score):
        self.__name = name        # Private value
        self.is_valid(stu_num)
        self.stu_num = stu_num
        self.score = score       
        
        # class attribute
        Student.num_of_student+=1


    def __str__(self):
        return f"name: {self.name} - stu_num: {self.stu_num} - score: {self.score}"


    def calc_avg(self):
        average=sum(self.score)/len(self.score)
        self.avg = average
    
    
    @classmethod 
    def show_instance_number(cls):
        print(cls.num_of_student)
        
        
    @staticmethod
    def is_valid(stu_num):
        if stu_num!=4 or not stu_num.startswith("s"):
            raise ValueError("Error! Student Number is not valid, instance can't be made.")
    
    
    # _______ [private method - property decorator] ____________
    @property
    def name(self):
        return self.__name    # با استفاده از این دکوراتور، این متد رو تبدیل به متغیر معمولی کردیم
        
    @name.setter              # با این دکوراتور یک متغیر محرمانه رو میشه تغییر داد
    def name(self,value):
        self.__name = value
    
        
    
    
    # ==============================[Result]===================================
    
s1=Student('n1', 's123', [14,17,20])
s2=Student('n2', 's345', [14,17,20])

#testing @staticmethod
try:
    s3=Student('n3', 'sh123', [14,17,20])
except Exception as e:
    print(e)    # ValueError: Error! Student Number is not valid, instance can't be made.

s1.calc_avg()                  # instance method
s1.avg                         # instance attribute
Student.show_instance_number()    # class method
s1.show_instance_number()
Student.num_of_student         # class attribute



















