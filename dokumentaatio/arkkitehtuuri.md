# Arkkitehtuuri

## Rakenne

Ohjelman kaikki koodi sijaitsee src-kansiossa. src-kansion sisällä oleva pakkaus services vastaa sovelluslogiikasta ja ui-pakkaus vastaa käyttöliittymästä.

## Käyttöliittymä

Käyttöliittymässä on kaksi näkymää. Ensimmäisenä avautuvassa näkymässä pelaaja voi pelata peliä. Painamalla nappia pääsee toiseen näkymään, jossa pelaaja voi lisätä omia sanojaan ohjelman muistiin.

## Tietojen tallennus

Ohjelma voi tallentaa käyttäjän lisäämiä sanoja. Pelaajan lisäämät sanat tallennetaan kansiossa data sijaitsevaan player_dictionary.xml -tiedostoon. Muita tietoja, kuten pistemääriä, ohjelma ei tallenna.

## Kaavioita

Luokka UI on riippuvainen luokasta GameService, joka taas on riippuvainen luokista DictionaryService ja Item. DictionaryService lukee sanoja "dictionary.xml" nimisestä xml-tiedostosta.


```mermaid
    classDiagram
        GameService --> DictionaryService
        GameService --> Item
        UI --> GameService
        DictionaryService
        class GameService{
            Item current_item
            int points
            int attempts
        }
        class DictionaryService{
            dictionary
            player_dictionary
        }
        class Item{

        }
```
Käyttöliittymän päänäkymässä pelaajalle annetaan lista arvattavan sanan määritelmiä, ja pelaaja voi kirjoittaa arvauksensa tekstikenttään.

Seuraava kaavio kuvaa ohjelman toimintaa, kun käyttäjä klikkaa "New Word" nappia:
```mermaid
    sequenceDiagram
        User ->> UI: clicks "New Word" button
        UI ->> GameService: new_item()
        GameService ->> DictionaryService: get_random_item()
        DictionaryService -->> GameService: item
        UI ->> GameService: get_readable_definitions()
        GameService ->> DictionaryService: get_definitions()
        DictionaryService -->> GameService: definitions
        GameService -->> UI: definitions
        
```
