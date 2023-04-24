import re
from main import main_f,kalendarz
from kalendarz import list_calendar

class Menu():
    def choice():
        MenuCommand.execute(main_f())

class MenuCommand():
    def dodawanie():
        print("\033c")
        #Dodawanie nowego wydarzenia
        print("Podaj niezbedne informacje, aby dodac wydarzenie!\n")
        
        name = input("Podaj nazwe wydarzenia: ")
        name_pattern = "^[A-Za-z0-9 \\,.-]"
        
        if re.match(name_pattern,name):
            day = input("Podaj dzien wydarzenia: ")
            day_pattern = "^(((0[1-9])|([12][0-9])|(3[01]))\.((0[0-9])|(1[012]))\.((20[012]\d|19\d\d)|(1\d|2[0123])))"

            if re.match(day_pattern,day):

                time_pattern = "^([0-1]?[0-9]|2[0-3]):[0-5][0-9]"
                time = input("Podaj godzine wydarzenia: ")

                if re.match(time_pattern,time):
                    values = []
                    values.append(time)
                    values.append(name)
                    kalendarz[day] = values
                    print('\nPoprawnie dodano nowe wydarzenie w twoim kalendarzu!\n')
                    input('Kliknij enter, aby wrocic do menu...')

                else:
                    print('\n-----------------------------')
                    print('Wprowadzono niewłaściwe dane!')
                    print('-----------------------------')
            else:
                print('\n-----------------------------')
                print('Wprowadzono niewłaściwe dane!')
                print('-----------------------------')
        else:
            print('\n-----------------------------')
            print('Wprowadzono niewłaściwe dane!')
            print('-----------------------------')

        Menu.choice()
        
    def txt():
        list_calendar("txt")
        Menu.choice()
        
    def iCalendar():
        list_calendar("icalendar")
        Menu.choice()

    def description(self):
        return MenuCommand().description()
    
    def execute(menuchoice):
        if menuchoice == 1:
            MenuCommand.dodawanie()
        if menuchoice == 2:
            MenuCommand.txt()
        if menuchoice == 3:
            MenuCommand.iCalendar()
        if menuchoice == 4:
            ExitCommand.wyjdz()
        else:
            print('Wybierz jeszcze raz...')
            Menu.choice()

class ExitCommand():
    def wyjdz():
        quit()

Menu.choice()

 