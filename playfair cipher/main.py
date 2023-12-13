def encrypt(matrix, mapping, dia):
    encrypted = ""
    for d in dia:
        l1 = d[0]
        l2 = d[1]
        r1, c1 = mapping[l1]  # matrix location
        r2, c2 = mapping[l2]
        if r1 == r2:
            r1 = (r1 + 1) % 6  # new location
            r2 = (r2 + 1) % 6
        elif c1 == c2:
            c1 = (c1 + 1) % 6
            c2 = (c2 + 1) % 6
        else:
            t = c1
            c1 = c2
            c2 = t

        encrypted += matrix[r1][c1] + matrix[r2][c2]
    return encrypted

def decrypt(matrix, encrypted,mapping):
    decrypted_temp = ""
    bogus="X"
    for i in range(0,len(encrypted),2):
        r1,c1= mapping[encrypted[i]]
        r2,c2= mapping[encrypted[i+1]]
        if r1==r2:
            r1=(r1-1)%6
            r2=(r2-1)%6
        elif c1==c2:
            c1=(c1-1)%6
            c2=(c2-1)%6
        else:
            t=c1
            c1=c2
            c2=t

        decrypted_temp+= matrix[r1][c1] + matrix[r2][c2]
    return decrypted_temp





def matrix(key):
    m = []
    row = []
    for i in key:
        row.append(i)
        if len(row) == 6:
            m.append(row)
            row = []
    m.append(row)
    l = len(row)
    n = ord("A")
    row = []
    for i in range(l, 6):
        while chr(n) in key:
            n += 1
        m[len(m) - 1].append(chr(n))
        n += 1
    for i in range(len(m), 6):
        for j in range(0, 6):
            if n > ord("Z"):
                n = ord("0")
            while chr(n) in key:
                n += 1
            row.append(chr(n))
            n += 1
        m.append(row)
        row = []

    return m


def diagraph(text):
    bogus = "X"
    dia = []
    i = 0
    while i < len(text):
        d = text[i:i + 2]
        if len(d) == 1:
            d = d + bogus
        if d[0] == d[1]:
            d1 = d[0] + bogus
            i += 1
            dia.append(d1)
        else:
            i += 2
            dia.append(d)
    return dia


if __name__ == '__main__':
    key1 = input("Enter the Key:")
    key2=key1.replace(" ","").upper()
    key=""
    for i in key2:
        if i not in key:
            key+=i
    print(key)

    m = matrix(key)
    print("Mappng:\n",m)
    mapping = {}
    for i in range(len(m)):
        for j in range(len(m)):
            mapping[m[i][j]] = (i, j)
    with open('plaintext.txt', 'r') as file:
        text = file.read().replace('\n', '')
    dia = diagraph(text)
    print("Diapgraphs:",dia)
    encryption = encrypt(m, mapping, dia)
    print("Encryption:",encryption)
    text_file = open("cipher.txt", "w")
    text_file.write(encryption)
    text_file.close()
    decryption =decrypt(m,encryption,mapping)
    print("Decryption:",decryption)
    text_file = open("recover.txt", "w")
    text_file.write(decryption)
    text_file.close()