
'''
===============================================================================
===============================================================================
================       Created on Thu Oct 15 10:59:36 2026     ================
================                IDE: Spyder                    ================
================         Author: Khashayar Alipour             ================
================     AI Generative Adversial network (GAN)     ================
===============================================================================
===============================================================================
'''




#✅ Introduction on generative models
#✅ VAE (Variational Autoencoder) full concepts
#✅ GAN (Generative Adversial network) full concepts
#✅ Comparison of GAN and VAE
#✅ GAN limitations
#✅ Preaparing MNIST data for GAN and VAE codes in pytorch
#✅ VAE coding in pytorch
#✅ GAN coding in pytorch
#✅ Comparison of VAE outcome with GAN outcome






'''
============================================================
=======  ⭐  Introduction on generative models  ⭐  =======
============================================================
'''

# در این درسنامه 2 مدل مهم در AI بررسی میشه:  GAN و VAE
# این دو مدل از روش‌های مهم یادگیری مولد هستند، اما تنها راه ساخت Generative Model نیستند
# مدل‌های Diffusion و مدل‌های زبانی بزرگ نیز از خانواده‌های مهم دیگرند


"✅ VAE (Variational Autoencoder) "
# خودرمزگذار واریانسی
# مدلی که یاد می‌گیرد داده‌ها چگونه در یک فضای احتمالی نمایش داده شوند و از آن‌ها نمونه‌های جدید بسازد


"✅ GAN (Generative Adversarial Network) "
# شبکه‌ی مولد تخاصمی
# مدلی که با رقابت دو شبکه یاد می‌گیرد داده‌های مصنوعی شبیه داده‌های واقعی تولید کند


"✅ What is Generative Model?"
# فرض کن 10 هزار تصویر از اعداد دست‌نویس به هوش مصنوعی بدهیم؛ تصاویر اعداد 0 تا 9 در MNIST database
# دو نوع هدف متفاوت می‌توانیم داشته باشیم:

#------------------------------------
# Discriminative Model (مدل تشخیصی)
#------------------------------------
# تصویر را می‌بیند و می‌گوید: «این عدد 7 است»
# یعنی از ورودی برای پیش‌بینی یک برچسب یا خروجی استفاده می‌کند

#-----------------------------
# Generative Model (مدل مولد)
#-----------------------------
# از الگوهایی که در تصاویر یاد گرفته است، یک تصویر جدید از عدد دست‌نویس تولید می‌کند
# تصویری که قبلاً دقیقاً در داده‌های آموزشی وجود نداشته است (ولی شباهت زیادی بهشون داره)
# مدل مولد صرفاً تصاویر قبلی را ذخیره و دوباره نمایش نمی‌دهد
# هدف این است که ساختار و الگوهای داده را یاد بگیرد و نمونه‌های تازه و معقول بسازد
# البته ممکن است در عمل بعضی مدل‌ها نمونه‌های آموزشی را تا حدی حفظ کنند
# بنابراین تولید نمونه‌ی جدید به‌تنهایی تضمین نمی‌کند که مدل واقعاً تعمیم خوبی یاد گرفته باشد

# کاربردهای Generative Modelها:
# ساخت تصویر، موسیقی و ویدئو    
# تولید متن و کد    
# ساخت داده‌ی مصنوعی برای آموزش    
# بازسازی و تغییر تصاویر    
# تولید طرح‌های اولیه‌ی محصول و طراحی    

# حالا سؤال اصلی: چطور به ماشین یاد می‌دهیم چیزی بسازد که قبلاً ندیده است؟
# یکی از پاسخ‌های مهم، VAE است










'''
=========================================================
=======  ⭐  VAE (Variational Auto Encoder)  ⭐  =======
=========================================================
'''

# برای فهم VAE، باید از Autoencoder معمولی که قبلاً یاد گرفتیم شروع کنیم
# محدودیت Autoencoder معمولی این بود که، مثلاً یک تصویر دست‌نویس از عدد 7 را وارد می‌کنیم:

#       Input
#      _______
#     |       |
#     |   7   |
#     |_______|
#         ↓
#      Encoder
#   Converting the image 
# into a squeezed vector
#         ↓
#     Latent Vector
# مثلاً 32 عدد که نمایش فشرده‌ی تصویر هستند  
#         ↓
#     Decoder
#   Make a reconstructed image
#     out of squeezed vector
#         ↓ 
#      _______
#     |       |
#     |   7   |
#     |_______|


"✅ Limitation of simple autoencoder"
# این مدل یاد می‌گیرد هر تصویر را به یک بردار فشرده تبدیل کند و سپس آن را بازسازی کند
# اما یک مشکل داریم: فضای نهفته یا Latent Space لزوماً ساختار منظمی ندارد
# مثلا ممکنه مدل تصویرهای آموزشی را در نقاطی از فضای نهفته قرار دهد که پراکنده و نامنظم‌اند
# اگر یک بردار کاملاً تصادفی انتخاب کنیم و به Decoder بدهیم، ممکنه خروجی بی‌معنی یا نامفهومی تولید شود
# پس برای تولید تصویر جدید، فقط داشتن Encoder و Decoder کافی نیست
# به روشی نیاز داریم که فضای نهفته را برای نمونه‌گیری و تولید داده مناسب‌تر کند

# تصویرهای آموزشی = •       
# بردار کاملا تصادفی = ❌   
#           Autoencoder
# _________Latent space_________       
# |  ••••                      | 
# |                ••          |
# |     ••                     |
# |                     ❌    |
# |     ••••     •             |
# |                            |
# | •••                 ••     |
# |____________________________|


"✅ Main idea of VAE"
# حالا VAE میگه به‌جای اینکه هر تصویر را به یک بردار ثابت تبدیل کنیم
# بهتره براش یک توزیع احتمالی (random distribution) یاد بگیریم

# فرض کن می‌خواهیم تصاویر دست‌نویس عدد 7 را یاد بگیریم. هر 7 ممکن است کمی متفاوت باشد:
# یکی باریک باشد
# یکی پهن باشد
# یکی خط بالایی کوتاه‌تری داشته باشد
# یکی کمی کج باشد

# به‌جای اینکه Encoder بگه «این تصویر دقیقاً این نقطه از فضای نهفته است»، در VAE میتونه بگه:
# «این تصویر احتمالاً به این ناحیه از latent space مربوطه. مرکزش اینجاست و میزان پراکندگیش هم مشخصه»

