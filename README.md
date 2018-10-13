# crytopals
for my homework of cryptography
may be including
http://cryptopals.com/sets/1
for challenges 1-6
and a report about challeng6
1.首先猜测密钥长度，记为keysize，建议猜测范围为2到40。 
2.写一个计算两个字符串的Hamming distance（汉明距离）的函数。Hamming distance是两个字符串不同比特的数量。例如，this is a test和wokka wokka!!!之间的Hamming distance为37。 
3.对于每一个keysize，获得密文文本的第一个长度为keysize的块以及第二个长度为keysize的块，计算这两个块的Hamming distance并除以keysize得到结果记为avg_distance。 
4.有着最小的avg_distance的keysize很可能就是密钥的长度。可以选择最小的三个avg_distance所对应的keysize进行接下来的操作。也可以在第3步中使用4个keysize大小的块来计算得到avg_distance。 
5.将密文分为长度为keysize的块。 
6.将每个块中的第一个字节组合成一个新的块，每个块中的第二个字节组合成一个新的块，依次类推。 
7.使用单字节XOR密码来处理每个新块。即第一个新块中的每个字节均和密钥的第一个字节异或，第二个新块中的每个字节均和密钥的第二个字节异或，依次类推。由此可得到每个keysize所对应的候选密钥key。
实验设想：
读取和解码文件内容，通过循环潜在的密钥大小范围，编写函数来计算汉明距离，规范汉明距离，将密文分解为块确定的密钥长度和转置块，然后实现XOR暴力破解。
