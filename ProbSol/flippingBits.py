
def toBinary(n):
    return ''.join(str(1 & int(n) >> i) for i in range(32)[::-1])
def toBinary2(n):
    ou=''
    for c in n:
        if c=='0':
            ou+='1'
        else:
            ou+='0'
    return (ou)

# Complete the flippingBits function below.
def flippingBits(n):

    bin1 = toBinary(n)
    bin2 = int(toBinary2(bin1),2)
    print(bin1, bin2)


n = 802743475
flippingBits(n)