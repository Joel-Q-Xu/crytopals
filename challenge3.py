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

def main():
    #将得到的c转化为十进制
    c = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    ciphertext = bytes.fromhex(c)
    messages = []
    for i in range(256):
        m = single_xor(ciphertext,i)
        score = get_score(m)
        data = {
            'message': m,
            'score': score,
            'key': chr(i)
            }
        messages.append(data)
    #排序(降序）,得到最高分
    best_score = sorted(messages, key=lambda x: x['score'], reverse=True)[0]
    for item in best_score:
        print(item,":", best_score[item])

if __name__ == '__main__':
    main()

