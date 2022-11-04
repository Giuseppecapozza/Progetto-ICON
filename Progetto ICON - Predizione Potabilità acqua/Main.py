import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import seaborn as sb
import missingno as msno
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.utils import resample
from sklearn.utils import shuffle

#Lettura dataset
df = pd.read_csv('../ICON/Dataset/water_potability.csv')
print(df.head())
print(f'This DataSet Contains {df.shape[0]} rows & {df.shape[1]} columns.')

#df = df.dropna() 
df = df.drop_duplicates() 

print(df.describe())
print(df.shape)
print(df.info())

y = df['Potability']
X = df.drop(columns=['Potability'],axis=1)

#conteggio valori di acqua potabile e non potabile e visualizzazione grafico
d= pd.DataFrame(df['Potability'].value_counts())
print(d)
print("\n")
plt.figure(figsize=(8,6))
plt.tick_params(axis='x', which='major')
sb.countplot(x='Potability', data=df, palette='pastel')
plt.show()

#visualizzazione del valore minimo/massimo/medio diviso per valore di potabilità
max=pd.DataFrame(df.groupby("Potability")['ph'].max())
print("max")
print(max)
print("\n")
mean=pd.DataFrame(df.groupby("Potability")['ph'].mean())
print("mean")
print(mean)
print("\n")
min=pd.DataFrame(df.groupby("Potability")['ph'].min())
print("min")
print(min)
print("\n")

plt.figure(figsize=(8,6))
plt.tick_params(axis='both', which='major')
o=sb.barplot( x='Potability', y= 'ph',data=df, palette='pastel')
o.set_ylim(7,7.1)
plt.show()

max=pd.DataFrame(df.groupby("Potability")['Hardness'].max())
print("max")
print(max)
print("\n")
mean=pd.DataFrame(df.groupby("Potability")['Hardness'].mean())
print("mean")
print(mean)
print("\n")
min=pd.DataFrame(df.groupby("Potability")['Hardness'].min())
print("min")
print(min)
print("\n")

plt.figure(figsize=(8,6))
plt.tick_params(axis='both', which='major')
o=sb.barplot( x='Potability', y= 'Hardness',data=df, palette='pastel')
o.set_ylim(190,199)
plt.show()

max=pd.DataFrame(df.groupby("Potability")['Solids'].max())
print("max")
print(max)
print("\n")
mean=pd.DataFrame(df.groupby("Potability")['Solids'].mean())
print("mean")
print(mean)
print("\n")
min=pd.DataFrame(df.groupby("Potability")['Solids'].min())
print("min")
print(min)
print("\n")

plt.figure(figsize=(8,6))
plt.tick_params(axis='both', which='major')
o=sb.barplot( x='Potability', y= 'Solids',data=df, palette='pastel')
o.set_ylim(20000,23000)
plt.show()

max=pd.DataFrame(df.groupby("Potability")['Chloramines'].max())
print("max")
print(max)
print("\n")
mean=pd.DataFrame(df.groupby("Potability")['Chloramines'].mean())
print("mean")
print(mean)
print("\n")
min=pd.DataFrame(df.groupby("Potability")['Chloramines'].min())
print("min")
print(min)
print("\n")

plt.figure(figsize=(8,6))
plt.tick_params(axis='both', which='major')
o=sb.barplot( x='Potability', y= 'Chloramines',data=df, palette='pastel')
o.set_ylim(6.5,7.3)
plt.show()

max=pd.DataFrame(df.groupby("Potability")['Sulfate'].max())
print("max")
print(max)
print("\n")
mean=pd.DataFrame(df.groupby("Potability")['Sulfate'].mean())
print("mean")
print(mean)
print("\n")
min=pd.DataFrame(df.groupby("Potability")['Sulfate'].min())
print("min")
print(min)
print("\n")

