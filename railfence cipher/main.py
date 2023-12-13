def encrypt(m):
    encrypted=""
    for i in m:
        for j in i:
            if len(j)!=0:
                encrypted+=j
    return encrypted

def decrypt(text,depth):

    rows, cols = (depth, len(text))
    m=[['' for i in range(cols)] for j in range(rows)]
    slope=1
    r,c=(0,0)
    for i in range(len(text)):
        m[r][c]=0 #marker
        if r==depth-1:
            slope=-1
        elif r==0:
            slope=1
        r = (r + slope)
        c+=1
    p=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]==0:
                m[i][j]=text[p]
                p+=1
    r,c=(0,0)
    decrypted=""
    for i in range(len(text)):
        decrypted+=m[r][c]
        if r==depth-1:
            slope=-1
        elif r==0:
            slope=1
        r = (r + slope)
        c+=1

    return decrypted

def build_fence(text,depth):
    r,c=(0,0)
    rows, cols = (depth, len(text))
    m=[['' for i in range(cols)] for j in range(rows)]
    slope = 1
    for i in range(len(text)):
        m[r][c]=text[i]

        if r==depth-1:
            slope=-1
        elif r==0:
            slope=1
        r = (r + slope)
        c+=1

    return m



if __name__ == '__main__':
    # text=input("Enter the text:")
    with open('plaintext.txt', 'r') as file:
        text = file.read().replace('\n', '')
    depth=int(input("Enter the depth:"))
    m=build_fence(text,depth)
    for i in m:
        print(i)
    encrypted=encrypt(m)
    text_file = open("cipher.txt", "w")
    text_file.write(encrypted)
    text_file.close()
    print(encrypted)
    decrypted=decrypt(encrypted,depth)
    print(decrypted)
    text_file = open("recover.txt", "w")
    text_file.write(decrypted)
    text_file.close()

