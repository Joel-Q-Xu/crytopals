from hashlib import sha1
from itertools import combinations
from re import findall
from gmpy2 import invert
y=int('2d026f4bf30195ede3a088da85e398ef869611d0f68f0713d51c9c1a3a26c95105d915e2d8cdf26d056b86b8a7b85519b1c23cc3ecdc6062650462e3063bd179c2a6581519f674a61f1d89a1fff27171ebc1b93d4dc57bceb7ae2430f98a6a4d83d8279ee65d71c1203d2c96d65ebbf7cce9d32971c3de5084cce04a2e147821',16)
fingerprint='ca8f6f7c66fa362d40760d135b763eb8527d3d52'
q=int('f4f47f05794b256174bba6e9b396a7707e563c5b',16)
g=int('5958c9d3898b224b12672c0b98e06c60df923cb8bc999d119458fef538b8fa4046c8db53039db620c094c9fa077ef389b5322a559946a71903f990f1f7e0e025e2d7f7cf494aff1a0470f5b64c36b625a097f1651fe775323556fe00b3608c887892878480e99041be601a62166ca6894bdd41a7054ec89f756ba9fc95302291',16)
p=int('800000000000000089e1855218a0e7dac38136ffafa72eda7859f2171e25e65eac698c1702578b07dc2a1076da241c76c62d374d8389ea5aeffd3226a0530cc565f3bf6b50929139ebeac04f48c3c84afb796d61e5a4f9a8fda812ab59494232c7d2b4deb50aa18ee9e132bfa85ac4374d7f9091abc3d015efc871a584471bb1',16)


def file():
    pattern = r'msg: ([a-zA-Z.,\' ]+)\n'\
              r's: ([0-9]+)\n' \
              r'r: ([0-9]+)\n' \
              r'm: ([0-9a-f]+)\n'

    with open('44.txt') as f:
        s = f.read()

    return findall(pattern, s)

t=file()
for i,j in combinations(range(len(t)),2):
    s1,m1=int(t[i][1]),int(t[i][3],16)
    s2,m2=int(t[j][1]),int(t[j][3],16)

    s=s1-s2
    s_inv=int(invert(s,q))

    m=m1-m2

    k=m*(s_inv)%q

    r=int(t[i][2])
    r1=int(invert(r,q))
    x=(s1*k-m1)*r1%q

    y_x=pow(g,x,p)
    
    if y_x==y:
        sha_x=sha1(hex(x)[2:-1]).hexdigest()
        print 'my private key is:',sha_x
        print 'x=',x
        print 'k=',k
        break
