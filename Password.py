import random

huruf = "abcdefghijklmnopqrstuvwxyz"
huruf_besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
angka = "0123456789"

semua = huruf + huruf_besar + angka 

Password = ''.join(random.sample(semua, 8))

print(f"Ini password kamu: {Password}")