# این ایده با دو خروجی اصلی Encoder پیاده‌سازی می‌شود:
    # Mean or μ: مرکز توزیع احتمالی
    # Variance or σ**2: میزان پراکندگی توزیع

# در VAE اینجوریه که Encoder دو مقدار یا دو بردار μ و σ را یاد می‌گیرد
# سپس یک نمونه‌ی تصادفی از توزیع مربوط به آن‌ها انتخاب می‌کنیم و به Decoder می‌دهیم
# این اتفاق باعث می‌شود مدل فقط یک مسیر ثابت برای بازسازی نداشته باشد
# بلکه بتواند از نمایش‌های احتمالی نمونه‌گیری کند

      
#  _____
# |     |
# هر تصویر به یک توزیع احتمالی نگاشت میشه =  |_____|  
# مرکز توزیع احتمالی = •                               
# بردار کاملا تصادفی = ❌                               
#               VAE
# __________Latent space___________ 
# |   _____              _____    |
# |  |  •  |            |  •  |   |
# |  |_____|            |_____|   |
# |                               |
# |             ______________    |
# |            |          ❌ |   |
# |            |      •      |    | 
# |            |_____________|    | 
# |                               |
# |_______________________________|


"✅ How the VAE samples the distribution?"
# حالا VAE چطوری از یک توزیع نمونه گیری میکنه؟
# مثلا Encoder برای یک تصویر این مقادیر را تولید کرده است:   μ=2, σ=0.5
# میانگین 2 است و انحراف معیار 0.5 هست. حالا می‌توانیم از توزیع نرمالی با این مشخصات نمونه‌گیری کنیم:
    # 2.1
    # 1.7
    # 2.3
    # 1.9
    # 2.0
# این اعداد نمونه‌های احتمالی از همان توزیع‌اند
# نه اینکه در هر بار نمونه‌گیری دقیقاً یکی از این مقادیر ثابت به دست بیاد

# در فضای نهفته‌ی واقعی، معمولاً به‌جای یک عدد، چند عدد داریم
# مثلاً اگر ابعاد نهفته 32 باشد، Encoder دو بردار 32 تایی تولید میکنه
# از این دو بردار برای تولید یک بردار نهفته‌ی نمونه‌گیری‌شده استفاده میشه:
    # mu     = [0.2, -0.1, 0.7, ...]   # 32 values
    # logvar = [-0.3, 0.1, -0.8, ...]  # 32 values


"✅ VAE: Reparameterization Trick"
# اگر نمونه‌گیری تصادفی است، شبکه چطور می‌تواند با Backpropagation یاد بگیرد؟
# این روش اجازه می‌ده گرادیان‌ها از مسیر محاسباتیِ قابل‌مشتق عبور کنن و Encoder و Decoder با هم آموزش ببینن
# راه‌حل، جداکردن بخش تصادفی از پارامترهای قابل‌آموزش است:
    # z=μ+σϵ
# که در آن:   ϵ∼N(0,I)    

# به زبان ساده:
# اول Encoder میانگین و میزان پراکندگی را یاد می‌گیرد
# سپس یک مقدار تصادفی استاندارد ϵ تولید می‌کنیم
# سپس آن را با میانگین و انحراف معیار ترکیب می‌کنیم تا z به دست بیاید
# سپس z وارد Decoder می‌شود و تصویر بازسازی‌شده تولید می‌شود


"✅ Why does VAE need 2 Loss?"
# کلا VAE به 2 تا Loss نیاز داره، چون برعکس autoencoder معمولی اینجا ما 2 تا هدف داریم که بهش برسیم
# در Autoencoder معمولی، هدف اصلی کاهش خطای بازسازی بود. در VAE، فقط بازسازی خوب کافی نیست
# می‌خواهیم فضای نهفته هم ساختار احتمالی منظمی داشته باشد

# به همین دلیل، تابع Loss دو قسمت اصلی دارد:
    # L_VAE = L_reconstruction + L_KL

#------------------------
#   Reconstruction Loss
#------------------------
# این بخش می‌سنجد که تصویر بازسازی‌شده چقدر به تصویر اصلی نزدیک است
# برای مثال، اگر ورودی تصویر عدد 7 باشد، Decoder باید تصویری شبیه همان 7 تولید کند

#-------------------
#   KL Divergence 
#-------------------
# این قسمت توزیع یادگرفته‌شده‌ی Encoder را به یک توزیع هدف، معمولاً توزیع نرمال استاندارد، نزدیک میکنه
# به زبان ساده، KL میگه:
# «فقط تصویر را خوب بازسازی نکن؛ فضای نهفته را هم طوری مرتب کن که بشه ازش به‌صورت قابل‌کنترل نمونه‌گیری کرد»

# مفهوم مهم این است که اگر فقط Reconstruction Loss را داشته باشیم، فضای نهفته ...
#... الزاماً برای تولید نمونه‌های تصادفی مناسب نمیشه. جمله‌ی KL به منظم‌ شدنش کمک می‌کنه
# البته این دو هدف گاهی باهم رقابت میکنن: اگر فشار KL بیش از حد باشد، بازسازی ممکنه ضعیف بشه
# اگر فشار KL کم باشد، فضای نهفته ممکنه کمتر از حد مطلوب منظم بشه


"✅ How does VAE generate a new photo, from a trained photo?"
# در آموزش، تصویر واقعی را به Encoder میدیم. اما در زمان تولید، دیگر به تصویر ورودی نیاز نداریم
# به همین دلیل VAE را یک مدل مولد می‌نامیم

# در مدل معمولی، Decoder برای بازسازی تصویری که Encoder به آن داده است استفاده می‌شود
# در VAE ولی Decoder را می‌توان با نمونه‌های تازه از فضای نهفته نیز اجرا کرد
# منظم بودن فضای نهفته احتمال تولید نمونه‌های معقول را افزایش می‌دهد
# اما تضمین نمی‌کند که هر بردار تصادفی خروجی معناداری داشته باشد

# 1-نمونه‌گیری از توزیع هدف           
# مثلاً یک بردار تصادفی از توزیع نرمال استاندارد   
                     # ↓
# 2-بردار نهفته‌ی z              
# یک نقطه در فضای نهفته          
                     # ↓
                  # 3-Decoder
