
'''
===============================================================================
===============================================================================
================       Created on Mon Oct 19 22:29:18 2026     ================
================                IDE: Spyder                    ================
================         Author: Khashayar Alipour             ================
================     AI Autoencoder (encoder-decoder) codes    ================
===============================================================================
===============================================================================
'''


# در این فایل کدزنی 0 تا 100 مدل Autoencoder هست و در نهایت یک فایل از کدهای آماده هست
# از دیتاست mnist استفاده شده برای ورودی

# این مدل 2 بخش داره: encoder - decoder
# بعد از train ما یک latent representation یا نمایش پنهان بدست میاریم که این مهمترین بخش هست
# از این بخش میشه یا به Encoder برسیم، یا بریم به decoder برسیم
# با decoder میتونیم تصویر ورودی رو compact کنیم
# با Decoder میشه برای Regeneration استفاده کرد مثلا در VAE یا GAN

# Input Image
#      ↓
#  Encoder
#      ↓
# Latent Representation
#      ↓
#  Decoder
#      ↓
# Reconstructed Image





"-------------------------"
"    Importing library    "
"-------------------------"

#pip install torch torchvision 

import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import matplotlib.pyplot as plt



"----------------------"
"    Importing data    "
"----------------------"

# با استفاده از transform میتونیم دیتای ورودی رو تبدیل به Tensor کنیم (فرمت مورد نیاز دیتا برای کارمون)
transform = transforms.Compose([
    transforms.ToTensor()
])

# اینجا دیتاست رو وارد میکنیم
# پارامتر root یه آدرس داره. برای بار اول میاد دیتا رو دانلود میکنه (download=True) و در این آدرس میذاره
# برای دفعات بعدی، میاد از دیتایی که در همین پوشه هست و قبلا دانلود کرده استفاده میکنه
train_dataset = datasets.MNIST(
    root="C:/Users/C P C/Desktop/mnist_data",
    train=True,
    download=True,
    transform=transform
)

test_dataset = datasets.MNIST(
    root="C:/Users/C P C/Desktop/mnist_data",
    train=False,
    download=True,
    transform=transform
)




"-----------------------------"
"      Creating dataloader    "
"-----------------------------"
# اینجا میایم برای دیتایی که import کردیم یک dataloader میسازیم
# حالا فایدش چیه؟
# این یک wrapper هست که دور دیتاست ما میاد و بهش قابلیت اینو میده که بصورت batch batch وارد training loop بشه
# وقتی میگیم shuffle=True یعنی بیا train_dataset مارو با این batch size که بهت دادیم shuffle کن

BATCH_SIZE = 128    # برای اینکه تغییر دادن کد راحت تر بشه اینجوری مینویسیم

train_loader = DataLoader(
    train_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True
)


test_loader = DataLoader(
    test_dataset,
    batch_size=BATCH_SIZE,
    shuffle=False
)




"---------------------------------------"
"      Creating Neural Network Model    "
"---------------------------------------"

# یک کلاس میسازیم که از nn.Module ارث بری میکنه
# اینجا مدل encoder و decoder رو عمدا جدا باید بسازیم چون عملا بعضی جاها فقط از یکیشون ممکنه استفاده بشه

# در init ما مدلهایی ساختیم که این کار رو برامون انجام میدن:
    # mnist image 28 x 28 pixel --> flatten --> 784
    # 784
    #  |
    # 128
    #  |
    # 64
    #  |
    # 32   <-- latent vector
    #  |
    # 64
    #  |
    # 128
    #  |
    # 784
    # Reconstructed image

# در تابع Forward این اتفاق میوفته:
# میگیم x رو به عنوان ورودی بگیر، بده Encoder تا کوچیکش (compact) کنه و تبدیل کنه به latent representation
# بعدش بده به decoder که بیاد برامون بازش کنه و Recontruction انجام بده


class Autoencoder(nn.Module):

    def __init__(self):

        super().__init__()

        # Encoder
        
        self.encoder = nn.Sequential(

            nn.Linear(784,128),
            nn.ReLU(),

            nn.Linear(128,64),
            nn.ReLU(),

            nn.Linear(64,32)   
        )


        # Decoder

        self.decoder = nn.Sequential(

            nn.Linear(32,64),
            nn.ReLU(),

            nn.Linear(64,128),
            nn.ReLU(),

            nn.Linear(128,784),
            nn.Sigmoid()

        )


    def forward(self,x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded
    
    

model = Autoencoder()
print(model)


# -----------
#   نتیجه   
# -----------
# تمام Weight و bias های اولیه در اینجا رندوم هستن

# Autoencoder(
#   (encoder): Sequential(
#     (0): Linear(in_features=784, out_features=128, bias=True)
#     (1): ReLU()
#     (2): Linear(in_features=128, out_features=64, bias=True)
#     (3): ReLU()
#     (4): Linear(in_features=64, out_features=32, bias=True)
#   )
#   (decoder): Sequential(
#     (0): Linear(in_features=32, out_features=64, bias=True)
#     (1): ReLU()
#     (2): Linear(in_features=64, out_features=128, bias=True)
#     (3): ReLU()
#     (4): Linear(in_features=128, out_features=784, bias=True)
#     (5): Sigmoid()
#   )
# )




"----------------------------"
"      Creating Optimizer    "
"----------------------------"

# اینجا میایم میگیم سنجش فاصله بین واقعیت (input image) و نتیجه پردازش (reconstructed image) رو با MSE انجام بده
criterion = nn.MSELoss()


optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)



