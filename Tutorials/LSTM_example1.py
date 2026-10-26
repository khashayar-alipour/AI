# -*- coding: utf-8 -*-

'''
===============================================================================
===============================================================================
================       Created on Thu Oct 22 12:53:44 2026     ================
================                IDE: Spyder                    ================
================         Author: Khashayar Alipour             ================
================           LSTM ANN model Coding               ================
===============================================================================
===============================================================================
'''

# در این فایل کدزنی 0 تا 100 مدل LSTM با استفاده از دیتاست coingecko bitcoin انجام شده
# در این پروژه پیشبینی قیمت bitcoin انجام میشه
# دیتای قیمت بیتکوین در 365 وارد میشه و برای پیشبینی قیمت در روزهای آینده استفاده میشه




"--------------------------------"
"    🟠 Importing library 🟠    "
"--------------------------------"

import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error

import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader




"---------------------------------------------------"
"    🟠 Download Bitcoin data from CoinGecko 🟠    "
"---------------------------------------------------"

url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

params = {
    "vs_currency": "usd",
    "days": 365,
    "interval": "daily"
}

response = requests.get( url, params=params, timeout=30 )

print("Status code:", response.status_code)   # Status code: 200

response.raise_for_status()

data = response.json()

print(data.keys())
# dict_keys(['prices', 'market_caps', 'total_volumes'])

# دیتایی که دانلود کردیم یک دیکشنری هست که 3 کلید داره
# همچنین valueها یک آرایه از آرایه‌ها هستن که قیمت هارو نشون میدن
# data = { "prices": [ [1761177600000, 107591.4605093986], [1761264000000, 110109.30522515893], ..... ],
#          "market_caps": [ [1789776000000, 80873.58287659245], [1789862400000, 81236.41383660372], ..... ],   
#          "total_volumes": [ [1792540800000, 27926195682.985336], [1792627200000, 32168983739.061207], ..... ]   
#         }


 

"-----------------------------------------"
"    🟠 Convert prices to DataFrame 🟠   "
"-----------------------------------------"

df = pd.DataFrame( data["prices"], columns=["timestamp", "Close"] )
print(df)                        
# Date     
# 2025-10-23 00:00:00  107591.460509
# 2025-10-24 00:00:00  110109.305225
#   ...         ...         ...
# 2026-10-22 00:00:00   84082.266463
# 2026-10-22 11:11:00   81927.295125
# [366 rows x 1 columns]


df["Date"] = pd.to_datetime( df["timestamp"], unit="ms" )
df = df.set_index("Date")
df = df.drop( columns=["timestamp"] )


print(df.head())
# Date                     
# 2025-08-26  110100.281956
# 2025-08-27  111712.868681
# 2025-08-28  111241.292648
# 2025-08-29  112512.680983
# 2025-08-30  108335.633152


print(df.tail())
# Date                             
# 2026-10-19 00:00:00  82019.582913
# 2026-10-20 00:00:00  81875.263916
# 2026-10-21 00:00:00  82943.831500
# 2026-10-22 00:00:00  84082.266463
# 2026-10-22 11:11:00  81927.295125


print("Number of observations:", len(df))     # Number of observations: 366




"-------------------------------------------"
"    🟠 Plot historical Bitcoin price 🟠   "
"-------------------------------------------"

plt.figure(figsize=(14, 6))
plt.plot( df.index, df["Close"] )
plt.title( "Bitcoin Historical Closing Price" )
plt.xlabel("Date")
plt.ylabel("BTC Price (USD)")
plt.grid(alpha=0.3)
plt.show()




"-------------------------------------"
"   🟠 Extract the Close column 🟠   "
"-------------------------------------"

close = df["Close"].copy()
close = close.dropna()

print(close.head())
# Date
# 2025-10-23    107591.460509
# 2025-10-24    110109.305225
# 2025-10-25    111030.183379
# 2025-10-26    111631.637265
# 2025-10-27    114419.221697
# Name: Close, dtype: float64

print("Shape:", close.shape)    # Shape: (366,)





"-------------------------------"
"    🟠 Convert to NumPy 🟠    "
"-------------------------------"

data_values = close.values.reshape(-1, 1)
print(data_values)
#  [[107591.4605094 ]
#  [110109.30522516]
#    ...      ...
#  [112893.85203625]]

