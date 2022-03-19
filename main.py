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
    for number in range(4):
        number = random.randrange(0, 9)
        cislo.append(number)
    if len(cislo) > len(set(cislo)) or cislo[0] == 0:
        cislo.clear()
        generuj_cislo()

def hrat_hru():
    # global pocet_pokusu
    pocet_pokusu =+ 1
    cows = 0
    bulls = 0
    pokus = input(">>> ")
    zvolene_cislo = int(pokus)




# Zacatek programu
print(
    "Hi there!" +
    "\n" + oddelovac +
    "\n" + "I've generated a random 4 digit number for you." +
    "\n" + "Let's play a bulls and cows game."
    "\n" + oddelovac
)
print("Enter a number: .... (4 digit, each digit has to be different, cannot start with 0)")
hrat_hru()