# بردار را به تصویر تبدیل می‌کند       
                     # ↓
# تصویر مصنوعی جدید            
                  # 🖼️










'''
=============================================================
=======  ⭐  GAN (Generative Adversial network)  ⭐  =======
=============================================================
'''
# این مدل مولد در سال ۲۰۱۴ معرفی شد
# ایده‌ی مرکزی آن، آموزش هم‌زمان دو شبکه است که هدف‌های متفاوت و تا حدی متضاد دارن

# در GAN، این دو شبکه با یکدیگر رقابت می‌کنند:
# اول Generator هست که می‌خواد نمونه‌هایی بسازه که Discriminator را فریب دهند    
# سپس Discriminator می‌خواهد نمونه‌های واقعی را از نمونه‌های مصنوعی تشخیص دهد    

# مثال ساده: جاعل و کارآگاه
# فرض کن یک نفر می‌خواد اسکناس تقلبی بسازد و یک کارآگاه وظیفه دارد اسکناس واقعی را از تقلبی تشخیص دهد
# 1-Generator — مولد
# نقش جاعل را دارد. تلاش می‌کند نمونه‌های مصنوعی بسازد که تا حد امکان شبیه نمونه‌های واقعی باشند    
# 2-Discriminator — تمایزدهنده
# نقش کارآگاه را دارد. تلاش می‌کند تشخیص دهد یک نمونه واقعی است یا توسط Generator تولید شده است    

# هرکدام از یادگیری هم سود می‌برن. هرچه Discriminator بهتر شود، Generator باید نمونه‌های بهتری بسازد
# و هرچه Generator بهتر شود، تشخیص برای Discriminator دشوارتر می‌شود
# این همان ایده‌ی رقابت خصمانه در GAN است


"✅ How does GAN work?"
# نکته: Discriminator در حالت معمول فقط بر اساس تصویر ورودی تصمیم می‌گیرد که واقعی است یا مصنوعی
# مثلا در GAN ساده‌ی MNIST لزوماً نمی‌گوید «این عدد 7 است»؛ کارش تشخیص واقعی یا تولیدشده بودن تصویر است

                 # Random noise
# مثلاً یک بردار شامل ۱۰۰ عدد تصادفی       
                     # ↓
                # Generator (G)
# نویز را به تصویر مصنوعی تبدیل می‌کند      
                     # ↓
# تصویر مصنوعی                
# مثلاً تصویری که شبیه عدد ۷ است          
                     # ↓
                # Discriminator (D)
# تصویر مصنوعی را با تصاویر واقعی مقایسه می‌کند
#                     /\
#                    /  \
#                   /    \
#                  /      \
#        Artificial              Real              
    # احتمال بیشتر برای      احتمال بیشتر برای  
# نمونه‌ی واقعی        نمونه‌ی تولیدشده   



#                                     ___________________________        Real 1
#  High dimentional  -->   Real  -->  |  Discriminative network | --->   Fake 0
#   sample space          images      |_________________________|
#                                                          ^
#                        ______________________            |
#  Low dimentional   --> | Generative network | --> Generated fake
#    latent space        |____________________|        images



"✅ How two networks train at the same time?"
# آموزش GAN را می‌توان در دو مرحله‌ی اصلی خلاصه کرد

# مرحله‌ی اول: آموزش Discriminator
# هدف از این مرحله تشخیص بهتر نمونه‌های واقعی و مصنوعی هست
# به Discriminator دو دسته نمونه می‌دهیم:
# 1-تصاویر واقعی از دیتاست    
# 2-تصاویر مصنوعی که Generator ساخته است    
# سپس Discriminator یاد می‌گیره به تصاویر واقعی امتیاز واقعی بودن بالاتر و به تصاویر مصنوعی امتیاز پایین‌تری بده

# مرحله‌ی دوم: آموزش Generator
# این بار هدف این است که Generator تصاویر بهتری بسازد تا Discriminator آن‌ها را واقعی تشخیص دهد
# نکته‌ی مهم: در این مرحله، گرادیان خطای Generator از طریق Discriminator عبور می‌کند تا وزن‌های Generator به‌روزرسانی شوند
# ولی وزن‌های Discriminator در همان مرحله ثابت نگه داشته می‌شوند

# این دو مرحله بارها تکرار می‌شوند
# تا جایی ادامه پیدا میکنه که ادامه‌ی رقابت باعث بهبود متقابل بشه
# در آموزش GAN اصلی، این فرایند به‌صورت یک بازی کمینه‌ـ‌بیشینه (Minimax Game) صورت‌بندی می‌شود


"✅ Does Generator really learn?"
# اگر آموزش خوب پیش برود، Generator به‌تدریج ویژگی‌هایی از داده‌های آموزشی را یاد می‌گیرد
# مثلآ، اگر روی MNIST آموزش ببیند، ممکن است الگوهایی مربوط به ضخامت خطوط، شکل منحنی‌ها ...
#... و ساختار کلی اعداد را یاد بگیرد و با ترکیب آن‌ها تصاویر جدیدی تولید کند
# اما یک نکته‌ی مهم: Generator در GAN معمولی معمولاً تصویر را با بازسازی یک تصویر مشخص از دیتاست تولید نمی‌کند
# ورودی‌اش نویز تصادفی است و خروجی‌اش نمونه‌ی مصنوعی. این تفاوت مهمی با Autoencoder معمولی و VAE دارد











'''
=====================================================
=======  ⭐  Comparison of GAN and VAE   ⭐  =======
=====================================================
'''

"VAE"
# یادگیری یک فضای احتمالی
# یاد می‌گیرد داده‌ها را در یک فضای نهفته‌ی احتمالی نمایش دهد
# سپس از آن فضا نمونه‌گیری می‌کند و با Decoder تصاویر تولید می‌کند
# ویژگی معمول: فضای نهفته‌ی ساختارمند و امکان بازسازی ورودی؛ تصاویر تولیدی گاهی نرم‌تر یا تارتر هستند

"GAN"
# یادگیری از طریق رقابت
# یاد می‌گیرد تصاویر مصنوعی تولید کند و Discriminator تلاش می‌کند آن‌ها را تشخیص دهد
# ویژگی معمول: امکان تولید تصاویر واضح و واقع‌گرایانه؛ اما آموزش می‌تواند ناپایدار باشد و تنوع خروجی‌ها کاهش یابد



