flag_register = 0x1234
mask = 8

flag_register = flag_register ^ mask
print(format(flag_register, '016b'))