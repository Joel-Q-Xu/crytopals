import base64
def get_score(m):
    """将每个输入字节与字符频率表进行比较，并根
据Englis语言中字符出现的相对频率返回消息的分数
    """
    freq = {
        "e": 0.12702, "t": 0.09056, "a": 0.08167, "o": 0.07507, "i": 0.06966,
        "n": 0.06749, "s": 0.06327, "h": 0.06094, "r": 0.05987, "d": 0.04253,
        "l": 0.04025, "c": 0.02782, "u": 0.02758, "m": 0.02406, "w": 0.02360,
        "f": 0.02228, "g": 0.02015, "y": 0.01974, "p": 0.01929, "b": 0.01492,
        "v": 0.00978, "k": 0.00772, "j": 0.00153, "x": 0.00150, "q": 0.00095,
        "z": 0.00074, ' ': 0.13000, "\n":0
    }
    score=0.0
    for i in m.lower():
        score+=freq.get(chr(i),0)
    return score

def single_xor(ciphertext,i):
    #返回使用单个值进行异或的每个字节的结果
    plaintext = b''  #令plaintext为bytes型
    for item in ciphertext:
        plaintext += bytes([item ^i])
    return plaintext

def break_single_xor(ciphertext):
    """对每个可能的值（0,255）执行单字符异或，
    并根据字符频率分配分数。 返回得分最高的结果。
    """
    messages = []
    for i in range(256):
        m = single_xor(ciphertext,i)
        score = get_score(m)
        data = {
            'message': m,
            'score': score,
            'key':chr(i)
            }
        messages.append(data)
    #排序(升序）,得到最高分，输出sorted[-1]
    best_m=sorted(messages, key=lambda x: x['score'])[-1]
    return best_m

def xor(m,key):
    #如果消息长于密钥，则密钥将重复。
    c = b''  #令plaintext为bytes型
    i=0
    for item in m:
        c+=bytes([item^key[i]])
        if (i+1)==len(key):
            i=0
        else:
            i+=1
    return c

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

""" 1.首先猜测密钥长度，记为keysize，建议猜测范围为2到40。 
    2.写一个计算两个字符串的Hamming distance（汉明距离）的函数。
    Hamming distance是两个字符串不同比特的数量。
    3.对于每一个keysize，获得密文文本的第一个长度为keysize的块
    以及第二个长度为keysize的块，计算这两个块的Hamming distance并
    除以keysize得到结果记为avg_distance。 
    4.有着最小的avg_distance的keysize很可能就是密钥的长度。可以选择
    最小的三个avg_distance所对应的keysize进行接下来的操作。
    也可以在第3步中使用4个keysize大小的块来计算得到avg_distance。 
    5.将密文分为长度为keysize的块。 
    6.将每个块中的第一个字节组合成一个新的块，
    每个块中的第二个字节组合成一个新的块，依次类推。 
    7.使用单字节XOR密码来处理每个新块。
    即第一个新块中的每个字节均和密钥的第一个字节异或，
    第二个新块中的每个字节均和密钥的第二个字节异或，依次类推。
    由此可得到每个keysize所对应的候选密钥key。

"""
def break_xor(ciphertext):
    avg_distance = []
    # 钥匙的长度; 尝试从2到（比如说）40的值 
    for keysize in range(2,41):
        #初始化列表以存储此密钥大小的汉明距离
        distances = []
        # 将密文分成密钥长度的块
        blocks = [ciphertext[i:i+keysize] for i in range(0, len(ciphertext), keysize)]        
        while True:
            try:
                # 从列表开头的两个块中获取汉明距离,除以KEYSIZE将此结果标准化
                block1 = blocks[0]
                block2 = blocks[1]
                distance = hamming_distance(block1, block2)
                distances.append(distance/keysize)

                #删除这些块，以便在循环重新开始时,可以计算下两个块的汉明距离
                del blocks[0]
                del blocks[1]

            # 当发生异常（已处理所有块）时，跳出循环
            except Exception :
                break
        avg= {
            'key': keysize,
            'avg_dist': sum(distances)/len(distances)
            }
        avg_distance.append(avg)
    #升序，即avg_distancr[0]最小
    possible_keysize = sorted(avg_distance,key=lambda x: x['avg_dist'])[0]
    
    possible_plaintext = []
    key = b''
    possible_length = possible_keysize['key']
    print('keysize:',possible_length)
    for i in range(possible_length):
        block = b''
        for j in range(i, len(ciphertext), possible_length):
            block += bytes([ciphertext[j]])
        key += bytes([ord(break_single_xor(block)['key'])]) 
    possible_plaintext.append((xor(ciphertext, key), key))
    return possible_plaintext[0]




def main():
    c=open('c6.txt').read()
    ciphertext=base64.b64decode(c)
    m,key= break_xor(ciphertext)
    print('key:{0}\nm:{1}'.format(key.decode(),m.decode()))


if __name__ == '__main__':
    main()
