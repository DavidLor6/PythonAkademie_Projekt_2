# Python Akademie - 2.projekt --- Bull & Cows

# import knihoven
import random

# definovani promennych
oddelovac = "-" * 47
cislo = []
pocet_pokusu = []

# vytvoreni hadaneho cisla
def generuj_cislo():
    for number in range(4):
        number = random.randrange(0, 9)
        cislo.append(number)
    if len(cislo) > len(set(cislo)) or cislo[0] == 0:
        cislo.clear()
        generuj_cislo()

def hrat_hru():
    global pocet_pokusu
    pocet_pokusu += 1
    cows = 0   # uhodnute cislo, ne umisteni
    bulls = 0  # uhodnute cislo i umisteni
    pokus = input(">>> ")
    if len(pokus) != 4 or len(pokus) > len(set(pokus)) or int(pokus[0]) == 0:
        print("Wrong input! Your number has to have 4 digit, each digit has to be different and cannot start with 0")
        hrat_hru()
    for i in range(4):
        if int(pokus[i]) == int(cislo[i]):
            bulls += 1
    for j in range(4):
        if int(pokus[j]) in int(cislo):
            cows +=1
    cows = cows - bulls
    if bulls <= 1 and cows <= 1:
        print(f"{bulls} bull, {cows} cow")
    elif bulls >= 1 and cows <= 1:
        print(f"{bulls} bulls, {cows} cow")
    elif bulls <= 1 and cows >= 1:
        print(f"{bulls} bull, {cows} cows")
    else:
        print(f"{bulls} bulls, {cows} cows")
    if bulls == 4:
        if pocet_pokusu <= 1:
            print(f"Correct, you've guessed the right number in {pocet_pokusu} guess!")
            print(oddelovac)
            print("It is amazing!")
        else:
            print(f"Correct, you've guessed the right number in {pocet_pokusu} guesses!")
            print(oddelovac)
            if pocet_pokusu < 10:
                print("Good job!")
            else:
                print("It could be better :)")
    if bulls != 4:
        hrat_hru()

# Zacatek programu
print(
    "Hi there!" +
    "\n" + oddelovac +
    "\n" + "I've generated a random 4 digit number for you." +
    "\n" + "Let's play a bulls and cows game."
    "\n" + oddelovac
)
print("Enter a number: .... (4 digit, each digit has to be different, cannot start with 0)")

generuj_cislo()
hrat_hru()
