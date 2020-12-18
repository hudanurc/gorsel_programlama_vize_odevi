# beginning of 4th question
sayac = 0
for j in range(102, 987, 1):
    a1 = int(j/100)
    b1 = int(j % 100/10)
    c1 = int(j % 10)
    if a1 != b1 and a1 != c1 and b1 != c1:
        print(j)
        sayac += 1
print("toplam sayi sayisi=", sayac)
