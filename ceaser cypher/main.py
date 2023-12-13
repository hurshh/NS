import pandas as pd
def encrypt(text, key):
    result = ""
    ans = ''
    for i in range(len(text)):
        char = text[i]
        if char == ' ':
            ans = char
        elif char.isupper():
            n = ord(char) - ord('A') + key
            n %= 26
            n += ord('A')
            ans = chr(n)

        elif char.islower():
            n = ord(char) - ord('a') + key
            n %= 26
            n += ord('a')
            ans = chr(n)

        result += ans

    return result


def decrypt(text, key):
    print(text)
    result = ""
    ans = ''
    for char in text:
        if char == ' ':
            ans = ' '
        elif char.isupper():
            n = ord(char) - ord('A') - key
            if n < 0:
                n += 25
            n += ord('A')
            ans = chr(n)

        elif char.islower():
            n = ord(char) - ord('a') - key
            if n < 0:
                n += 25
            n += ord('a')
            ans = chr(n)

        result += ans

    return result


def brute_force(text):
    result = []
    keys = []
    for key in range(0, 26):
        result.append(decrypt(text, key))
        keys.append(key)
    return result, keys


def freq_analysis(text):
    dict = {}
    for char in text:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1

    sort = sorted(dict.items(), key=lambda kv: kv[1], reverse=True)
    ideal = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    for i in range(len(sort)):
        n1 = ord(sort[i][0])
        for j in range(len(ideal)):
            n2 = ord(ideal[j])
            key = n1 - n2
            result = decrypt(text, key)
            print("Here is the decryption: ", result)
            stop = int(input("Enter 1 if you are satisfied with the outcome and 0 if you are not:"))
            if stop == 1:
                return result, key


def main():
    case = int(input("Enter 1 for Encryption, 2 for Decryption, 3 for Brute-Force approach ,4 for Freq_Analysis "
                     "approach: "))

    if case == 1:
        with open('data.txt', 'r') as file:
            text = file.read().replace('\n', '')
        print("Encrypting")
        key = int(input("Enter a Key : "))
        result = encrypt(text, key)
        print(result)
        text_file = open("encrypt.txt", "w")
        text_file.write(result)
        text_file.close()

    elif case == 2:
        with open('encrypt.txt', 'r') as file:
            text = file.read().replace('\n', '')
        print("Decrypting")
        key = int(input("Enter a Key : "))
        result = decrypt(text, key)
        print(result)
        text_file = open("decypher.txt", "w")
        text_file.write(result)
        text_file.close()

    elif case == 3:
        with open('encrypt.txt', 'r') as file:
            text = file.read().replace('\n', '')
        print("Brute Force")
        result, keys = brute_force(text)
        import pandas as pd
        df = pd.DataFrame({"Decipher": result, "key": keys})
        print(df)
        df.to_csv("brute_force.csv")

    elif case == 4:
        with open('encrypt.txt', 'r') as file:
            text = file.read().replace('\n', '')
        print("Freq_Analysis")
        result, key = freq_analysis(text)
        result += " Key:" + str(key)
        text_file = open("frequency_analysis.txt", "w")
        text_file.write(result)
        text_file.close()


if __name__ == "__main__":
    main()