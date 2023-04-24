kalendarz = {}
def main_f():
    print("[1] Dodaj nowe wydarzenie. \n[2] Wyswietl wydarzenia. (txt) \n[3] Wyswietl wydarzenia. (iCalendar)\n[4] Zamknij program")
    menuchoice = int(input("Wybierz: "))
    if menuchoice > 0 and menuchoice <= 4:
        return menuchoice
    else:
        print('Wybierz poprawnie')
        main_f()
