#challangezwembad

# --- stap 1:

lengtezwembad1 = float(input("Wat is de lengte in meters? "))
breedtezwembad1 = float(input("Wat is de breedte in meters? "))
dieptezwembad1 = float(input("Wat is de diepte in meters? "))

uitgravenperm3 = 25
afvoerperm3 = 32.50

TotaalGrondAfgevoerdZwembad1 = lengtezwembad1 * breedtezwembad1 * dieptezwembad1
# print(f"{TotaalGrondAfgevoerdZwembad1} m3 grond in totaal. ")

# --- stap 2: 

uitgraafkosten = uitgravenperm3 * TotaalGrondAfgevoerdZwembad1
afvoerkosten = afvoerperm3 * TotaalGrondAfgevoerdZwembad1
# totaal = uitgraafkosten + afvoerkosten

# print(f"Offerte voor een zwembad van 8 bij 3 bij 1.5 meter (inhoud: {TotaalGrondAfgevoerdZwembad1} m3)")
# print(f"Uitgraven:          € {uitgraafkosten}")
# print(f"Afvoeren grond:     € {afvoerkosten} ")
# print(f"Totaal:             € {totaal} ")

# --- stap 3:

vasteprijsklein = 100
vasteprijsgroot = 250

voorrijkostafstand = float(input("Hoeveel KM moet het worden voor gereden? "))

if voorrijkostafstand < 50 and TotaalGrondAfgevoerdZwembad1 < 20:
    voorijkosten = vasteprijsklein + voorrijkostafstand * 1.25 
elif voorrijkostafstand >= 50 and TotaalGrondAfgevoerdZwembad1 < 20:
    voorijkosten = vasteprijsklein + TotaalGrondAfgevoerdZwembad1 * 1.15
elif voorrijkostafstand < 50 and TotaalGrondAfgevoerdZwembad1 >= 20:
    voorijkosten = vasteprijsgroot * 2.15
elif voorrijkostafstand >= 50 and TotaalGrondAfgevoerdZwembad1 >= 20:
    voorijkosten = vasteprijsgroot * 2.05

# totaal = uitgraafkosten + afvoerkosten + voorijkosten

# print("")
# print(f"Offerte voor een zwembad van 8 bij 3 bij 1.5 meter (inhoud: {TotaalGrondAfgevoerdZwembad1} m3)")
# print(f"Uitgraven:          € {uitgraafkosten}")
# print(f"Afvoeren grond:     € {afvoerkosten} ")
# print(f"Voorrijkosten:      € {voorijkosten} ")
# print(f"Totaal:             € {totaal} ")

# --- stap 4:

# input in stap 1 ^^ 

# --- stap 5a:

m2 = lengtezwembad1 * breedtezwembad1 # bodem
m22 = lengtezwembad1 * dieptezwembad1 # lang muur 
m222 = dieptezwembad1 * dieptezwembad1 # korte muur
totaalm2 = m2 + m22 * 2 + m222 * 2

prijsperm2klein = 250
prijsperm2groot = 200
meerprijsroodklein = 25
meerprijsroodgroot = 20
meerprijskleurklein = 100
meerprijskleurgroot = 125

print(f"Uw zwembad is {totaalm2} vierkante meter. ")
kleur = input("Wilt u rood of kleuren tegels? (antwoord met rood/ kleur) ")

if TotaalGrondAfgevoerdZwembad1 < 20 and kleur == "rood": 
    prijs1 = totaalm2 * prijsperm2klein
    rood = totaalm2 * meerprijsroodklein
    totaaltegels = prijs1 + rood
elif TotaalGrondAfgevoerdZwembad1 >= 20 and kleur == "rood": 
    prijs1 = totaalm2 * prijsperm2groot
    rood = totaalm2 * meerprijsroodgroot
    totaaltegels = prijs1 + rood
elif TotaalGrondAfgevoerdZwembad1 < 20 and kleur == "kleur":
    prijs1 = totaalm2 * prijsperm2klein
    kleurbedrag = totaalm2 * meerprijskleurklein
    totaaltegels = prijs1 + kleurbedrag
elif TotaalGrondAfgevoerdZwembad1 >= 20 and kleur == "kleur":
    prijs1 = totaalm2 * prijsperm2groot
    kleurbedrag = totaalm2 * meerprijskleurgroot 
    totaaltegels = prijs1 * kleurbedrag

# --- stap 5b 

totaal = uitgraafkosten + afvoerkosten + voorijkosten + totaaltegels

print("")
print(f"Offerte voor een zwembad van 8 bij 3 bij 1.5 meter (inhoud: {round(TotaalGrondAfgevoerdZwembad1, 2)} m3)")
print(f"Uitgraven:                          € {round(uitgraafkosten, 2)}")
print(f"Afvoeren grond:                     € {round(afvoerkosten, 2)} ")
print(f"Voorrijkosten:                      € {round(voorijkosten, 2)} ")
print(f"Beton + tegels, {round(totaalm2, 2)} m2:            € {round(totaaltegels,2)} ")
print(f"Totaal:                             € {round(totaal, 2)} ")
