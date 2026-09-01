import decimal

x = decimal.Decimal("1.234")          # 精确值 1.234
y = x.quantize(decimal.Decimal("0.01"))  # 修约到 0.01

print(y)
# 1.234 -> 1.23，数值变了，精度丢失了，触发了 Inexact 异常
# 但因为没写 try，程序会直接报错终止。