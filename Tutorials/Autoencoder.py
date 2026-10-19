
'''
===============================================================================
===============================================================================
================       Created on Tue Oct 13 16:12:40 2026     ================
================                IDE: Spyder                    ================
================         Author: Khashayar Alipour             ================
================                AI Autoencoder                 ================
===============================================================================
===============================================================================
'''




#✅ What is autoencoder?
#✅ How does Autoencoder learn?
#✅ Types of Autoencoder (Undercomplete / Sparse / Denoising / Convolutional / VAE / ... )
#✅ Common mistakes during creation of Autoencoder
#✅ Simple Autoencoder codes in pytorch (MNIST dataset)
#✅ Denoising Autoencoder codes in pytorch 
#✅ Sparse Autoencoder codes in pytorch 
#✅ Convolutional Autoencoder codes in pytorch 
#✅ Simple Autoencoder codes in Tensorflow/keras (MNIST dataset)
#✅ Denoising Autoencoder codes in Tensorflow/keras
#✅ Sparse Autoencoder codes in Tensorflow/keras
#✅ Convolutional Autoencoder codes in Tensorflow/keras







'''
===============================================
=======  ⭐  What is Autoencoder?  ⭐  =======
===============================================
'''
# فرض کن تصویری از عدد ۷ داری. می‌خواهی شبکه‌ی عصبی این تصویر را یاد بگیرد،
# اما به‌جای اینکه مستقیماً عدد ۷ را پیش‌بینی کند می‌خواهی ابتدا اطلاعات تصویر را فشرده کند
# و سپس از روی اطلاعات فشرده‌شده، تصویر را دوباره بسازد.

# این دقیقاً ایده‌ی اصلی Autoencoder است:
    # شبکه Input خودش را به‌عنوان هدف یادگیری می‌گیرد و تلاش می‌کند نسخه‌ای (Output) شبیه آن را بازسازی کند


"✅ Important parts of Autoencoder:"

"Encoder"
# ورودی را می‌گیرد و آن را به یک نمایش فشرده تبدیل می‌کند
# در شبکه‌های ساده، این بخش ممکن است شامل لایه‌های Linear و تابع فعال‌سازی ReLU باشد

"Latent Space or Bottleneck"
# فضای نمایش فشرده‌ای است که اطلاعات ورودی در آن نگهداری می‌شود
# این فضا ممکن است یک بردار ۳۲تایی یا، در مدل‌های تصویری، یک مجموعه از نقشه‌های ویژگی باشد

"Decoder"
# نمایش فشرده را می‌گیرد و تلاش می‌کند ورودی اصلی را بازسازی کند
# در پایان آموزش، خروجی این بخش باید تا حد امکان به ورودی نزدیک باشد


# در این مثال، Flatten تصویر (عدد 7 از دیتاست mnist) را از ماتریس 28×28 به برداری با 784 مقدار تبدیل می‌کند
# در پایان نیز Reshape خروجی را دوباره به شکل تصویر درمی‌آورد
# نکته‌ی کلیدی این است که هدف شبکه در این پروژه، مثلا تشخیص عدد 7 نیست؛ هدفش بازسازی تصویر عدد 7 است
'''
    Image 28 × 28    
          ▼
      Flatten
   28 × 28 → 784 number   
          ▼
    Linear: 784 → 128
          ▼
    Linear: 128 → 32  ← Latent space
          ▼
    Linear: 32 → 128
          ▼
    Linear: 128 → 784
          ▼
        Reshape
    784 → 28 × 28
          ▼
   Regenerated photo    
'''









'''
======================================================
=======  ⭐  How does Autoencoder learn?  ⭐  =======
======================================================
'''
# فرض کن ورودی، تصویر واقعی باشد و خروجی، تصویر بازسازی‌شده. شبکه باید اختلاف آن‌ها را کم کند
# به این اختلاف، Reconstruction Error می‌گوییم و تابعی که آن را اندازه می‌گیرد، Loss Function نام دارد

# یکی از رایج‌ترین گزینه‌ها MSELoss است: میانگین مربع اختلاف پیکسل‌های ورودی و خروجی
    # MSE = (1/N)∑(Xi-X^i​)**2
    # N= تعداد مقادیر پیکسل‌هایی که خطا روی آن‌ها محاسبه می‌شود
    # Xi= مقدار پیکسل اصلی
    # X^i= مقدار همان پیکسل در تصویر بازسازی‌شده

# شبکه با کمک Backpropagation و به‌روزرسانی وزن‌ها تلاش می‌کند خطای کلی را کاهش دهد
# داده‌ی آموزشی ما به دو دسته‌ی ورودی و هدف تقسیم می‌شود
# اما در Autoencoder معمولی هر دو از همان تصویر می‌آیند:
input_image = x
target_image = x
reconstructed = model(input_image)
loss = criterion(reconstructed, target_image)



#             AUTOENCODER

#        ┌────── Encoder ──────┐
#        │                     │
# 784 → 128 → 64 → 32
#                   │
#                   │ z
#                   │
#                   ↓
#               Latent Space
#                   │
#                   │
# 32 → 64 → 128 → 784
#        │
#        └────── Decoder ──────┘

# Input x                  Output x̂
#    │                        │
#    └──── compare ───────────┘
#               ↓
#              Loss
#               ↓
#         Backpropagation
#               ↓
#    Update Encoder + Decoder












'''
===============================================
=======  ⭐  Types of Autoencoder  ⭐  =======
===============================================
'''
# انواع مختلف Autoencoder وجود داره که هرکدوم کاربرد های مختلف دارن
# اینها رقیب همدیگه نیستن بلکه ممکنه توی یه شبکه از چند مدل autoencoder بصورت همزمان استفاده بشه

