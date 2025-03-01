temperatura = int(input("Unesite temperaturu: "))
test_temperatura = -1
test_temperatura = 35
temperatura = test_temperatura
poruka = ""
if temperatura <0:
    poruka = "Oprez, klizavo!"

if temperatura > 0:
    poruka = "Temperatura iznad 0"
    if temperatura >30:
        poruka = "Ukljucite klima uredjaje"


ocekivana_poruka = "Oprez, klizavo!"
if ocekivana_poruka == poruka:
    print("Case ispod nule - test prošao")