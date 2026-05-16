# Power BI Dashboard – Dokumentation

## Ziel

Ziel des Power-BI-Dashboards ist es, die finanzielle Lage und Working-Capital-Situation der fiktiven Müller Maschinenbau GmbH managementgerecht darzustellen.

Das Dashboard soll nicht nur Kennzahlen anzeigen, sondern eine klare Business-Story unterstützen:

> Das Unternehmen ist operativ profitabel, bindet jedoch relevante Liquidität im Working Capital. Haupttreiber sind Forderungen und Lagerbestand, während Lieferanten vergleichsweise schnell bezahlt werden.

---

## Datenbasis

Für das Dashboard wurden die bereinigten CSV-Dateien aus `data/clean/` verwendet:

- `clean_umsaetze.csv`
- `clean_kosten.csv`
- `clean_forderungen.csv`
- `clean_lagerbestand.csv`
- `clean_verbindlichkeiten.csv`

---

## Dashboard-Seite 1: Finanzübersicht

### Zweck

Die erste Seite zeigt die operative Performance des Unternehmens. Sie beantwortet vor allem die Frage, ob das Unternehmen grundsätzlich profitabel arbeitet.

### Visuals

- KPI-Karte: Gesamtumsatz
- KPI-Karte: Gesamtkosten
- KPI-Karte: EBITDA
- KPI-Karte: EBITDA-Marge
- Liniendiagramm: Umsatzentwicklung nach Monat
- Säulendiagramm: Umsatz nach Produktgruppe
- Tabelle: Top-Kunden nach Umsatz
- Slicer: Produktgruppe

### DAX-Measures

```DAX
Gesamtumsatz = SUM(clean_umsaetze[gesamtbetrag])

Gesamtkosten = SUM(clean_kosten[betrag])

EBITDA = [Gesamtumsatz] - [Gesamtkosten]

EBITDA_Marge = DIVIDE([EBITDA], [Gesamtumsatz], 0)
```

### Interpretation

Die Finanzübersicht zeigt, dass das Unternehmen operativ profitabel ist. Der Umsatz liegt deutlich über den Kosten, wodurch eine positive EBITDA-Marge entsteht. Die Krisensituation entsteht daher nicht primär durch fehlende Profitabilität, sondern durch Liquiditätsbindung im Working Capital.

---

## Dashboard-Seite 2: Working-Capital-Analyse

### Zweck

Die zweite Seite analysiert, wo Liquidität im Unternehmen gebunden ist. Im Fokus stehen Forderungen, Lagerbestand und Verbindlichkeiten.

### Visuals

- KPI-Karte: Forderungsvolumen / offene Forderungen
- KPI-Karte: Lagerbestand Wert
- KPI-Karte: Verbindlichkeiten
- KPI-Karte: Working Capital
- KPI-Karte: DSO – Forderungslaufzeit
- KPI-Karte: DIO – Lagerreichweite
- KPI-Karte: DPO – Verbindlichkeitenlaufzeit
- Säulendiagramm: Forderungen nach Kunde
- Balkendiagramm: Lagerbestand nach Produktgruppe
- Tabelle: Überfällige Forderungen

### DAX-Measures

```DAX
Offene Forderungen = SUM(clean_forderungen[betrag])

Offene Verbindlichkeiten = SUM(clean_verbindlichkeiten[betrag])

Lagerbestand Wert = SUM(clean_lagerbestand[wert])

Working Capital =
[Offene Forderungen] + [Lagerbestand Wert] - [Offene Verbindlichkeiten]

Materialkosten =
CALCULATE(
    SUM(clean_kosten[betrag]),
    clean_kosten[kostenart] = "Material"
)

DSO =
DIVIDE([Offene Forderungen], [Gesamtumsatz], 0) * 365

DIO =
DIVIDE([Lagerbestand Wert], [Materialkosten], 0) * 365

DPO =
DIVIDE([Offene Verbindlichkeiten], [Materialkosten], 0) * 365
```

### Interpretation

Die Working-Capital-Seite zeigt, dass rund 6,7 Mio. € im Working Capital gebunden sind. Besonders Forderungen und Lagerbestand binden Liquidität. Der vergleichsweise niedrige DPO deutet darauf hin, dass Lieferanten schnell bezahlt werden und dadurch weniger Liquidität im Unternehmen verbleibt.

---

## Kennzahlenübersicht

| Kennzahl | Wert |
|---|---:|
| Gesamtumsatz | 65.224.911 € |
| Gesamtkosten | 44.187.005 € |
| EBITDA | 21.037.906 € |
| EBITDA-Marge | ca. 32,26 % |
| Forderungsvolumen | 5.403.632 € |
| Lagerbestand | 2.791.153 € |
| Verbindlichkeiten | 1.493.071 € |
| Working Capital | ca. 6.701.714 € |
| DSO | ca. 30,24 Tage |
| DIO | ca. 44,48 Tage |
| DPO | ca. 23,80 Tage |

---

## Management Insight

Das Unternehmen ist operativ profitabel, bindet jedoch rund 6,7 Mio. € im Working Capital. Haupttreiber sind Forderungen und Lagerbestand. Der vergleichsweise niedrige DPO deutet darauf hin, dass Lieferanten schnell bezahlt werden und dadurch Liquiditätspotenzial ungenutzt bleibt.

---

## Hinweis zur Datenqualität und Definition

Im Dashboard wird die Kennzahl `Offene Forderungen` technisch als Summe der gesamten Forderungstabelle berechnet. In einem produktiven Projekt sollte die Kennzahl eindeutig zwischen gesamtem Forderungsbestand und tatsächlich offenen Forderungen nach Status getrennt werden.

Für dieses Portfolio-Projekt wurde die Kennzahl bewusst als Forderungsvolumen verwendet, um die Working-Capital-Story konsistent mit den berechneten Kennzahlen zu halten.