print("Original data shape:", data_values.shape)     #Original data shape: (366, 1)




"-----------------------"
"   🟠 Parameters 🟠   "
"-----------------------"

SEQUENCE_LENGTH = 60   # میخوایم 60 روز قبل رو ببینه

FORECAST_DAYS = 7   # دونه دونه 7 روزآینده رو پیشبینی کنه

BATCH_SIZE = 32

EPOCHS = 50




"-----------------------------"
"   🟠 Train/Test split 🟠   "
"-----------------------------"

# اینجا میگیم 80% رو به عنوان train dataset در نظر بگیر. نکته مهم اینه که اینجا دیگه Shuffle نمیکنیم
train_size = int( len(data_values) * 0.80 )

print("Total number of days:", len(data_values))    # Total number of days: 366

print("Training days:", train_size)    # Training days: 292

print("Testing days:", len(data_values) - train_size )   # Testing days: 74





"------------------------------------"
"   🟠 Normalize data (scaling) 🟠  "
"------------------------------------"
# دیتارو میاریم بین 0 و 1 تا نرمال بشه

scaler = MinMaxScaler( feature_range=(0, 1) )

# IMPORTANT:
# Fit scaler ONLY on training data

scaler.fit( data_values[:train_size] )

scaled_data = scaler.transform( data_values )

print("First scaled values:")
print( scaled_data[:5] )

# First scaled values:
# [[0.87775508]
#  [0.92283483]
#  [0.93932232]
#  [0.95009081]
#  [1.        ]]




"------------------------------"
"   🟠 Creating sequences 🟠  "
"------------------------------"

def create_sequences( data, sequence_length, forecast_days ):

    X = []
    y = []

    for i in range( len(data) - sequence_length - forecast_days + 1 ):

        # --------------------------------
        # Input:
        # Previous 60 days
        # --------------------------------

        input_sequence = data[ i : i + sequence_length ]

        # --------------------------------
        # Target:
        # Next 7 days
        # --------------------------------

        target_sequence = data[ i + sequence_length: i + sequence_length + forecast_days ]

        X.append( input_sequence )

        y.append( target_sequence.flatten() )

    return ( np.array(X), np.array(y) )


X, y = create_sequences(
    scaled_data,
    SEQUENCE_LENGTH,
    FORECAST_DAYS
)

print("X shape:", X.shape)    # X shape: (300, 60, 1)
print("y shape:", y.shape)    # y shape: (300, 7)




"-----------------------------------------------------"
"   🟠 Split sequences into training and testing 🟠  "
"-----------------------------------------------------"

train_samples = ( train_size - SEQUENCE_LENGTH - FORECAST_DAYS + 1 )

print( "Training sequence samples:", train_samples )

X_train = X[:train_samples]

y_train = y[:train_samples]

X_test = X[train_samples:]

y_test = y[train_samples:]


print("X_train:", X_train.shape)

print( "y_train:", y_train.shape)

print( "X_test:", X_test.shape)

print( "y_test:", y_test.shape)


# Training sequence samples: 226
# X_train: (226, 60, 1)
# y_train: (226, 7)

# Test sequence samples: 74
# X_test: (74, 60, 1)
# y_test: (74, 7)




"--------------------------------------"
"   🟠 Convert to PyTorch tensors 🟠  "
"--------------------------------------"

X_train = torch.tensor( X_train, dtype=torch.float32 )

y_train = torch.tensor( y_train, dtype=torch.float32 )

X_test = torch.tensor( X_test, dtype=torch.float32 )

y_test = torch.tensor( y_test, dtype=torch.float32 )


print("PyTorch X_train shape:", X_train.shape)
print("PyTorch y_train shape:", y_train.shape)

# PyTorch X_train shape: torch.Size([226, 60, 1])
# PyTorch y_train shape: torch.Size([226, 7])



"-----------------------------"
"   🟠 Create DataLoader 🟠  "
"-----------------------------"

train_dataset = TensorDataset(
    X_train,
    y_train
)

train_loader = DataLoader(
    train_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True
)




"---------------------------"
"    🟠 Select device 🟠   "
"---------------------------"

if torch.cuda.is_available():
    device = torch.device("cuda")

elif torch.backends.mps.is_available():
    device = torch.device("mps")

