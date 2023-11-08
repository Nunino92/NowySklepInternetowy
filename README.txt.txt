Sklep Internetowy - Polega na zarejestrowaniu uzytkownika, przejrzeniu ofert.

Wykorzystywany jest głownie Django. 
Posiada 5 osoby pakietów, które ze soba wspólpracują. Dodatkowo w kazdym z pakietów znajduje sie folder na templates.
Wszystkie biblioteki znajdują sie w pliku requirements.txt.
Dodatkowo znaduje się dodatkowy plik ToDo.txt, w ktory jest zawarta informacja co jeszzce trzeba dodać w przyszloci, czyli jak zostanie rozbudowany
Wejsc na strone mozna przez http://127.0.0.1:8000/ w momencie uruchomienia manage.py
Projekt posiada 5 foldery:
1. glowne konto - sa tam najwazniejszy kod do funkcjonowania projektu jak glowna strona, update danych czy hasła
2. konto - pakiet odpowiadajacy za odzyskiwanie hasla po przez emaila
3. media - obrazy do sprzedawanych przedmiotow.
4. panel - jest to panel, w ktorym wyswietlane sa informacje o posiadanych przedmiotach
5. przedmioty - drugi najbardziej rozbudowany pakiet. Zawiera informacje o przedmiotach, dodawanie itp.
6. sklep - folder, w ktorym znajduja sie najwazniejsze urls oraz settings

W aplikacji mozemy się rejestrowac, logować, zmieniac dane, dodawac rozne przedmioty, odzyskiwać hasło. 
Kategorie można dodawać jedynie przez panel admina. Jest to umyslne działanie, by nie pojawiło sie za duzo kategori.
