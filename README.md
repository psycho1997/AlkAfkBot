# AlkAfkBot
## Installation
### Vorraussetzungen:
- Python 3.7.4
- py-ts3

### Installation
- installiere Python für dein System
- installiere py-ts3 über pip3: ``` pip3 install "ts3>=2.0.0b2" --upgrade ```
- Fals der Bot nicht auf dem Selben Server wie der TS-Server läuft füge die IP des Bots zur query_ip_whitelist.txt in der Config des TS-Servers hinzu
- Lege Querry-Login Daten für den Bot an
    - In TS auf dem Server auf Extras klicken "ServerQuerry Login drücken"
    - Logindaten in preferences.json in den dafür bereitgestellten Feldern speichern
- Restliche Parameter wie unten beschrieben ausfüllen und programm starten 
    - in cmd/ terminal ```python3 ts3bot.py``` 

##Parameter
Grundlegend: alle Strings (also Wörter bestehend aus Buchstaben) müssen mit Anführungzeichen ("/') versehen werden, sont funktioniert nichts
- LoginName: Login Name der ServerQuerry
- Password: Passwort der ServerQuerry
- threshHold: Anzahl der Minuten, nachdem ein inaktiver User gemoved wird
- delay: Gibt in Sekunden an, wie lange der wartet, bis er die Liste der Clients prüft (weniger = schneller aber auch Resourcenhungriger)
- whitelistedgroups: Gruppen, die nicht gemoved werden 
- afkchannels: Afkräume, in denen nicht gemoved wird (effektiv whitelist)
- moveTo: Raum in dem die gemovedten Clients landen
- pokeAfterMove: Soll eine nachricht nach dem Moven per Anstupsen versendet werden? true/false
- moveMsg: Poke-Nachricht
- nickName: Name des Bots (Erscheint beim Poken und in der Clientliste)
}