# ====================================================================================================================================
#|                   ایده‌ی اصلی                      |                 کاربرد معمول                    |             نوع            |
# |--------------------------|--------------------------------------------------|----------------------------------------------------|
# | Undercomplete AE         |            کوچک‌تر کردن نمایش میانی             |      فشرده‌سازی ویژگی‌ها و کاهش ابعاد              |
# | Overcomplete AE          | داشتن فضای میانی بزرگ‌تر از ورودی        | یادگیری ویژگی‌ها، معمولاً با محدودیت یا منظم‌سازی         |
# | Sparse AE                |              فعال بودن تعداد کمی از نورون‌های نمایش میانی   |          یادگیری ویژگی‌های کم‌تراکم   |
# | Denoising AE             |             بازسازی تصویر تمیز از ورودی نویزی         |         حذف نویز تصاویر و سیگنال‌ها        |
# | Convolutional AE         |        استفاده از لایه‌های کانولوشنی           |    تصاویر و داده‌های دارای ساختار مکانی             |
# | Stacked/Deep AE          |             داشتن چندین لایه در رمزگذار و رمزگشا         |          یادگیری نمایش‌های پیچیده‌تر      |
# | Variational AE (VAE)     |          یادگیری توزیع احتمالی در فضای نهفته         |   تولید نمونه‌های جدید و مدل‌سازی داده      |
# | Contractive AE           |                مقاوم‌تر کردن نمایش در برابر تغییرات کوچک ورودی  |         یادگیری ویژگی‌های پایدار |
# | Sequence AE              |                رمزگذاری و بازسازی دنباله‌ها           |        متن، صدا و داده‌های زمانی             |
# ====================================================================================================================================


"✅ Undercomplete Autoencoder"
# واژه‌ی Undercomplete یعنی نمایش فشرده از ورودی کم‌بعدتر است
# در مثال ما:   784⟶128⟶32
# تصویر 784 مقدار دارد، اما شبکه مجبور است اطلاعات لازم برای بازسازی آن را در 32 مقدار قرار دهد
# چرا این محدودیت مهم است؟
# اگر شبکه بتواند اطلاعات را بدون هیچ محدودیتی از ورودی به خروجی کپی کند، ممکن است یادگیری مفیدی انجام ندهد
# کوچک‌کردن latent space، شبکه را تشویق می‌کند نمایش فشرده‌تری از ورودی یاد بگیرد
# البته کوچک بودن latent space به‌تنهایی تضمین نمی‌کند که ویژگی‌های خوبی یاد گرفته شود
# در کد پایه‌ای که کمی جلوتر می‌نویسیم، با تعیین latent_dim=32 همین نوع Autoencoder را خواهیم داشت



"✅ Overcomplete Autoencoder"
# در این نوع، ابعاد فضای نهفته از ابعاد ورودی بیشتر است.
# مثلاً:   784 → 1024 → 784
# در ظاهر، شبکه به‌جای فشرده‌سازی، تعداد مقادیر را بیشتر کرده است
# بنابراین احتمال دارد یاد بگیرد ورودی را تقریباً مستقیم کپی کند، بدون اینکه نمایش مفیدی یاد بگیرد
# برای کاهش این مشکل، می‌توان از روش‌هایی مانند sparse، حذف تصادفی بعضی فعال‌سازی‌ها یا دیگر روش‌های منظم‌سازی استفاده کرد



"✅ Sparse Autoencoder"
# در این نوع، هدف فقط کوچک‌کردن تعداد ویژگی‌ها نیست؛ بلکه می‌خواهیم در هر نمونه، تعداد کمی از نورون‌های نمایش نهفته فعال باشند
# فرض کن نمایش میانی ۶۴ مقدار دارد:
    # [0, 0, 0.8, 0, 0, 0.2, 0, 0, 0.9, ...]
    
# در چنین نمایشی، تعداد زیادی از مقادیر صفر یا نزدیک صفر هستند. این همان ایده‌ی تنکی یا Sparsity است.
# برای تشویق شبکه به این رفتار، یک جریمه به Loss اضافه می‌کنیم:
    # L_total = L_reconstruction + λ*L_sparsity
        # λ: ضریب اهمیت جریمه
        # L_sparsity = mean(|z|)    mean value of |absolute value| of activation function in latent space
            # z: نمایش فشرده‌ی ورودی

# اگر λ خیلی کم باشد، تنکی ممکن است چندان محسوس نباشد
# اگر خیلی زیاد باشد، شبکه ممکنه بیش از حد به صفر کردن فعال‌سازی‌ها تمایل پیدا کند و بازسازی بدی انجام دهد
 
# نکته: Sparse به معنای Undercomplete نیست
# یک Sparse Autoencoder می‌تواند فضای نهفته‌ی بزرگ‌تر از ورودی نیز داشته باشد؛ محدودیت تنکی جایگزین محدودیت ابعاد نیست



"✅ Sparse Autoencoder"
# اینجا شبکه باید از ورودی ناقص یا خراب‌شده، نسخه‌ی اصلی را بازسازی کند
# درواقع تفاوت کارش اینه که autoencoder معمولی تصویر تمیز ورودی میگیره و خروجی تصویر تمیز میده
# ولی denoising تصویر noisy میگیره و تصویر تمیز خروجی میده بهمون
# در نتیجه، شبکه یاد می‌گیرد به‌جای کپی‌کردن نویز، الگوهای مفید تصویر را بازیابی کند

# مثلاً تصویر تمیز عدد 7 را داریم، روی آن نویز تصادفی می‌ریزیم و از شبکه می‌خواهیم دوباره تصویر تمیز را بسازد:
# Clean photo
#    ▼
# Adding random noise
#    ▼
# Noisy photo ──► Encoder ──► Decoder ──► Clean photo



"✅ Convolutianal Autoencoder"
# مدل denoising از لایه‌های Linear استفاده می‌کند
# این لایه‌ها برای تصاویر کار می‌کنند، اما Flatten رابطه‌ی مکانی پیکسل‌ها را به شکل صریح در معماری حفظ نمی‌کند
# یک Convolutional Autoencoder نیز می‌تواند Denoising باشد؛ کافی است آن را با تصویر نویزی به‌عنوان ورودی و تصویر تمیز به‌عنوان هدف آموزش دهیم

