import pandas as pd
dfKB = pd.read_csv('../ICON/Dataset/acquacsv.csv')

KNOWLEDGE_BASE = "../ICON/Dataset/potability.pl"
def is_empty(s):
    if s and s.strip():
        return True
    return False

file_data = ""

dfKB['marca'] = dfKB['marca'].astype(str)
dfKB['residuo'] = dfKB['residuo'].astype(str)
dfKB['bicarbonati'] = dfKB['bicarbonati'].astype(str)
dfKB['solfato'] = dfKB['solfato'].astype(str)
dfKB['cloruri'] = dfKB['cloruri'].astype(str)
dfKB['calcio'] = dfKB['calcio'].astype(str)
dfKB['magnesio'] = dfKB['magnesio'].astype(str)
dfKB['fluoruro'] = dfKB['fluoruro'].astype(str)
dfKB['ph'] = dfKB['ph'].astype(str)
dfKB['sodio'] = dfKB['sodio'].astype(str)

# Generating marca - residuo
for row in dfKB.itertuples():
    marca = row[1]
    residuo = row[2]
    string = "marca-residuo(\"" + marca + "\",\"" + residuo + "\")."

    if is_empty(marca) and is_empty(residuo) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"

# Generating marca - bicarbonati
for row in dfKB.itertuples():
    marca = row[1]
    bicarbonati = row[3]
    string = "marca-bicarbonati(\"" + marca + "\",\"" + bicarbonati + "\")."

    if is_empty(marca) and is_empty(bicarbonati) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"

# Generating marca - solfato
for row in dfKB.itertuples():
    marca = row[1]
    solfato = row[4]
    string = "marca-solfato(\"" + marca + "\",\"" + solfato + "\")."

    if is_empty(marca) and is_empty(solfato) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"

# Generating marca - cloruri
for row in dfKB.itertuples():
    marca = row[1]
    cloruri = row[5]
    string = "marca-cloruri(\"" + marca + "\",\"" + cloruri + "\")."

    if is_empty(marca) and is_empty(cloruri) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"

# Generating marca - calcio
for row in dfKB.itertuples():
    marca = row[1]
    calcio = row[6]
    string = "marca-calcio(\"" + marca + "\",\"" + calcio + "\")."

    if is_empty(marca) and is_empty(calcio) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"

# Generating marca - magnesio
for row in dfKB.itertuples():
    marca = row[1]
    magnesio = row[7]
    string = "marca-magnesio(\"" + marca + "\",\"" + magnesio + "\")."

    if is_empty(marca) and is_empty(magnesio) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"

# Generating marca - fluoruro
for row in dfKB.itertuples():
    marca = row[1]
    fluoruro = row[8]
    string = "marca-fluoruro(\"" + marca + "\",\"" + fluoruro + "\")."

    if is_empty(marca) and is_empty(fluoruro) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"

# Generating marca - ph
for row in dfKB.itertuples():
    marca = row[1]
    ph = row[9]
    string = "marca-ph(\"" + marca + "\",\"" + ph + "\")."

    if is_empty(marca) and is_empty(ph) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"

# Generating marca - sodio
for row in dfKB.itertuples():
    marca = row[1]
    sodio = row[10]
    string = "marca-sodio(\"" + marca + "\",\"" + sodio + "\")."

    if is_empty(marca) and is_empty(sodio) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"

# Generating marca - residuo - bicarbonati
for row in dfKB.itertuples():
    marca = row[1]
    residuo = row[2]
    bicarbonati = row[3]
    string = "marca-residuo-bicarbonati(\"" + marca + "\",\"" + residuo + "\",\"" + bicarbonati + "\")."

    if is_empty(marca) and is_empty(residuo) and is_empty(bicarbonati) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"

# Generating marca - residuo - calcio
for row in dfKB.itertuples():
    marca = row[1]
    residuo = row[2]
    calcio = row[6]
    string = "marca-residuo-calcio(\"" + marca + "\",\"" + residuo + "\",\"" + calcio + "\")."

    if is_empty(marca) and is_empty(residuo) and is_empty(calcio) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"

# Generating marca - residuo - magnesio
for row in dfKB.itertuples():
    marca = row[1]
    residuo = row[2]
    magnesio = row[7]
    string = "marca-residuo-magnesio(\"" + marca + "\",\"" + residuo + "\",\"" + magnesio + "\")."

    if is_empty(marca) and is_empty(residuo) and is_empty(magnesio) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"

# Generating marca - residuo - fluoruro
for row in dfKB.itertuples():
    marca = row[1]
    residuo = row[2]
    fluoruro = row[8]
    string = "marca-residuo-fluoruro(\"" + marca + "\",\"" + residuo + "\",\"" + fluoruro + "\")."

    if is_empty(marca) and is_empty(residuo) and is_empty(fluoruro) and (string not in file_data):
        file_data += string + "\n"

file_data += "\n"
        
knowledge_base = open(KNOWLEDGE_BASE, mode="w")
knowledge_base.write(file_data)
knowledge_base.close()
print("\nFile created in: ", KNOWLEDGE_BASE)