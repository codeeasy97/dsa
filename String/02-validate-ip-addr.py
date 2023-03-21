# Program to validate an IP address
"""
Everything must be an int
Empty not acceptable
Block of digit should not be greater than 4
There must be no leading 0 like 00.01.02.03 (wrong leading 0)
There must be only 4 block : 192.168.8.9.67 (wrong 5 block)
The range must be from 0-255 : 192.168.390.55 (wrong 390 out of range)
1. a.b.c.d - everything should be digit
2. 1...1 - blank is not allowed
3. 0000.0000.0000.0000 - only 3 digit in each block allowed
4. 01.00.00.00 - leading 0 not allowed
5. 256.256.256.256 - only 0-255 is allowed
6. 2.2.2.2.2 - only 4 block is allowed
"""
def isValidIp(str):
    str = str.split('.')
    n = len(str)
    if n != 4:
        return False
    
    for i in range(n):
        try:
            a = int(str[i])
        except:
            return False
        
        if not str[i]:
            return False
        
        if len(str[i]) > 3:
            return False
        
        if  int(str[i][0]) == 0 and len(str[i]) > 1:
            return False
        
        if int(str[i]) < 0 or int(str[i]) > 255:
            return False
        
    return True

str = "222.111.111.111"
# str = "222.111.0.111"
# str = "0000.0000.0000.0000"
# str = "00.00.00.00"
# str="1...1"
# str="2.2.2.2.2"
# str="256.256.256.256"
# str = "a.b.c.e"
n = len(str)
res = isValidIp(str)
print(res)