import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("../ICON/Dataset/Potabilityfinale.csv")
X = df.drop('Potability',axis=1).values
y = df['Potability'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

print('enter values')
ph = input("Enter ph value: ")

Hardness = input("Enter hardness value: ")

Solids = input("Enter solids value: ")

Chloramines = input("Enter chloramines value: ")

Sulfate = input("Enter sulfate value: ")

Conductivity = input("Enter conductivity value: ")

Organic_carbon = input("Enter organic carbon value: ")

Trihalomethanes = input("Enter trihalmethanes value: ")

Turbidity = input("Enter trurbidity value: ")

c = np.array([ph,Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity]).reshape(1,9)

forest = RandomForestClassifier(max_depth=12, random_state=42)
forest.fit(X_train, y_train)
forest_pred = forest.predict(c)
if forest_pred == 1:
    print("Potabile")
elif forest_pred == 0:
    print("Non potabile")

