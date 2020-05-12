import numpy as np

def rendez(v, d, e, f):
    global c
    if f == "+":
        for i in range(d, e):
            for j in range(i + 1, e + 1):
                if v[i] > v[j]:
                    v[i], v[j] = v[j], v[i]
    if f == "-":
        for i in range(d, e):
            for j in range(i + 1, e + 1):
                if v[i] < v[j]:
                    v[i], v[j] = v[j], v[i]
    t = v.tolist()
    t.insert(d, '|')
    t.insert(e + 2, '|')
    v_uj = np.asarray(t, dtype=object)
    return v_uj
f=True
while f:
    try:
        c = int(input("Adja meg a vektor méretét: "))
        if c <= 0:
            raise ValueError
        break
    except ValueError:
        print("Kérem pozitív egész számot adjon meg!")
        f=True
while f:
    try:
        a = int(input("Adja meg a vektor kezdőértékét: "))
        break
    except ValueError:
        print("Kérem egész számot adjon meg!")
        f=True
while f:
    try:
        b = int(input("Adja meg a vektor végértékét: "))
        if b<=a:
            raise ValueError
        break
    except ValueError:
        print("Kérem egész számot adjon meg, ami {a}-nál/nél nagyobb!".format(a = a))
        f=True
v = np.random.randint(a,b,c)
print(v)
while f:
    try:
        d = int(input("Hol kezdődjön a rendezés? (egész szám 0 és {c} között) ".format(c = c - 1)))
        if d < 0 or d > c-1:
            raise ValueError
        break
    except:
        print("Kérem pozitív egész számot adjon meg, ami 0 és {c} között van!".format(c = c - 1))
        f=True
while f:
    try:
        e = int(input("Hol érjen véget? (egész szám {d} és {c} között) ".format(d = d , c = c - 1)))
        if e < d or e > c - 1:
            raise ValueError
        break
    except:
        print("Kérem pozitív egész számot adjon meg, ami {d} és {c} között van!".format(d=d, c=c-1))
        f = True
while f:
    try:
        mv=["+","-"]
        f = input("Növekvő (+) vagy csökkenő (-) sorrendben legyenek a számok? Írjon + vagy - jelet: ")
        if f not in mv:
            raise KeyError
        break
    except KeyError:
        print("Nem megfelelő a műveleti jel!")
        f=True

print(rendez(v, d, e, f))