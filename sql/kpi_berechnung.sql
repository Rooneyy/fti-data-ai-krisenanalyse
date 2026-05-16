-- ============================================================
-- KPI-Berechnung für Krisenanalyse Müller Maschinenbau GmbH
-- Datenbasis: projekt_datenbank.db
-- ============================================================


-- 1. Gesamtumsatz
SELECT
    ROUND(SUM(gesamtbetrag), 2) AS gesamtumsatz
FROM umsaetze;


-- 2. Gesamtkosten
SELECT
    ROUND(SUM(betrag), 2) AS gesamtkosten
FROM kosten;


-- 3. EBITDA und EBITDA-Marge
SELECT
    ROUND(u.gesamtumsatz, 2) AS gesamtumsatz,
    ROUND(k.gesamtkosten, 2) AS gesamtkosten,
    ROUND(u.gesamtumsatz - k.gesamtkosten, 2) AS ebitda,
    ROUND((u.gesamtumsatz - k.gesamtkosten) * 1.0 / u.gesamtumsatz * 100, 2) AS ebitda_marge_prozent
FROM
    (SELECT SUM(gesamtbetrag) AS gesamtumsatz FROM umsaetze) u,
    (SELECT SUM(betrag) AS gesamtkosten FROM kosten) k;


-- 4. Working Capital
SELECT
    ROUND(f.offene_forderungen, 2) AS offene_forderungen,
    ROUND(l.lagerbestand_wert, 2) AS lagerbestand_wert,
    ROUND(v.offene_verbindlichkeiten, 2) AS offene_verbindlichkeiten,
    ROUND(f.offene_forderungen + l.lagerbestand_wert - v.offene_verbindlichkeiten, 2) AS working_capital
FROM
    (SELECT SUM(betrag) AS offene_forderungen FROM forderungen) f,
    (SELECT SUM(wert) AS lagerbestand_wert FROM lagerbestand) l,
    (SELECT SUM(betrag) AS offene_verbindlichkeiten FROM verbindlichkeiten) v;


-- 5. DSO - Days Sales Outstanding
SELECT
    ROUND(f.offene_forderungen, 2) AS offene_forderungen,
    ROUND(u.gesamtumsatz, 2) AS gesamtumsatz,
    ROUND(f.offene_forderungen * 1.0 / u.gesamtumsatz * 365, 2) AS dso_tage
FROM
    (SELECT SUM(betrag) AS offene_forderungen FROM forderungen) f,
    (SELECT SUM(gesamtbetrag) AS gesamtumsatz FROM umsaetze) u;


-- 6. DIO - Days Inventory Outstanding
SELECT
    ROUND(l.lagerbestand_wert, 2) AS lagerbestand_wert,
    ROUND(m.materialkosten, 2) AS materialkosten,
    ROUND(l.lagerbestand_wert * 1.0 / m.materialkosten * 365, 2) AS dio_tage
FROM
    (SELECT SUM(wert) AS lagerbestand_wert FROM lagerbestand) l,
    (SELECT SUM(betrag) AS materialkosten FROM kosten WHERE kostenart = 'Material') m;


-- 7. DPO - Days Payables Outstanding
SELECT
    ROUND(v.offene_verbindlichkeiten, 2) AS offene_verbindlichkeiten,
    ROUND(m.materialkosten, 2) AS materialkosten,
    ROUND(v.offene_verbindlichkeiten * 1.0 / m.materialkosten * 365, 2) AS dpo_tage
FROM
    (SELECT SUM(betrag) AS offene_verbindlichkeiten FROM verbindlichkeiten) v,
    (SELECT SUM(betrag) AS materialkosten FROM kosten WHERE kostenart = 'Material') m;


    -- Diagnose: Basiswerte für KPI-Berechnung
SELECT
    (SELECT ROUND(SUM(gesamtbetrag), 2) FROM umsaetze) AS gesamtumsatz,
    (SELECT ROUND(SUM(betrag), 2) FROM kosten) AS gesamtkosten,
    (SELECT ROUND(SUM(betrag), 2) FROM kosten WHERE kostenart = 'Material') AS materialkosten,
    (SELECT ROUND(SUM(betrag), 2) FROM forderungen) AS offene_forderungen,
    (SELECT ROUND(SUM(wert), 2) FROM lagerbestand) AS lagerbestand_wert,
    (SELECT ROUND(SUM(betrag), 2) FROM verbindlichkeiten) AS offene_verbindlichkeiten;