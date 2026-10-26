
'''
===============================================================================
===============================================================================
================       Created on Wed Oct 21 12:54:15 2026     ================
================                IDE: Spyder                    ================
================         Author: Khashayar Alipour             ================
================   VAE(Variational Auto Encoder) model codes   ================
===============================================================================
===============================================================================
'''

# در این فایل کدزنی 0 تا 100 مدل VAE با استفاده از دیتاست mnist انجام میدیم

# همانطور که میدونیم، وقتی ورودی در Autoencoder میاد decode میشه در فضایل latent ما یک latent representation داریم
# یعنی نقاط در یک فضای چندبعدی بصورت بردار قرار دارن ولی این توزیع هیچ نظمی نداره
# اگه بصورت رندوم یک نقطه در این فضا رو انتخاب کنیم که هیج برداری اونجا نیست، نتیجه reconstruction عکس معناداری در نمیاد

# ولی در معماری VAE نه تنها از input میاد در latent یک vector میسازه
# همچنین از این input یک miu و variance هم میگیره که فضای latent رو با توزیعی بسازه که منظم باشه
# در این توزیع 
# در نتیجه در loss function نه تنها یک loss برای reconstruntion میده بهمون، همچنین یک loss میده که بتونیم باهاش فضای latent رو مرتب کنیم
    # Loss fucntion = loss reconstruct + loss moratab konim fazaye latent

# در نتیجه‌ی این کار، فضای latent رو جوری میسازه که در این توزیع ما همپوشانی داریم، و نقطه‌ی خالی که هیچ وکتوری اونجا نباشه نداریم
# به اینصورت میتونیم از قسمت decoder این مدل به عنوان یک generator استفاده کنیم (در autoencoder معمولی، Decoder بدرد نمیخوره)
# چون هر نقطه‌ای بصورت رندوم از فضای latent انتخاب کنیم، احتمال زیاد در آنجا بلخره یک دیتایی هست که بشه باهاش چیزی Reconstruct کنه که شبیه input هست



#                 INPUT
#                    x
#                    │
#                    ▼
#              ┌───────────┐
#              │  Encoder  │
#              └───────────┘
#                    │
#             ┌──────┴──────┐
#             ▼             ▼
#             μ          log σ² -> logarithm variance
#             │             │
#             └──────┬──────┘
#                    │
#          ε ~ N(0,I)│
#                    ▼
#          z = μ + σ × ε
#                    │
#                    ▼
#              ┌───────────┐
#              │  Decoder  │
#              └───────────┘
#                    │
#                    ▼
#                    x̂
#             ┌─────────────┐
#             │    LOSS     │
#             └─────────────┘
#      Reconstruction + KL Divergence





"-------------------------"
"    Importing library    "
"-------------------------"

import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import matplotlib.pyplot as plt



"------------------------------------------------"
"    Importing Dataset and creating data loader  "
"------------------------------------------------"

transform = transforms.ToTensor()

train_dataset = datasets.MNIST(
    root="C:/Users/C P C/Desktop/mnist_data",
    train=True,
    download=True,
    transform=transform
)


loader = DataLoader(
    train_dataset,
    batch_size=128,
    shuffle=True
)




"------------------------------"
"    Creating Encoder Class    "
"------------------------------"

class Encoder(nn.Module):

    def __init__(self, latent_dim):

        super().__init__()


        self.network = nn.Sequential(

            nn.Linear(784,128),
            nn.ReLU(),

            nn.Linear(128,64),
            nn.ReLU()
        )

# با استفاده از latent_dim میتونیم خودمون dimention رو تغییر بدیم        
        self.mu = nn.Linear( 64, latent_dim )
        self.logvar = nn.Linear( 64, latent_dim )


    def forward(self,x):

        h = self.network(x)
        mu = self.mu(h)
        logvar = self.logvar(h)

# همونطور که گفتیم encoder در VAE علاوه بر compact کردن، میخواد latent dimention هم توزیع منظم داشته باشه        
# یعنی برعکس autoencoder معمولی که فقط میخواد compact کنه، VAE دو هدف داره. بنابراین اینجا دو خروجی داریم (mu, logvar)        
        # Logvar = Logarithm of variance (distribution)      
        return mu, logvar
    



"-------------------------------------"
"    Creating Parametrize function    "
"-------------------------------------"

def reparameterize(mu, logvar):

    std = torch.exp( 0.5 * logvar )
    eps = torch.randn_like(std)
    z = mu + eps * std

    return z

# این تابع دوتا ورودی میگیره (مثلا 2 عدد رندوم)
# سپس Z رو که یک نقطه در latent space هست برامون بدست میاره




"------------------------------"
"    Creating Decoder Class    "
"------------------------------"

class Decoder(nn.Module):

    def __init__(self,latent_dim):

        super().__init__()


        self.network = nn.Sequential(

            nn.Linear(latent_dim,64),
            nn.ReLU(),

            nn.Linear(64,128),
            nn.ReLU(),

            nn.Linear(128,784),
            nn.Sigmoid()
        )


    def forward(self,z):
        
        return self.network(z)
    





    
"---------------------------------"
"    Creating VAE(model) Class    "
"---------------------------------"

# کلاس های decoder و encoder و تابع parameterize همشون میرن زیر کلاس VAE

class VAE(nn.Module):

    def __init__(self,latent_dim):

        super().__init__()

        self.encoder = Encoder( latent_dim )

        self.decoder = Decoder( latent_dim )


    def forward(self,x):

        # اتفاقی که در تابع forward میوفته اینه:       
            # اول ورودی وارد میشه و Encode میشه 784 -> 128 -> 64 -> 32        
         # سپس از 32 دوتا linear network میشه که بهمون mu و logvar رو میده        