# برای تصاویر معمولاً از لایه‌های زیر کمک می‌گیریم:
# Conv2d: استخراج ویژگی‌های محلی، مثل لبه‌ها و شکل‌ها
# ConvTranspose2d: افزایش ابعاد نقشه‌های ویژگی برای بازسازی تصویر
# ReLU: معرفی غیرخطی‌بودن به شبکه
# Sigmoid: محدود کردن مقادیر خروجی به بازه‌ی صفر تا یک، زمانی که پیکسل‌های هدف در همین بازه نرمال شده‌اند

# در این ساختار، شبکه ابتدا تصویر را به نقشه‌های ویژگی کوچک‌تر تبدیل می‌کند و سپس اندازه‌ی مکانی را برای بازسازی افزایش می‌دهد
# 28 × 28 × 1
#      ↓ Conv2d
# 14 × 14 × 16
#      ↓ Conv2d
#  7 ×  7 × 8
#      ↓ ConvTranspose2d
# 14 × 14 × 16
#      ↓ ConvTranspose2d
# 28 × 28 × 1



"✅ Variational Autoencoder (VAE)"
# تا اینجا در Autoencoder معمولی، Encoder یک بردار مشخص تولید می‌کند:    x⟶z

# اما در VAE یکم متفاوته. اینجا Encoder به‌جای تولید یک بردار ثابت به‌عنوان نمایش نهفته ...
#... پارامترهای یک توزیع احتمالی را یاد می‌گیرد؛ معمولاً میانگین μ و لگاریتم واریانس log σ**2

# سپس از آن توزیع نمونه‌گیری می‌کنیم:
    # z=μ+σϵ
    # که در آن ϵ از یک توزیع نرمال استاندارد نمونه‌گیری می‌شود    

# کلا VAE معمولاً دو بخش اصلی Loss دارد:      L_VAE = L_reconstruction + β_LKL
# بخش اول کیفیت بازسازی را اندازه می‌گیرد و بخش دوم فضای نهفته را به توزیع هدف، معمولاً توزیع نرمال استاندارد، نزدیک می‌کند

# تفاوت مهم: در Autoencoder معمولی، هر ورودی به یک نمایش نهفته تبدیل می‌شود. در VAE، یادگیری احتمالی ...
#... فضای نهفته کمک می‌کند بتوانیم با نمونه‌گیری از این فضا، داده‌های جدید تولید کنیم

# یک مثال ساده: بعد از آموزش VAE روی تصاویر ارقام دست‌نویس (MNIST dataset)، می‌توانیم یک ...
#... بردار تصادفی از فضای نهفته نمونه‌گیری کنیم و آن را به Decoder بدهیم تا تصویری جدید تولید کند
# البته کیفیت خروجی به آموزش و معماری بستگی دارد و تولید تصویر معتبر تضمین‌شده نیست



"✅ Stacked / Deep Autoencoder"
# در مدل پایه‌ی ما تنها یک لایه‌ی پنهان در هر سمت داشتیم:
    # 784 → 128 → 32 → 128 → 784
# اگر بخواهیم ساختار عمیق‌تری بسازیم، می‌توانیم چند لایه اضافه کنیم:
    # 784 → 512 → 256 → 64 → 256 → 512 → 784
# این کار می‌تواند به یادگیری روابط پیچیده‌تر کمک کند، اما به معنای بهتر بودن قطعی مدل نیست
# افزایش عمق و تعداد پارامترها ممکن است آموزش را دشوارتر کند و نیاز به تنظیم دقیق‌تر داشته باشد



"✅ Contractive Autoencoder"
# اینجا می‌خواهیم نمایش نهفته نسبت به تغییرات کوچک ورودی بیش از حد حساس نباشد
# برای این کار، علاوه بر reconstruction loss، جریمه‌ای مرتبط با تغییرات نمایش نهفته نسبت به ورودی اضافه می‌کنیم
# این نوع برای یادگیری ویژگی‌های پایدار مفهوم جالبی است
# اما معمولاً به محاسبات و پیاده‌سازی پیچیده‌تری نسبت به مدل پایه نیاز دارد



"✅ Sequence Autoencoder"
# تمام داده‌ها تصویر نیستند. فرض کن بخواهیم الگوی مصرف برق یک ساختمان را در طول 24 ساعت به نمایش فشرده تبدیل کنیم
# ورودی می‌تواند یک دنباله باشد:
    # مصرف ساعت 1    
# مصرف ساعت 2    
# مصرف ساعت 3    
    # ...
# مصرف ساعت 24    

# اینجا Encoder این دنباله را به یک نمایش نهفته تبدیل می‌کند و Decoder تلاش می‌کند مقادیر زمانی را بازسازی کند
# برای چنین کاربردهایی، بسته به شکل داده، می‌توان از لایه‌های LSTM، GRU یا معماری‌های دیگر استفاده کرد









'''
=========================================================================
=======  ⭐  Common mistakes during creation of Autoencoder  ⭐  =======
=========================================================================
'''
# اشتباهات رایج هنگام ساخت Autoencoder

# 1-استفاده از ورودی و هدف متفاوت در مدل معمولی
# در Autoencoder معمولی، خطا باید بین خروجی بازسازی‌شده و تصویر اصلی محاسبه شود؛ نه برچسب رقم

# 2-ناهماهنگی ابعاد خروجی و ورودی
# اگر ورودی 28×28 باشد، برای بازسازی پیکسل‌به‌پیکسل باید ابعاد خروجی نیز با آن سازگار باشند

# 3-نرمال‌سازی نادرست
# اگر پیکسل‌ها به بازه‌ی [0, 1] تبدیل شده‌اند، Sigmoid برای خروجی انتخاب مناسبی است
# اگر دامنه‌ی داده متفاوت باشد، باید خروجی و تابع Loss را متناسب با آن انتخاب کرد

