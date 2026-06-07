import random

angka_rahasia = random.randint(1, 100)
ronde = 0
max_ronde = 7

print("=====TEBAK ANGKA=====")
print("Saya telah memilih satu angka, dari  1- 100!")
print("Nt tebak angka itu, Nt punya " + str(max_ronde) + "kesempatan")

while(ronde < max_ronde):
    tebakan = int(input("Tebakan Kamu: "))
    ronde += 1

    if (tebakan < angka_rahasia):
        print("Tebakan terlalu kecil! ")
    elif (tebakan > angka_rahasia):
        print("Tebakan terlalu besar! ")
    else:
        print("SELAMAT!!!, Jawaban Nt benar")
        exit(0)
    print("Kesempatan Nt tersisa: " + str(max_ronde - ronde))
    print("________________________________________________")

print("Kesempatan Nt habis ")
print("Angka rahasianya adalah: =>" + str(angka_rahasia))