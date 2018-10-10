import base64
#生成bytes类型字符串
s=bytes.fromhex('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
c=base64.b64encode(s)
#转换为字符串
str1=c.decode()
str2='SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
if(str1==str2):
    print(str1)