plt.figure(figsize=(8,6))
plt.tick_params(axis='both', which='major')
o=sb.barplot( x='Potability', y= 'Sulfate',data=df, palette='pastel')
o.set_ylim(325,335)
plt.show()

max=pd.DataFrame(df.groupby("Potability")['Conductivity'].max())
print("max")
print(max)
print("\n")
mean=pd.DataFrame(df.groupby("Potability")['Conductivity'].mean())
print("mean")
print(mean)
print("\n")
min=pd.DataFrame(df.groupby("Potability")['Conductivity'].min())
print("min")
print(min)
print("\n")

plt.figure(figsize=(8,6))
plt.tick_params(axis='both', which='major')
o=sb.barplot( x='Potability', y= 'Conductivity',data=df, palette='pastel')
o.set_ylim(400,470)
plt.show()

max=pd.DataFrame(df.groupby("Potability")['Organic_carbon'].max())
print("max")
print(max)
print("\n")
mean=pd.DataFrame(df.groupby("Potability")['Organic_carbon'].mean())
print("mean")
print(mean)
print("\n")
min=pd.DataFrame(df.groupby("Potability")['Organic_carbon'].min())
print("min")
print(min)
print("\n")

plt.figure(figsize=(8,6))
plt.tick_params(axis='both', which='major')
o=sb.barplot( x='Potability', y= 'Organic_carbon',data=df, palette='pastel')
o.set_ylim(14,15)
plt.show()

max=pd.DataFrame(df.groupby("Potability")['Trihalomethanes'].max())
print("max")
print(max)
print("\n")
mean=pd.DataFrame(df.groupby("Potability")['Trihalomethanes'].mean())
print("mean")
print(mean)
print("\n")
min=pd.DataFrame(df.groupby("Potability")['Trihalomethanes'].min())
print("min")
print(min)
print("\n")

plt.figure(figsize=(8,6))
plt.tick_params(axis='both', which='major')
o=sb.barplot( x='Potability', y= 'Trihalomethanes',data=df, palette='pastel')
o.set_ylim(65,67)
plt.show()

max=pd.DataFrame(df.groupby("Potability")['Turbidity'].max())
print("max")
print(max)
print("\n")
mean=pd.DataFrame(df.groupby("Potability")['Turbidity'].mean())
print("mean")
print(mean)
print("\n")
min=pd.DataFrame(df.groupby("Potability")['Turbidity'].min())
print("min")
print(min)
print("\n")
plt.figure(figsize=(8,6))
plt.tick_params(axis='both', which='major')
o=sb.barplot( x='Potability', y= 'Turbidity',data=df, palette='pastel')
o.set_ylim(3.9,3.97)
plt.show()

#pareggio valori nel dataset essendo non equilibrato
df.Potability.value_counts().plot(kind ='pie')
plt.show()
zero  = df[df['Potability']==0]   
one = df[df['Potability']==1]  

resample = resample(zero, replace = True, n_samples = 1278) 
df = pd.concat([one, resample])
df = shuffle(df) 
df.Potability.value_counts().plot(kind ='pie')
plt.show()
print("\n")
fig = msno.matrix(df,color=(0,0.5,0.5))
plt.show()

#conto tutti i valori mancanti del dataset
print(df.isnull().sum())
print("\n")
#print(df[df['Potability']==0].describe())
#print(df[df['Potability']==1].describe())
print(df[df['Potability']==0][['ph','Sulfate','Trihalomethanes']].median())
print(df[df['Potability']==1][['ph','Sulfate','Trihalomethanes']].median())

