from requests import get
from json import loads
from tkinter import Label as lbl
from tkinter import OptionMenu as om
from tkinter.font import Font
import tkinter as t





# FUNCS

def callback(selection):
    city = selection
    pogoda(city)

    # City Based Weather Filler
def pogoda(city):
    global response_pogoda
    response = response_pogoda

    for row in response:
        if row["stacja"] == city:
            response = row
            break

        # pure data variables  -  Pogoda

    data_pomiaru = response['data_pomiaru']
    godzina_pomiaru = response['godzina_pomiaru']

    suma_opadu = float(response['suma_opadu'])
    predkosc_wiatru = float(response['predkosc_wiatru'])

    temperatura = float(response['temperatura'])

    pogodaFiller(data_pomiaru, godzina_pomiaru, suma_opadu, predkosc_wiatru, temperatura)


    # Fill Labels with Data
def pogodaFiller(data_pomiaru, godzina_pomiaru, suma_opadu, predkosc_wiatru, temperatura):
    pogoda_ico.config(          text =  f"\U0001F30C")
    pogoda_lbl.config(          text =  f"POGODA")
    pogoda_val1.config(         text =  f"{data_pomiaru}")
    pogoda_val2.config(         text =  f"{godzina_pomiaru}:00")

    opad_ico.config(            text =  f"\U0001F327")
    opad_lbl.config(            text =  f"Opady")
    opad_val1.config(           text =  f"{suma_opadu}")
    opad_val2.config(           text =  f"mm")

    wiatr_ico.config(           text =  f"\U0001F32A")
    wiatr_lbl.config(           text =  f"Wiatr")
    wiatr_val1.config(          text =  f"{predkosc_wiatru}")
    wiatr_val2.config(          text =  f"km/h")

    temperatura_ico.config(     text =  f"\U0001F321")
    temperatura_lbl.config(     text =  f"Temperatura")
    temperatura_val1.config(    text =  f"{temperatura}")
    temperatura_val2.config(    text =  f"C")    






# DATA

url1 = "http://api.worldbank.org/v2/country/PL/indicator/SP.POP.TOTL/?date=2019&format=JSON"
url2 = "https://coronavirus-19-api.herokuapp.com/countries/poland"
url3 = "https://danepubliczne.imgw.pl/api/data/synop"

CITIES = []

response_people = get(url1)
response_covid = get(url2)
response_pogoda = get(url3)

response_people = loads(response_people.text)
response_covid = loads(response_covid.text)
response_pogoda = loads(response_pogoda.text)

for row in response_pogoda:
    CITIES.append(row['stacja'])

    # pure data variables  -  Covid

cases = response_covid['cases']
todayCases = response_covid['todayCases']

deaths = response_covid['deaths']
todayDeaths = response_covid['todayDeaths']

recovered = response_covid['recovered']
population = response_people[1][0]["value"]

sick_percentage = round(response_covid["cases"] * 100 / population, 2)
dead_percentage = round(response_covid["deaths"] * 100 / population, 2)







# GUI ELEMENTS

    # main window
mwin = t.Tk()

mwin.geometry("1000x850+5+5")
mwin.title("Daily info")
# mwin.iconbitmap('../img/favi.ico')

mw = t.Frame(mwin)
mw.grid(pady = 10, padx = 10)

    # fonts
myFontBld = Font(family="Arial", size=20, weight = 'bold')
myFont = Font(family="Arial", size=20)

    # labels