# =============================================================================
#                            مقایسه جامع VAE و GAN                            
# =============================================================================
# [1] تعداد شبکه های اصلی
#     ├── VAE : Encoder , Decoder
#     └── GAN : Generator , Discriminator
# -----------------------------------------------------------------------------
# [2] ورودی در زمان تولید
#     ├── VAE : نمونه از فضای نهفته
#     └── GAN : نویز تصادفی
# -----------------------------------------------------------------------------
# [3] هدف آموزش
#     ├── VAE : بازسازی مناسب و منظم کردن فضای نهفته
#     └── GAN : رقابت برای تولید نمونه های واقعی نما
# -----------------------------------------------------------------------------
# [4] تابع هدف
#     ├── VAE : Reconstruction Loss , KL Divergence
#     └── GAN : تابع هدف رقابتی
# -----------------------------------------------------------------------------
# [5] بازسازی یک ورودی مشخص
#     ├── VAE : قابلیت اصلی معماری استاندارد
#     └── GAN : not in simple GAN
# -----------------------------------------------------------------------------
# [6] کیفیت نمونه ها
#     ├── VAE : گاهی نرم تر یا تارتر
#     └── GAN : اغلب می تواند واضح تر باشد
# -----------------------------------------------------------------------------
# [7] چالش رایج
#     ├── VAE : تعادل بین بازسازی و منظم سازی
#     └── GAN : Unstability of training and Mode Collapse
# =============================================================================










'''
===========================================
=======  ⭐  GAN limitations   ⭐  =======
===========================================
'''
# دو مشکل مهم در GAN وجود داره

#----------------
# Mode Collapse
#----------------
# فرض کن دیتاست شامل تمام اعداد 0 تا 9 باشد. Generator باید بتواند انواع مختلف عدد را تولید کند
# اما ممکن است یاد بگیرد که فقط چند نوع تصویر را تولید کند
# مثلاً بارها و بارها تصویری شبیه عدد 7 بسازد، چون همین تعداد محدود تصویر برای فریب‌دادن Discriminator کافیه
# به این اتفاق Mode Collapse می‌گیم: مدل به‌جای یادگیری تنوع داده‌ها، به تعداد محدودی از الگوها وابسته می‌شود

#-------------------------
# Unstability of training
#-------------------------
# در GAN، دو شبکه باید هم‌زمان یاد بگیرند
# اگر Discriminator خیلی سریع قوی شود، Generator ممکن است سیگنال آموزشی مفیدی دریافت نکند
#  اگر Generator سریع‌تر پیشرفت کند، Discriminator نیز ممکن است به‌درستی آموزش نبیند
# بنابراین تنظیم نرخ یادگیری، معماری، روش آموزش و تعادل میان دو شبکه اهمیت زیادی دارد












'''
==================================================================================
=======  ⭐  Preaparing MNIST data for GAN and VAE codes in pytorch   ⭐  =======
==================================================================================
'''
# در اینجا Dataloader های mnist رو آماده میکنیم
# در ادامه برای کدزنی GAN و VAE از همینا استفاده میکنیم برای دیتای ورودی


#------------------------------
#    Preaparing mnist dataset
#------------------------------

import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import matplotlib.pyplot as plt

# Reproducibility
torch.manual_seed(42)

# Choose CPU or GPU automatically
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Device:", device)

# MNIST images will be tensors with values in [0, 1]
transform = transforms.ToTensor()

train_dataset = datasets.MNIST(
    root="data",
    train=True,
    download=True,
    transform=transform
)

test_dataset = datasets.MNIST(
    root="data",
    train=False,
    download=True,
    transform=transform
)

train_loader = DataLoader(
    train_dataset,
    batch_size=128,
    shuffle=True,
    num_workers=0
)

test_loader = DataLoader(
    test_dataset,
    batch_size=128,
    shuffle=False,
    num_workers=0
)

print("Training images:", len(train_dataset))
print("Test images:", len(test_dataset))


# خروجی مورد انتظار:
    # Training images: 60000
    # Test images: 10000

#  متود ToTensor() پیکسل‌ها را به بازه‌ی [0, 1] می‌برد
# تصاویر MNIST خاکستری و دارای ابعاد 28 × 28 هستند





#---------------------------
#    Displaying real data
#---------------------------
# نمایش تعدادی تصویر واقعی

images, labels = next(iter(train_loader))

fig, axes = plt.subplots(2, 8, figsize=(12, 4))

for i, ax in enumerate(axes.flat):
    ax.imshow(images[i, 0], cmap="gray")
    ax.set_title(f"Label: {labels[i].item()}")
    ax.axis("off")

plt.tight_layout()
plt.show()

print("Batch shape:", images.shape)


# شکل Batch باید این باشد:
    # torch.Size([128, 1, 28, 28])

# معنی ابعاد:
# عدد 128: تعداد تصاویر در Batch    
# عدد 1: تعداد کانال‌های تصویر    
# عدد 28: ارتفاع    
# عدد 28: عرض    










'''
=================================================
=======  ⭐  VAE coding in pytorch   ⭐  =======
=================================================
'''
# معماری مدل
# در این پروژه از یک مدل fully connected VAE استفاده میکنیم

# ورودی: تصویر 28x28        
# مقدار پیکسل= 784        
#               ↓  
#            Encoder
#           784 → 400
#               ↓  
# دو خروجی: μ و logvar       
# هر کدام 20 مقدار        
#               ↓  
#        Reparameterization
# تولید بردار نهفته z با ابعاد 20
#               ↓  
#            Decoder
#        20 → 400 → 784
#               ↓  
# خروجی: تصویر بازسازی‌شده     
#            28 × 28



"----------------------------"
"    Creating VAE class      "
"----------------------------"