# 4-کم کردن بیش از حد فضای نهفته
# مثلاً ممکن است latent_dim=2 بازسازی را دشوار کند، چون اطلاعات بسیار زیادی
# باید در تعداد کمی مقدار ذخیره شود. فضای کوچک‌تر الزاماً مدل بهتر ایجاد نمی‌کند

# 5-نگاه کردن فقط به Loss
# گاهی دو مدل Loss نزدیک به هم دارند، اما کیفیت بصری خروجی ...
#... آن‌ها متفاوت است. برای تصاویر، هم Loss و هم نمایش بصری بازسازی‌ها را بررسی کن

# 6-تصور اینکه هر Autoencoder مولد است
# مدل پایه عموماً برای بازسازی ورودی آموزش داده می‌شود نمی‌توان فرض کرد که نمونه‌گیری از یک ...
#... بردار کاملاً تصادفی، تصویر معناداری ایجاد می‌کند. این موضوع یکی از تفاوت‌های مهم VAE با Autoencoder معمولی است

# 7-استفاده از داده‌ی آزمایش برای تنظیم مکرر مدل
# اگر برای انتخاب معماری و تعداد Epochها مرتباً به داده‌ی آزمایش رجوع کرد، ارزیابی نهایی دیگر کاملاً مستقل نیست
# بهتر است از داده‌ی آموزش برای یادگیری، داده‌ی اعتبارسنجی برای انتخاب تنظیمات و داده‌ی آزمایش برای ارزیابی نهایی استفاده کرد

# 8-تصور اینکه Autoencoder همیشه فایل را به شکل مؤثرتری فشرده می‌کند
# کم شدن ابعاد نمایش نهفته، به‌تنهایی یک سامانه‌ی فشرده‌سازی کامل ایجاد نمی‌کند
# برای فشرده‌سازی واقعی باید هزینه‌ی ذخیره‌ی نمایش نهفته، مدل، دقت بازسازی و روش کدگذاری را نیز در نظر گرفت











'''
==============================================================================
=======  ⭐  Simple Autoencoder codes in pytorch (MNIST dataset)  ⭐  =======
==============================================================================
'''

#-------------------------
# 1-loading MNIST dataset
#-------------------------

import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import matplotlib.pyplot as plt

# Reproducibility
torch.manual_seed(42)

# Use GPU if available; otherwise use CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Device:", device)

# Converts each image into a tensor in [0, 1]
transform = transforms.ToTensor()

train_dataset = datasets.MNIST(
    root="data",
    train=True,
    download=True,
    transform=transform  )

test_dataset = datasets.MNIST(
    root="data",
    train=False,
    download=True,
    transform=transform  )

train_loader = DataLoader(
    train_dataset,
    batch_size=128,
    shuffle=True  )

test_loader = DataLoader(
    test_dataset,
    batch_size=128,
    shuffle=False  )

print("Training images:", len(train_dataset))    # 60000
print("Test images:", len(test_dataset))    # 10000


# خروجی چه شکلی است؟
# هر تصویر MNIST به صورت تنسوری با شکل زیر به شبکه داده می‌شود:   [1, 28, 28]
# عدد اول، کانال تصویر است؛ چون تصاویر ما خاکستری‌اند و فقط یک کانال دارند (مثلا تصاویر رنگی 3 کانال دارن RGB)

# هنگام آموزش، تصاویر در دسته‌هایی با این شکل به مدل داده می‌شوند:  [128, 1, 28, 28]
# عدد 128 همون Batch Size است



#------------------------------
# 2-Creating Autoencoder Model
#------------------------------

class Autoencoder(nn.Module):

    def __init__(self, latent_dim=32):
        super().__init__()

        # Encoder: 784 -> 128 -> latent_dim
        self.encoder = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28 * 28, 128),
            nn.ReLU(),
            nn.Linear(128, latent_dim)  )

        # Decoder: latent_dim -> 128 -> 784
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 28 * 28),
            nn.Sigmoid(),
            nn.Unflatten(1, (1, 28, 28))  )

    def encode(self, x):
        return self.encoder(x)

    def decode(self, z):
        return self.decoder(z)

    def forward(self, x):
        z = self.encode(x)
        reconstructed = self.decode(z)
        return reconstructed


model = Autoencoder(latent_dim=32).to(device)
print(model)

# مدل:
# Autoencoder(
#   (encoder): Sequential(
#     (0): Flatten(start_dim=1, end_dim=-1)
#     (1): Linear(in_features=784, out_features=128, bias=True)
#     (2): ReLU()
#     (3): Linear(in_features=128, out_features=32, bias=True)  )
  
#   (decoder): Sequential(
#     (0): Linear(in_features=32, out_features=128, bias=True)
#     (1): ReLU()
#     (2): Linear(in_features=128, out_features=784, bias=True)
#     (3): Sigmoid()
#     (4): Unflatten(dim=1, unflattened_size=(1, 28, 28))  )
# )


#--------encoder--------
# متود nn.Flatten() تصویر را از 1×28×28 به 784 مقدار تبدیل می‌کند
# متود nn.Linear(784, 128) هر 784 ورودی را به 128 مقدار تبدیل می‌کند
# متود nn.ReLU() یک Activation function است که به شبکه کمک می‌کند الگوهای غیرخطی یاد بگیرد
# متود nn.Linear(128, latent_dim) نمایش نهفته‌ی ما را می‌سازد. اینجا latent_dim=32 است، بنابراین نمایش فشرده 32 مقدار دارد

#-------decoder---------
# سپس Decoder همین مسیر را برعکس پیش می‌برد: از 32 مقدار به 128 مقدار و در پایان به 784 مقدار می‌رسد
# متود Unflatten خروجی را دوباره به شکل تصویر درمی‌آورد
# چرا آخرش Sigmoid داریم؟ چون مقادیر پیکسل‌های ورودی بین 0 و 1 هستند. پس می‌خواهیم خروجی هم در همین بازه باشد



