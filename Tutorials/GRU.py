
'''
===============================================================================
===============================================================================
================       Created on Tue Oct 13 12:49:56 2026     ================
================                IDE: Spyder                    ================
================         Author: Khashayar Alipour             ================
================           GRU (Gated Recurrent Unit)          ================
===============================================================================
===============================================================================
'''

# شبکه عصبی مصنوعی (Artificial Neural Network) اسم کلی یک خانواده از مدل‌هاست
# که از لایه‌هایی از نورون‌ها تشکیل شده‌اند و از داده یاد می‌گیرند 
# این شبکه از معماری های مختلفی تشکیل شده که هرکدوم ویژگی‌ها، کاربردها و ساختارهای مخصوص خودشون دارن
# مثلا MLP/ANN که تا الان درموردش یاد گرفتیم شبکه عصبی معمولی هست که کاربرد اصلی آن داده‌های جدولی، classification/regression هست

#                ANN
#         ┌───────┼──────┐
#         ↓       ↓      ↓
#       MLP     CNN     RNN
#                    ┌───┴──┐
#                    ↓      ↓
#                  LSTM   ⭐GRU



#✅ Why GRU?
#✅ GRU Structure (Update gate / Reset gate)
#✅ Comparison of RNN, GRU, LSTM
#✅ GRU codes with Numpy
#✅ GRU codes with Pytorch









'''
===================================
=======  ⭐  Why GRU?  ⭐  =======
===================================
'''
# برای پردازش داده های Sequential میتونیم از شبکه‌ی بازگشتی ساده یا RNN (Recurrent Neural Network) استفاده کنیم
# ایده اصلیش اینه که برای پیشبینی مثلا یک کلمه، باید اطلاعات مربوط به همون کلمه رو از اول جلمه داشته باشه

# درواقع (Recurrent Neural Network) اطلاعات قبلی را در متغیری به نام Hidden State نگه می‌دارد:
    # hₜ​=tanh(Wx​*Xₜ ​+ Wh*​Hₜ₋₁​ + b)
    # tanh: تابع فعال سازی
    # Wx/Wh: ماتریس های وزن قابل یادگیری
    # Xₜ: ورودی در زمان فعلی
    # ​Hₜ₋₁: اطلاعاتی که از مرحله قبل آمده
    # b: بایاس

# مشکل این است که RNN ساده ممکن است هنگام آموزش روی توالی‌های بلند، اطلاعات مهم گذشته ...
#... را به‌خوبی حفظ نکند. این مسئله به‌ویژه با مشکل Vanishing Gradient ارتباط دارد


# حالا GRU برای حل چه مشکلی طراحی شد؟
# معماری GRU نوعی شبکه بازگشتی است که با استفاده از دو دروازه (Gate)، کنترل می‌کند:
# چه مقدار از اطلاعات قبلی حفظ شود؟    
# چه مقدار از اطلاعات جدید وارد وضعیت شبکه شود؟    
# در نتیجه، GRU می‌تواند وابستگی‌های طولانی‌تری را نسبت به RNN ساده یاد بگیرد و معمولاً معماری ساده‌تری از LSTM دارد


"✅ RNN ✅"
# یک Hidden state دارد و کنترل مستقلی برای حفظ یا جایگزینی اطلاعات ندارد
'''                  Output         Output         Output
                        ^              ^              ^
                        |              |              |
Input sequence --> |RNN Cell| --> |RNN Cell| --> |RNN Cell|
                       ^              ^              ^   
              _________|______________|______________|
                       |      Hidden State           |
                     Step1         Step2          Step3  
'''


"✅ GRU ✅"
# با دو Gate اطلاعات قدیمی و جدید را مدیریت می‌کند


"✅ LSTM ✅"
# علاوه بر Hidden State، یک Cell State مستقل و سه Gate دارد



"✅ When can we use GRU? ✅"
    # Time Series Forecasting: پیش‌بینی دما، مصرف انرژی یا داده‌های سنسورها
    # NLP: تحلیل احساسات، طبقه‌بندی متن و مدل‌سازی توالی کلمات
    # Speech Processing: پردازش توالی‌های صوتی
    # Anomaly Detection: شناسایی الگوهای غیرعادی در داده‌های متوالی










