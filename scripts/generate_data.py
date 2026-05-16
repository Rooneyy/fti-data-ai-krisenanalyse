import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from pathlib import Path

# ------------------------------------------------------------
# Rohdaten-Generator für Krisenanalyse-Projekt
# Unternehmen: Müller Maschinenbau GmbH
# Ziel: 5 CSV-Dateien mit realistischen, aber absichtlich "dreckigen" Daten erzeugen
# ------------------------------------------------------------

# Damit bei jedem Lauf ähnliche Zufallsdaten entstehen
random.seed(42)
np.random.seed(42)

# Projektpfade
BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

# Grunddaten
kunden = [
    "Müller GmbH",
    "Schmidt AG",
    "TechBau GmbH",
    "IndustriePartner KG",
    "NordMaschinen GmbH",
    "Alpha Components GmbH",
    "KraftWerk Solutions",
    "Meier Produktion GmbH",
    "HanseTech AG",
    "Bergmann Anlagenbau"
]

produktgruppen = [
    "Maschinen",
    "Ersatzteile",
    "Wartung",
    "Software",
    "Service"
]

kostenarten = [
    "Material",
    "Personal",
    "Miete",
    "Energie",
    "Sonstiges"
]

kostenstellen = [
    "Produktion",
    "Vertrieb",
    "Verwaltung",
    "IT",
    "Logistik"
]

lieferanten = [
    "Stahlhandel Weber",
    "ElektroTech Lieferanten GmbH",
    "Logistik Express",
    "Software Solutions AG",
    "MaschinenService Süd"
]


def random_date(start_date, end_date):
    """Erzeugt ein zufälliges Datum zwischen start_date und end_date."""
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)


start = datetime(2024, 1, 1)
end = datetime(2024, 12, 31)


# ------------------------------------------------------------
# 1. Umsätze erzeugen
# ------------------------------------------------------------

umsaetze = []

for i in range(500):
    datum = random_date(start, end)
    kunde = random.choice(kunden)
    produktgruppe = random.choice(produktgruppen)
    menge = random.randint(1, 20)

    if produktgruppe == "Maschinen":
        einzelpreis = random.randint(15000, 80000)
    elif produktgruppe == "Ersatzteile":
        einzelpreis = random.randint(100, 2000)
    elif produktgruppe == "Wartung":
        einzelpreis = random.randint(500, 5000)
    elif produktgruppe == "Software":
        einzelpreis = random.randint(1000, 15000)
    else:
        einzelpreis = random.randint(300, 8000)

    gesamtbetrag = menge * einzelpreis

    umsaetze.append({
        "datum": datum.strftime("%Y-%m-%d"),
        "kunde": kunde,
        "produktgruppe": produktgruppe,
        "menge": menge,
        "einzelpreis": einzelpreis,
        "gesamtbetrag": gesamtbetrag
    })

df_umsaetze = pd.DataFrame(umsaetze)


# ------------------------------------------------------------
# 2. Kosten erzeugen
# ------------------------------------------------------------

kosten = []

for i in range(200):
    datum = random_date(start, end)
    kostenart = random.choice(kostenarten)
    kostenstelle = random.choice(kostenstellen)

    if kostenart == "Material":
        betrag = random.randint(350000, 900000)
    elif kostenart == "Personal":
        betrag = random.randint(180000, 450000)
    elif kostenart == "Miete":
        betrag = random.randint(30000, 90000)
    elif kostenart == "Energie":
        betrag = random.randint(25000, 80000)
    else:
        betrag = random.randint(20000, 70000)

    kosten.append({
        "datum": datum.strftime("%Y-%m-%d"),
        "kostenart": kostenart,
        "betrag": betrag,
        "kostenstelle": kostenstelle
    })

df_kosten = pd.DataFrame(kosten)


# ------------------------------------------------------------
# 3. Offene Forderungen erzeugen
# ------------------------------------------------------------

forderungen = []

for i in range(80):
    kunde = random.choice(kunden)
    rechnungsdatum = random_date(start, end)
    faelligkeitsdatum = rechnungsdatum + timedelta(days=random.choice([14, 30, 45, 60]))
    betrag = random.randint(1000, 120000)

    status = "überfällig" if faelligkeitsdatum < datetime(2024, 12, 31) and random.random() < 0.5 else "offen"

    forderungen.append({
        "kunde": kunde,
        "rechnungsnummer": f"RE-{2024}-{i+1:04d}",
        "rechnungsdatum": rechnungsdatum.strftime("%Y-%m-%d"),
        "faelligkeitsdatum": faelligkeitsdatum.strftime("%Y-%m-%d"),
        "betrag": betrag,
        "status": status
    })

