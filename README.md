# Praktinės informatikos Python užduotys

aut.: **Ugnius Teišerskis**

Programų sistemų studijų programos 1 kurso 1 grupės 2 pogrupio studentas

## 07 užduotis

Sukurta programa, randanti pirminius skaičius vartotojo pateiktame intervale. Programa veikia tik su sveikaisiais teigiamais skaičiais.

### Programos funkcionalumas

- [X] Vartotojo įvesties surinkimas
- [X] Vartotojo įvesties patikrinimas
- [X] Pirminių skaičių paieška
- [ ] Efektyvus pirminių skaičių algoritmas

### Programos paleidimas

Programa gali būti paleidžiama nuėjus į programos katalogą su terminalu:

```
$ cd 07-uzduotis
$ python3 pirminiai-skaiciai.py
```

Asmeniniame kompiuteryje su įdiegtu Python interpretatoriumi:

```
$ cd 07-uzduotis
$ python pirminiai-skaiciai.py
```

## 07B užduotis (papildoma)

Sukurta programa, kuri suprastina vartotojo įvestą šaknies išraišką.

### Programos funkcionalumas

- [X] Vartotojo įvesties surinkimas
- [X] Vartotojo įvesties patikrinimas
- [X] Šaknies išraiškos prastinimas
- [ ] Efektyvus šaknies prastinimo algoritmas

### Programos įvesties skaičių rėžiai

Programa buvo parašyta priskiriant minimalius bei maksimalius įvesties skaičių rėžius atitinkamai *-10000* ir *10000*, siekiant apsaugoti programą nuo nenuspėjamų veiksmų ar per ilgo skaičiavimo laiko. Šiuos rėžius galima koreguoti kodo viršuje pakeičiant **SKAICIUS_MIN** bei **SKAICIUS_MAX** reikšmes.

## 08 užduotis

Sukurta programa, kuri išanalizuoja Donelaičio "Metai" kūrinio sandarą.

### Programos funkcionalumas

- [X] Atrandamas ilgiausias žodis
- [X] Randamas žodžių skaičius
- [X] Apskaičiuojamas kiekvieno žodžio pasikartojimo dažnis
- [X] Žodžiai surikiuojami pagal dažnį

### Programos paleidimas

Jog programa veiktų, visų pirma, į jos katalogą reikia įkelti tekstinį failą pavadinimu "Metai.txt", kuriame yra atitinkamas kūrinys. Programa gali būti paleidžiama nuėjus į programos katalogą su terminalu:

```
$ cd 08-uzduotis
$ python3 metai.py
```

## 08B užduotis (papildoma)

Sukurta programa, kuri atranda duomenų bazėje slaptažodį, kuris sutampa su programos kode įvestu užkodavimu.

### Programos funkcionalumas

- [X] Išveda rastą slaptažodį
- [X] Išveda, kiek laiko užtruko jį surasti
- [X] Išveda, kiek patikrina slaptažodžių per sekundę
- [X] Išveda, kiek laiko užtruktų su esama įranga nulaužti stiprų 8 simbolių ilgio slaptažodį.

### Programos paleidimas

Jog programa veiktų, visų pirma, į jos katalogą reikia įkelti tekstinį failą pavadinimu "rockyou.txt", jei jo dar ten nėra. Šiame tekstiniame faile yra galimų slaptažodžių variantai. Programa gali būti paleidžiama nuėjus į programos katalogą su terminalu:

```
$ cd 08B-uzduotis
$ python3 slaptazodziai.py
```

## 09 užduotis

Sukurta programa, kuri atidaro failą pavadinimu "transistor-counts.csv", pagal failę esančius duomenis sukuria grafiką, kuriame matosi pagamintų tranzistorių pagaminimo kiekio kaita ir išsaugo šį grafiką trejais formatais: .pdf, .png ir .svg.

### Programos funkcionalumas

- [X] Sukuria grafiką
- [X] Išsaugo grafiką į diską

### Programos paleidimas

Jog programa veiktų, visų pirma, į jos katalogą reikia įkelti tekstinį failą pavadinimu "transistor-counts.csv", jei jo dar ten nėra.Programa gali būti paleidžiama nuėjus į programos katalogą su terminalu:

```
$ cd 09-uzduotis
$ python3 moores_law.py
```