else:
    device = torch.device("cpu")


print("Using device:", device)
# Using device: cpu




"-----------------------------"
"   🟠 Define LSTM model 🟠  "
"-----------------------------"

class BitcoinLSTM(nn.Module):

    def __init__( self, input_size=1, hidden_size=32, num_layers=1, forecast_days=7 ):
        super().__init__()

        # ----------------------------------
        # LSTM
        # ----------------------------------
        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=0.2   # to avoid overfitting
        )

        # ----------------------------------
        # Fully connected output layer
        # ----------------------------------
        self.fc = nn.Linear( hidden_size, forecast_days )


    def forward(self, x):

        # x shape: (batch_size, sequence_length, features)
        # Example: (32, 60, 1)

        output, (hidden_state, cell_state) = self.lstm(x)

        # output shape: (batch_size, sequence_length, hidden_size)
        # Example: (32, 60, 64)

        # We only take the output of the LAST timestep
        last_output = output[:, -1, :]

        # last_output shape: (batch_size, hidden_size)
        # Example: (32, 64)

        prediction = self.fc(last_output)
        # prediction shape: (batch_size, 7)

        return prediction






"-------------------------------"
"    🟠 Create LSTM model 🟠   "
"-------------------------------"

model = BitcoinLSTM(
    input_size=1,
    hidden_size=128,
    num_layers=1,
    forecast_days=FORECAST_DAYS
)

model = model.to(device)
print(model)

# BitcoinLSTM(
#   (lstm): LSTM(1, 128, batch_first=True, dropout=0.2)
#   (fc): Linear(in_features=128, out_features=7, bias=True)
# )



#  60 previous Bitcoin prices
#             ↓
#           LSTM
#     hidden_size = 64
#             ↓
#           LSTM
#     hidden_size = 64
#             ↓
#     Last LSTM output
#             ↓
#          Linear
#          64 → 7
#             ↓
#          Day +1
#          Day +2
#          Day +3
#          Day +4
#          Day +5
#          Day +6
#          Day +7
 



"-----------------------------------------"
"    🟠 Loss function and optimizer 🟠   "
"-----------------------------------------"

criterion = nn.MSELoss()

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)



"-------------------------"
"   🟠 Training loop 🟠  "
"-------------------------"

loss_history = []

for epoch in range(EPOCHS):

    model.train()

    total_loss = 0

    for (X_batch, y_batch) in train_loader:

        # Move batch to device
        X_batch = X_batch.to(device)
        y_batch = y_batch.to(device)

        # ----------------------------------
        # Forward propagation
        # ----------------------------------
        predictions = model(X_batch)

        # ----------------------------------
        # Calculate loss
        # ----------------------------------
        loss = criterion( predictions, y_batch )

        # ----------------------------------
        # Clear old gradients
        # ----------------------------------
        optimizer.zero_grad()

        # ----------------------------------
        # Backpropagation
        # ----------------------------------
        loss.backward()

        # ----------------------------------
        # Gradient clipping
        #
        # Useful for recurrent networks
        # ----------------------------------

        torch.nn.utils.clip_grad_norm_(
            model.parameters(),
            max_norm=1.0  )

        # ----------------------------------
        # Update weights
        # ----------------------------------
        optimizer.step()


        total_loss += ( loss.item() )


    average_loss = ( total_loss / len(train_loader) )

    loss_history.append( average_loss )


    if (epoch + 1) % 5 == 0:

        print(
            f"Epoch "
            f"{epoch + 1}/{EPOCHS} "
            f"| Loss: "
            f"{average_loss:.6f}"   )


# hiden state 128 
# Epoch 5/50  | Loss: 0.003755
# Epoch 10/50 | Loss: 0.003006
# Epoch 15/50 | Loss: 0.003294
# Epoch 20/50 | Loss: 0.003099
# Epoch 25/50 | Loss: 0.003012
# Epoch 30/50 | Loss: 0.003944
# Epoch 35/50 | Loss: 0.004390
# Epoch 40/50 | Loss: 0.004523
# Epoch 45/50 | Loss: 0.003465
# Epoch 50/50 | Loss: 0.003002




"--------------------------------"
"   🟠 Plot training loss 🟠    "
"--------------------------------"

