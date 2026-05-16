# Datenmodell – Krisenanalyse

## Projektszenario

Das Projekt simuliert ein Data-&AI-Beratungsprojekt für ein mittelständisches Unternehmen mit Liquiditätsproblemen.

Fiktives Unternehmen:
Müller Maschinenbau GmbH

Problem:
Das Unternehmen hat stagnierende Umsätze, steigende Kosten, hohe offene Forderungen und zu viel Kapital im Lager gebunden.

Analysezeitraum:
01.01.2024 bis 31.12.2024


## Tabelle 1: Umsätze

Zweck:
Diese Tabelle zeigt, welche Kunden welche Produkte gekauft haben und wie viel Umsatz dadurch entstanden ist.

Spalten:
- datum
- kunde
- produktgruppe
- menge
- einzelpreis
- gesamtbetrag


## Tabelle 2: Kosten

Zweck:
Diese Tabelle zeigt die laufenden Kosten des Unternehmens.

Spalten:
- datum
- kostenart
- betrag
- kostenstelle


## Tabelle 3: Offene Forderungen

Zweck:
Diese Tabelle zeigt Rechnungen, die Kunden noch nicht bezahlt haben.

Spalten:
- kunde
- rechnungsnummer
- rechnungsdatum
- faelligkeitsdatum
- betrag
- status


## Tabelle 4: Offene Verbindlichkeiten

Zweck:
Diese Tabelle zeigt Rechnungen, die das Unternehmen seinen Lieferanten noch bezahlen muss.

Spalten:
- lieferant
- rechnungsdatum
- faelligkeitsdatum
- betrag


## Tabelle 5: Lagerbestand

Zweck:
Diese Tabelle zeigt, welche Produktgruppen im Lager liegen und wie viel Kapital darin gebunden ist.

Spalten:
- produktgruppe
- menge
- wert
- letzte_bewegung


## Geplante Datenqualitätsprobleme

Die Rohdaten sollen absichtlich typische Fehler enthalten:

- fehlende Werte
- doppelte Einträge
- inkonsistente Kundennamen
- gemischte Datumsformate
- unrealistische Ausreißer

## Erzeugte Rohdaten

Die Rohdaten wurden mit dem Python-Skript `scripts/generate_data.py` erzeugt.

Erzeugte Dateien:
- `data/raw/umsaetze.csv`
- `data/raw/kosten.csv`
- `data/raw/forderungen.csv`
- `data/raw/verbindlichkeiten.csv`
- `data/raw/lagerbestand.csv`

Hinweis:
Die CSV-Dateien werden mit Semikolon als Trennzeichen gespeichert (`sep=";"`), damit sie in der deutschen Excel-Version korrekt in Spalten geöffnet werden.

Bekannte Datenqualitätsprobleme:
- inkonsistente Kundennamen wie "Müller GmbH", "Mueller GmbH" und "Fa. Müller"
- fehlende Werte in einzelnen Spalten
- doppelte Einträge
- gemischte Datumsformate
- unrealistische Ausreißer bei Beträgen