hr               = lbl(mw, width = 60 ,  height = 2 , anchor = 'w',  font=myFontBld, text="- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
divider1         = lbl(mw, width = 1 ,   height = 2 , anchor = 'e',  font=myFont, text="|")
divider2         = lbl(mw, width = 1 ,   height = 2 , anchor = 'e',  font=myFont, text="|")
divider3         = lbl(mw, width = 1 ,   height = 2 , anchor = 'e',  font=myFont, text="|")
divider4         = lbl(mw, width = 1 ,   height = 3 , anchor = 'ne', font=myFont, text="|")
divider5         = lbl(mw, width = 1 ,   height = 2 , anchor = 'e',  font=myFont, text="|")
divider6         = lbl(mw, width = 1 ,   height = 2 , anchor = 'e',  font=myFont, text="|")
divider7         = lbl(mw, width = 1 ,   height = 2 , anchor = 'e',  font=myFont, text="|")

            # select list loader
def_city = t.StringVar(mw)
def_city.set('Katowice')

city_selector    = om( mw, def_city , *CITIES, command=callback)
city_selector.config(font = "Arial 15 bold")


        # pogoda labels
pogoda_ico       = lbl(mw, width = 3 ,   height = 3 , anchor = 'w', font=myFontBld, text = f"")
pogoda_lbl       = lbl(mw, width = 11 ,  height = 3 , anchor = 'w', font=myFontBld, text = f"")
pogoda_val1      = lbl(mw, width = 9 ,   height = 3 , anchor = 'e', font=myFontBld, text = f"")
pogoda_val2      = lbl(mw, width = 7 ,   height = 3 , anchor = 'e', font=myFontBld, text = f"")

opad_ico         = lbl(mw, width = 3 ,   height = 2 , anchor = 'e',  font=myFont, text = f"")
opad_lbl         = lbl(mw, width = 11 ,  height = 2 , anchor = 'e',  font=myFont, text = f"")
opad_val1        = lbl(mw, width = 9 ,   height = 2 , anchor = 'e',  font=myFont, text = f"")
opad_val2        = lbl(mw, width = 7 ,   height = 2 , anchor = 'e',  font=myFont, text = f"")

wiatr_ico        = lbl(mw, width = 3 ,   height = 2 , anchor = 'e',  font=myFont, text = f"")
wiatr_lbl        = lbl(mw, width = 11 ,  height = 2 , anchor = 'e',  font=myFont, text = f"")
wiatr_val1       = lbl(mw, width = 9 ,   height = 2 , anchor = 'e',  font=myFont, text = f"")
wiatr_val2       = lbl(mw, width = 7 ,   height = 2 , anchor = 'e',  font=myFont, text = f"")

temperatura_ico  = lbl(mw, width = 3 ,   height = 2 , anchor = 'e',  font=myFont, text = f"")
temperatura_lbl  = lbl(mw, width = 11 ,  height = 2 , anchor = 'e',  font=myFont, text = f"")
temperatura_val1 = lbl(mw, width = 9 ,   height = 2 , anchor = 'e',  font=myFont, text = f"")
temperatura_val2 = lbl(mw, width = 7 ,   height = 2 , anchor = 'e',  font=myFont, text = f"")


        # covid labels
covid_ico        = lbl(mw, width = 3 ,   height = 3 , anchor = 'nw', font=myFontBld, text = "\U0001F4A9")
covid_lbl        = lbl(mw, width = 11 ,  height = 3 , anchor = 'nw', font=myFontBld, text = "COVIDOWO")

populacja_ico    = lbl(mw, width = 3 ,   height = 3 , anchor = 'ne', font=myFont, text = f"\U0001F464")
populacja_lbl    = lbl(mw, width = 11 ,  height = 3 , anchor = 'ne', font=myFont, text = f"Chyba żywych")
populacja_val1   = lbl(mw, width = 9 ,   height = 3 , anchor = 'ne', font=myFont, text = f"{population:,}".format(population).replace(',',' '))

przypadki_ico    = lbl(mw, width = 3 ,   height = 2 , anchor = 'e',  font=myFont, text = f"\U0001F922")
przypadki_lbl    = lbl(mw, width = 11 ,  height = 2 , anchor = 'e',  font=myFont, text = f"Przypadków")
przypadki_val1   = lbl(mw, width = 9 ,   height = 2 , anchor = 'e',  font=myFont, text = f"{cases:,}".format(cases).replace(',',' '))
przypadki_val2   = lbl(mw, width = 7 ,   height = 2 , anchor = 'e',  font=myFont, text = f"+{todayCases:,}".format(todayCases).replace(',',' '))
przypadki_val3   = lbl(mw, width = 7 ,   height = 2 , anchor = 'e',  font=myFont, text = f"{sick_percentage} %")

smierci_ico      = lbl(mw, width = 3 ,   height = 2 , anchor = 'e',  font=myFont, text = f"\U0001F480")
smierci_lbl      = lbl(mw, width = 11 ,  height = 2 , anchor = 'e',  font=myFont, text = f"Umarniętych")
smierci_val1     = lbl(mw, width = 9 ,   height = 2 , anchor = 'e',  font=myFont, text = f"{deaths:,}".format(deaths).replace(',',' '))
smierci_val2     = lbl(mw, width = 7 ,   height = 2 , anchor = 'e',  font=myFont, text = f"+{todayDeaths:,}".format(todayDeaths).replace(',',' '))
smierci_val3     = lbl(mw, width = 7 ,   height = 2 , anchor = 'e',  font=myFont, text = f"{dead_percentage} %")

wyleczeni_ico    = lbl(mw, width = 3 ,   height = 2 , anchor = 'e',  font=myFont, text = f"\U0001F49E")
wyleczeni_lbl    = lbl(mw, width = 11 ,  height = 2 , anchor = 'e',  font=myFont, text = f"Łozdrowionych")
wyleczeni_val1   = lbl(mw, width = 9 ,   height = 2 , anchor = 'e',  font=myFont, text = f"{recovered:,}".format(recovered).replace(',',' '))






# GUI BUILDING

covid_ico.grid(             row = 0, column = 0, sticky = "ew")
covid_lbl.grid(             row = 0, column = 1)

populacja_ico.grid(         row = 1, column = 0)
populacja_lbl.grid(         row = 1, column = 1)
divider4.grid(              row = 1, column = 2)
populacja_val1.grid(        row = 1, column = 3)

przypadki_ico.grid(         row = 2, column = 0)
przypadki_lbl.grid(         row = 2, column = 1)
divider5.grid(              row = 2, column = 2)
przypadki_val1.grid(        row = 2, column = 3)
przypadki_val2.grid(        row = 2, column = 4)
przypadki_val3.grid(        row = 2, column = 5)

smierci_ico.grid(           row = 3, column = 0)
smierci_lbl.grid(           row = 3, column = 1)
divider6.grid(              row = 3, column = 2)
smierci_val1.grid(          row = 3, column = 3)
smierci_val2.grid(          row = 3, column = 4)
smierci_val3.grid(          row = 3, column = 5)

wyleczeni_ico.grid(         row = 4, column = 0)
wyleczeni_lbl.grid(         row = 4, column = 1)
divider7.grid(              row = 4, column = 2)
wyleczeni_val1.grid(        row = 4, column = 3)


hr.grid(                    row = 5, column = 0, columnspan = 7, sticky = "ew")

city_selector.grid(         row = 6, column =0, columnspan = 2, sticky = "ew")

pogoda_ico.grid(            row = 7, column = 0, sticky = "ew")
pogoda_lbl.grid(            row = 7, column = 1)
pogoda_val1.grid(           row = 7, column = 3)
pogoda_val2.grid(           row = 7, column = 4)

opad_ico.grid(              row = 8, column = 0)
opad_lbl.grid(              row = 8, column = 1)
divider1.grid(              row = 8, column = 2)
opad_val1.grid(             row = 8, column = 3)
opad_val2.grid(             row = 8, column = 4)

wiatr_ico.grid(             row = 9, column = 0)
wiatr_lbl.grid(             row = 9, column = 1)
divider2.grid(              row = 9, column = 2)
wiatr_val1.grid(            row = 9, column = 3)
wiatr_val2.grid(            row = 9, column = 4)

temperatura_ico.grid(       row = 10, column = 0)
temperatura_lbl.grid(       row = 10, column = 1)
divider3.grid(              row = 10, column = 2)
temperatura_val1.grid(      row = 10, column = 3)
temperatura_val2.grid(      row = 10, column = 4)




# END
callback('Katowice')
mw.mainloop()