plt.figure( figsize=(10, 5) )
plt.plot( loss_history )
plt.title( "LSTM Training Loss" )
plt.xlabel( "Epoch" )
plt.ylabel( "MSE Loss" )
plt.grid( alpha=0.3 )
plt.show()




"---------------------------------"
"   🟠 Evaluate on test data 🟠  "
"---------------------------------"

model.eval()

with torch.no_grad():
    test_predictions = model( X_test.to(device) )


# Move back to CPU
test_predictions = ( test_predictions.cpu().numpy() )
actual_test = ( y_test.cpu().numpy())


print("Predictions shape:", test_predictions.shape )    # Predictions shape: (74, 7)
print( "Actual shape:", actual_test.shape )   # Actual shape: (74, 7)




"---------------------------------------------"
"    🟠 Convert predictions back to USD 🟠   "
"---------------------------------------------"

predicted_prices = (
    scaler.inverse_transform(
        test_predictions.reshape(-1, 1)
    )
    .reshape( test_predictions.shape )
 )


actual_prices = (
    scaler.inverse_transform(
        actual_test.reshape(-1, 1)
    )
    .reshape( actual_test.shape )
 )


print("First predicted 7 days:")
print(predicted_prices[0])
print("\nActual 7 days:")
print(actual_prices[0])


# First predicted 7 days:
# [63577.5   63539.438 63581.438 63457.434 63634.26  63800.473 63760.188]

# Actual 7 days:
# [64062.17  64608.703 64262.75  64879.754 64917.24  64856.098 63915.71 ]




"---------------------"
"    🟠 Metrics 🟠   "
"---------------------"

mae = mean_absolute_error(
    actual_prices.flatten(),
    predicted_prices.flatten()
)

rmse = np.sqrt(
    mean_squared_error(
        actual_prices.flatten(),
        predicted_prices.flatten()
    )
)

print(f"MAE: "f"${mae:,.2f}")      # MAE: $3,527.39
print(f"RMSE: "f"${rmse:,.2f}")    # RMSE: $5,205.39

# وقتی میگه MAE مقدارش برابر 3,527.39$ هست یعنی پیشبینی ما همینقدر با واقعیت فاصله داره




"---------------------------------"
"    🟠 Actual vs predicted 🟠   "
"---------------------------------"

actual_day1 = ( actual_prices[:, 0] )

predicted_day1 = ( predicted_prices[:, 0] )

plt.figure( figsize=(14, 6) )
plt.plot( actual_day1, label="Actual BTC Price" )
plt.plot( predicted_day1, label="Predicted BTC Price" )
plt.title( "Bitcoin LSTM Prediction on Test Data")
plt.xlabel( "Test Sequence" )
plt.ylabel( "BTC Price (USD)" )
plt.legend()
plt.grid( alpha=0.3 )
plt.show()




"-----------------------------------"
"   🟠 Show one 7-day example 🟠   "
"-----------------------------------"

example = 10

print("Actual:")

for day, price in enumerate( actual_prices[example], start=1 ):

    print( f"Day +{day}: "
           f"${price:,.2f}"  )

# Actual:
# Day +1: $62,984.29
# Day +2: $63,031.05
# Day +3: $62,843.71
# Day +4: $64,491.35
# Day +5: $64,686.26
# Day +6: $69,291.02
# Day +7: $73,020.95


print("\nPredicted:")

for day, price in enumerate( predicted_prices[example], start=1 ):

    print( f"Day +{day}: "
           f"${price:,.2f}"   )

# Predicted:
# Day +1: $64,070.50
# Day +2: $64,053.78
# Day +3: $64,082.86
# Day +4: $63,995.46
# Day +5: $64,192.39
# Day +6: $64,348.89
# Day +7: $64,334.13




"-------------------------------------"
"    🟠 Plot one 7-day forecast 🟠   "
"-------------------------------------"

days = np.arange( 1, FORECAST_DAYS + 1 )

plt.figure( figsize=(10, 5) )
plt.plot( days, actual_prices[example], marker="o", label="Actual" )
plt.plot( days, predicted_prices[example], marker="o", label="Predicted" )
plt.xticks( days )
plt.xlabel( "Days into Future" )
plt.ylabel( "BTC Price (USD)" )
plt.title( "LSTM 7-Day Bitcoin Prediction" )
plt.legend()
plt.grid( alpha=0.3 )
plt.show()