#------------------------------
# 3-setting Loss and Optimizer
#------------------------------
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# اینجا criterion میزان اختلاف ورودی و تصویر بازسازی‌شده را اندازه می‌گیرد
# همچنین optimizer وزن‌های شبکه را به‌روزرسانی می‌کند. Adam انتخاب مناسبی برای شروع است



#------------------------
# 4-Teaining the network
#------------------------

def train_one_epoch(model, loader, optimizer, criterion):

    model.train()    # مدل را برای آموزش آماده میکند
    total_loss = 0.0

 # نکته‌: در این پروژه برچسب رقم‌ها را استفاده نمی‌کنیم. بخش x, _ در حلقه‌ی آموزش یعنی تصویر را می‌گیریم و برچسب را نادیده می‌گیریم    
    for x, _ in loader:

        x = x.to(device)

        # Forward pass
        reconstructed = model(x)      # تصویر بازسازی‌شده را تولید می‌کند

        # Input and target are the same image (x,x)
        loss = criterion(reconstructed, x)      # محاسبه خطای بازسازی

        # Clear old gradients
        optimizer.zero_grad()   # گرادیان‌های باقی‌مانده از مرحله‌ی قبلی را پاک می‌کند

        # Calculate gradients
        loss.backward()   # گرادیان‌های لازم برای یادگیری را محاسبه می‌کند

        # Update weights
        optimizer.step()  # وزن‌های مدل را به‌روزرسانی می‌کند

        total_loss += loss.item() * x.size(0)

    return total_loss / len(loader.dataset)


@torch.no_grad()   # در ارزیابی، محاسبه‌ی گرادیان را غیرفعال می‌کند
def evaluate(model, loader, criterion):

    model.eval()   # مدل را در حالت ارزیابی قرار می‌دهد
    total_loss = 0.0

    for x, _ in loader:

        x = x.to(device)

        reconstructed = model(x)
        loss = criterion(reconstructed, x)

        total_loss += loss.item() * x.size(0)

    return total_loss / len(loader.dataset)


epochs = 10

for epoch in range(epochs):
    train_loss = train_one_epoch( model, train_loader, optimizer, criterion  )
    val_loss = evaluate( model, test_loader, criterion  )
    print(
        f"Epoch {epoch + 1:02d}/{epochs} | "
        f"Train Loss: {train_loss:.5f} | "
        f"Validation Loss: {val_loss:.5f}"  )


# Epoch 01/10 | Train Loss: 0.04824 | Validation Loss: 0.02551
# Epoch 02/10 | Train Loss: 0.02085 | Validation Loss: 0.01696
# Epoch 03/10 | Train Loss: 0.01520 | Validation Loss: 0.01322
# Epoch 04/10 | Train Loss: 0.01271 | Validation Loss: 0.01154
# Epoch 05/10 | Train Loss: 0.01134 | Validation Loss: 0.01054
# Epoch 06/10 | Train Loss: 0.01038 | Validation Loss: 0.00976
# Epoch 07/10 | Train Loss: 0.00976 | Validation Loss: 0.00931
# Epoch 08/10 | Train Loss: 0.00929 | Validation Loss: 0.00899
# Epoch 09/10 | Train Loss: 0.00889 | Validation Loss: 0.00852
# Epoch 10/10 | Train Loss: 0.00855 | Validation Loss: 0.00820



#----------------------------------------
# 5-View the main and reconstructed photo
#----------------------------------------
# ردیف اول تصاویر اصلی و ردیف دوم خروجی شبکه است

model.eval()

images, _ = next(iter(test_loader))
images = images[:10].to(device)

with torch.no_grad():
    reconstructed = model(images).cpu()

images = images.cpu()

fig, axes = plt.subplots(2, 10, figsize=(15, 4))

for i in range(10):

    # Original image
    axes[0, i].imshow(images[i, 0], cmap="gray")
    axes[0, i].set_title("Original")

    # Reconstructed image
    axes[1, i].imshow(reconstructed[i, 0], cmap="gray")
    axes[1, i].set_title("Reconstructed")

    axes[0, i].axis("off")
    axes[1, i].axis("off")

plt.tight_layout()
plt.show()



#-------------------------
# 6-View the latent space
#-------------------------
# اینجا خروجی Encoder را میتونیم مستقیما ببینیم

# خروجی شکل‌ها باید شبیه این باشد:
    # Input shape: torch.Size([1, 1, 28, 28])
    # Latent shape: torch.Size([1, 32])
# یعنی یک تصویر با 784 مقدار پیکسلی به یک بردار 32 تایی تبدیل شده است
# این روش کاهش ابعاد است، اما دقت کن که هر 32 مقدار لزوماً ویژگی‌های معنایی واضحی نیستند
# که بتوانیم با نگاه کردن به آن‌ها بگوییم «این یکی نشان‌دهنده‌ی انحنای عدد ۷ است»
# نمایش نهفته، مقادیری است که مدل برای انجام وظیفه‌ی بازسازی یاد گرفته است

model.eval()

image, _ = test_dataset[0]
image = image.unsqueeze(0).to(device)

with torch.no_grad():
    z = model.encode(image)

print("Input shape:", image.shape)
print("Latent shape:", z.shape)
print(z)










'''
=================================================================================
=======  ⭐  Denoising Autoencoder codes in pytorch (MNIST dataset)  ⭐  =======
=================================================================================
'''
# می‌توانیم همان معماری پایه را استفاده کنیم، اما ورودی را نویزی کنیم و هدف را تصویر اصلی قرار دهیم
# ابتدا یک مدل مستقل میسازیم تا آموزش Denoising از آموزش مدل معمولی جدا باشد

