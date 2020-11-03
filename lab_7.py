# encode binary sequence

def main(bits): # 7
    M=[-16,-16,-23,9,-9,14,23,16]
    B=[0xe0000000,0x10000000,0xf800000,0x600000,0x1fc000,0x3f80,0x60,0x1f]
    t=[*map(lambda x:bits&B.pop(0),M)]
    return hex(sum(t[i]<<M[i]if M[i]>0 else t[i]>>abs(M[i])
                   for i in range(len(M))))