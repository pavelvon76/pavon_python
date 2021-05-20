# dictionary
adresar = dict()
print(adresar)

# hodnota dict je list
adresar["Petr Novák"]= list()
print(adresar)

zaznam = adresar.get("Petr Novák",0)
zaznam.append("+420 123 456 789")
print(adresar)

#vypis petrova cisla
print(adresar.get("Petr Novák",0))

#pridejte dalsi cislo
adresar.get("Petr Novák",0).append("+66666666")

#posledni petrovo cislo
print(adresar)
print(adresar.get("Petr Novák",0)[-1]) # adresa obsahuje list

#existuje Miro? v seznamu
print(adresar.get("Miro",0))
print(adresar.get("Petr Novák",0))

# počet záznamů
print(len(adresar.keys()))

# vypište jména osob
print(adresar.keys())

# pridame Zbira
adresar["Miro Zbiro"]= list()
adresar.get("Miro Zbiro",0).append("+45674576")
print(adresar.keys())