# این مدل ممکن است بخشی از نویز را کاهش دهد، اما الزاماً تمام جزئیات را دقیق بازیابی نمی‌کند
# اگر نویز بسیار شدید باشد، اطلاعات اصلی تصویر ممکن است از بین رفته باشد و شبکه نتواند آن را به‌درستی بازسازی کند

#--------------------
# Creating the model
#--------------------

denoise_model = Autoencoder(latent_dim=32).to(device)

denoise_optimizer = torch.optim.Adam(denoise_model.parameters(), lr=0.001)

noise_factor = 0.30
epochs = 10

for epoch in range(epochs):

    denoise_model.train()
    total_loss = 0.0

    for clean, _ in train_loader:

        clean = clean.to(device)

        # Add Gaussian noise
        noisy = clean + noise_factor * torch.randn_like(clean)

        # Keep values inside [0, 1]
        noisy = noisy.clamp(0.0, 1.0)

        # Reconstruct the clean image
        reconstructed = denoise_model(noisy)

        # Target is clean, NOT noisy
        loss = criterion(reconstructed, clean)

        denoise_optimizer.zero_grad()
        loss.backward()
        denoise_optimizer.step()

        total_loss += loss.item() * clean.size(0)

    train_loss = total_loss / len(train_loader.dataset)

    print(
        f"Epoch {epoch + 1:02d} | "
        f"Loss: {train_loss:.5f}"  )



# تفاوت اصلی با آموزش معمولی فقط در چند خط است:
noisy = (clean + noise_factor * torch.randn_like(clean)).clamp(0, 1)
reconstructed = denoise_model(noisy)
loss = criterion(reconstructed, clean)



#------------
#   Result
#------------

denoise_model.eval()

clean, _ = next(iter(test_loader))
clean = clean[:10].to(device)

noisy = (clean + noise_factor * torch.randn_like(clean) ).clamp(0.0, 1.0)

with torch.no_grad():
    restored = denoise_model(noisy)

clean = clean.cpu()
noisy = noisy.cpu()
restored = restored.cpu()

fig, axes = plt.subplots(3, 10, figsize=(15, 5))

for i in range(10):

    axes[0, i].imshow(clean[i, 0], cmap="gray")
    axes[1, i].imshow(noisy[i, 0], cmap="gray")
    axes[2, i].imshow(restored[i, 0], cmap="gray")

    axes[0, i].set_title("Clean")
    axes[1, i].set_title("Noisy")
    axes[2, i].set_title("Restored")

    for row in range(3):
        axes[row, i].axis("off")

plt.tight_layout()
plt.show()













'''
==============================================================================
=======  ⭐  Sparse Autoencoder codes in pytorch (MNIST dataset)  ⭐  =======
==============================================================================
'''
# در این نسخه، علاوه بر reconstruction loss، فعال‌سازی‌های latent space را هم جریمه می‌کنیم


sparse_model = Autoencoder(latent_dim=64).to(device)

sparse_optimizer = torch.optim.Adam( sparse_model.parameters(), lr=0.001 )

lambda_sparse = 0.001
epochs = 10

for epoch in range(epochs):

    sparse_model.train()
    total_loss = 0.0

    for x, _ in train_loader:

        x = x.to(device)

        # Get latent representation
        z = sparse_model.encode(x)

        # Encourage non-negative, sparse activations
        z = torch.relu(z)

        reconstructed = sparse_model.decode(z)

        reconstruction_loss = criterion(reconstructed, x)

        # Penalize large/non-sparse activations
        sparsity_loss = z.abs().mean()

        loss = ( reconstruction_loss + lambda_sparse * sparsity_loss )

        sparse_optimizer.zero_grad()
        loss.backward()
        sparse_optimizer.step()

        total_loss += loss.item() * x.size(0)

    print(
        f"Epoch {epoch + 1:02d} | "
        f"Total Loss: {total_loss / len(train_loader.dataset):.5f}"  )



# در اینجا:    loss = reconstruction_loss + lambda_sparse * sparsity_loss
# به این معنی است که مدل باید دو هدف را هم‌زمان دنبال کند: تصویر را خوب بازسازی کند و فعال‌سازی‌های فضای نهفته را تا حد ممکن کم‌تراکم نگه دارد
# اینجا lambda_sparse را میشه تغییر داد و اثر آن را بر Loss و کیفیت تصاویر مقایسه کرد


# این مثال یک نسخه‌ی آموزشی ساده است؛ چون مدل آن را از معماری پایه گرفته‌ایم، latent space هنوز کوچک‌تر از ورودی است
# یعنی این مدل هم Sparse و هم Undercomplete است
# برای دیدن اثر واقعی منظم‌سازی sparse باید هم کیفیت بازسازی و هم مقدار و تعداد فعال‌سازی‌های غیرصفر را بررسی کرد











'''
=====================================================================================
=======  ⭐  Convolutional Autoencoder codes in pytorch (MNIST dataset)  ⭐  =======
=====================================================================================
'''
# حالا به‌جای اینکه تصویر را ابتدا با Flatten به بردار تبدیل کنیم، از خود ساختار تصویر استفاده می‌کنیم

#-------------------------------------------------
#  Creating simple Convolutional Autoencoder model
#-------------------------------------------------

class ConvAutoencoder(nn.Module):

    def __init__(self):
        super().__init__()

        self.encoder = nn.Sequential(
            nn.Conv2d( in_channels=1, out_channels=16, kernel_size=3, stride=2, padding=1 ),
            nn.ReLU(),
            nn.Conv2d( in_channels=16, out_channels=8, kernel_size=3, stride=2, padding=1 ),
            nn.ReLU()  )

        self.decoder = nn.Sequential(
            nn.ConvTranspose2d( in_channels=8, out_channels=16, kernel_size=3, stride=2, padding=1, output_padding=1  ),
            nn.ReLU(),
            nn.ConvTranspose2d( in_channels=16, out_channels=1, kernel_size=3, stride=2, padding=1, output_padding=1   ),
            nn.Sigmoid()  )

    def encode(self, x):
        return self.encoder(x)

    def decode(self, z):
        return self.decoder(z)

    def forward(self, x):
        z = self.encode(x)
        return self.decode(z)


