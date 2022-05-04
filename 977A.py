#
# Wrong!  
# Code go to 977Aa.py => it is the corect answer
#

import math
a,b = input().split()
b = int(b)

for i in range(0,len(a)+1):
    
    if math.trunc(int(a[-1])) == 0:
        a,_ = str(int(a)/10).split(".")
    else:
        x = math.trunc(int(a[-1]) -1) # 324 => 3
       
        x = str(x) #=> 3
        y = a[:-1] # 32
        a = y+x
    # print(a)
    
# print(a)


#
# Wrong!  
# Code go to 977Aa.py => it is the corect answer
#
