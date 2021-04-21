# Guidelines pro psaní dokumentace

## Jak zadávat základní informace

Help, jak si rychle ukázat, co jaká značka v MD dělá je  [Tady](https://markdown-it.github.io/)

- blok textu max. 5-6 řádků, více ne
používat odrážky. Jinak se v tom nikdo nevyzná.
- Názvy polí a objektů (stránek, reportů) a funkcí tučně. Př.: Zadejte **Počet stránek** k tisku na záložce **Obecné** v reportu **Potvrzení prodejí objednávky**.
- používat notes
- 2 úrovně: nadpis celé stránky (vlevo ve stromu), nižší úroveň v pravém stromu navigace na stránce 
- nadpisy nižších úrovní ne moc dlouhé (jsou pak těžko čitelné v pravém navigačním stromu)
- v případě, že chcete, aby uživatel vyhledal page/akci/report (atd.), používetje slovní spojení ve stylu: Vyberte ikonu :mag_right:, zadejte **...** a poté vyberte související odkaz.
- pro termín "fasttab" budeme jako český překlad používat slovo "záložka"

> :warning: **NEPOUŽÍVEJTE Italic** font, je v tom textu přehlédnutelný a nečitelný. Raději používejte **BOLD**, maximálně ***BOLD ITALIC***

## Postup v krocích
Pokud dojde na postup v krocích, tak postupujte takto:
1. Začátky číslovaného odskoku číslujte klidně jen pomocí 1. znaku
1. Pokud dojde na podúroveň, tedy jako, třeba, že v tomto kroku proveďte ještě
    - krok A
    - pak krok B

    Jednoduše zanořte minusy do nižší úrovně
1. V klidu pak zase pokračujte dalším krokem.
1. That's IT! 

## Další vychytávky
### Zobrazení dat v tabulce

| Pole | Popis |
| ---- | ----- |
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |

### Zarovnání čísel v tabulce doprava

| Parametr | Hodnota |
| -------- | -------:|
| odhad   | 153,34 |
| realizace | 3487,65|
| test| 157,77 |

### Zarovnání čísel v tabulce Doprostřed

| Parametr | Hodnota |
|:--------:|:-------:|
| odhad   | 153,34 |
| realizace | 3487,65|
| test| 157,77 |

### Odkazy na další zdroje

[link text](http://dev.nodeca.com)

### Obrázky 
Obrázky ksou spefické tím, že je máte všechny v jedné složce s názvem **Media**

![Text pro zobrazení v případě problémů s obr.](/media/essencelogo.png "Obrázek ukazuje Logo společnosti Essence")


### warning a poznámky
> :warning: It works with almost all markdown flavours (the below blank line matters).

Alternativy oproti :warning: warningu:
- :heavy_check_mark: když se něco fakt daří
- :x: když někdo něco fakt nemá dělat 

### kdo by musel čáru, tak ...
---

## Best practice
- pokud něco nejde vidět a je na konci řídící znak, přidej mezeru
- přidel prázdnou řádku Enterem za odstavci, na webu to vypadá líp
- pokud má tabulka 1 řádek, nepřidávej nakonec ---
- ta mezera je fakt super nápad, i ten novej řádek
- snažte se ctít typografická pravidla
- ten náhled vpravo od toho, co píšete není vždycky to, jak to vypadá na webu. Používej často **docfx build --serve** v terminálovém okně, aby jsi se naučil si to zobrazovat na webové stránce.