'''
========================================
=======  ⭐  GRU Structure  ⭐  =======
========================================
'''
# در GRU استاندارد، برخلاف LSTM هیچ Cell State مستقلی نداریم
# اطلاعات حافظه در همان Hidden State نگهداری می‌شود.

# در حالت استاندار GRU دو عدد Gate داره:
    # Update Gate --> تعیین می‌کند چه مقدار از وضعیت قبلی حفظ شود و چه مقدار از وضعیت جدید جایگزین آن شود
    # Reset Gate --> کنترل می‌کند اطلاعات قبلی هنگام محاسبه محتوای جدید چقدر اثر داشته باشد



"✅ Update Gate ✅"
# اگر مقدار Gate به صفر نزدیک باشد، وضعیت قبلی بیشتر حفظ می‌شود
# اگر مقدار Gate به یک نزدیک باشد، وضعیت جدید سهم بیشتری در Hidden State خواهد داشت

# فرمولش:
    # zₜ​=σ(Wz​*Xₜ ​+ Uz*​Hₜ₋₁​ + Bz​)
    # σ: sigmoid activation function     0<sigmoid<1
    # Wz/Uz: ماتریس های وزن قابل یادگیری
    # Xₜ: Update gate value
    # ​Hₜ₋₁: previous hidden state
    # b: bias



"✅ Reset Gate ✅"
# این Gate مشخص می‌کند که اطلاعات قبلی هنگام محاسبه محتوای جدید چه میزان تأثیر داشته باشد
# این Gate به مدل کمک می‌کند در صورت نیاز، وابستگی به بخشی از اطلاعات قبلی را کاهش دهد

# اگر مقدار آن برای یک مؤلفه به صفر نزدیک شود، اثر آن مؤلفه از Hidden State قبلی در محاسبه محتوای جدید کاهش می‌یابد
# اگر به یک نزدیک باشد، اطلاعات قبلی در این محاسبه بیشتر استفاده می‌شود

# فرمولش:
    # rₜ​=σ(Wr​*Xₜ ​+ Ur*​Hₜ₋₁​ + Br​)



"✅ Calculating recommended Hidden state ✅"
# ابتدا یک وضعیت جدید پیشنهادی محاسبه می‌شود:
    # h~ₜ=tanh(Wh*​Xₜ ​+ Uh​(rₜ​⊙hₜ₋₁​) + Bh​)

# علامت ⊙ به معنی ضرب عنصر به عنصر (Element-wise Multiplication) است:
    # rₜ​=[0.1      hₜ₋₁​=[0.8
    #    0.9​]           0.5​]
    # rₜ​⊙hₜ₋₁​=[0.08
    #         0.45​]

# در این مثال، مؤلفه اول اطلاعات قبلی با ضریب ۰٫۱ و مؤلفه دوم با ضریب ۰٫۹ وارد محاسبه محتوای جدید می‌شود
# این Hidden State پیشنهادی هنوز وضعیت نهایی شبکه نیست؛ در مرحله بعد با وضعیت قبلی ترکیب می‌شود



"✅ Calculating final Hidden state ✅"
# در قرارداد رایج فرمول‌بندی GRU، وضعیت جدید به شکل زیر محاسبه می‌شود:
    # hₜ​=(1−zₜ)⊙h~ₜ + zₜ⊙hₜ₋₁
    # h~ₜ:  اطلاعات جدید پیشنهادی
    # hₜ₋₁:  اطلاعات قبلی
    # zₜ:   میزان حفظ وضعیت قبلی در این قرارداد فرمول‌بندی
    # 1−zₜ:  میزان سهم وضعیت پیشنهادی

# برای مثال، اگر برای یک مؤلفه داشته باشیم:
    # zₜ​=0.8   hₜ₋₁​=0.5   h~ₜ​=0.9

# آنگاه:
    # hₜ​=(1−0.8)(0.9)+0.8(0.5)
    # hₜ​=0.18+0.40=0.58     یعنی وضعیت نهایی 0.58 می‌شود؛ اطلاعات قبلی سهم بیشتری در آن داشته است












'''
=======================================================
=======  ⭐  Comparison of GRU, RNN, LSTM  ⭐  =======
=======================================================
'''

