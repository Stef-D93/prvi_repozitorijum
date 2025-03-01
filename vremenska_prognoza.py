temperatura = int(input("Unesite temperaturu: "))
test_temperatura = -1
temperatura = test_temperatura
poruka = ""
if temperatura <0:
    poruka = "Oprez, klizavo!"
if temperatura > 0:
    poruka = "Temperatura iznad 0"
    if temperatura >30:
        poruka = "Ukljucite klima uredjaje"

#testiranje iznad navedenog koda - case <0 
# NAPOMENA: test se piše izvan ovog fajla. Ovo je čisto za primjer.
ocekivana_poruka = "Oprez, klizavo!"
if ocekivana_poruka == poruka:
    print("Case ispod nule - test prošao")