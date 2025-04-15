import requests

def haal_voertuig_info_op(kenteken):
    basis_url = "https://opendata.rdw.nl/resource/m9d7-ebf2.json"
    parameters = {"kenteken": kenteken.replace("-", "").upper()}
    antwoord = requests.get(basis_url, params=parameters)
    
    if antwoord.status_code == 200:
        gegevens = antwoord.json()
        if gegevens:
            return gegevens[0]
        else:
            return None
    else:
        antwoord.raise_for_status()

ingevoerd_kenteken = input("Voer het kenteken in: ")
voertuig_info = haal_voertuig_info_op(ingevoerd_kenteken)

if voertuig_info:
    print(f"Merk: {voertuig_info.get('merk', 'Onbekend')}")
    print(f"Benaming: {voertuig_info.get('handelsbenaming', 'Onbekend')}")
    print(f"Voertuigsoort: {voertuig_info.get('voertuigsoort', 'Onbekend')}")
    print(f"Eerste toelating: {voertuig_info.get('datum_eerste_toelating', 'Onbekend')}")
    print(f"Aantal cilinders: {voertuig_info.get('aantal_cilinders', 'Onbekend')}")
    print(f"Cilinderinhoud: {voertuig_info.get('cilinderinhoud', 'Onbekend')} cc")
    print(f"Massa voertuig: {voertuig_info.get('massa_ledig_voertuig', 'Onbekend')} kg")
    print(f"Brandstof: {voertuig_info.get('brandstof_omschrijving', 'Onbekend')}")
    print(f"CO₂-uitstoot: {voertuig_info.get('co2_uitstoot_comb', 'Onbekend')} g/km")
else:
    print("Geen gegevens gevonden voor dit kenteken.")
