import pyupbit

access = "Your access code"
secret = "Your secret code"
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))
print(upbit.get_balance("KRW"))
print(upbit.get_balances())