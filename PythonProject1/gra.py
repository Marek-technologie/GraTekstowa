import random

def zapytaj_o_decyzje(pytanie):
    #funkcja pytania tak lub nie
    while True:
        odpowiedz = input(pytanie).lower()
        if odpowiedz == "tak":
            return True
        elif odpowiedz == "nie":
            return False
        else:
            print("Niewłaściwa odpowiedź. Proszę wpisać 'tak' lub 'nie'.")


def graj():
    # definicje zmiennych textowych i liczbowej
    schody = 0
    red = "\033[31m"
    green = "\033[32m"
    reset = "\033[0m"
    text = f"{red}ŚMIERTELNY LABIRYNT{reset}"
    centered_text = text.center(55)
    text2 = "KONIEC".center(50)
    text3 = f"{green}UDAŁO CI SIĘ PRZEŻYĆ{reset}".center(50)
    text4 = ("Gratulację graczu, wygląda na to, że przezwyciężyłeś niebezpieczeństwa labiryntu."
             "\nTeraz możesz odejść w chwale, ze zdobytym bogactwem, wiedząc, że przetrwałeś")


    opcja_pozytywna = ("Pod wpływem adrenaliny podnosisz ze ściany zdobiony topór."
                       "\nW ostatnim momencie udaje ci się zamachnąć toporem w stronę postaci."
                       "\nTrafiasz nieczysto w ramię raniąc ją. Z rany leje się czarna jak smoła krew"
                       "\nPostać odsuwa się w cień i znika. Drzwi w których stała postać zatrzaskują się."
                       "\nMożesz iść już tylko wgłąb labiryntu.")


    opcja_negatywna = ("Nie udaje ci się na czas podnieść topora. Postać rzuca cię mocno na kamienną podłogę."
                       "\nJesteś zdezorientowany, postać klęka przy tobie i dotyka posadzki kościstą ręką."
                       "\nZaczynasz wsiąkać wgłąb kamienia, czujesz, że nie możesz się ruszyć."
                       "\nTwoje ciało zaczyna być zgniatane z ogromną siłą. Czujesz jak łamie ci kości i wygina kończyny."
                       "\nZaczynasz się dusić. Nic już nie widzisz, tracisz przytomność.")


    print(centered_text)
    print("Trafiłeś podczas swojej podróży na ogromny labirynt."
          "\nWygląda on groźnie.")


    if zapytaj_o_decyzje("Czy chcesz wejść do labiryntu? (tak/nie): "):
        print("\nWchodzisz do labiryntu."
              "\nIdziesz ciemnym korytarzem. Zauważasz na ścianie płonącą pochodnię")

    else:
        print("\nZdecydowałeś się nie wchodzić do labiryntu. Odchodzisz w swoją drogę."
              "\nWiedziesz długie i spokojne życie.")
        print(text2)
        return

    if zapytaj_o_decyzje("Czy chcesz zabrać ze sobą pochodnię? (tak/nie): "):
        print("\nZabierasz pochodnię. Idziesz dalej korytarzem.\nDochodzisz do rozległej komnaty."
              "\nZnajduję się w niej biurko, zakurzona szafa na mapy i stare drewniane łóżko. "
              "\nNa ścianie wisi złocony topór."
              "\nObok topora zauważasz kolejne drzwi, zamknięte na kłódkę")

        if zapytaj_o_decyzje("Czy chcesz podnieść topór? (tak/nie): "):
            print("\nPodnosząc ciężki topór straciłeś równowagę."
                  "\nUpadłeś na podłogę razem z toporem, który wbił ci się w pierś."
                  "\nWykrwawiasz się.")
            print(text2)
            return

        else:
            print("\nNie podnosisz topora. Znajdujesz w biurku komnaty dziwny klucz."
                  "\nOtwierasz nim drugie drzwi komnaty i wychodzisz."
                  "\nIdąc dalej korytarzem docierasz do pomieszczenia ze schodami prowadzącymi w dół."
                  "\nSłychać od nich złowrogi ryk.")
        while True:
            if zapytaj_o_decyzje("Czy chcesz zejść po schodach? (tak/nie): "):
                print("\nSchodzisz po schodach, odgłosy stają się coraz głośniejsze. "
                      "\nZ każdym stopniem robi się coraz zimniej."
                      "\nZaskakująco na dole schodów nie słychać już ryków, a powietrze jest lodowate."
                      "\nPrzed tobą rozciągają się ogromne podwójne drzwi."
                      "\nDrewniane ciemnoczerwone, o podobnym odcieniu do krwi, ze złotą głową smoka na środku.")

                if zapytaj_o_decyzje("Czy chcesz otworzyć drzwi i zmierzyć się z nieznanym kryjącym się za nimi? (tak/nie): "):
                    print("\nOtwierasz drzwi i przez nie przechodzisz. Idziesz powoli przed siebię, "
                          "\nprzed tobą rozciąga się ogromna grota."
                          "\nSkłada się z rzędów masywnych, kamiennych kolumn, "
                          "\nwyrzeźbione na nich znaki nie należą do żadnego znanego ci języka."
                          "\nKolumny są symetrycznie rozmieszczone. Całe wnętrze ma ciemny, ziemisty kolor."
                          "\nNa kamiennych powierzchniach widoczne są ślady upływu czasu."
                          "\nNa ziemi widać porozrzucane przedmioty, rozdarte części zbroi i uszkodzoną broń."
                          "\nW głębi, pośrodku korytarza, znajduje się intensywne, złociste źródło światła, "
                          "\nktóre rozświetla wnętrze i rzuca długie cienie na podłogę oraz ściany. "
                          "\nIdziesz w jego stronę. Z każdym krokiem światło staje się coraz mocniejsze."
                          "\nZaczyna cię oślepiać. Dalej kroczysz w stronę światła, czujesz, "
                          "\nże temperatura drastycznie się podnosi."
                          "\nW powietrzu czuć zapach dymu i siarki. Nagle oślepienie ustępuje, "
                          "\nstoisz w ogromnej komnacie wypełnionej złotem i klejnotami."
                          "\nJest ich tak wiele, że nie widzisz końca pomieszczenia. "
                          "\nRozświetlają komnatę, która sprawia wrażenie błyszczeć. "
                          "\nNa przeciw ciebie leży Czarny smok, jego masywne, "
                          "\npotężne ciało jest pokryte twardymi, czarnymi łuskami."
                          "\nPysk pełen ostrych, pożółkłych zębów. Jego oczy świecą intensywną, złowrogą czerwienią."
                          "\nDwa ogromne wygięte rogi wyrastają z tyłu jego głowy. "
                          "\nPazury na jego łapach są długie, zakrzywione i błyszczące,"
                          "\ngotowe do rozrywania wrogów na strzępy. Jego ogon jest smukły i silny, "
                          "\nzakończony ostrymi kolcami."
                          "\nSmok wydaje głębokie, gardłowe pomruki, "
                          "\nktóre rezonują w powietrzu jak odgłos odległego grzmotu. "
                          "\nPatrzy się na ciebie. Emanuje mroczną, złowrogą inteligencją. "
                          "\nW jego spojrzeniu kryje się przebiegłość. "
                          "\nZastygasz w bezruchu, ogarnia cię przerażenie. Smok przemawia do ciebie niskim gardłowym głosem."
                          "\nOznajmia, że zakłuciłeś jego spokój,świadomy swojej potęgi chce dać ci szansę na przeżycie. "
                          "\nMusisz odpowiedzieć na jego trzy pytania.")


                    if zapytaj_o_decyzje("Czy chcesz odpowiedzieć na pytania smoka? (tak/nie): "):
                        print("Zgadzasz się odpowiedzieć na jego pytania. Smok zadaję ci pierwsze pytanie.")
                        pytanie1 = input("\n\"Nie ma skrzydeł, a trzepocze, nie ma ust, a mamrocze, nie ma nóg, "
                                         "\na pląsa, nie ma zębów, a kąsa. Co to jest?\": ").lower()

                        if pytanie1 == "wiatr":
                            print("\"To poprawna odpowiedź. Czas na następne pytanie.\"")
                            pytanie2 = input("\n\"W czerwonej stajni trzydzieści białych koni, kłapie, "
                                             "\ntupie, a czasem ze strachu dzwoni. Co to jest?\": ").lower()

                            if pytanie2 == "zęby":
                                print("\"To poprawna odpowiedź. Czas na ostatnie pytanie.\"")
                                pytanie3 = input("\n\"Coś, przed czym w świecie nic nie uciecze, co gnie żelazo, "
                                                 "\nprzegryza miecze, pożera ptaki, zwierzęta, ziele,"
                                                 "\nnajtwardszy kamień na mąkę miele, królów nie szczędzi, rozwala mury, "
                                                 "\nponiża nawet najwyższe góry. Co to jest?\": ").lower()

                                if pytanie3 == "czas":
                                    print("\"Udało ci się poprawnie odpowiedzieć na wszystkie moje zagadki.\" "
                                          "\nSmok machnął swoim ogonem obok ciebie i otworzył portal prowadzący poza labirynt."
                                          "\n\"W nagrodę możesz otrzymać część mojego skarbu i odejść stąd żywy.\""
                                          "\nSmok podaję ci skrzynię wypełąnioną złotem. Przechodzisz przez portal.")
                                    print(text3)
                                    print(text4)
                                    print(centered_text)

                                else:
                                    print("\"To niepoprawna odpowiedź\"")
                                    print("Smok ociążale podnosi się i szybkim ruchem łapy ćwiartuję cię ostrymi pazurami.")
                                    print(text2)
                                    return

                            else:
                                print("\"To niepoprawna odpowiedź\"")
                                print("Smok ociążale podnosi się i szybkim ruchem łapy ćwiartuję cię ostrymi pazurami.")
                                print(text2)
                                return

                        else:
                            print("\"To niepoprawna odpowiedź\"")
                            print("Smok ociążale podnosi się i szybkim ruchem łapy ćwiartuję cię ostrymi pazurami.")
                            print(text2)
                            return


                    else:
                        print("Nie zgadzasz się odpowiedzieć na jego pytania.")
                        print("Smok ociążale podnosi się i szybkim ruchem łapy ćwiartuję cię ostrymi pazurami.")
                        print(text2)
                        return

                else:
                    print("\nNie otwierasz drzwi, odwracasz się i zmierzasz po schodach w górę. "
                          "\nNagle słyszysz odległy pisk zawiasów ocierających o siebie,"
                          "\nogromne drzwi otworzyły się same. Z dołu schodów zaczynają wylewać się płomienie, "
                          "\nlecą z ogromną prędkością w twoją stronę."
                          "\nNie masz gdzie się schronic. Zaczynasz biec po schodach w przerażeniu. "
                          "\nPłomienie docierają do ciebie paląc cię żywcem."
                          "\nIch temperatura momentalnie zwęgla twoje ciało. "
                          "\nZostaje z ciebie tylko proch.")
                    print(text2)
                    return

            else:
                if schody == 0:
                    print("\nOdwracasz się i uciekasz. Docierasz do drzwi komnaty z których przyszedłeś."
                          "\nWchodząc do komnaty zauważasz podłogę pełną krwi. "
                          "\nW drzwiach naprzeciwko stoi wysoka zakapturzona postać."
                          "\nCzujesz jej przeszywające spojrzenie.")
                    schody += 1

                    if zapytaj_o_decyzje("Postać zaczyna iść w twoją stronę. Czy chcesz podnieść topór ze ściany i ją zaatakować? (tak/nie): "):
                        wybrana_opcja = random.choice([opcja_pozytywna, opcja_negatywna])
                        if wybrana_opcja == opcja_pozytywna:
                            print(f"\n{wybrana_opcja}")
                        else:
                            print(f"\n{wybrana_opcja}")
                            print(text2)
                            return


                    else:
                        print("\nNie atakujesz zakapturzonej postaci. "
                            "\nPodchodzi do ciebie i kładzie ci kościstą rękę na ramieniu."
                            "\nCzujesz nienaturalny chłód, który od niej promieniuje. "
                            "\nPowoli ucieka z ciebie życie. Zamykasz oczy.")
                        print(text2)
                        return
                else:
                    print("\nZmierzasz w stronę schodów docierając do pomieszczenia decydujesz się po nich nie schodzić. "
                          "\nNagle słyszysz odległy pisk zawiasów ocierających o siebie."
                          "\nZ dołu schodów zaczynają wylewać się płomienie, "
                          "\nlecą z ogromną prędkością w twoją stronę."
                          "\nNie masz gdzie się schronic. Zaczynasz uciekać w przerażeniu. "
                          "\nPłomienie docierają do ciebie paląc cię żywcem."
                          "\nIch temperatura momentalnie zwęgla twoje ciało. "
                          "\nZostaje z ciebie tylko proch.")
                    print(text2)
                    return

    else:
        print("\nNie zabierasz pochodni. Idziesz dalej w ciemności."
              "\nPotykasz się o nierówną kamienną podłogę i umierasz od upadku.")
        print(text2)
        return

def main():
    while True:
        graj()
        if not zapytaj_o_decyzje("Czy chcesz zagrać jeszcze raz? (tak/nie): "):
            print("DZIĘKUJĘ ZA GRĘ")
            break  # Jeśli odpowiedź to tak restart gry jeśli nie to kończy program
main()




