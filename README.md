#  Open Data Analysis Project

Dieses Projekt zeigt die Verarbeitung, Bereinigung und Visualisierung von CSV-Daten mit Python und pandas.

---

##  Features

- Laden von CSV-Daten (pandas)
- Datenanalyse (Durchschnitt, Maximum)
- Filtern von Daten
- Datenbereinigung (Data Cleaning)
- Erstellung von Diagrammen (Visualisierung)

---

##  Data Cleaning

In diesem Projekt werden typische Probleme realer Datensätze behandelt:

### Erkannte Probleme:

- Fehlende Werte (NaN)
- Doppelte Einträge
- Unsaubere Strings (Leerzeichen)
- Falsche Datentypen

### Lösungen:

- Entfernen oder Ersetzen fehlender Werte
- Entfernen von Duplikaten
- Bereinigung von Strings
- Korrektur von Datentypen

---

##  Verwendete Methoden

```python
df.isnull().sum()        # Fehlende Werte erkennen
df.dropna()              # Zeilen entfernen
df.fillna()              # Werte ersetzen
df.drop_duplicates()     # Duplikate entfernen
df.astype()              # Datentyp ändern
df.str.strip()           # Leerzeichen entfernen
df.plot()                # Diagramm erstellen
plt.show()               # Diagramm anzeigen
```

##  Visualisierung

Die Ergebnisse werden als Diagramme dargestellt:

- Bar Charts für Städtevergleiche  
- Pie Chart für Verteilung