# +------------------------------+---------+-----------------+-----------------+
# | Feature                      |   RNN   |      LSTM       |       GRU       |
# +------------------------------+---------+-----------------+-----------------+
# | Hidden State                 |   Yes   |       Yes       |       Yes       |
# | Separate Cell State          |    No   |       Yes       |        No       |
# | Gates                        |   None  |  3 main gates   |  2 main gates   |
# | Long-term Dependency Handling|  Weaker |      Good       |      Good       |
# | Number of Parameters         |   Few   |      More       | Usually fewer   |
# | Complexity                   |   Low   |     Higher      |     Medium      |
# | Speed                        | Usually |    Usually      | Usually faster  |
# |                              | faster  |    slower       |   than LSTM     |
# | Vanishing Gradient Resistance|  Weaker |      Better     |     Better      |
# | Keras Implementation         |   Easy  |      Easy       |      Easy       |
# +------------------------------+---------+-----------------+-----------------+












'''
=================================================
=======  ⭐  GRU codes with Pytorch  ⭐  =======
=================================================
'''

# کتابخوانه PyTorch برای GRU سه مجموعه پارامتر دارد: Reset Gate، Update Gate و New Gate
# با اینحال، تعداد Gateهای کنترلی اصلی همچنان دو عدد است؛ New Gate برای ساخت محتوای پیشنهادی به کار می‌رود


"Tensor shape in GRU"
# در PyTorch، اگر batch_first=True باشد، ورودی به این شکل است:
    # X ∈ ℝᴮˣᵀˣᶠ
    # B: number of samples in every batch
    # T: lenght of sequence (طول توالی)
    # F: number of features of every time step

# مثلا این یعنی:
X.shape = (32, 20, 1)
# 32 نمونه در Batch    
# 20 تا time step در هر نمونه    
# 1 ویژگی در هر time step    

# برای این model:
nn.GRU(
    input_size=1,
    hidden_size=32,
    num_layers=1,
    batch_first=True   )


"Outputs of GRU in Pytorch"
# در GRU کتابخوانه Pytorch این خروجی‌ها را برمی‌گرداند:
output, h_n = gru(X)
# برخلاف LSTM در GRU خروجی c_n نداریم؛ چون Cell State مستقلی ندارد



"⭐ Pytorch full GRU project⭐ "
# مدل باید با مشاهده ۲۰ مقدار قبلی یک سری زمانی، مقدار بعدی را پیش‌بینی کند
# مثلاً ورودی مدل چنین است:   [x1,x2,…,x20]
# خروجی مطلوب:  y=x21

# در این مثال یک سری زمانی مصنوعی می‌سازیم که از ترکیب دو موج سینوسی تشکیل شده است
# در پروژه واقعی میشه از دیتاهای واقعی استفاده کرد

# این کد شامل موارد زیر است:
# تولید سری زمانی    
# تقسیم زمانی Train و Test    
# نرمال‌سازی داده‌ها بدون استفاده از آمار بخش Test    
# ساخت پنجره‌های ورودی    
# تعریف Dataset و DataLoader    
# ساخت مدل GRU    
# آموزش با Adam و MSE Loss    
    # Gradient Clipping
# ارزیابی مدل    
# رسم نمودار Loss و پیش‌بینی    
# پیش‌بینی مقدار بعدی    


# ============================================================
# GRU TIME SERIES FORECASTING WITH PYTORCH
# Complete beginner-friendly project
# ============================================================

# ------------------------------------------------------------
# 1. IMPORT LIBRARIES
# ------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn

from torch.utils.data import TensorDataset, DataLoader


# ------------------------------------------------------------
# 2. REPRODUCIBILITY AND DEVICE
# ------------------------------------------------------------

np.random.seed(42)
torch.manual_seed(42)

device = torch.device("cpu")

print("PyTorch version:", torch.__version__)
print("Device:", device)


# ------------------------------------------------------------
# 3. CREATE A SYNTHETIC TIME SERIES
# ------------------------------------------------------------

t = np.arange(0, 600, dtype=np.float32)

series = (
    np.sin(0.05 * t)
    + 0.3 * np.sin(0.15 * t)
    + 0.05 * np.sin(0.50 * t)
)

plt.figure(figsize=(12, 4))
plt.plot(t, series)
plt.title("Original Time Series")
plt.xlabel("Time")
plt.ylabel("Value")
plt.grid(True)
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 4. CHRONOLOGICAL TRAIN / TEST SPLIT
# ------------------------------------------------------------

