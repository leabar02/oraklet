import random 

datorn_tänker = random.randint(1, 10)

print("Gissa på ett tal mellan 1 och 10.")

användarens_gissning = int(input("användarens_gissning"))

print(f"Du gissade {användarens_gissning}")
print(f"Datorn tänkte på {datorn_tänker}")

if användarens_gissning == datorn_tänker:
    print("Du vann!")
else:
    print("Du fick fel, bättre tur nästa gång.")
