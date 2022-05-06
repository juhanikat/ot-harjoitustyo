# Dictionary Game

Peli antaa pelaajalle satunnaisesti valitun sanan määritelmän, jonka avulla pelaaja yrittää arvata sanan.
## Dokumentaatio

[Vaatimusmäärittely](https://github.com/juhanikat/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/juhanikat/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/juhanikat/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/juhanikat/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Asennus

Riippuvuudet asennetaan komennolla:
```
poetry install
```
Tmänä jälkeen sovelluksen voi käynnistää komennolla:
```
poetry run invoke start
```

## Testaus

Testit voi suorittaa komennolla:
```
poetry run invoke test
```
ja testikattavuusraportti luodaan komennolla:
```
poetry run invoke coverage-report
```