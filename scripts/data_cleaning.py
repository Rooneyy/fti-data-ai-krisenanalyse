import pandas as pd
from pathlib import Path

# ------------------------------------------------------------
# Datenbereinigung für Krisenprojekt Müller Maschinenbau GmbH
# Quellen: 5 CSV-Dateien aus simulierten Rohdaten
# Bekannte Probleme:
# - Duplikate
# - fehlende Werte
# - inkonsistente Kundennamen
# - gemischte Datumsformate
# - Ausreißer bei Beträgen
#
# Vorgehen:
# 1. Rohdaten einlesen
# 2. Struktur und Datenqualität prüfen
# 3. Duplikate entfernen
# 4. Fehlende Werte behandeln
# 5. Namen und Datumsformate standardisieren
# 6. Ausreißer markieren oder entfernen
# 7. Bereinigte CSV-Dateien speichern
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"
CLEAN_DIR = BASE_DIR / "data" / "clean"
CLEAN_DIR.mkdir(parents=True, exist_ok=True)


# Rohdaten einlesen
df_umsaetze = pd.read_csv(RAW_DIR / "umsaetze.csv", sep=";")
df_kosten = pd.read_csv(RAW_DIR / "kosten.csv", sep=";")
df_forderungen = pd.read_csv(RAW_DIR / "forderungen.csv", sep=";")
df_verbindlichkeiten = pd.read_csv(RAW_DIR / "verbindlichkeiten.csv", sep=";")
df_lagerbestand = pd.read_csv(RAW_DIR / "lagerbestand.csv", sep=";")


# Erste Prüfung
print("=== Daten wurden eingelesen ===")
print("Umsätze:", df_umsaetze.shape)
print("Kosten:", df_kosten.shape)
print("Forderungen:", df_forderungen.shape)
print("Verbindlichkeiten:", df_verbindlichkeiten.shape)
print("Lagerbestand:", df_lagerbestand.shape)

print("\n=== Fehlende Werte pro Tabelle ===")
print("\nUmsätze:")
print(df_umsaetze.isna().sum())

print("\nKosten:")
print(df_kosten.isna().sum())

print("\nForderungen:")
print(df_forderungen.isna().sum())

print("\nVerbindlichkeiten:")
print(df_verbindlichkeiten.isna().sum())

print("\nLagerbestand:")
print(df_lagerbestand.isna().sum())

print("\n=== Duplikate pro Tabelle ===")
print("Umsätze:", df_umsaetze.duplicated().sum())
print("Kosten:", df_kosten.duplicated().sum())
print("Forderungen:", df_forderungen.duplicated().sum())
print("Verbindlichkeiten:", df_verbindlichkeiten.duplicated().sum())
print("Lagerbestand:", df_lagerbestand.duplicated().sum())


def parse_mixed_date(series):
    """
    Wandelt gemischte Datumsformate in echte Datumswerte um.
    Unterstützt z.B.:
    - 2024-03-15
    - 15.03.2024
    """
    parsed = pd.to_datetime(series, format="%Y-%m-%d", errors="coerce")

    missing_mask = parsed.isna()
    parsed.loc[missing_mask] = pd.to_datetime(
        series.loc[missing_mask],
        format="%d.%m.%Y",
        errors="coerce"
    )

    return parsed



def standardize_customer_name(name):
    """
    Standardisiert inkonsistente Kundennamen.
    Beispiel:
    - Mueller GmbH -> Müller GmbH
    - Fa. Müller -> Müller GmbH
    """
    if pd.isna(name):
        return "Unbekannt"

    name = str(name).strip()

    replacements = {
        "Mueller GmbH": "Müller GmbH",
        "Fa. Müller": "Müller GmbH",
        "Fa. Mueller": "Müller GmbH",
        "Müller": "Müller GmbH"
    }

    return replacements.get(name, name)


# ------------------------------------------------------------
# Bereinigungsschritt 1: Duplikate entfernen
# ------------------------------------------------------------

df_umsaetze = df_umsaetze.drop_duplicates()
df_kosten = df_kosten.drop_duplicates()
df_forderungen = df_forderungen.drop_duplicates()
df_verbindlichkeiten = df_verbindlichkeiten.drop_duplicates()
df_lagerbestand = df_lagerbestand.drop_duplicates()


# ------------------------------------------------------------
# Bereinigungsschritt 2: Fehlende Werte behandeln
# ------------------------------------------------------------

# Umsätze:
# Fehlender Kunde wird als "Unbekannt" markiert, weil der Umsatzbetrag trotzdem analysiert werden kann.
df_umsaetze["kunde"] = df_umsaetze["kunde"].fillna("Unbekannt")

# Fehlender Einzelpreis wird aus Gesamtbetrag / Menge rekonstruiert, wenn Menge vorhanden ist.
df_umsaetze["einzelpreis"] = df_umsaetze["einzelpreis"].fillna(
    df_umsaetze["gesamtbetrag"] / df_umsaetze["menge"]
)

# Kosten:
# Fehlende Kostenart wird als "Unbekannt" markiert, statt die Kostenzeile zu löschen.
df_kosten["kostenart"] = df_kosten["kostenart"].fillna("Unbekannt")

