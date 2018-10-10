from challenge3 import single_xor
from challenge3 import get_score
#同challenge3中的主要函数，暴力破解每一列密文
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

def main():
    #返回一个各行作为元素的列表
    ciphers = open('c4.txt').read().splitlines()
    plaintext = []
    for item in ciphers:
        ciphertext = bytes.fromhex(item)
        plaintext.append(break_single_xor(ciphertext))
    best_score = sorted(plaintext, key=lambda x: x['score'], reverse=True)[0]
    for item in best_score:
        print(item,":", best_score[item])
        
if __name__ == '__main__':
    main()
