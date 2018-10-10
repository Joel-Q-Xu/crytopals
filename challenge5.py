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


def main():
    p_m= "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
    p_m1=p_m.encode()
    m1=p_m1.hex()
    m=bytearray.fromhex(m1)

    p_key='ICE'
    p_key1=p_key.encode()
    key1=p_key1.hex()
    key=bytearray.fromhex(key1)
    print(xor(m,key).hex())

if __name__=='__main__':
    main()