sequence_length = 20

# Split the raw time series chronologically.
train_end = int(0.8 * len(series))

train_raw = series[:train_end]

# Fit normalization statistics on TRAIN data only.
train_mean = train_raw.mean()
train_std = train_raw.std()

series_normalized = (
    series - train_mean
) / (train_std + 1e-8)

print("Training samples in raw series:", len(train_raw))
print("Training mean:", train_mean)
print("Training standard deviation:", train_std)


# ------------------------------------------------------------
# 5. CREATE SEQUENCES
# ------------------------------------------------------------

X_list = []
y_list = []
target_indices = []

for i in range(len(series_normalized) - sequence_length):

    # 20 previous values
    X_list.append(
        series_normalized[i:i + sequence_length]
    )

    # The next value
    y_list.append(
        series_normalized[i + sequence_length]
    )

    # Index of the target in the original time series
    target_indices.append(i + sequence_length)


X = np.array(X_list, dtype=np.float32)
y = np.array(y_list, dtype=np.float32)
target_indices = np.array(target_indices)

# Add the feature dimension:
# (samples, sequence_length, input_size)
X = X[..., np.newaxis]

# Regression target:
# (samples, 1)
y = y.reshape(-1, 1)

print("\nFull X shape:", X.shape)
print("Full y shape:", y.shape)


# ------------------------------------------------------------
# 6. SPLIT WINDOWS BY TARGET TIME
# ------------------------------------------------------------

train_mask = target_indices < train_end
test_mask = target_indices >= train_end

X_train = torch.tensor(X[train_mask], dtype=torch.float32)
y_train = torch.tensor(y[train_mask], dtype=torch.float32)

X_test = torch.tensor(X[test_mask], dtype=torch.float32)
y_test = torch.tensor(y[test_mask], dtype=torch.float32)

print("\nX_train:", X_train.shape)
print("y_train:", y_train.shape)

print("X_test:", X_test.shape)
print("y_test:", y_test.shape)


# ------------------------------------------------------------
# 7. DATASET AND DATALOADER
# ------------------------------------------------------------

train_dataset = TensorDataset(X_train, y_train)

train_loader = DataLoader(
    train_dataset,
    batch_size=32,
    shuffle=True
)


# ------------------------------------------------------------
# 8. DEFINE THE GRU MODEL
# ------------------------------------------------------------

class GRURegressor(nn.Module):

    def __init__(
        self,
        input_size=1,
        hidden_size=32,
        num_layers=1,
        dropout=0.0
    ):
        super().__init__()

        self.gru = nn.GRU(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout if num_layers > 1 else 0.0
        )

        self.fc = nn.Linear(
            hidden_size,
            1
        )

    def forward(self, x):

        # output shape:
        # (batch_size, sequence_length, hidden_size)

        # h_n shape:
        # (num_layers, batch_size, hidden_size)

        output, h_n = self.gru(x)

        # Last layer's final hidden state
        last_hidden = h_n[-1]

        # Map hidden features to one numerical prediction
        prediction = self.fc(last_hidden)

        return prediction


model = GRURegressor(
    input_size=1,
    hidden_size=32,
    num_layers=1
).to(device)

print("\nModel architecture:")
print(model)

total_parameters = sum(
    parameter.numel()
    for parameter in model.parameters()
    if parameter.requires_grad
)

print("Trainable parameters:", total_parameters)


# ------------------------------------------------------------
# 9. LOSS FUNCTION AND OPTIMIZER
# ------------------------------------------------------------

criterion = nn.MSELoss()

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)


# ------------------------------------------------------------
# 10. TRAINING LOOP
# ------------------------------------------------------------

epochs = 50

train_losses = []

for epoch in range(epochs):

    model.train()

    total_loss = 0.0

    for X_batch, y_batch in train_loader:

        X_batch = X_batch.to(device)
        y_batch = y_batch.to(device)

        # Clear gradients from the previous step
        optimizer.zero_grad()

        # Forward pass
        predictions = model(X_batch)

        # Calculate prediction error
        loss = criterion(predictions, y_batch)

        # Backpropagation through time
        loss.backward()

        # Prevent excessively large gradients
        nn.utils.clip_grad_norm_(
            model.parameters(),
            max_norm=1.0
        )

        # Update model parameters
        optimizer.step()

        total_loss += loss.item() * len(X_batch)

    epoch_loss = total_loss / len(train_dataset)

    train_losses.append(epoch_loss)

    if (epoch + 1) % 5 == 0:
        print(
            f"Epoch [{epoch + 1:02d}/{epochs}] "
            f"Train MSE: {epoch_loss:.6f}"
        )


