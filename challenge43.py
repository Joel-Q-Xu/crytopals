from hashlib import sha1
from gmpy2 import invert

r = 548099063082341131477253921760299949438196259240
s = 857042759984254168557880549501802188789837994940
p=int('800000000000000089e1855218a0e7dac38136ffafa72eda7859f2171e25e65eac698c1702578b07dc2a1076da241c76c62d374d8389ea5aeffd3226a0530cc565f3bf6b50929139ebeac04f48c3c84afb796d61e5a4f9a8fda812ab59494232c7d2b4deb50aa18ee9e132bfa85ac4374d7f9091abc3d015efc871a584471bb1',16)
q=int('f4f47f05794b256174bba6e9b396a7707e563c5b',16)
g=int('5958c9d3898b224b12672c0b98e06c60df923cb8bc999d119458fef538b8fa4046c8db53039db620c094c9fa077ef389b5322a559946a71903f990f1f7e0e025e2d7f7cf494aff1a0470f5b64c36b625a097f1651fe775323556fe00b3608c887892878480e99041be601a62166ca6894bdd41a7054ec89f756ba9fc95302291',16)

y=int('84ad4719d044495496a3201c8ff484feb45b962e7302e56a392aee4abab3e4bdebf2955b4736012f21a08084056b19bcd7fee56048e004e44984e2f411788efdc837a0d2e5abb7b555039fd243ac01f0fb2ed1dec568280ce678e931868d23eb095fde9d3779191b8c0299d6e07bbb283e6633451e535c45513b2d33c99ea17',16)
m = 'For those that envy a MC it can be hazardous to your health\nSo be friendly, a matter of life and death, just like a etch-a-sketch\n'
fingerprint='0954edd5e0afe5542a4adf012611a91912a3ec16'

for k in range(2**16):
    h_m=sha1(m.encode()).hexdigest()
    h_m_int=int(h_m,16)
    r1=int(invert(r,q))
    x=((s*k-h_m_int)*r1)%q
    
    y_x=pow(g,x,p)
    
    if y_x==y:
        sha_x=sha1(hex(x)[2:-1]).hexdigest()
        print 'my private key is:',sha_x
        print 'x=',x
        print 'k=',k
        break
