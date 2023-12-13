import numpy as np

def encrypt(matrix):
    encrypted=""
    m=np.array(matrix)
    s=sorted(''.join(m[0]))#sorting key to fetch letters in order
    for i in s:
        for j in range(len(m[0])):
            if m[0][j]==i:
                encrypted+=''.join(m[1:,j])

    return encrypted

def decrypt(text, key):
    decrypted=""
    s=sorted(key)#sorting key to fetch letters in order
    nrows = int(len(text) / len(key))
    rows, cols = (nrows+1, len(key))
    m = [[' ' for i in range(cols)] for j in range(rows)]
    for i in range(len(m[0])):
        m[0][i]=key[i]
    ch=0
    for i in s:
        for j in range(len(m[0])):
            if m[0][j]==i:
                for k in range(1,nrows+1):
                    m[k][j]=text[ch]
                    ch+=1

    for i in range(1,nrows+1):
        for j in range(len(key)):
            decrypted+=m[i][j]

    return decrypted


def build_matrix(key,text):
    row=[]
    m=[]
    l = len(key)
    for i in key:
        row.append(i)
    m.append(row)
    nrows=int(len(text)/l)
    if nrows*l!=len(text):
        text+=' '*(len(text)-nrows)
        nrows+=1


    for j in range(nrows):
        r=[]
        chindex=l*j
        for i in range(l):
            r.append(text[chindex+i])

        m.append(r)
    return m



if __name__ == '__main__':

    with open('key.txt', 'r') as file:
        key = file.read().replace('\n', '')
    with open('plaintext.txt', 'r') as file:
        text = file.read().replace('\n', '')
    m = build_matrix(key,text)

    encrypted=encrypt(m)
    text_file = open("cipher.txt", "w")
    text_file.write(encrypted)
    text_file.close()
    print(encrypted)
    decrypted=decrypt(encrypted,key)
    print(decrypted)
    text_file = open("recover.txt", "w")
    text_file.write(decrypted)
    text_file.close()

