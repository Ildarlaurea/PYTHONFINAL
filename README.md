
# **Interaktiivinen tekstipohjainen sovellus**

## **Sovelluksen kuvaus**
Tämä projekti on kurssilla opittuja taitoja hyödyntävä interaktiivinen tekstipohjainen sovellus, jossa pelaajat voivat osallistua klassisen Blackjack-korttipelin simulointiin. Sovellus tarjoaa pelikokemuksen suoraan terminaalissa tai IDE:ssä ilman graafista käyttöliittymää. Pelaajien tavoitteena on saada käsi mahdollisimman lähelle arvoa 21 ilman, että sen arvo ylittää sen, samalla kilpailtaessa virtuaalista jakajaa vastaan.

Sovellus sisältää keskeiset Blackjack-pelin ominaisuudet, kuten:
- Korttipakan luominen ja sekoittaminen.
- Pelaajan ja jakajan korttien hallinta.
- Panostusjärjestelmä, jossa pelaaja aloittaa ennalta määrätyillä pelimerkeillä.
- Reaaliaikaiset peliohjeet ja tulosten laskenta.

## **Toteutustapa**
Sovellus on toteutettu Pythonilla, ja siinä hyödynnetään kurssilla opittuja ohjelmointikäsitteitä, kuten:
- **Olio-ohjelmointi:** Kortit, korttipakka ja pelaajien kädet mallinnetaan luokilla.
- **Ehtolauseet ja silmukat:** Pelin logiikka ja tapahtumien kulku toteutetaan näillä rakenteilla.
- **Satunnaisuus:** Korttipakan sekoittaminen käyttää Pythonin `random`-kirjastoa.

Sovellus on suunniteltu toimimaan suoraan terminaalissa tai IDE:ssä ilman ylimääräisiä kirjastoasennuksia.

## **Ohjeet ohjelman käynnistämiseen**
1. **Lataa koodi:** Lataa sovelluksen lähdekoodi GitHub-repositorysta paikalliselle koneellesi.
2. **Asenna Python:** Varmista, että Python 3 on asennettu koneellesi. Voit tarkistaa version komennolla:
   ```bash
   python --version
   ```
3. **Suorita ohjelma:** Avaa koodi tekstieditorilla tai IDE:llä (esim. Visual Studio Code, PyCharm) ja suorita se komennolla:
   ```bash
   python blackjack.py
   ```
4. **Seuraa ohjeita:** Sovellus tarjoaa pelaajalle ohjeet korttien nostamiseen, panostamiseen ja pelin etenemiseen.

## **Minun tavoitteet**
- Luoda käyttäjäystävällinen, yksinkertainen ja toimiva tekstipohjainen sovellus.
- Hyödyntää kurssilla opittuja taitoja ja harjoitella ohjelmointia.
- Saada sovellus toimimaan luotettavasti eri ympäristöissä.

## **Vaatimukset**
- Python 3.6 tai uudempi.