df_forderungen = pd.DataFrame(forderungen)


# ------------------------------------------------------------
# 4. Offene Verbindlichkeiten erzeugen
# ------------------------------------------------------------

verbindlichkeiten = []

for i in range(60):
    lieferant = random.choice(lieferanten)
    rechnungsdatum = random_date(start, end)
    faelligkeitsdatum = rechnungsdatum + timedelta(days=random.choice([14, 30, 45, 60]))
    betrag = random.randint(1000, 50000)

    verbindlichkeiten.append({
        "lieferant": lieferant,
        "rechnungsdatum": rechnungsdatum.strftime("%Y-%m-%d"),
        "faelligkeitsdatum": faelligkeitsdatum.strftime("%Y-%m-%d"),
        "betrag": betrag
    })

df_verbindlichkeiten = pd.DataFrame(verbindlichkeiten)


# ------------------------------------------------------------
# 5. Lagerbestand erzeugen
# ------------------------------------------------------------

lagerbestand = []

for i in range(40):
    produktgruppe = random.choice(produktgruppen)
    menge = random.randint(5, 200)
    wert = menge * random.randint(50, 1500)
    letzte_bewegung = random_date(start, end)

    lagerbestand.append({
        "produktgruppe": produktgruppe,
        "menge": menge,
        "wert": wert,
        "letzte_bewegung": letzte_bewegung.strftime("%Y-%m-%d")
    })

df_lagerbestand = pd.DataFrame(lagerbestand)


# ------------------------------------------------------------
# Absichtlich Datenqualitätsprobleme einbauen
# ------------------------------------------------------------

# Inkonsistente Kundennamen
df_umsaetze.loc[0, "kunde"] = "Mueller GmbH"
df_umsaetze.loc[1, "kunde"] = "Fa. Müller"
df_forderungen.loc[0, "kunde"] = "Mueller GmbH"
df_forderungen.loc[1, "kunde"] = "Fa. Müller"

# Fehlende Werte
df_umsaetze.loc[5, "kunde"] = np.nan
df_umsaetze.loc[10, "einzelpreis"] = np.nan
df_kosten.loc[3, "kostenart"] = np.nan
df_forderungen.loc[4, "faelligkeitsdatum"] = np.nan
df_lagerbestand.loc[2, "wert"] = np.nan

# Doppelte Einträge
df_umsaetze = pd.concat([df_umsaetze, df_umsaetze.iloc[[2]]], ignore_index=True)
df_kosten = pd.concat([df_kosten, df_kosten.iloc[[5]]], ignore_index=True)
df_forderungen = pd.concat([df_forderungen, df_forderungen.iloc[[7]]], ignore_index=True)

# Unrealistische Ausreißer
df_forderungen.loc[10, "betrag"] = 999999
df_kosten.loc[12, "betrag"] = 888888

# Gemischte Datumsformate
df_umsaetze.loc[15, "datum"] = "15.03.2024"
df_kosten.loc[20, "datum"] = "22.04.2024"
df_forderungen.loc[8, "rechnungsdatum"] = "05.02.2024"


# ------------------------------------------------------------
# CSV-Dateien speichern
# ------------------------------------------------------------

df_umsaetze.to_csv(RAW_DIR / "umsaetze.csv", index=False, encoding="utf-8-sig", sep=";")
df_kosten.to_csv(RAW_DIR / "kosten.csv", index=False, encoding="utf-8-sig", sep=";")
df_forderungen.to_csv(RAW_DIR / "forderungen.csv", index=False, encoding="utf-8-sig", sep=";")
df_verbindlichkeiten.to_csv(RAW_DIR / "verbindlichkeiten.csv", index=False, encoding="utf-8-sig", sep=";")
df_lagerbestand.to_csv(RAW_DIR / "lagerbestand.csv", index=False, encoding="utf-8-sig", sep=";")

print("Rohdaten wurden erfolgreich erstellt:")
print(RAW_DIR)