# Forderungen:
# Fehlendes Fälligkeitsdatum wird mit Rechnungsdatum + 30 Tage geschätzt.
df_forderungen["rechnungsdatum"] = parse_mixed_date(df_forderungen["rechnungsdatum"])
df_forderungen["faelligkeitsdatum"] = parse_mixed_date(df_forderungen["faelligkeitsdatum"])
df_forderungen["faelligkeitsdatum"] = df_forderungen["faelligkeitsdatum"].fillna(
    df_forderungen["rechnungsdatum"] + pd.Timedelta(days=30)
)

# Lagerbestand:
# Fehlender Lagerwert wird durch den Median der jeweiligen Produktgruppe ersetzt.
df_lagerbestand["wert"] = df_lagerbestand.groupby("produktgruppe")["wert"].transform(
    lambda x: x.fillna(x.median())
)


# Werte als ganze Zahlen speichern, damit Power BI den Dezimalpunkt nicht falsch interpretiert
df_lagerbestand["wert"] = df_lagerbestand["wert"].round(0).astype(int)


# ------------------------------------------------------------
# Bereinigungsschritt 3: Datumsformate vereinheitlichen
# ------------------------------------------------------------

df_umsaetze["datum"] = parse_mixed_date(df_umsaetze["datum"])
df_kosten["datum"] = parse_mixed_date(df_kosten["datum"])

df_verbindlichkeiten["rechnungsdatum"] = parse_mixed_date(df_verbindlichkeiten["rechnungsdatum"])
df_verbindlichkeiten["faelligkeitsdatum"] = parse_mixed_date(df_verbindlichkeiten["faelligkeitsdatum"])

df_lagerbestand["letzte_bewegung"] = parse_mixed_date(df_lagerbestand["letzte_bewegung"])


# ------------------------------------------------------------
# Bereinigungsschritt 4: Kundennamen standardisieren
# ------------------------------------------------------------

df_umsaetze["kunde"] = df_umsaetze["kunde"].apply(standardize_customer_name)
df_forderungen["kunde"] = df_forderungen["kunde"].apply(standardize_customer_name)


# ------------------------------------------------------------
# Kontrolle nach Bereinigungsschritt 1 und 2
# ------------------------------------------------------------

print("\n=== Nach Duplikat- und Missing-Value-Bereinigung ===")
print("Umsätze:", df_umsaetze.shape)
print("Kosten:", df_kosten.shape)
print("Forderungen:", df_forderungen.shape)
print("Verbindlichkeiten:", df_verbindlichkeiten.shape)
print("Lagerbestand:", df_lagerbestand.shape)

print("\nFehlende Werte nach Bereinigung:")
print("\nUmsätze:")
print(df_umsaetze.isna().sum())

print("\nKosten:")
print(df_kosten.isna().sum())

print("\nForderungen:")
print(df_forderungen.isna().sum())

print("\nVerbindlichkeiten:")
print(df_verbindlichkeiten.isna().sum())

print("\nLagerbestand:")
print(df_lagerbestand.isna().sum())

print("\nDuplikate nach Bereinigung:")
print("Umsätze:", df_umsaetze.duplicated().sum())
print("Kosten:", df_kosten.duplicated().sum())
print("Forderungen:", df_forderungen.duplicated().sum())
print("Verbindlichkeiten:", df_verbindlichkeiten.duplicated().sum())
print("Lagerbestand:", df_lagerbestand.duplicated().sum())

print("\n=== Kunden nach Standardisierung ===")
print(df_umsaetze["kunde"].value_counts())
print("\nForderungen:")
print(df_forderungen["kunde"].value_counts())


# ------------------------------------------------------------
# Bereinigungsschritt 5: Ausreißer markieren
# ------------------------------------------------------------

# Schwellenwerte sind Annahmen für dieses Lernprojekt.
# In echten Projekten würden sie fachlich mit Finance/Controlling abgestimmt.
df_kosten["ist_ausreisser"] = df_kosten["betrag"] > 200000
df_forderungen["ist_ausreisser"] = df_forderungen["betrag"] > 300000

print("\n=== Ausreißerprüfung ===")
print("Kosten-Ausreißer:")
print(df_kosten[df_kosten["ist_ausreisser"] == True])

print("\nForderungs-Ausreißer:")
print(df_forderungen[df_forderungen["ist_ausreisser"] == True])


# ------------------------------------------------------------
# Bereinigte Daten speichern
# ------------------------------------------------------------

df_umsaetze.to_csv(CLEAN_DIR / "clean_umsaetze.csv", index=False, encoding="utf-8-sig", sep=";")
df_kosten.to_csv(CLEAN_DIR / "clean_kosten.csv", index=False, encoding="utf-8-sig", sep=";")
df_forderungen.to_csv(CLEAN_DIR / "clean_forderungen.csv", index=False, encoding="utf-8-sig", sep=";")
df_verbindlichkeiten.to_csv(CLEAN_DIR / "clean_verbindlichkeiten.csv", index=False, encoding="utf-8-sig", sep=";")
df_lagerbestand.to_csv(CLEAN_DIR / "clean_lagerbestand.csv", index=False, encoding="utf-8-sig", sep=";")

print("\nBereinigte CSV-Dateien wurden gespeichert unter:")
print(CLEAN_DIR)