class VAE(nn.Module):

    def __init__(self, input_dim=784, hidden_dim=400, latent_dim=20):
        super().__init__()

        self.latent_dim = latent_dim

        # Encoder
        self.fc1 = nn.Linear(input_dim, hidden_dim)

        # Mean of latent distribution
        self.fc_mu = nn.Linear(hidden_dim, latent_dim)

        # Log variance of latent distribution
        self.fc_logvar = nn.Linear(hidden_dim, latent_dim)

        # Decoder
        self.fc2 = nn.Linear(latent_dim, hidden_dim)
        self.fc3 = nn.Linear(hidden_dim, input_dim)

    def encode(self, x):

        h = torch.relu(self.fc1(x))

        mu = self.fc_mu(h)
        logvar = self.fc_logvar(h)

        return mu, logvar

    def reparameterize(self, mu, logvar):

        # Convert log variance to standard deviation
        std = torch.exp(0.5 * logvar)

        # Random standard normal noise
        eps = torch.randn_like(std)

        # Reparameterization trick
        z = mu + std * eps

        return z

    def decode(self, z):

        h = torch.relu(self.fc2(z))

        # Pixel probabilities / intensities in [0, 1]
        reconstructed = torch.sigmoid(self.fc3(h))

        return reconstructed

    def forward(self, x):

        # Flatten: [B, 1, 28, 28] -> [B, 784]
        x = x.view(x.size(0), -1)

        mu, logvar = self.encode(x)

        z = self.reparameterize(mu, logvar)

        reconstructed = self.decode(z)

        return reconstructed, mu, logvar



"----------------------------"
"    Creating VAE model      "
"----------------------------"
# در اینجا latent_dim = 20 است. یعنی هر تصویر 784 پیکسلی به یک نمایش احتمالی 20 بعدی تبدیل می‌شود

latent_dim = 20
vae = VAE(latent_dim=latent_dim).to(device)
print(vae)



"-------------------------------"
"    Explaining the parameters  "  
"-------------------------------"

# اول اینکه fc_mu میانگین توزیع نهفته را تولید می‌کند
# همچنین fc_logvar لگاریتم واریانس را تولید می‌کند؛ استفاده از لگاریتم به پایداری محاسبات کمک می‌کند

# متود reparameterize() بردار z را با استفاده از میانگین، انحراف معیار و نویز تصادفی می‌سازد
# که در آن ϵ از توزیع نرمال استاندارد نمونه‌گیری می‌شود
    # z=μ+exp(0.5logσ**2)ϵ

# چرا مستقیماً randn را به Encoder نمی‌دهیم؟
# چون می‌خواهیم مقدار تصادفی از پارامترهای یادگرفتنی جدا باشد
# تا بتوانیم با Backpropagation پارامترهای Encoder را آموزش دهیم



"----------------------------"
"   Defining Loss function   "
"----------------------------"
# اینجا تابع Loss رو تعریف میکنیم

# کلا VAE دو هدف دارد:
# بازسازی مناسب تصویر    
# منظم‌کردن فضای نهفته با KL Divergence    

# برای این نسخه‌ی آموزشی، از Binary Cross-Entropy برای بازسازی پیکسل‌ها و KL Divergence استاندارد استفاده می‌کنیم


def vae_loss(reconstructed, x, mu, logvar):

    # Flatten original images
    x = x.view(x.size(0), -1)

    # Reconstruction loss
    reconstruction_loss = nn.functional.binary_cross_entropy( reconstructed, x, reduction="sum" )

    # KL divergence
    kl_loss = -0.5 * torch.sum( 1 + logvar - mu.pow(2) - logvar.exp() )

    total_loss = reconstruction_loss + kl_loss

    return total_loss, reconstruction_loss, kl_loss


# فرمول Loss
    # L = L_BCE​ + L_KL
# چرا BCE؟ چون پیکسل‌ها در بازه‌ی صفر تا یک هستند و خروجی Decoder نیز با Sigmoid به همین بازه محدود می‌شود
# این انتخاب را می‌توان به‌عنوان یک مدل برنولی برای پیکسل‌ها تفسیر کرد
# هرچند تصویرهای خاکستری واقعی الزاماً داده‌های برنولی نیستند

# از reduction="sum" استفاده کرده‌ایم؛ بنابراین مقدار Loss با اندازه‌ی Batch نیز افزایش می‌یابد
# هنگام گزارش نتایج، Loss را بر تعداد تصاویر تقسیم می‌کنیم تا مقدار میانگین هر تصویر قابل‌مقایسه باشد



"----------------------"
"   Training the VAE   "
"----------------------"

vae_optimizer = torch.optim.Adam( vae.parameters(), lr=0.001  )

epochs = 15

vae_train_history = []
vae_val_history = []

for epoch in range(epochs):

    # -------------------------
    # Training
    # -------------------------
    vae.train()

    train_total = 0.0
    train_reconstruction = 0.0
    train_kl = 0.0

    for x, _ in train_loader:

        x = x.to(device)

        reconstructed, mu, logvar = vae(x)

        loss, rec_loss, kl_loss = vae_loss( reconstructed, x, mu, logvar )

        vae_optimizer.zero_grad()

        loss.backward()

        vae_optimizer.step()

        train_total += loss.item()
        train_reconstruction += rec_loss.item()
        train_kl += kl_loss.item()

    n_train = len(train_loader.dataset)

    train_loss = train_total / n_train
    train_rec = train_reconstruction / n_train
    train_kl_avg = train_kl / n_train

    # -------------------------
    # Validation
    # -------------------------
    vae.eval()

    val_total = 0.0

    with torch.no_grad():

        for x, _ in test_loader:

            x = x.to(device)

            reconstructed, mu, logvar = vae(x)

            loss, _, _ = vae_loss( reconstructed, x, mu, logvar )

            val_total += loss.item()

    val_loss = val_total / len(test_loader.dataset)

    vae_train_history.append(train_loss)
    vae_val_history.append(val_loss)

    print(
        f"Epoch [{epoch + 1}/{epochs}] "
        f"Train: {train_loss:.2f} | "
        f"Val: {val_loss:.2f} | "
        f"Recon: {train_rec:.2f} | "
        f"KL: {train_kl_avg:.2f}"  )


# هنگام آموزش چه اتفاقی می‌افتد؟
# این vae(x) تصویر را بازسازی می‌کند    
# این vae_loss() خطای بازسازی و KL را محاسبه می‌کند    
# متود loss.backward() گرادیان‌ها را به دست می‌آورد    
# متود vae_optimizer.step() وزن‌ها را به‌روزرسانی می‌کند    
# در پایان هر Epoch، مدل روی مجموعه‌ی ارزیابی بررسی می‌شود    



"----------------------------"
"   Drawing graph for Loss   "
"----------------------------"
# رسم نمودار Loss
# در این نمودار، Loss پایین‌تر معمولاً نشانه‌ی بهبود هدف آموزشی است، اما برای ارزیابی VAE کافی نیست
# باید کیفیت بازسازی و تنوع تصاویر تولیدشده را نیز بررسی کرد

