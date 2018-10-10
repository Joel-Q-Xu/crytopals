#以字符串形势传入
def test_hamming_distance(m1, m2):
    """我们以d（x,y）表示两个字x,y之间的汉明距离。对两个字符串进行异或运算，
        并统计结果为1的个数，那么这个数就是汉明距离。——百度百科
    """
    hamming_distance = 0
    for b1, b2 in zip(m1,m2):
        x = ord(b1) ^ord(b2)
        hamming_distance += sum([1 for bit in bin(x) if bit == '1'])
    return hamming_distance

#以字节型传入
def hamming_distance(m1, m2):
    """我们以d（x,y）表示两个字x,y之间的汉明距离。对两个字符串进行异或运算，
        并统计结果为1的个数，那么这个数就是汉明距离。——百度百科
    """
    hamming_distance = 0
    for b1, b2 in zip(m1,m2):
        x = b1^b2
        hamming_distance += sum([1 for bit in bin(x) if bit == '1'])
    return hamming_distance

def main() :
    m1='this is a test'
    mm1=bytearray.fromhex((m1.encode()).hex())
    m2='wokka wokka!!!'
    mm2=bytearray.fromhex((m2.encode()).hex())
    print(test_hamming_distance(m1,m2))
    print(hamming_distance(mm1,mm2))
    
if __name__ == '__main__':
    main()





