rsz_es_asz = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

def atalakit(a):
    arab = 0
    for i in range(len(a)):
        if i>0 and rsz_es_asz[a[i]]>rsz_es_asz[a[i-1]]:
            arab += rsz_es_asz[a[i]]-2*rsz_es_asz[a[i-1]]
        else:
            arab += rsz_es_asz[a[i]]
    return arab

ossz = 0
f=True
while f:
    try:
        while ossz<1000:
            a = input("Adj meg egy római számot: ").upper()
            x = atalakit(a)
            ossz += x
            print(f"{a}->{x}")
        if ossz>=1000:
            break
    except KeyError:
        print("Ha nem római számot adsz meg, nem tudunk együtt dolgozni!")
        f=True
        continue
