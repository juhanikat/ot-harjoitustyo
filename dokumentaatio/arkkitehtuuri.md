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
        }
        class Item{

        }
```
Käyttöliittymän päänäkymässä pelaajalle annetaan lista arvattavan sanan määritelmiä, ja pelaaja voi kirjoittaa arvauksensa tekstikenttään.

Esimerkiksi ohjelman toiminta, kun käyttäjä klikkaa "New Word" nappia:
```mermaid
    sequenceDiagram
        User ->> ui: clicks "New Word" button
        UI ->> GameService: new_item()
        UI ->> GameService: get_readable_definitions()
        GameService ->> DictionaryService: get_random_item()
        GameService ->> DictionaryService: get_word()
        GameService -->> UI: definitions
```