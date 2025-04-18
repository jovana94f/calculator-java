# Izveštaj o statičkoj analizi koda

## LOC metrike
- **Start.java**: 19 linija
- **Calculator.java**: 129 linija
- **Ukupno**: 148 linija

## Zapažanja
### Start.java
- Linija 9: Scanner `scanIn` se kreira unutar petlje, što može dovesti do nepotrebnog trošenja resursa. Preporučuje se kreiranje skenera van petlje.
- Linija 15: `scanIn.close()` se poziva unutar uslova, ali može biti problematično ako se petlja prekine na drugi način.

### Calculator.java
- Linija 12: Klasa `Operations` ima privatni konstruktor, ali nije jasno zašto je to potrebno jer se koristi samo za definisanje konstanti.
- Linija 32: Metoda `Run` samo poziva `evaluateExpression`. Može se razmotriti spajanje ove dve metode radi pojednostavljenja.
- Linija 47: Nema provere za prazne izraze. Ako korisnik unese prazan string, može doći do greške.
- Linija 66: Korišćenje `try-catch` bloka za parsiranje brojeva je u redu, ali povratna vrednost "ERROR" nije dovoljno deskriptivna.
- Linija 94: Rekurzivna metoda `Calculate` može izazvati StackOverflowError za veoma velike izraze. Preporučuje se iterativni pristup.
- Linija 123: Operacije množenja i deljenja imaju prioritet, ali kod za rukovanje ovim operacijama je previše složen i može se optimizovati.

## Preporuke
- Refaktorisati kod kako bi se smanjila složenost metoda.
- Dodati validaciju ulaznih podataka.
- Razmotriti upotrebu alata za statičku analizu poput Checkstyle ili SonarQube za dodatne uvide.