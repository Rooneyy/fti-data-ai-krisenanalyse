# Datenbereinigung – Dokumentation

## Ziel

Ziel der Datenbereinigung war es, aus simulierten Rohdaten saubere und analysierbare Datensätze für eine Krisenanalyse zu erstellen.

## Eingabedaten

Die Rohdaten lagen im Ordner `data/raw/`:

- `umsaetze.csv`
- `kosten.csv`
- `forderungen.csv`
- `verbindlichkeiten.csv`
- `lagerbestand.csv`

## Gefundene Datenqualitätsprobleme

Folgende Probleme wurden identifiziert:

- doppelte Einträge in Umsätzen, Kosten und Forderungen
- fehlende Werte in einzelnen Spalten
- gemischte Datumsformate
- inkonsistente Kundennamen
- unrealistische Ausreißer bei Kosten und Forderungen

## Bereinigungsschritte

### 1. Duplikate entfernen

Doppelte Zeilen wurden mit `drop_duplicates()` entfernt.

### 2. Fehlende Werte behandeln

Fehlende Werte wurden nicht pauschal gelöscht, sondern abhängig von der jeweiligen Spalte behandelt:

- fehlender Kunde: ersetzt durch `Unbekannt`
- fehlender Einzelpreis: berechnet aus `gesamtbetrag / menge`
- fehlende Kostenart: ersetzt durch `Unbekannt`
- fehlendes Fälligkeitsdatum: geschätzt als `rechnungsdatum + 30 Tage`
- fehlender Lagerwert: ersetzt durch den Median der jeweiligen Produktgruppe

### 3. Datumsformate vereinheitlichen

Gemischte Datumsformate wie `2024-03-15` und `15.03.2024` wurden in ein einheitliches Datumsformat umgewandelt.

### 4. Kundennamen standardisieren

Inkonsistente Kundennamen wurden vereinheitlicht:

- `Mueller GmbH` → `Müller GmbH`
- `Fa. Müller` → `Müller GmbH`

### 5. Ausreißer markieren

Unrealistische Beträge wurden nicht gelöscht, sondern mit einer zusätzlichen Spalte `ist_ausreisser` markiert.

Schwellenwerte im Lernprojekt:

- Kosten > 200.000 €
- Forderungen > 300.000 €


### 6. Lagerwerte Power-BI-kompatibel speichern

Die Lagerwerte wurden nach der Bereinigung als ganze Zahlen gespeichert. Dadurch wird verhindert, dass Power BI Dezimalpunkte im deutschen Zahlenformat falsch interpretiert und Lagerwerte zu hoch darstellt.

## Ausgabedaten

Die bereinigten Daten wurden im Ordner `data/clean/` gespeichert:

- `clean_umsaetze.csv`
- `clean_kosten.csv`
- `clean_forderungen.csv`
- `clean_verbindlichkeiten.csv`
- `clean_lagerbestand.csv`

## Fachliche Einordnung

Die Bereinigung ist wichtig, weil fehlerhafte Rohdaten zu falschen Kennzahlen, falschen Dashboards und falschen Management-Entscheidungen führen können. Besonders in einer Krisensituation müssen Forderungen, Kosten und Working Capital sauber analysiert werden.