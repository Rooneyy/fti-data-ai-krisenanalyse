-- ============================================================
-- SQL-Abfragen für Krisenanalyse Müller Maschinenbau GmbH
-- Datenbasis: projekt_datenbank.db
-- ============================================================


-- 1. Top 10 Kunden nach Gesamtumsatz
SELECT
    kunde,
    ROUND(SUM(gesamtbetrag), 2) AS gesamtumsatz
FROM umsaetze
GROUP BY kunde
ORDER BY gesamtumsatz DESC
LIMIT 10;


-- 2. Umsatz pro Monat
SELECT
    substr(datum, 1, 7) AS monat,
    ROUND(SUM(gesamtbetrag), 2) AS monatsumsatz
FROM umsaetze
GROUP BY substr(datum, 1, 7)
ORDER BY monat;


-- 3. Umsatz pro Produktgruppe
SELECT
    produktgruppe,
    ROUND(SUM(gesamtbetrag), 2) AS gesamtumsatz
FROM umsaetze
GROUP BY produktgruppe
ORDER BY gesamtumsatz DESC;


-- 4. Alle überfälligen Forderungen, sortiert nach Betrag
SELECT
    kunde,
    rechnungsnummer,
    rechnungsdatum,
    faelligkeitsdatum,
    betrag,
    status
FROM forderungen
WHERE status = 'überfällig'
ORDER BY betrag DESC;


-- 5. Offene Forderungen nach Altersklassen
SELECT
    CASE
        WHEN julianday('2024-12-31') - julianday(faelligkeitsdatum) <= 30 THEN '0-30 Tage'
        WHEN julianday('2024-12-31') - julianday(faelligkeitsdatum) <= 60 THEN '31-60 Tage'
        WHEN julianday('2024-12-31') - julianday(faelligkeitsdatum) <= 90 THEN '61-90 Tage'
        ELSE '>90 Tage'
    END AS altersklasse,
    ROUND(SUM(betrag), 2) AS gesamtbetrag,
    COUNT(*) AS anzahl_rechnungen
FROM forderungen
WHERE status = 'überfällig'
GROUP BY altersklasse
ORDER BY gesamtbetrag DESC;


-- 6. Top 5 Lieferanten nach offenen Verbindlichkeiten
SELECT
    lieferant,
    ROUND(SUM(betrag), 2) AS offene_verbindlichkeiten
FROM verbindlichkeiten
GROUP BY lieferant
ORDER BY offene_verbindlichkeiten DESC
LIMIT 5;


-- 7. Lagerbestand nach Produktgruppe
SELECT
    produktgruppe,
    SUM(menge) AS gesamtmenge,
    ROUND(SUM(wert), 2) AS lagerwert
FROM lagerbestand
GROUP BY produktgruppe
ORDER BY lagerwert DESC;


-- 8. Monatliche Kostenentwicklung nach Kostenart
SELECT
    substr(datum, 1, 7) AS monat,
    kostenart,
    ROUND(SUM(betrag), 2) AS kosten
FROM kosten
GROUP BY substr(datum, 1, 7), kostenart
ORDER BY monat, kostenart;