from main import kalendarz

def list_calendar(format):
    if format == "txt":
        ListingStrategy.list_calendar_txt()
    if format == "icalendar":
        ListingStrategy.list_calendar_icalendar()

class ListingStrategy():
    def list_calendar_txt():
        print("\033c")
        for key, value in kalendarz.items():
            print(f"\nData: {key}\nGodzina: {value[0]}\nNazwa: {value[1]}\n")
        input("Kliknij enter aby wrocic do menu")
        
    def list_calendar_icalendar():
        print("\033c")
        print("BEGIN:VCALENDAR\nVERSION:2.0\nBEGIN:VTIMEZONE\nTZID:Europe/Warsaw\nX-LIC-LOCATION:Europe/Warsaw\nEND:VTIMEZONE")
        for key, value in kalendarz.items():
            data_start = str(key).split('.')[-1] + str(key).split('.')[1] + str(key).split('.')[0]+"T"+str(value[0]).split(':')[0]+str(value[0]).split(':')[1]+"Z"
            data_end = str(key).split('.')[-1] + str(key).split('.')[1] + str(key).split('.')[0]+"T"+str(int(str(value[0]).split(':')[0])+1)+str(value[0]).split(':')[1]+"Z"
            nazwa_wydarzenia= value[1]
            print(f"BEGIN:VEVENT\nDTSTART:{data_start}\nDTEND:{data_end}\nSUMMARY:{nazwa_wydarzenia}\nEND:VEVENT")
        print("END:VCALENDAR")