plt.figure(figsize=(8, 5))

plt.plot(vae_train_history, label="Train Loss")
plt.plot(vae_val_history, label="Validation Loss")

plt.xlabel("Epoch")
plt.ylabel("Loss per image")
plt.title("VAE Training History")

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



"-----------------------------------------------"
"  Viewing the reconstruction of images by VAE  "
"-----------------------------------------------"
# تا اینجا مدل را آموزش داده‌ایم. حالا بررسی می‌کنیم که آیا می‌تواند تصاویر واقعی را بازسازی کند یا خیر

vae.eval()

images, labels = next(iter(test_loader))
images = images[:10].to(device)

with torch.no_grad():
    reconstructed, mu, logvar = vae(images)

# Convert flattened output back to images
original_images = images.cpu()
reconstructed_images = reconstructed.view(-1, 1, 28, 28).cpu()

fig, axes = plt.subplots(2, 10, figsize=(15, 4))

for i in range(10):

    axes[0, i].imshow( original_images[i, 0], cmap="gray" )

    axes[1, i].imshow( reconstructed_images[i, 0], cmap="gray" )

    axes[0, i].set_title("Original")
    axes[1, i].set_title("Reconstructed")

    axes[0, i].axis("off")
    axes[1, i].axis("off")

plt.tight_layout()
plt.show()


# ردیف اول تصویر واقعی و ردیف دوم بازسازی VAE است
# چون VAE در این معماری از توزیع احتمالی نمونه‌گیری می‌کند
# ممکن است تصاویر بازسازی‌شده کمی نرم‌تر یا تارتر از تصاویر اصلی باشند



"--------------------------------------------"
"   Generating totally new photos with VAE   "
"--------------------------------------------"

# این قسمت مهم‌ترین بخش مدل مولد است
# در اینجا دیگر تصویر واقعی را به مدل نمی‌دهیم
# مستقیماً از توزیع نرمال استاندارد، بردارهای تصادفی با ابعاد 20 می‌سازیم و به Decoder می‌دهیم

vae.eval()

num_samples = 64

with torch.no_grad():

    # Sample latent vectors from N(0, I)
    z = torch.randn( num_samples, latent_dim, device=device )

    # Generate new images
    generated = vae.decode(z)

generated = generated.view(-1, 1, 28, 28).cpu()

fig, axes = plt.subplots(8, 8, figsize=(8, 8))

for i, ax in enumerate(axes.flat):

    ax.imshow(generated[i, 0], cmap="gray")
    ax.axis("off")

plt.suptitle("New Images Generated by VAE")
plt.tight_layout()
plt.show()

# اگر آموزش خوب انجام شده باشد، باید تصاویری شبیه ارقام دست‌نویس ببینیم
# البته ممکن است بعضی تصاویر مبهم یا نامعتبر باشند

# نکته‌ی اصلی این است که این 64 تصویر از تصاویر تست انتخاب نشده‌اند
# آن‌ها از بردارهای تصادفی فضای نهفته تولید شده‌اند



"----------------------------------------"
"   Save and Load of trained VAE Model   "
"----------------------------------------"

# برای اینکه مجبور نباشیم هر بار مدل را از ابتدا آموزش بدیم:
torch.save( vae.state_dict(), "vae_mnist.pth" )

# برای بارگذاری:
loaded_vae = VAE(latent_dim=latent_dim).to(device)
loaded_vae.load_state_dict(  torch.load("vae_mnist.pth", map_location=device, weights_only=True)  )
loaded_vae.eval()

# فایل vae_mnist.pth شامل وزن‌های یادگرفته‌شده است
# برای بارگذاری صحیح، باید معماری مدل و مقدار latent_dim با مدل ذخیره‌شده مطابقت داشته باشند












'''
=================================================
=======  ⭐  GAN coding in pytorch   ⭐  =======
=================================================
'''

# برخلاف VAE، در GAN دو شبکه‌ی جداگانه داریم:
# شبکه Generator: از نویز تصویر تولید می‌کند    
# شبکه Discriminator: احتمال واقعی بودن تصویر را تخمین می‌زند    

# در این پروژه از یک GAN ساده و کاملاً متصل استفاده می‌کنیم
# این مدل برای یادگیری مفاهیم مناسب است؛ بعداً می‌توانیم نسخه‌ی DCGAN را با لایه‌های convolutionic پیاده‌سازی کنیم


#---------------------
# Architecture of GAN
#---------------------
# تفاوت این معماری با VAE اینه: Generator مستقیماً نویز را می‌گیرد؛ لازم نیست تصویر ورودی را Encode کند

#         Noise Vector
# 100 عدد تصادفی        
#               ↓ 
#          Generator
#     100 → 256 → 512 → 784
#               ↓ 
# تصویر مصنوعی 28 × 28       
#               ↓ 
#        Discriminator
#    784 → 512 → 256 → 1
#               ↓ 
# امتیاز واقعی بودن     
# عددی بین صفر و یک     



"------------------------"
"   Creating Generator   "
"------------------------"

class Generator(nn.Module):

    def __init__(self, latent_dim=100, image_dim=784):
        super().__init__()

        self.net = nn.Sequential(

            nn.Linear(latent_dim, 256),
            nn.LeakyReLU(0.2),

            nn.Linear(256, 512),
            nn.LeakyReLU(0.2),

            nn.Linear(512, 784),
            nn.Sigmoid()
        )

    def forward(self, z):

        img = self.net(z)

        # [B, 784] -> [B, 1, 28, 28]
        img = img.view(z.size(0), 1, 28, 28)

        return img

# اینجا latent_dim=100 یعنی Generator در هر بار تولید، یک بردار شامل 100 عدد تصادفی می‌گیرد
# خروجی لایه‌ی آخر Sigmoid است؛ پس مقدار پیکسل‌ها در بازه‌ی 0 تا 1 قرار می‌گیرند، درست مانند تصاویر MNIST پس از ToTensor().



"----------------------------"
"   Creating Discriminator   "
"----------------------------"

