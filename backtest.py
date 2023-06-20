import pyupbit
import numpy as np


df = pyupbit.get_ohlcv("KRW-BTC", count=7)

k = 0.4
df['range'] = (df['high'] - df['low']) * k
df['target'] = df['open'] + df['range'].shift(1)

fee = 0.00
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] - fee,
                     1)

df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
df.to_excel("dd.xlsx")