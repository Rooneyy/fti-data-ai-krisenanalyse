# FTI Data & AI Krisenanalyse – Müller Maschinenbau GmbH

## Projektüberblick

Dieses Projekt ist eine fiktive, consulting-nahe Data-&AI-Krisenanalyse eines mittelständischen Maschinenbauunternehmens.

Die **Müller Maschinenbau GmbH** ist operativ profitabel, bindet jedoch relevante Liquidität im Working Capital. Besonders Forderungen und Lagerbestand wirken als Liquiditätstreiber. Ziel des Projekts ist es, aus simulierten Rohdaten eine nachvollziehbare Analyse aufzubauen: von Datenbereinigung über SQL-Kennzahlen bis hin zu einem Power-BI-Dashboard mit Management Summary.

Das Projekt dient als Portfolio-Nachweis für Rollen im Bereich **Data Analytics, AI Consulting, Digital Transformation und Business Technology Consulting**.

---

## Business-Fragestellung

Das Projekt beantwortet unter anderem folgende Fragen:

- Wie profitabel ist das Unternehmen operativ?
- Wie viel Liquidität ist im Working Capital gebunden?
- Welche Kunden verursachen hohe Forderungsvolumen?
- Welche Forderungen sind überfällig?
- In welchen Produktgruppen ist besonders viel Kapital im Lager gebunden?
- Welche Handlungsempfehlungen ergeben sich für das Management?

---

## Verwendete Technologien

- **Python** für Datengenerierung und Datenbereinigung
- **Pandas** für Transformation, Bereinigung und Validierung der Daten
- **SQLite** als lokale relationale Datenbank
- **SQL** für KPI-Berechnung und Analyseabfragen
- **Power BI** für Dashboarding und Visualisierung
- **DAX** für Measures und Working-Capital-Kennzahlen
- **Markdown** für technische und fachliche Projektdokumentation

---

## Projektstruktur

```text
fti_data_ai_krisenanalyse/
│
├── dashboards/
│   └── fti_krisenanalyse_dashboard.pbix
│
├── data/
│   ├── raw/
│   │   ├── forderungen.csv
│   │   ├── kosten.csv
│   │   ├── lagerbestand.csv
│   │   ├── umsaetze.csv
│   │   └── verbindlichkeiten.csv
│   │
│   └── clean/
│       ├── clean_forderungen.csv
│       ├── clean_kosten.csv
│       ├── clean_lagerbestand.csv
│       ├── clean_umsaetze.csv
│       └── clean_verbindlichkeiten.csv
│
├── docs/
│   ├── datenbereinigung.md
│   ├── datenmodell.md
│   ├── kennzahlen_erklaerung.md
│   ├── powerbi_dashboard.md
│   └── sql_kennzahlen.md
│
├── scripts/
│   ├── generate_data.py
│   ├── data_cleaning.py
│   └── load_to_db.py
│
├── sql/
│   ├── abfragen.sql
│   └── kpi_berechnung.sql
│
├── projekt_datenbank.db
└── README.md
```

---

## Vorgehen

### 1. Datengenerierung

Für das Projekt wurden synthetische Unternehmensdaten erzeugt. Die Daten simulieren typische Tabellen eines mittelständischen Unternehmens:

- Umsätze
- Kosten
- Forderungen
- Verbindlichkeiten
- Lagerbestand

Die Daten sind fiktiv und enthalten bewusst Datenqualitätsprobleme, um einen realistischen Analyseprozess abzubilden.

### 2. Datenbereinigung

Die Rohdaten wurden mit Python und Pandas bereinigt. Dabei wurden unter anderem folgende Probleme behandelt:

- Duplikate
- fehlende Werte
- gemischte Datumsformate
- inkonsistente Kundennamen
- Ausreißer bei Kosten und Forderungen
- Power-BI-relevante Formatprobleme bei Lagerwerten

Die bereinigten Daten wurden im Ordner `data/clean/` gespeichert.

### 3. Datenbank und SQL-Kennzahlen

Die bereinigten CSV-Dateien wurden in eine lokale SQLite-Datenbank geladen. Anschließend wurden zentrale Finanz- und Working-Capital-Kennzahlen mit SQL berechnet.

### 4. Power-BI-Dashboard

Das Dashboard besteht aus zwei Analysebereichen:

