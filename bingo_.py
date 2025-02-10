data = open("Banko/bingo_plader.txt", "r")
lines = data.readlines()
lines = [line.strip() for line in lines]
lines = [line.split() for line in lines]
data.close()

banko_plader = []
current_plade = []
for line in lines:
    if line != []:
        current_plade.append(line)
    else:    
        banko_plader.append(current_plade)
        current_plade = []
if current_plade != []:
    banko_plader.append(current_plade)

spil_mode = 1

def skift_mode(mode):
    global spil_mode
    if mode in [1,2,3]:
        spil_mode = mode
        print("Mode skiftet til", mode)
    else:
        print("UGYLDIG MODE")

def draw_number(n):
    numbers = open("Banko/bingo_tal.txt", "a")
    numbers.write(str(n) + "\n")
    numbers.close()

def list_numbers():
    numbers = open("Banko/bingo_tal.txt", "r")
    lines = numbers.readlines()
    lines = [line.strip() for line in lines]
    numbers.close()
    return lines

def list_numbers_ordered():
    numbers = list_numbers()
    numbers.sort()
    return numbers

def reset_numbers():
    numbers = open("Banko/bingo_tal.txt", "w")
    numbers.close()

def undo_last_draw():
    numbers = open("Banko/bingo_tal.txt", "r")
    lines = numbers.readlines()
    lines = [line.strip() for line in lines]
    numbers.close()
    numbers = open("Banko/bingo_tal.txt", "w")
    for line in lines[:-1]:
        numbers.write(line + "\n")
    numbers.close()

def check_bingo_line():
    numbers = list_numbers()
    for p, plade in enumerate(banko_plader):
        for i, linje in enumerate(plade):
            if all([number in numbers for number in linje]):
                return p, i
    return False

def check_bingo_full():
    numbers = list_numbers()
    for p, plade in enumerate(banko_plader):
        if all([all([number in numbers for number in linje]) for linje in plade]):
            return p
    return False

def check_winner():
    if spil_mode == 1:
        return check_bingo_line()
    if spil_mode == 3:
        return check_bingo_full()
    else:
        print("ERROR: UGYLDIG MODE")

def check_if_close():
    numbers = list_numbers()
    potential_winners = []
    for i in range(1,91):
        number = str(i)
        if number not in numbers:
            draw_number(number)
            if check_winner() != False:
                potential_winners.append(number)
            undo_last_draw()
    return potential_winners



while True:
    print("-------------------------------------------------------------\nVi spiller om " + str(spil_mode) + " række(r). Hvad kunne du tænke dig at gøre nu?")
    svar = input("n: Træk tallet n.          se: Se de trukne tal.          ses: Se tallene sorteret.          nulstil: Nulstil de trukne tal.          skift: Skift, hvad der spilles om.          fortryd: Fortryd sidste tal.\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    if svar and svar[0] in ["1","2","3","4","5","6","7","8","9"]:
        number = svar
        draw_number(number)
        print("Tallet", number, "er nu trukket.")
        winner = check_winner()
        if winner != False:
            if spil_mode == 1:
                print("BINGO! Der er bingo på plade", winner[0]+1, "i linje", winner[1]+1)
            if spil_mode == 3:
                print("BINGO! Der er bingo på plade", winner+1)
        else:
            print("Der er bingo på vej for følgende tal:", *check_if_close())

    elif svar == "se":
        print("De trukne tal er:", *list_numbers())
    
    elif svar == "ses":
        print("De trukne tal er:", *list_numbers_ordered())

    elif svar == "nulstil":
        sikkerhed = input("Er du sikker på at du vil nulstille de trukne tal? (ja/nej)\n")
        if sikkerhed == "ja":
            reset_numbers()
            print("De trukne tal er nu nulstillet.")

    elif svar == "skift":
        mode = int(input("Hvilket mode vil du skifte til? (1, 2, 3) Lige nu spilles der om " + str(spil_mode) + " række(r).\n"))
        skift_mode(mode)

    elif svar == "fortryd":
        undo_last_draw()
        print("Sidste trækning er blevet fortrudt.")

    else:
        print("DET FORSTOD JEG IKKE. PRØV IGEN.")