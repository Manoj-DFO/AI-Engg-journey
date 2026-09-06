
#INT TO ROMAN
dit={  1000:'M', 900:'CM',500:'D',400:'CD',100:'C', 90:'XC' ,50:'L',  40:'XL' ,10:'X', 9:'IX' ,5:'V' ,4:'IV',1:'I'}
num=3749
ans=''
for i in dit:
    while num >= i:
        ans += dit[i]
        num -= i

print(ans)