import math

def CAN_To_Decimal(data, signed, res):
    value = 0
    length = 0
    for i in range(4):
        length = length + int(data[19-i])*(2**i)
    length = length * 8
    
    if (signed == 0 | ((signed == 1) & (int(data[20]) == 0))):
        for i in range(length):
            value = value + int(data[19+length-i])*(2**i)
    else:
        carry = 1
        for i in range(length):
            if (int(not(int(data[19+length-i])))==1):
                if (carry == 0):
                    value = value + (2**i)
            else:
                if (carry == 1):
                    value = value + (2**i)
                    carry = 0
        value = value * (-1)
    
    if (res == 1):
        return value
    else:
        return math.floor(value*res*10)/10
    
    
    
#                                      |  |
#             Data length code (2byte) v  v
#                                          |              ||               |
#                                          v  Data(16bit) vv    maradék    v
print( CAN_To_Decimal("00000000000000000010100000000000000022222222222222222",1,1))