"--------------------------------"
"      Creating Training Loop    "
"--------------------------------"

# اگه تعداد epoch خیلی کم باشه شاید accuracy خوب نشه و اگه خیلی زیاد باشه شاید overfit بشه
epochs = 20


for epoch in range(epochs):

    total_loss = 0

# علامت _ یعنی label های عکس‌ها. تعریفش نمیکنیم چون لیبل‌ها توی این مدل به کارمون نمیاد    
    # اینجا روی trainloader در بازه epoch حلقه زدیم. این Trainloader که بالاتر ساختیمش عکسهارو 128تا 128تا میده    
    for images,_ in train_loader:

        # اینجا عکس ورودی رو Flatten میکنیم چون مدل یه ورودی 784 نورونی میخواد        
        # اگر از CNN استفاده میکنیم، نیازی به این مرحله نیست        
        images = images.view(images.size(0), -1 )
        
       # در مرحله بعد عکسی که Flatten شده رو میدیم به مدل        
       # پردازش در داخل کلاس مدل در تابع forward انجام میشه        
# در مرحله پردازش، ورودی میره Encoded میشه و سپس decoded و در نهایت output یا recontructed image بدست میاد        
        output = model(images)
        
        # اینجا به Loss تابع criterion رو میدیم تا با استفاده از MSE بیاد input image با output مارو مقایسه کنه       
        loss = criterion( output, images)
        
# برای جلوگیری از اینکه pytorch بیاد acumulate کنه، گرادیان های قبلی رو حذف میکنیم        
        optimizer.zero_grad()

# تا الان feed forward انجام شده بود، اینجا میگیم که backpropagation رو شروع کن و loss رو محاسبه کن        
        loss.backward()
        
        # حالا اینجا optimizer میاد برای ما با استفاده از loss که بالا محاسبه شده، وزن و بایاس هارو آپدیت میکنه        
        #w_new = w_old + grsadient loss
        #b_new = b_old + gradient loss
        optimizer.step()
         
        total_loss += loss.item()

# به ازای هر epoch، بیا total_loss مارو نشون بده    
    print( epoch, total_loss / len(train_loader) )



# ----------
#   نتیجه   
# ----------
# اطلاعات Training loop رو اینجوری مینویسیم
# تا اگه خواستیم مقادیر رو کم و زیاد کنیم بدونیم چیو چیکار کنیم

# 3 shahrivar 19:30
# 784-->128 -->64 -->32 --> 64 --> 128 --> 784
# BATCH_SIZE = 128
# epoch : 20 
# learnin rate lr=0.001  , Adam

# 0 0.05990031891381308
# 1 0.031128693348182034
# 2 0.02481026262410287
# 3 0.021267051842294014
# 4 0.019132345172165555
# 5 0.017601642565035235
# 6 0.01656717282217512
# 7 0.01574911693456585
# 8 0.0148059030208411
# 9 0.013856048763259006
# 10 0.013136773721686304
# 11 0.012582457967912719
# 12 0.012092121618627103
# 13 0.011640000774630352
# 14 0.011217946631472502
# 15 0.010837863157711812
# 16 0.010521079969606292
# 17 0.010199230734203289
# 18 0.009925536616747058
# 19 0.00964217947553724

# اینجا میبینیم که از epoch=0 مقدار loss تا epoch=19 به تدریج کم شده
# این یعنی training درست انجام شده و مراحل کم کردن loss به درستی انجام شده

# اگه تا یه جایی loss کم شد، ولی مثلا از epoch وسط یهو دیدیم دوباره زیاد شده یعنی optimization اشتباهه
# یا learning rate زیادی براش انتخاب کردیم
# یا تعداد Epoch زیاده و باید کم بشه

# یا ممکنه loss کلا کم بشه، ولی بازم عددش بزرگ مونده نشون میده بازم optimization درست نیست
# یا learning rate خیلی خیلی کوچیکه
# یا epoch اینقد کمه که convergence نمیکنه




