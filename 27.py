import string

def kotojel(m):
    for i in range(len(m)):
        for j in range(i+1, len(m)+1):
            if m[i] == " " or m[i] in string.punctuation or m[j] == " " or m[j] in string.punctuation or m[i].isdigit() or m[j].isdigit():
                print(m[i], end="")
            else:
                print(m[i], end="-")
            break

a = input("Írj be valamit:")
kotojel(a)