1. **Finanzübersicht – Operative Performance**
   - Umsatz
   - Kosten
   - EBITDA
   - EBITDA-Marge
   - Umsatzentwicklung
   - Umsatz nach Produktgruppe
   - Top-Kunden nach Umsatz

2. **Working-Capital-Analyse – Liquiditätsbindung**
   - Forderungen
   - Lagerbestand
   - Verbindlichkeiten
   - Working Capital
   - DSO, DIO und DPO
   - überfällige Forderungen
   - Lagerbestand nach Produktgruppe


## Dashboard Preview

### Finanzübersicht

![Finanzübersicht](assets/dashboard_finanzuebersicht.png)

### Working-Capital-Analyse

![Working Capital](assets/dashboard_working_capital.png)

---

## Zentrale Kennzahlen

| Kennzahl | Wert |
|---|---:|
| Gesamtumsatz | 65.224.911 € |
| Gesamtkosten | 44.187.005 € |
| Materialkosten | 22.904.888 € |
| Forderungsvolumen | 5.403.632 € |
| Lagerbestand | 2.791.153 € |
| Verbindlichkeiten | 1.493.071 € |
| EBITDA | 21.037.906 € |
| EBITDA-Marge | ca. 32,26 % |
| Working Capital | ca. 6.701.714 € |
| DSO | ca. 30,24 Tage |
| DIO | ca. 44,48 Tage |
| DPO | ca. 23,80 Tage |

**Hinweis:** Im Dashboard wird die Kennzahl „Offene Forderungen“ als gesamtes Forderungsvolumen der Forderungstabelle verwendet. Für ein produktives Projekt müsste die Definition eindeutig zwischen gesamtem Forderungsbestand und tatsächlich offenen Forderungen nach Status getrennt werden.

---

## Management Summary

Die Müller Maschinenbau GmbH ist auf Basis der simulierten Daten operativ profitabel. Bei einem Gesamtumsatz von rund **65,2 Mio. €** und Gesamtkosten von rund **44,2 Mio. €** ergibt sich ein EBITDA von rund **21,0 Mio. €** und eine EBITDA-Marge von rund **32,3 %**.

Trotz der positiven operativen Ergebnislage zeigt die Analyse eine relevante Kapitalbindung im Working Capital. Insgesamt sind rund **6,7 Mio. €** im Working Capital gebunden. Haupttreiber sind das Forderungsvolumen und der Lagerbestand. Gleichzeitig deutet ein DPO von rund **23,8 Tagen** darauf hin, dass Lieferanten vergleichsweise schnell bezahlt werden und dadurch Liquiditätspotenzial ungenutzt bleibt.

---

## Handlungsempfehlungen

1. **Forderungsmanagement verbessern**
   - Überfällige Forderungen priorisiert verfolgen
   - Mahnprozess standardisieren
   - Zahlungsziele und Bonitätsprüfung bei Großkunden prüfen

2. **Lagerbestand gezielt reduzieren**
   - Produktgruppen mit hoher Kapitalbindung analysieren
   - Bestandsreichweiten überprüfen
   - langsam drehende Lagerpositionen identifizieren

3. **Zahlungsziele mit Lieferanten prüfen**
   - DPO schrittweise optimieren
   - Skonto-Vorteile gegen Liquiditätswirkung abwägen
   - Lieferantenkonditionen neu verhandeln

4. **Management-Dashboard regelmäßig nutzen**
   - Working-Capital-KPIs monatlich überwachen
   - Forderungen, Lagerbestand und Verbindlichkeiten gemeinsam betrachten
   - Maßnahmen nicht nur finanzseitig, sondern auch prozessseitig steuern

---

## Portfolio-Relevanz

Dieses Projekt zeigt einen praxisnahen End-to-End-Workflow, der für Business-/Data-/AI-Consulting-Rollen relevant ist:

- Datenqualität erkennen und verbessern
- Daten mit Python und Pandas bereinigen
- strukturierte Daten in SQLite speichern
- KPIs mit SQL berechnen
- Kennzahlen mit Power BI visualisieren
- technische Analyse in Management-relevante Empfehlungen übersetzen

Damit demonstriert das Projekt nicht nur Tool-Kenntnisse, sondern auch die Fähigkeit, Datenanalyse mit Business-Kontext und Beratungsperspektive zu verbinden.

---

## Hinweis zur Datenbasis

Alle Daten in diesem Projekt sind synthetisch erzeugt. Es wurden keine echten Unternehmensdaten verwendet.