#riempio tutti i campi vuoti del dataset
df['ph'].fillna(value=df['ph'].median(),inplace=True)
df['Sulfate'].fillna(value=df['Sulfate'].median(),inplace=True)
df['Trihalomethanes'].fillna(value=df['Trihalomethanes'].median(),inplace=True)
fig = msno.matrix(df,color=(0,0.5,0.5))
plt.show()
print(df.isnull().sum())
print("\n")
#salvo il nuovo csv con le modifiche effettuate
df.to_csv("../ICON/Dataset/Potabilityfinale.csv", index=False)
#heatmap per vedere la correlazione tra le varie caratteristiche
plt.figure(figsize=(10,9))
map =sb.heatmap(df.corr(), annot=True, cmap="YlGnBu",xticklabels=True, yticklabels=True)
map.set_yticklabels(map.get_yticklabels(), rotation=0, fontsize=8)
map.set_xticklabels(map.get_xticklabels(), rotation=45, fontsize=8, rotation_mode='anchor', ha='right')
plt.show()
print("\n")

#train-test split
X = df.drop('Potability',axis=1).values
y = df['Potability'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

#standardizzazione
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

#verifico la profondità ideale per il random forest
accuracy = []
error = []
interval = np.arange(1, 20)
for i in interval:
    clf = RandomForestClassifier(max_depth=i, random_state=10)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    accuracy.append(accuracy_score(y_test, predictions))
    error.append(np.mean(predictions!= y_test))

plt.show()
plt.plot(interval, accuracy, linewidth=4, markersize=10)
plt.grid()
plt.title('Accuracy vs. Random Forest Depth')
plt.xlabel('Depth')
plt.ylabel('Accuracy')
plt.show()
plt.plot(interval,error,linewidth=4, markersize=10)
plt.title('Error Rate Depth Value')
plt.xlabel('Depth Value')
plt.ylabel('Mean Error')
plt.show()

#verifico il valore più appropriato per l’iperparametro K del KNN
scores = []
error = []
for k in interval:
    knn = KNeighborsClassifier(p=k)
    knn.fit(X_train, y_train)
    predictions = knn.predict(X_test)
    scores.append(accuracy_score(y_test,predictions))
    error.append(np.mean(predictions!= y_test))

plt.plot(interval, scores, linewidth=4, markersize=10)
plt.grid()
plt.title('Accuracy vs. KNN')
plt.xlabel("K in K-nearest Neighbors")
plt.ylabel("Cross Validation Test Accuracy")
plt.show()
plt.plot(interval,error,linewidth=4, markersize=10)
plt.title('Error Rate K Value')
plt.xlabel('K Value')
plt.ylabel('Mean Error')
plt.show()

#Creazione modello
model_kn = KNeighborsClassifier(p=2)
#Allenamento
model_kn.fit(X_train, y_train)
#Predizione
pred_kn = model_kn.predict(X_test)
#Calcolo dell'accuratezza
kn = accuracy_score(y_test, pred_kn)
print("Accuracy KNN")
print(kn)
print(classification_report(y_test,pred_kn))
#confusion Maxtrix
cm5 = confusion_matrix(y_test, pred_kn)
sb.heatmap(cm5/np.sum(cm5), annot = True, fmt=  '0.2%', cmap = 'Reds')
plt.show()

#Creazione modello
model_rf = RandomForestClassifier(max_depth=12, random_state=42)
#Allenamento
model_rf.fit(X_train, y_train)
#Predizione
pred_rf = model_rf.predict(X_test)
#Calcolo dell'accuratezza
rf = accuracy_score(y_test, pred_rf)
print("Accuracy Random Forest")
print(rf)
print(classification_report(y_test,pred_rf))

#confusion Maxtrix
cm3 = confusion_matrix(y_test, pred_rf)
sb.heatmap(cm3/np.sum(cm3), annot = True, fmt=  '0.2%', cmap = 'Reds')
plt.show()

#confronto accuratezza tra i due algoritmi
models = pd.DataFrame({
    'Model':[ 'Random Forest', 'KNeighbours'],
    'Accuracy_score' :[ rf, kn]
})
models
sb.barplot(x='Accuracy_score', y='Model', data=models)
models.sort_values(by='Accuracy_score', ascending=False)
plt.show()
