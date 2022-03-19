# Python Akademie - 2.projekt --- Bull & Cows

# import knihoven
import random

# definovani promennych
oddelovac = "-" * 47
cislo = []
pocet_pokusu = []

# bulls = 0    # uhodnute cislo i umisteni
# cows = 0     # uhodnute pouze cislo, ne umisteni

# vytvoreni hadaneho cisla
def generuj_cislo():
    for i in range(4):
        x = random.randrange(0, 9)
        cislo.append(x)
    if len(cislo) > len(set(cislo)):
        cislo.clear()
        generuj_cislo()

print(cislo)

# Zacatek programu
print(
    "Hi there!" +
    "\n" + oddelovac +
    "\n" + "I've generated a random 4 digit number for you." +
    "\n" + "Let's play a bulls and cows game."
    "\n" + oddelovac
)

