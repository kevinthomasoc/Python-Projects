def add_binary(a,b):
    num = a + b
    binary = "000000000"
    if num >= 256:
        num -= 256
        binary = binary[:0] + "1" + binary[0+1:]
    if num >= 128:
        num -= 128
        binary += '1'
    if num >= 64:
        num -= 64
        binary += '1'
    if num >= 32:
        num -= 32
        binary += '1'
    if num >= 16:
        num -= 16
        binary += '1'
    if num >= 8:
        num -= 8
        binary += '1'
    if num >= 4:
        num -= 4
        binary += '1'
    if num >= 2:
        num -= 2
        binary += '1'
    if num >= 1:
        num -= 1
        binary += '1'
    else:
        binary = binary 

    return binary



print(add_binary(256,1))
