# Final Checklist – FTI Data & AI Krisenanalyse

## Status

Das Projekt ist technisch und dokumentarisch in einem portfoliofähigen Zustand. Die Datenbereinigung, SQL-Kennzahlen, Power-BI-Datei und Projektdokumentation sind vorhanden.

## Vor GitHub-Upload prüfen

1. `README.md` öffnen und kurz prüfen, ob die Darstellung auf GitHub sauber aussieht.
2. `docs/powerbi_dashboard.md` öffnen und prüfen, ob die DAX-Codeblöcke korrekt angezeigt werden.
3. Power-BI-Datei öffnen und sicherstellen, dass die Werte weiterhin ungefähr so aussehen:
   - Gesamtumsatz: ca. 65 Mio. €
   - Gesamtkosten: ca. 44 Mio. €
   - EBITDA: ca. 21 Mio. €
   - Working Capital: ca. 6,7 Mio. €
   - DSO: ca. 30,2 Tage
   - DIO: ca. 44,5 Tage
   - DPO: ca. 23,8 Tage
4. Optional: Dashboard-Screenshot für LinkedIn oder Bewerbung erstellen.

## Wichtigste manuelle Power-BI-Design-Fixes

Diese Punkte müssen in Power BI Desktop manuell erledigt werden, weil die `.pbix` nicht zuverlässig automatisch bearbeitet werden sollte:

1. Seitentitel hinzufügen:
   - Finanzübersicht – Operative Performance
   - Working-Capital-Analyse – Liquiditätsbindung
2. Visual-Titel professionell benennen:
   - Monatliche Umsatzentwicklung
   - Umsatz nach Produktgruppe
   - Top 10 Kunden nach Umsatz
   - Forderungen nach Kunde
   - Lagerbestand nach Produktgruppe
   - Überfällige Forderungen
3. KPI-Karten sauber ausrichten.
4. Tabellenfelder lesbar umbenennen:
   - Kunde
   - Betrag
   - Fälligkeitsdatum
   - Status
5. Eine kleine Management-Insight-Box auf der Working-Capital-Seite ergänzen.

## Nicht mehr machen

- Keine neuen KPIs hinzufügen
- Kein neues Datenmodell bauen
- Keine neue Datensimulation starten
- Kein Dashboard komplett neu designen
- Kein künstliches AI-Feature einbauen

Das Projekt soll jetzt veröffentlicht werden, nicht weiter wachsen.
