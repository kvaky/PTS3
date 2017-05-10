# PTS3
Program simuluje jednoduchý turnaj. Na začiatku vložíte tímy a ich skill, potom program simuluje zápasy medzi tímami
zohľadňujúc ich skill.
Program skončí, keď odohral zápas každý s každým.

## Zoznam príkazov:

`stav`
  vypíše dátum a tímy (názov tímu, počet zápasov a body) zoradené zostupne podľa bodov a počtu zápasov.

`next`
  odsimuluje jeden zápas a spustí `stav` 

`cely_turnaj`
  odsimuluje a vypíše všetky zápasy

`help`
  zobrazí nápovedu

## Dizajn

Program komunikuje s užívateľom pomocou knižnice `cmd`. Globálna premenná triedy `State` si pamätá dátum (`date`), tímy
(`teams`) a počet odohraných zápasov (`games`). Každý tím je reprezentovaný objektom triedy `Team`, ktorý v sebe má
názov tímu (`name`), počet bodov (`points`), počet zápasov (`matches`), tímy, s ktorými už hral (`played`) a svoj skill
(`skill`).

Do zápasu sa vyberajú náhodne dva tímy, ktoré proti sebe ešte nehrali. Nech x a y sú skilly tímov A a B v uvedenom
poradí. Pomer pravdepodobností výhier A a B je potom x/y.
