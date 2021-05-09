liczba = int(input("Wprowadz liczbe (0-999): "))
dict_jednosci = {
        1:"jeden", 
        2:"dwa",
        3:"trzy",
        4:"cztery",
        5:"pięć",
        6:"sześć",
        7:"siedem",
        8:"osiem",
        9:"dziewięć"}
dict_dziesiatki = {
        10:"dziesięć", 
        20:"dwadzieścia", 
        30:"trzydzieści",
        40:"czterdzieści",
        50:"pięćdziesiąt",
        60:"sześćdziesiąt",
        70:"siedemdziesiąt",
        80:"osiemdziesiąt",
        90:"dziewięćdziesiąt"}
dict_nastki = {
        10: "dziesięć", 
        11:"jedenaście", 
        12:"dwanaście", 
        13:"trzynaście",
        14:"czternaście", 
        15:"piętnaście", 
        16:"szesnaście", 
        17:"siedemnaście",
        18:"osiemnaście", 
        19:"dziewiętnaście"}
dict_setki = {
        100:"sto", 
        200:"dwieście", 
        300:"trzysta", 
        400:"czterysta",
        500:"pięćset", 
        600:"sześćset", 
        700:"siedemset", 
        800:"osiemset",
        900:"dziewięćset"}
setki = (liczba//100) % 10 * 100
dziesiatki = liczba//10 %10 * 10 
jednosci = liczba % 10
print(setki, dziesiatki, jednosci)
wynik = []
str_wynik = ""
if setki>0:
    wynik.append(dict_setki[setki])
if dziesiatki==1:
    wynik.append(dict_nastki[dziesiatki])
else:
    if dziesiatki>0:
        wynik.append(dict_dziesiatki[dziesiatki])
    if jednosci>0:
        wynik.append(dict_jednosci[jednosci])

for x in wynik:
    str_wynik += str(x)
    str_wynik += " "
print(str_wynik)