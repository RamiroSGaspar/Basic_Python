var = 17
var_right = var >> 1
var_left = var << 2

print(var, var_left, var_right)
print(format(var & 0xFFFF, '016b'), format(var_left & 0xFFFF, '016b'), format(var_right & 0xFFFF, '016b'))