# ------------------------------------------------------------
# 11. PLOT TRAINING LOSS
# ------------------------------------------------------------

plt.figure(figsize=(10, 4))

plt.plot(
    range(1, epochs + 1),
    train_losses,
    label="Training MSE"
)

plt.title("GRU Training Loss")
plt.xlabel("Epoch")
plt.ylabel("MSE Loss")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 12. EVALUATE ON THE TEST SET
# ------------------------------------------------------------

model.eval()

with torch.no_grad():

    X_test_device = X_test.to(device)

    predictions_test = model(
        X_test_device
    ).cpu().numpy()

    actual_test = y_test.numpy()

test_mse = np.mean(
    (predictions_test - actual_test) ** 2
)

test_mae = np.mean(
    np.abs(predictions_test - actual_test)
)

print("\nTest MSE:", round(float(test_mse), 6))
print("Test MAE:", round(float(test_mae), 6))


# ------------------------------------------------------------
# 13. PLOT ACTUAL VS PREDICTED VALUES
# ------------------------------------------------------------

test_target_times = target_indices[test_mask]

actual_original_scale = (
    actual_test.squeeze() * train_std + train_mean
)

predicted_original_scale = (
    predictions_test.squeeze() * train_std + train_mean
)

plt.figure(figsize=(12, 5))

plt.plot(
    test_target_times,
    actual_original_scale,
    label="Actual"
)

plt.plot(
    test_target_times,
    predicted_original_scale,
    label="GRU Prediction"
)

