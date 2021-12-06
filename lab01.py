def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    res=1
    while k>0:
        res=res*n
        n=n-1
        k=k-1
    return res


    #**********************************************************下面第一遍做的,两个星期前的弱鸡做的
    #n*(n-1)*（n-2）...(n-b)  一共k个循环
    #if k==0:           #排除k=0的
    #    return 1
    #elif k==1:         #试了一下K=1的时候也不好弄
    #    return n
    #else:
    #    b=1
    #    c=n            #把初始值的 n储存起来，后面要用到
    #    while b!=k:
    #        n=n*(c-b)
    #        b=b+1
    #    return n


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    #循环除以10，余数就是每一位的值，取整的商继续除以10，妙啊
    res=0
    k=0
    length=len(str(y))
    while k<length:  #一开始写的len(str(y))但是y后面是变的.....没看到
        res=res+y%10
        y=y//10
        k=k+1
    return res

    #****************下面是第一次做的
    #k=1
    #b=0
    #while y>=10**k:
    #    k=k+1
    #return k   #确定y的位数
    #for i in range(0,k):       #range后面左包右不包，0.......k-1
    #    b=b+int(str(y)[i])     #但是这边正好 y[0] 是第一个字符 y[k-1]是第k个字符
    #return b

    #突然做出来了

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    for i in range(0,len(str(n))-1):
        if str(n)[i]=="8":
            if str(n)[i+1]=="8":
                return True
    else:
        return False


    #if "88" in str(n):
    #    return True
    #else:
    #    return False

    #*******************下面是第一次做的，两个星期前弱鸡的我做的
    #k=0
    #n=str(n) # "880088"
    #或者这样 return '88' in n
    #if "88" in n:
    #    return True
    #else:
    #    return False