class Discriminator(nn.Module):

    def __init__(self, image_dim=784):
        super().__init__()

        self.net = nn.Sequential(

            nn.Linear(image_dim, 512),
            nn.LeakyReLU(0.2),

            nn.Linear(512, 256),
            nn.LeakyReLU(0.2),

            nn.Linear(256, 1)
        )

    def forward(self, img):

        # [B, 1, 28, 28] -> [B, 784]
        img = img.view(img.size(0), -1)

        # Return raw logits
        return self.net(img)

# در انتهای Discriminator از Sigmoid استفاده نکردیم. چرا؟
# چون قرار است از BCEWithLogitsLoss استفاده کنیم که... 
#... محاسبه‌ی Sigmoid و Binary Cross-Entropy را به شکل عددی پایدار در یک تابع ترکیب می‌کند

# خروجی Discriminator در اینجا یک Logit است؛ نه احتمال نهایی بین 0 و 1
# اگر بخواهیم احتمال را ببینیم، بعداً می‌توانیم torch.sigmoid(logits) را محاسبه کنیم



"------------------------------------------"
"   Creating Model and setting optimizer   "
"------------------------------------------"
# برای GAN دو Optimizer جدا داریم، چون هر شبکه وزن‌های خودش را دارد و هدف آموزشی آن‌ها متفاوت است

latent_dim_gan = 100

generator = Generator( latent_dim=latent_dim_gan).to(device)

discriminator = Discriminator().to(device)

criterion_gan = nn.BCEWithLogitsLoss()

optimizer_g = torch.optim.Adam( generator.parameters(), lr=0.0002, betas=(0.5, 0.999) )

optimizer_d = torch.optim.Adam( discriminator.parameters(), lr=0.0002, betas=(0.5, 0.999))

print(generator)
print(discriminator)



"------------------------"
"   Training GAN model   "
"------------------------"
# آموزش GAN؛ مهم‌ترین بخش پروژه
# در هر Batch، ابتدا Discriminator را آموزش می‌دهیم و سپس Generator را آموزش میدیم

# مرحله‌ی اول: آموزش Discriminator
# اول Discriminator باید یاد بگیرد:
# به تصویر واقعی امتیاز واقعی بودن بالا بدهد    
# به تصویر تولیدشده امتیاز واقعی بودن پایین بدهد    
# برای این کار، هدف تصویر واقعی را 1 و هدف تصویر مصنوعی را 0 قرار می‌دهیم    

# مرحله‌ی دوم: آموزش Generator
# این بار Generator می‌خواهد تصاویرش به‌عنوان واقعی تشخیص داده شوند
# بنابراین به Discriminator تصاویر مصنوعی می‌دهد، اما هدف آموزشی را 1 قرار می‌دهیم

# این نکته را خوب به خاطر بسپار: در مرحله‌ی آموزش Generator، برچسب هدف برای تصاویر تولیدشده 1 است
# چون Generator می‌خواهد Discriminator را فریب دهد؛ نه اینکه تصویر تولیدشده واقعاً از دیتاست آمده باشد


epochs_gan = 30

g_losses = []
d_losses = []

for epoch in range(epochs_gan):

    generator.train()
    discriminator.train()

    total_g_loss = 0.0
    total_d_loss = 0.0

    for real_images, _ in train_loader:

        real_images = real_images.to(device)
        batch_size = real_images.size(0)

        # Labels
        real_labels = torch.ones( batch_size, 1, device=device )
        fake_labels = torch.zeros( batch_size, 1, device=device )

        # ==================================
        # 1. Train Discriminator
        # ==================================

        optimizer_d.zero_grad()

        # Score real images
        real_logits = discriminator(real_images)
        real_loss = criterion_gan( real_logits, real_labels )

        # Generate fake images
        z = torch.randn( batch_size, latent_dim_gan, device=device )
        fake_images = generator(z)

        # Detach: do not update Generator here
        fake_logits = discriminator( fake_images.detach() )
        fake_loss = criterion_gan( fake_logits, fake_labels)
        d_loss = real_loss + fake_loss

        d_loss.backward()
        optimizer_d.step()

        # ==================================
        # 2. Train Generator
        # ==================================

        optimizer_g.zero_grad()

        # Generate a fresh batch of fake images
        z = torch.randn( batch_size, latent_dim_gan, device=device )
        fake_images = generator(z)

        # Generator wants fake images to look real
        fake_logits = discriminator(fake_images)
        g_loss = criterion_gan( fake_logits, real_labels )

        g_loss.backward()
        optimizer_g.step()

        total_d_loss += d_loss.item() * batch_size
        total_g_loss += g_loss.item() * batch_size

    epoch_d_loss = total_d_loss / len(train_loader.dataset)
    epoch_g_loss = total_g_loss / len(train_loader.dataset)

    d_losses.append(epoch_d_loss)
    g_losses.append(epoch_g_loss)

    print(
        f"Epoch [{epoch + 1}/{epochs_gan}] "
        f"D Loss: {epoch_d_loss:.4f} | "
        f"G Loss: {epoch_g_loss:.4f}"    )



# چرا detach() مهم است؟
# در مرحله‌ی آموزش Discriminator، تصویر مصنوعی را از Generator می‌گیریم
# اما نمی‌خواهیم خطای این مرحله وزن‌های Generator را تغییر دهد
# fake_images.detach()

# باعث می‌شود گرادیان از این مسیر به Generator برنگردد
# سپس در مرحله‌ی دوم، تصویر جدید را بدون detach() وارد Discriminator می‌کنیم
# تا گرادیان بتواند از Discriminator عبور کند و Generator را به‌روزرسانی کند

# در مرحله‌ی دوم، وزن‌های Discriminator با optimizer_g.step() تغییر نمی‌کنند، چون Optimizer مربوط به Generator است
# برای کارایی بهتر می‌توان هنگام آموزش Generator، محاسبه‌ی گرادیان وزن‌های Discriminator را ...
# ... نیز غیرفعال کرد، اما این نسخه برای آموزش اولیه ساده‌تر است




"----------------------------------"
"   Drawing graph for GAN Losses   "
"----------------------------------"
# رسم نمودار Lossهای GAN

plt.figure(figsize=(8, 5))

plt.plot(g_losses, label="Generator Loss")
plt.plot(d_losses, label="Discriminator Loss")

