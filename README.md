# Progetto ICON - Predizione potabilità acqua

## Indice

1. [Introduzione](#1-introduzione)
2. [Struttura Progetto](#2-struttura-progetto)
3. [Requisiti Per Eseguire Il Progetto](#3-requisiti-per-eseguire-il-progetto)
4. [Sviluppi Futuri](#4-sviluppi-futuri)

## 1. Introduzione

Il progetto  è stato creato per sostenere l'esame di Ingegneria della conoscenza da:  
- Capozza Giuseppe - Matricola: 708803  

Il progetto ha come fine quello di capire cosa costituisce un'acqua potabile e sicura basandosi su un dataset con all'interno informazioni riguardo diverse sostanze chimiche presenti nell'acqua e successivamente applicare l'apprendimento automatico ad essa per distinguere, secondo i valori inseriti dall'utente, tra acqua potabile e non potabile.  
Inoltre sarà possibile all'utente ricevere consigli su quale tipo di acqua bere in base all'età o a determinati sintomi/condizioni fisiche che si hanno.

## 2. Struttura Progetto

Nella cartella del progetto "Progetto ICON - Predizione Potabilità acqua" sono presenti due cartelle:
  - **Dataset** -> Qui troviamo tutti i vari dataset utilizzati nel progetto:  
    - ***water_potability.csv*** -> dataset principale utilizzato nelle analisi  
    - ***acquacsv.csv*** -> dataset creato da me stesso per la creazione della KB  
    - ***Potabilityfinale.csv*** -> dataset principale equilibrato, senza valori nulli e senza doppioni  
    - ***potability.pl*** -> base di conoscenza creata a aprtire dal dataset  
  - **Presentazione** -> Qui troviamo due file:  
    - ***Water prediction documentazione.pdf*** -> documentazione del progetto  
    - ***Water presentazione.pptx*** -> power point utile alla presentazione del progetto  
  - **Immagini** -> In questa cartella sono contenute le immagini presenti nella documentazione  
  
All'interno della cartella principale stessa invece sono presenti i file .py che contengono il codice del progetto, nel dettaglio:  
  - ***Main.py*** -> File sorgente utilizzato per le analisi sul dataset  
  - ***Predizione.py*** -> File sorgente utilizzato per eseguire le predizioni sulla potabilità dell'acqua  
  - ***Create KB.py*** -> File sorgente utilizzato per costruire la KB  
  - ***Use KB.py*** -> File sorgente utilizzato per interfacciarsi con la KB  

## 3. Requisiti Per Eseguire Il Progetto

Per eseguire il progetto è necessario installare i seguenti programmi:

- `Python 3.10.8`
- `SWI-Prolog 8.2.4`
- IDE utilizzato : `VSCode`
- Moduli necessari :  
                     - `numpy`  
                     - `pandas`  
                     - `pyswip`  
                     - `scikit-learn`  
                     - `matplotlib`  
                     - `seaborn`  
                     - `missingno`  

## 4. Sviluppi Futuri

Uno dei possibili sviluppi futuri è quello di ampliare il dataset in modo tale da avere più scelte a disposizione per ogni richiesta di eventuali clienti o anche ampliare i sintomi che i tipi diversi di acqua mirano a curare/prevenire.  
Oltre questo potrebbe essere opportuno sviluppare un’interfaccia software in modo tale da rendere l’esperienza utente decisamente più apprezzabile ed usufruibile dopodiché far eseguire questo software su dei dispositivi, come ad esempio tablet, che verranno collocati all’interno di supermercati cosicché i clienti possano utilizzarli per cercare i tipi di acqua a loro utili sulla base delle marche presenti all’interno del supermercato.