conv_model = ConvAutoencoder().to(device)
print(conv_model)

# برخلاف مدل قبلی، latent representation این شبکه یک بردار ساده نیست؛ یک feature map با شکل تقریبی زیر است:
    # [Batch, 8, 7, 7]
# این شبکه 8 تا feature map دارد و هر map ابعاد مکانی 7×7 دارد    



#--------------------------------------------------
#  Training simple Convolutional Autoencoder model
#--------------------------------------------------
# کد زیر از همان train_loader و test_loader قبلی استفاده می‌کند

conv_optimizer = torch.optim.Adam( conv_model.parameters(), lr=0.001   )

for epoch in range(10):

    train_loss = train_one_epoch( conv_model, train_loader, conv_optimizer, criterion )

    val_loss = evaluate( conv_model, test_loader, criterion )

    print(
        f"Epoch {epoch + 1:02d} | "
        f"Train Loss: {train_loss:.5f} | "
        f"Validation Loss: {val_loss:.5f}"   )



# چون ورودی و خروجی مدل همان شکل N × 1 × 28 × 28 را دارند ...
#... می‌توانیم همان توابع آموزش و ارزیابی مدل پایه را استفاده کنیم




#-------------------------------------------------------
# تبدیل همین مدل به Denoising Convolutional Autoencoder
#-------------------------------------------------------
# برای Denoising، لازم نیست معماری را تغییر دهیم. فقط آموزش باید به شکل زیر باشد:

for clean, _ in train_loader:

    clean = clean.to(device)

    noisy = ( clean + 0.30 * torch.randn_like(clean) ).clamp(0.0, 1.0)

    reconstructed = conv_model(noisy)

    loss = criterion(reconstructed, clean)

    conv_optimizer.zero_grad()
    loss.backward()
    conv_optimizer.step()


# این قطعه باید به‌جای حلقه‌ی معمولی داخل تابع آموزش اجرا شود
# نه اینکه هم‌زمان با حلقه‌ی قبلی و با همان مدل آموزش داده شود
# برای یک آزمایش تمیز، بهتر است مدل و Optimizer جدیدی ساخت تا آموزش Denoising از آموزش قبلی مستقل باشد










'''
=======================================================================================
=======  ⭐  Simple Autoencoder codes in Tensorflow/keras (MNIST dataset)  ⭐  =======
=======================================================================================
'''

#--------------------
# Preaparing dataset
#--------------------

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Load MNIST
(x_train, _), (x_test, _) = tf.keras.datasets.mnist.load_data()

# Normalize pixel values to [0, 1]
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# Flatten each image: 28 x 28 -> 784
x_train_flat = x_train.reshape(-1, 784)
x_test_flat = x_test.reshape(-1, 784)

print(x_train_flat.shape)
print(x_test_flat.shape)


#خروجی ابعاد باید این‌گونه باشد:
    # (60000, 784)  Train
    # (10000, 784)  Test



#----------------------------
# Creating encoder / decoder
#----------------------------
# در اینجا encoder یک بردار 32 تایی تولید می‌کند و decoder آن را به بردار 784 تایی تبدیل می‌کند

from tensorflow.keras import layers, Model

latent_dim = 32

encoder = tf.keras.Sequential([
    layers.Input(shape=(784,)),
    layers.Dense(128, activation="relu"),
    layers.Dense(latent_dim)
], name="encoder")


decoder = tf.keras.Sequential([
    layers.Input(shape=(latent_dim,)),
    layers.Dense(128, activation="relu"),
    layers.Dense(784, activation="sigmoid")
], name="decoder")


inputs = layers.Input(shape=(784,))

z = encoder(inputs)
outputs = decoder(z)

autoencoder = Model( inputs=inputs, outputs=outputs, name="autoencoder"  )

autoencoder.summary()



#------------------------
#   Training the model
#------------------------

autoencoder.compile( optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss="mse" )

history = autoencoder.fit(
    x_train_flat,
    x_train_flat,
    epochs=10,
    batch_size=128,
    shuffle=True,
    validation_data=(x_test_flat, x_test_flat)   
   )

# به fit() دقت کن:
# autoencoder.fit(x_train_flat, x_train_flat, ...)
# آرگومان اول داده‌ی ورودی و آرگومان دوم هدف آموزشی است
# چون در مدل معمولی ورودی و هدف یکسان‌اند، هر دو آرگومان را از یک آرایه می‌گیریم



#----------------------------------
#   Dispaying the reconstructions
#----------------------------------

reconstructed = autoencoder.predict( x_test_flat[:10], verbose=0 )

reconstructed = reconstructed.reshape(-1, 28, 28)

fig, axes = plt.subplots(2, 10, figsize=(15, 4))

for i in range(10):

    axes[0, i].imshow(x_test[i], cmap="gray")
    axes[1, i].imshow(reconstructed[i], cmap="gray")

    axes[0, i].set_title("Original")
    axes[1, i].set_title("Reconstructed")

    axes[0, i].axis("off")
    axes[1, i].axis("off")

plt.tight_layout()
plt.show()













'''
=======================================================================================
=======  ⭐  Sparse Autoencoder codes in Tensorflow/keras (MNIST dataset)  ⭐  =======
=======================================================================================
'''
# در Keras می‌توان با activity_regularizer روی فعال‌سازی‌های یک لایه جریمه‌ی sparse اعمال کرد

# توجه داشته باش که جریمه‌ی تنکی در activity_regularizer توسط Keras به Loss مدل اضافه می‌شود
# بنابراین در این پیاده‌سازی لازم نیست آن را به‌صورت دستی به MSE جمع کنی
# مقدار 1e-4 صرفاً نقطه‌ی شروع است، نه یک مقدار بهینه برای تمام دیتاست‌ها و معماری‌ها

