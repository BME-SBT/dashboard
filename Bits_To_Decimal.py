import math

def CAN_To_Decimal(data, length, sign, res):
    value = 0
    if (sign == 0 | ((sign == 1) & (int(data[0]) == 0))):
        for i in range(length):
            value = value + int(data[length-1-i])*(2**i)
    else:
        carry = 1
        for i in range(length):
            if (int(not(int(data[length-1-i])))==1):
                if (carry == 0):
                    value = value + (2**i)
            else:
                if (carry == 1):
                    value = value + (2**i)
                    carry = 0
        value = value * (-1)
    
    return math.floor(value*res*10)/10

    
    
    
#asdasd  
print(CAN_To_Decimal("1000000000000000",16,1,0.1))