"---------------------------------------"
"      Creating Predictator function    "
"---------------------------------------"

def predictor(sample_number):

    # از test loader یک image میکشه بیرون که هر image اینجا 28 * 28 هست    
    images,_ = next(iter(test_loader))
    
    # اینجا میگیم که مثلا عکس شماره فلان رو بهمون بده    
    # مثلا images[0] یعنی عکس صفرم رو بهمون بده    
    image = images[sample_number]

    print(image.shape) #torch.Size([1, 28, 28])   اینو نمیشه بدیم به مدل

# از اونجایی که نمیشه عکسی که shape آن برابر torch.Size([1, 28, 28]) هست رو به مدل بدیم    
# بنابراین باید تبدیلش کنیم به image 28 x 28  --> 784    
    input_image = image.view( 1, 784 )

# مدل رو وارد فاز Evaluation کن    
    model.eval()

# گرادیان رو حساب نکن    
    with torch.no_grad():
        # اینجا هم دوباره input image میدیم به مدل و میاد Decode و Encode رو انجام میده        
        # با این تقاوت که دیگه در این مرحله، وزن‌ها و بایاس‌ها دیگه رندوم نیستن و Train شده هستن        
        reconstructed = model( input_image )
        
        
  # چیزی که در متغیر reconstructed ذخیره شده، یک prediction هست که 784 هست    
  # باید دوباره فرمت عکس 28*28 رو بهش بدیم پس از تابع view استفاده میکنیم    
  # این تابع torch tensor های مارو reshape میکنه به شکلی که میخوایم    
    reconstructed = reconstructed.view( 28, 28 )

    # Matplotlib
    plt.figure(figsize=(6,3))
    plt.subplot(1,2,1)
    plt.imshow( image.squeeze(), cmap="gray" )
    plt.title("Original")
    plt.subplot(1,2,2)
    plt.imshow( reconstructed, cmap="gray" )
    plt.title("Reconstructed")
    plt.show()
    
    
# هر عددی که به تابع predictor بدیم، میاد همون عکس رو پیشبینی میکنه
# مثلا اگه عدد 0 رو بدیم میاد عکس 0 رو پیشبینی میکنه که میشه تصویری از عدد 7
# مثلا اگه عدد 10 بدیم میاد 10امین عکس رو پیشبینی میکنه که میشه تصویری از عدد 0
# اگه عدد 15 بدیم میاد 15امین عکس رو پیشبینی میکنه که میشه تصویری از عدد 5
predictor(0)
predictor(10)
predictor(15)




"------------------------------------"
"      Extract Encoder from Model    "
"------------------------------------"
# اینجا میخوایم فقط از قسمت Encoder مدل استفاده کنیم

# مثلا میخوایم عکس 0ام (تصویر عدد 7) رو بدیم به مدل تا encode کنه
images,_ = next(iter(test_loader))
image = images[0]
print(image.shape)   #torch.Size([1, 28, 28])
input_image = image.view( 1, 784 )   # image 28 x 28  --> 784

print(input_image)
# اینجا اگه از input_image بیایم پرینت بگیریم، یه تنسور هست که 784 المنت داره و نشون دهنده عدد 7 هست
# tensor([[0.0000, 0.0000, 0.7533, 0.6511, 0.2290, ... ,0.0000, 0.0000, 0.0000, 0.0000, 0.7643, 0.1910]])


# encoder 784 --> 128 -->64 --> 32
latent = model.encoder(input_image)

print(latent.shape)
# torch.Size([1, 28, 28])
# torch.Size([1, 32])

# درنهایت این latend نتیجه Encode هست که اگه ازش پرینت بگیریم یه تنسور هست مه 32 المنت داره
# یعنی یه 784 تایی رو تبدیل کرده به 32تایی که اگه deocde کنیم خروجی خیلی شبیه ورودی خواهد بود
print(latent)  #32 
# tensor([[  2.4986,   0.4013,  12.2562,   6.1126,  -1.6389,  -0.1747,   6.5088,
#           -6.1541,  -3.0457,   3.3572,  -6.1867,  -2.2521,   2.3027,  -1.1488,
#            0.8401,  -1.3280,  -6.3448,   0.6795,  -4.7161,   8.1691,   1.5787,
#           -2.1075,  -8.8134,   1.3824,  -0.1968,   4.6737,  -1.1708,  -3.1054,
#            5.9101, -10.7373,  14.0128,   3.8900]], grad_fn=<AddmmBackward0>)



#-----------------------------------------------
# نمایش latent representation بوسیله matplotlib
#-----------------------------------------------
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 2))
plt.bar(range(32), latent.squeeze().detach().numpy())
plt.xlabel("Latent dimension")
plt.ylabel("Value")
plt.title("Latent Representation")
plt.show()
































































































