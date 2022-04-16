# SłowotokBot

Aplikacja pozwala na wyszukiwanie słów, które można znaleźć w popularnej grze słownej Słowotok.
Program nie został stworzony po to, aby zachęcać kogokolwiek do oszukiwania, a po to, aby przetrenować swoje umiejętności w pisaniu aplikacji w django oraz w ramach pewnej ciekawostki.

Funkcje:
 - zapisywanie zapytań użytkowników
 - panel logowania i rejestracji
 - ograniczanie liczby zapytań dla niezalogowanych użytkowników
 - generowanie kodu, który po wklejeniu do konsoli na Słowotoku doda wszystkie prawidłowe słowa
 - generowanie przykładowych liter, które można użyć do zapytania. Litery są generowane zgodnie z wagami, które odpowiadają częstości występowania liter w języku polskim


Słownik który został użyty to znajdywania słów zawiera wszystkie indeksy ze [Słownika Języka Polskiego](https://sjp.pwn.pl/lista/).
Skrypt, który pozwolił zebrać te dane znajduje się w [tym repozytorium](https://github.com/Arkenin/SJP_downloader/).
Niestety nie są to wszystkie słowa, które są wykorzystywane przez Słowotok. 

## Wymagania

Aby uruchomić aplikację należy użyć Dockera wraz z pakietem docker-compose.
Moduły, które są wykorzystywane przez python wylistowane są w pliku requirements.txt

## Uruchamianie
1. Sklonuj repozytorium

```sh
clone https://github.com/Arkenin/SlowotokBot.git
```

2. Skopiuj plik .env.sample z nazwą .env i dokonaj korekcji ustawień:
```sh
cd SlowotokBot
mv .env.sample .env
vi .env
# ustawienie sekretnego klucza django i zaufanych domen
```

3. Zbuduj i uruchom kontenery:
```sh
docker-compose build
docker-compose up
```

Możesz dodać administratora wpisując:
```sh
docker-compose exec web python manage.py createsuperuser
```
## Prezentacja

![Image](/static/github/1.png)
![Image](/static/github/2.png)
![Image](/static/github/3.png)
![Image](/static/github/4.png)
![Image](/static/github/5.png)

