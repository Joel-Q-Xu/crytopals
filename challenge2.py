m1=bytes.fromhex('1c0111001f010100061a024b53535009181c')
m2=bytes.fromhex('686974207468652062756c6c277320657965')
s1=m1.decode()
s2=m2.decode()
def xor_strings(strA, strB):
	return "".join(chr(ord(x) ^ ord(y)) for (x,y) in zip(strA, strB))
c1=xor_strings(s1,s2)
c2=c1.encode('utf-8')
c3=c2.hex()
z='746865206b696420646f6e277420706c6179'
if c3==z:
    print(c3)


 