# در مرحله بعد با استفاده از روش reparameterization میایم mu و logvar رو تبدیل به یک نقطه (z) در latent dimention میکنیم        
# حالا این نقطه رو میدیم به Decoder تا برامون reconstruction انجام بده        

        mu,logvar = self.encoder(x)

        z = reparameterize( mu, logvar )
        
        # z --> decoder 1 --> 784
        reconstruction = self.decoder(z)

        return reconstruction,mu,logvar
    

#------------------
#  Creating model
#------------------

latent_dim = 32

model = VAE(latent_dim)

    
    
    
"------------------------------"
"    Creating Loss function    "
"------------------------------"

# اینجا تابع loss رو میسازیم و میاد از روش binary cross entropy استفاده میکنه
# کارش اینه که بسنجه که distribution هایی که در latent dimention قرار دارن، چقدر قوی باهم همپوشانی دارن


def vae_loss( reconstruction, x, mu, logvar ):
    
    recon_loss = nn.functional.binary_cross_entropy(  reconstruction, x, reduction="sum" )
    
    kl_loss = -0.5 * torch.sum( 1 + logvar - mu.pow(2) - logvar.exp() )

    return recon_loss + kl_loss




"--------------------------"
"    Creating Optimizer    "
"--------------------------"

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)




"--------------------"
"    Training loop   "
"--------------------"

epochs=20    # میگیم 20 بار اجرا کن

for epoch in range(epochs):

    total_loss=0

    for images,_ in loader:
        
        images = images.view( images.size(0), -1 )   # input image: 28 x 28 --> 784

        # تصاویری که در متغیر images قرار دارن الان قالب درست برای پردازش توسط مدل رو دارن. پس اینجا میدیمش به مدل        
        # در کلاس مدل VAE مشخص کردیم که در نهایت سه خروجی بهمون بده: reconstruction, mu, logvar        
        reconstruction,mu,logvar = model(images)

        #loss = loss autoencoder(input - output) + KD(latent dimention)
        # این loss هم میسنجه که input و output چقد بهم شبیه هستن، هم اینکه میسنجه latent dimention (KD) چقد توزیع منظمی داره        
        loss = vae_loss( reconstruction, images, mu, logvar )

        optimizer.zero_grad()    # erase gradients

        loss.backward()   # calculate loss

        optimizer.step()  # Update parameters

        total_loss += loss.item()


    print( epoch, total_loss/len(loader) )



# -------------
#   نتیجه     
# -------------

# 3 shahrivar 19:54
# 784 -> 128 -> 64 -> 32 -> 64 -> 128 -> 784
# BATCH_SIZE = 128
# epoch : 20 
# learnin rate=0.001  , Adam


# 0 26360.403026719083
# 1 20282.282428538114
# 2 17785.23787521655
# 3 16583.5038333722
# 4 15845.599634361673
# 5 15395.58894839419
# 6 15102.454180686967
# 7 14873.046658448828
# 8 14710.54892390725
# 9 14577.809343350213
# 10 14480.693298990538
# 11 14391.627994236407
# 12 14318.76106076759
# 13 14258.23489972015
# 14 14201.763736423907
# 15 14160.417460687633
# 16 14112.349426139392
# 17 14073.366123484142
# 18 14037.311702508661
# 19 13999.265096115405


    

"-----------------------------"
"    Reconstruction example   "
"-----------------------------"

# میخوایم بصورت رندوم یه generate انجام بدیم
# مثلا image صفرم رو انتخاب میکنیم، میکشیم بیرون و فرمتشو برای مدل تغییر میدیم و تبدیلش میکنیم به ورودی

images,_ = next(iter(loader))   # image -> 28 x 28 

x = images[0].view( 1, 784 )   # --> 784-> input

model.eval()

with torch.no_grad():
    reconstruction,mu,logvar = model(x)
    


"----------------------------------------------------"
"    Comparing input and reconstruction with graph   "
"----------------------------------------------------"

# میخوایم تصویر ورودی، و تصویری که مدل در بالا generate کرده رو رسم کنیم و در کنار هم مقایسه کنیم

plt.subplot(1,2,1)
plt.imshow( x.view(28,28), cmap="gray" )
plt.title("Original")
plt.subplot(1,2,2)
plt.imshow( reconstruction.view(28,28), cmap="gray" )
plt.title("VAE Output")
plt.show()



"------------------------------------"
"    generate compeltly new digits   "
"------------------------------------"

# الان یک z کاملا تصادفی درست میکنیم و فقط از قسمت Decoder مدل برای generate کردن استفاده میکنیم
# اینجا decoder که train شده هست میاد با استفاده ازین نقطه Z که بهش میدیم یه عکس کاملا جدید میسازه
# نکتش اینه که این عکس شاید خیلی زیاد شبیه دیتاهایی باشه که مدل باهاش آموزش دیده، شاید خیلی کم شبیه باشه

z = torch.randn( 1, latent_dim )

print(z)

# الان نقطه z رندومی که ساختیم یک وکتور 32 تایی هست
# tensor([[-2.4843, -1.1931,  0.8406,  0.6691,  0.8323, -1.4667, -0.0887,  0.0384,
#           0.9666,  0.7734, -0.4413, -0.0648,  1.2424,  1.4595, -0.3362,  0.1339,
#           1.4931,  0.3426, -0.6378, -1.5840, -1.1157, -0.7099, -0.0469, -1.3462,
#          -0.8102,  0.6867,  0.9458, -0.5482,  0.7311,  0.4828,  1.0286, -0.2729]])


with torch.no_grad():
    generated = model.decoder(z)    # فقط از دکودر استفاده میشه

# تصویری که Decoder برامون ساخته رو نمایش میدیم
plt.imshow( generated.view(28,28), cmap="gray" )
plt.show()