sparse_encoder = tf.keras.Sequential([
    layers.Input(shape=(784,)),
    layers.Dense(128, activation="relu"),
    layers.Dense( 64, activation="relu", activity_regularizer=tf.keras.regularizers.L1(1e-4) )
 ])

sparse_decoder = tf.keras.Sequential([
    layers.Input(shape=(64,)),
    layers.Dense(128, activation="relu"),
    layers.Dense(784, activation="sigmoid")
])

inputs = layers.Input(shape=(784,))
z = sparse_encoder(inputs)
outputs = sparse_decoder(z)

sparse_autoencoder = tf.keras.Model(inputs, outputs)

sparse_autoencoder.compile( optimizer="adam", loss="mse" )

sparse_autoencoder.fit(
    x_train_flat,
    x_train_flat,
    epochs=10,
    batch_size=128,
    validation_data=(x_test_flat, x_test_flat)
)










'''
==========================================================================================
=======  ⭐  Denoising Autoencoder codes in Tensorflow/keras (MNIST dataset)  ⭐  =======
==========================================================================================
'''
# این بار ورودی نویزی را جداگانه تولید می‌کنیم:
    
noise_factor = 0.30

x_train_noisy = np.clip( x_train_flat + noise_factor * np.random.normal( loc=0.0, scale=1.0, size=x_train_flat.shape), 0.0, 1.0).astype("float32")

x_test_noisy = np.clip( x_test_flat + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=x_test_flat.shape), 0.0, 1.0).astype("float32")



# سپس یک مدل مستقل برای حذف نویز می‌سازیم تا آموزش آن با مدل پایه قاطی نشود:
# باز هم تفاوت مهم این است که ورودی شبکه x_train_noisy است، ولی هدف آموزشی x_train_flat، یعنی تصویر تمیز، است.

inputs = layers.Input(shape=(784,))

z = layers.Dense(128, activation="relu")(inputs)
z = layers.Dense(32, activation="relu")(z)

decoded = layers.Dense(128, activation="relu")(z)
outputs = layers.Dense(784, activation="sigmoid")(decoded)

denoise_autoencoder = Model(inputs, outputs)

denoise_autoencoder.compile( optimizer="adam", loss="mse" )

denoise_autoencoder.fit(
    x_train_noisy,
    x_train_flat,
    epochs=10,
    batch_size=128,
    validation_data=(x_test_noisy, x_test_flat)
)

















'''
==============================================================================================
=======  ⭐  Convolutional Autoencoder codes in Tensorflow/keras (MNIST dataset)  ⭐  =======
==============================================================================================
'''
# برای شبکه‌ی کانولوشنی دیگر تصاویر را Flatten نمی‌کنیم
# شکل ورودی باید 28 × 28 × 1 باشد؛ در Keras ترتیب ابعاد معمولاً به شکل Height × Width × Channels است.

#---------------------
#   Preaparing data
#---------------------

import tensorflow as tf
import numpy as np

(x_train, _), (x_test, _) = tf.keras.datasets.mnist.load_data()

x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# Add the channel dimension
x_train_img = x_train[..., np.newaxis]
x_test_img = x_test[..., np.newaxis]

print(x_train_img.shape)


# خروجی:   (60000, 28, 28, 1)



#--------------------------------
#   Creating convolutional Model
#--------------------------------

from tensorflow.keras import layers, Model

inputs = layers.Input(shape=(28, 28, 1))

# Encoder
x = layers.Conv2D( 16, 3, strides=2, padding="same", activation="relu")(inputs)
x = layers.Conv2D( 8, 3, strides=2, padding="same", activation="relu")(x)

# Decoder
x = layers.Conv2DTranspose( 8, 3, strides=2, padding="same", activation="relu")(x)
x = layers.Conv2DTranspose( 16, 3, strides=2, padding="same", activation="relu")(x)

outputs = layers.Conv2D( 1, 3, padding="same", activation="sigmoid")(x)

conv_autoencoder = Model(inputs, outputs)

conv_autoencoder.compile( optimizer="adam", loss="mse")

conv_autoencoder.summary()


# در این معماری، strides=2 باعث کاهش ابعاد مکانی هنگام رمزگذاری و افزایش ابعاد مکانی هنگام رمزگشایی می‌شود



#--------------------------------
#   Training the simple version
#--------------------------------

conv_autoencoder.fit(
    x_train_img,
    x_train_img,
    epochs=10,
    batch_size=128,
    validation_data=(x_test_img, x_test_img)
)



#----------------------------------
#   Turning into denoising version
#----------------------------------
# در این حالت ورودی‌ها را نویزی می‌کنیم، اما تصاویر تمیز را به‌عنوان هدف نگه می‌داریم:

noise_factor = 0.30
x_train_noisy = np.clip( x_train_img + noise_factor * np.random.normal( 0.0, 1.0, x_train_img.shape), 0.0, 1.0).astype("float32")
x_test_noisy = np.clip( x_test_img + noise_factor * np.random.normal( 0.0, 1.0, x_test_img.shape ), 0.0, 1.0).astype("float32")


# برای آموزش Denoising، یک مدل و Optimizer جدید میسازیم یا وزن‌های یک مدل آموزش‌دیده ...
#... را آگاهانه برای ادامه‌ی آموزش انتخاب کن. سپس آن را با ورودی نویزی و هدف تمیز آموزش میدیم:

# Use a freshly initialized model for this experiment
denoising_conv_model = tf.keras.models.clone_model( conv_autoencoder )
denoising_conv_model.compile( optimizer="adam", loss="mse" )

denoising_conv_model.fit(
    x_train_noisy,
    x_train_img,
    epochs=10,
    batch_size=128,
    validation_data=(x_test_noisy, x_test_img)  )