plt.xlabel("Epoch")
plt.ylabel("Loss per image")
plt.title("GAN Training History")

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# توجه: در GAN، برخلاف Autoencoder، پایین آمدن هر دو Loss به‌طور هم‌زمان الزاماً نشانه‌ی آموزش بهتر نیست
# چون دو شبکه هدف‌های متضاد دارند، باید نمودار Loss را همراه با کیفیت تصاویر تولیدشده بررسی کرد



"----------------------------------"
"   Drawing graph for GAN Losses   "
"----------------------------------"
# نمایش تصاویر تولیدشده توسط GAN
# حالا می‌خواهیم ببینیم Generator چه چیزی یاد گرفته است

generator.eval()

num_samples = 64

with torch.no_grad():

    z = torch.randn( num_samples, latent_dim_gan, device=device )

    generated_images = generator(z).cpu()

fig, axes = plt.subplots(8, 8, figsize=(8, 8))

for i, ax in enumerate(axes.flat):

    ax.imshow( generated_images[i, 0], cmap="gray" )

    ax.axis("off")

plt.suptitle("New Images Generated by GAN")
plt.tight_layout()
plt.show()

# این تصاویر از نویز تصادفی تولید شده‌اند
# انتظار داریم با آموزش مناسب، شکل‌هایی شبیه ارقام دست‌نویس ظاهر شوند

# اگر تصاویر شبیه نویز باشند، یا همه‌ی تصاویر تقریباً یکسان باشند، احتمالاً آموزش هنوز کافی نبوده
#  یا GAN دچار مشکل شده. تعداد Epoch بیشتر همیشه مشکل را حل نمی‌کند؛ تنظیم معماری و روش آموزش نیز اهمیت دارد



"-------------------------------------"
"   Inspecting discriminator output   "
"-------------------------------------"
# بررسی خروجی Discriminator
# می‌توانیم از Discriminator بپرسیم که تصاویر تولیدشده چقدر واقعی به نظر می‌رسند:

generator.eval()
discriminator.eval()

with torch.no_grad():

    z = torch.randn( 16, latent_dim_gan, device=device )

    fake_images = generator(z)

    logits = discriminator(fake_images)

    probabilities = torch.sigmoid(logits)

print(probabilities.squeeze().cpu())


# مقادیر بین 0 و 1 اند:
# مقدار نزدیک به 0: Discriminator نمونه را بیشتر مصنوعی ارزیابی می‌کند
# مقدار نزدیک به 1: Discriminator نمونه را بیشتر واقعی ارزیابی می‌کند

# اما یک نکته‌ی مهم وجود دارد: این اعداد معیار قطعی کیفیت تصویر نیستند
# ممکن است Discriminator ضعیف باشد و تصویر نامناسبی را هم واقعی تشخیص دهد



"-------------------------------------"
"   Save and Load trained GAN model   "
"-------------------------------------"

# برای ذخیره:
    
torch.save( generator.state_dict(),"generator_mnist.pth" )
torch.save( discriminator.state_dict(), "discriminator_mnist.pth" )


# برای بارگذاری Generator:

loaded_generator = Generator( latent_dim=latent_dim_gan ).to(device)
loaded_generator.load_state_dict( torch.load( "generator_mnist.pth", map_location=device, weights_only=True)  )
loaded_generator.eval()

# حالا میشه بدون آموزش مجدد Generator، تصاویر جدید تولید کرد



"-------------------------------------"
"Improving the Quality of Experiments"
"-------------------------------------"
# ذخیره‌ی تصاویر در پایان هر Epoch
# در GAN، دیدن روند تولید تصاویر از بررسی Lossها نیز مهم‌تر میتونه باشه
# میشه در انتهای هر Epoch یک Batch ثابت از نویز را به Generator داد و خروجی‌ها را ذخیره کرد یا نمایش داد

# ابتدا یک نویز ثابت میسازیم:
fixed_noise = torch.randn( 64, latent_dim_gan, device=device  )

# سپس در پایان هر Epoch، پس از آموزش:
generator.eval()

with torch.no_grad():
    sample_images = generator(fixed_noise).cpu()

fig, axes = plt.subplots(8, 8, figsize=(8, 8))

for i, ax in enumerate(axes.flat):
    ax.imshow(sample_images[i, 0], cmap="gray")
    ax.axis("off")

plt.suptitle(f"GAN - Epoch {epoch + 1}")
plt.tight_layout()
plt.show()

generator.train()


# چون نویز ثابت است، میشه تغییر همان ورودی‌ها را در طول آموزش دنبال کرد
# در پروژه‌های طولانی بهتره تصاویر را در فایل ذخیره کرد، نه اینکه برای تمام Epochها پنجره‌ی جدید باز بشه














'''
======================================================================
=======  ⭐  Comparison of VAE outcome with GAN outcome   ⭐  =======
======================================================================
'''
# مقایسه‌ی خروجی VAE و GAN.  خلاصه‌ی تفاوت در کد

"VAE"
# ورودی تصویر واقعی است و مدل برای بازسازی آن آموزش می‌بیند
# در زمان تولید، Decoder از بردار تصادفی فضای نهفته استفاده می‌کند

reconstructed, mu, logvar = vae(images)
loss = reconstruction_loss + kl_loss


"GAN"
# اینجا Generator از ابتدا با نویز تصادفی تصویر می‌سازد
# سپس Discriminator کمک می‌کند این تصاویر به نمونه‌های واقعی شبیه شوند

z = torch.randn(batch_size, 100, device=device)
fake_images = generator(z)




# ==============================================================================
#                              مقایسه موضوعی VAE و GAN                            
# ==============================================================================
# [1] ورودی آموزش
#     ├── VAE : تصویر واقعی
#     └── GAN : Real photo for discriminator and noise for generator
# ------------------------------------------------------------------------------
# [2] تعداد شبکه ها
#     ├── VAE : A model with decoder and encoder
#     └── GAN : دو مدل مستقل
# ------------------------------------------------------------------------------
# [3] هدف اصلی
#     ├── VAE : بازسازی و یادگیری توزیع نهفته
#     └── GAN : تولید نمونه های واقعی نما
# ------------------------------------------------------------------------------
# [4] تولید تصویر جدید
#     ├── VAE : Sampling the hidden space and decoder
#     └── GAN : Noise and generator
# ------------------------------------------------------------------------------
# [5] چالش اصلی
#     ├── VAE : Regeneration and balance
#     └── GAN : پایداری آموزش و تنوع خروجی
# ==============================================================================



