plt.title("GRU: Actual vs Predicted Time Series")
plt.xlabel("Time")
plt.ylabel("Original Value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 14. PREDICT THE NEXT VALUE
# ------------------------------------------------------------

# Use the latest 20 available observations.
last_sequence = series_normalized[-sequence_length:]

# Shape: (1, sequence_length, 1)
last_sequence_tensor = torch.tensor(
    last_sequence,
    dtype=torch.float32
).reshape(1, sequence_length, 1)

model.eval()

with torch.no_grad():

    next_prediction_normalized = model(
        last_sequence_tensor.to(device)
    ).item()

# Convert back to the original scale
next_prediction = (
    next_prediction_normalized * train_std + train_mean
)

print("\nLast observed value:", float(series[-1]))
print("Predicted next value:", float(next_prediction))


# ------------------------------------------------------------
# 15. SHOW THE LATEST WINDOW AND PREDICTION
# ------------------------------------------------------------

plt.figure(figsize=(10, 4))

recent_times = np.arange(
    len(series) - sequence_length,
    len(series)
)

plt.plot(
    recent_times,
    series[-sequence_length:],
    marker="o",
    label="Last 20 observed values"
)

plt.scatter(
    [len(series)],
    [next_prediction],
    marker="x",
    s=100,
    label="Next predicted value"
)

plt.title("Next-Step Forecast")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print("\nGRU project completed successfully.")






"✅ Code Explanation ✅"

# آموزش GRU دقیقاً چگونه انجام می‌شود؟

#---------------
#  Forward pass
#---------------
predictions = model(X_batch)
# داده‌ها وارد مدل می‌شوند و از لایه GRU عبور می‌کنند
#سپس  GRU اطلاعات 20 گام زمانی را به‌صورت متوالی پردازش می‌کند و Hidden State نهایی را به لایه Linear می‌دهد
# لایه Linear آن را به یک عدد تبدیل می‌کند؛ یعنی پیش‌بینی مقدار بعدی

#-----------------------
#  Calculation of Loss
#-----------------------
loss = criterion(predictions, y_batch)
# ما از nn.MSELoss() استفاده کرده‌ایم
# فرمول MSE میشه     2**MSE=(1/N)*∑(Y-Y^)
    # N: تعداد پیشبینی ها 
    # Y: مقدار واقعی
    # Y^: مقدار پیشبینی
# هرچه مقدار MSE کمتر باشد، پیش‌بینی‌های مدل روی همان داده‌ها به‌طور متوسط به مقادیر واقعی نزدیک‌ترند
# البته پایین بودن Training Loss به‌تنهایی به معنای عملکرد خوب روی داده‌های جدید نیست

#---------------------------------------
#  Backpropagation Through Time یا BPTT
#---------------------------------------
loss.backward()
# در شبکه بازگشتی، یک ورودی از چند time step عبور می‌کند. هنگام محاسبه گرادیان، PyTorch اثر خطای نهایی ...
#... را از مسیر محاسباتی به عقب انتشار می‌دهد؛ این روش را Backpropagation Through Time (BPTT) می‌نامیم
# به کمک گرادیان‌ها، مدل متوجه می‌شود که وزن‌ها برای کاهش خطا چگونه باید تغییر کنند

#--------------------
#  Gradient Clipping
#--------------------
nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
# در آموزش شبکه‌های بازگشتی، ممکن است گرادیان‌ها بیش‌ازحد بزرگ شوند
# متود Gradient Clipping اندازه کلی گرادیان‌ها را محدود می‌کند تا به‌روزرسانی وزن‌ها بیش‌ازحد شدید نشود
# این کار لزوماً مشکل Vanishing Gradient را برطرف نمی‌کند؛ هدف اصلی آن کنترل گرادیان‌های بزرگ است

#-------------------
#  Updating weights
#-------------------
optimizer.step()
# به کمک الگوریتم Adam، وزن‌ها و بایاس‌ها بر اساس گرادیان‌های محاسبه‌شده به‌روزرسانی می‌شوند
# این چرخه برای Batchهای مختلف و سپس برای Epochهای متعدد تکرار می‌شود












'''
===============================================
=======  ⭐  GRU codes with Numpy  ⭐  =======
===============================================
'''
# پیاده‌سازی دستی GRU با NumPy
# هدف این بخش، درک ریاضی GRU است
# این کد فقط یک time step از Forward Pass را اجرا می‌کند و هنوز شبکه را آموزش نمی‌دهد

# این پیاده‌سازی برای آموزش مفهومی است. محل اعمال Reset Gate با پیاده‌سازی داخلی PyTorch دقیقاً یکسان نیست
# هدف این است که سازوکار Gateها را ببینی، نه اینکه وزن‌های این دو پیاده‌سازی مستقیماً قابل‌جایگزینی باشند


import numpy as np

# -----------------------------
# 1. Activation functions
# -----------------------------
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

# -----------------------------
# 2. Dimensions
# -----------------------------
input_size = 2
hidden_size = 3

rng = np.random.default_rng(42)

# Current input
x_t = rng.normal(size=(input_size, 1))

# Previous hidden state
h_prev = rng.normal(size=(hidden_size, 1))

# -----------------------------
# 3. Initialize parameters
# -----------------------------
def init_weights():
    W = rng.normal(
        scale=0.3,
        size=(hidden_size, input_size)    )

    U = rng.normal(
        scale=0.3,
        size=(hidden_size, hidden_size)   )

    b = np.zeros((hidden_size, 1))

    return W, U, b


W_r, U_r, b_r = init_weights()
W_z, U_z, b_z = init_weights()
W_n, U_n, b_n = init_weights()


# -----------------------------
# 4. Reset gate
# -----------------------------
r_t = sigmoid(
    W_r @ x_t +
    U_r @ h_prev +
    b_r   )


# -----------------------------
# 5. Update gate
# -----------------------------
z_t = sigmoid(
    W_z @ x_t +
    U_z @ h_prev +
    b_z   )


# -----------------------------
# 6. Candidate hidden state
# -----------------------------
n_t = np.tanh(
    W_n @ x_t +
    U_n @ (r_t * h_prev) +
    b_n   )


# -----------------------------
# 7. New hidden state
# -----------------------------
h_t = (
    (1 - z_t) * n_t +
    z_t * h_prev  )


# -----------------------------
# 8. Print results
# -----------------------------
print("Input shape:", x_t.shape)
print("Previous hidden state:\n", h_prev)

print("\nReset gate:\n", r_t)
print("\nUpdate gate:\n", z_t)
print("\nCandidate state:\n", n_t)
print("\nNew hidden state:\n", h_t)
print("\nNew hidden shape:", h_t.shape)





































































































































































































































