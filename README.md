## Projekt 1 - Programiranje za Web
**Opis:** Opis: stranica ZTravel (Zadar Travel) nudi informacije o lokacijama s iznimnim prirodnim ljepotama u široj okolici Zadra. Svaka lokacija ima kratak opis te informacije o cijeni karata (ako se plaća ulaz) i točnoj lokaciji svake.
Korisnici imaju mogućnost registracije i prijave na web stranicu. Nakon registracije korisnici zaprimaju email dobrodošlice. 
Nakon što se korisnici prijave na web stranicu nudi im se mogućnost odabira najdražih lokacija (favorites). Jednom kada korisnik favorite-a lokaciju kraj njenog imena se pojavljuje srce koje označava da je lokacija uspješno dodana u korisnikove omiljene lokacije.

**Autori:**
- Zvonimir Nekić
- Ivor Grego
- Dino Damjanović

**Pokretanje aplikacije:**
```py -m venv venv```

```.\venv\Scripts\activate``` ili ```.\venv\Scripts\Activate.ps1```

```pip install -r requirements.txt```


```flask run```

**Po potrebi**

``` $env:FLASK_DEBUG=1```

``` $env:FLASK_APP="app.py```

**Kako dobiti mail?**

*ZTravel > project > __init__.py* ---> 
app.config['MAIL_DEFAULT_SENDER'] = 'ivor.grego@gmail.com' 
**postaviti vlastiti verificirani sendgrid email koji šalje poštu**

Također je potrebno postaviti odgovarajući SENDGRID_API_KEY u Environment Variables:
[Storing an API key in an environment variable](https://docs.sendgrid.com/ui/account-and-settings/api-keys#storing-an-api-key-in-an-environment-variable)