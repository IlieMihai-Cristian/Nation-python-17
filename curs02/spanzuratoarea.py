cuvant = 'OnomatopEe'.lower() # conversie la litera mica
cuvant_de_ghicit = list(cuvant)
for index, valoare in enumerate(cuvant):  # parcurgem fiecare caracter prin index si valoare
    if valoare != cuvant[0] and valoare != cuvant[-1]: # verificam daca i(caracterul parcurs) este egal cu primul sau ultimul caracter
        cuvant_de_ghicit[index] = '_' # inlocuim cu _ caractere neghicite
cuvant_de_ghicit = ''.join(cuvant_de_ghicit) # afisam pe ecran stringul de inlocuit
nr_total_vieti = 7
litere_incercate = set()  # aici stocam literele unice
while nr_total_vieti >= 1: # atata timp cat nu am ramas fara vieti
    print(cuvant_de_ghicit)
    litera = input("Alege o litera: ").lower() # il lasam pe utilizator sa aleaga o litera

    cuvant_de_ghicit = list(cuvant_de_ghicit)
    if litera in cuvant:
        for index, valoare in enumerate(cuvant):
            if litera == valoare:
                cuvant_de_ghicit[index] = litera
        cuvant_de_ghicit = ''.join(cuvant_de_ghicit)
        if '_' not in cuvant_de_ghicit:
            print('Ai castigat!')
            print(f"Cuvantul era: {cuvant_de_ghicit}")
            break
    elif litera not in cuvant:
        if litera in litere_incercate or not litera.isalpha() or len(
                litera) > 1:
            nr_total_vieti -= 1
            print(f'Mai ai {nr_total_vieti} incercari')
        litere_incercate.add(litera)
        if litera in litere_incercate or not litera.isalpha() or len(
                litera) > 1:  # verificam daca litera a mai fost incercata si nu este cifra sau simbol si utilizatorul introduce mai mult de un caracter
            print(f"Literele incercate sunt {','.join(litere_incercate)}")
            cuvant_de_ghicit = ''.join(cuvant_de_ghicit)


            continue

    # print(cuvant_de_ghicit)

