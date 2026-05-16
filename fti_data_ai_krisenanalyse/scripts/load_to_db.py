import sqlite3
import pandas as pd
from pathlib import Path

# ------------------------------------------------------------
# Lädt bereinigte CSV-Dateien in eine SQLite-Datenbank
# Projekt: Krisenanalyse Müller Maschinenbau GmbH
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[1]
CLEAN_DIR = BASE_DIR / "data" / "clean"
DB_PATH = BASE_DIR / "projekt_datenbank.db"

# Bereinigte CSV-Dateien einlesen
df_umsaetze = pd.read_csv(CLEAN_DIR / "clean_umsaetze.csv", sep=";")
df_kosten = pd.read_csv(CLEAN_DIR / "clean_kosten.csv", sep=";")
df_forderungen = pd.read_csv(CLEAN_DIR / "clean_forderungen.csv", sep=";")
df_verbindlichkeiten = pd.read_csv(CLEAN_DIR / "clean_verbindlichkeiten.csv", sep=";")
df_lagerbestand = pd.read_csv(CLEAN_DIR / "clean_lagerbestand.csv", sep=";")

# Verbindung zur SQLite-Datenbank erstellen
conn = sqlite3.connect(DB_PATH)

# Tabellen in Datenbank schreiben
df_umsaetze.to_sql("umsaetze", conn, if_exists="replace", index=False)
df_kosten.to_sql("kosten", conn, if_exists="replace", index=False)
df_forderungen.to_sql("forderungen", conn, if_exists="replace", index=False)
df_verbindlichkeiten.to_sql("verbindlichkeiten", conn, if_exists="replace", index=False)
df_lagerbestand.to_sql("lagerbestand", conn, if_exists="replace", index=False)

# Kontrolle: Tabellen und Zeilenanzahl ausgeben
tables = ["umsaetze", "kosten", "forderungen", "verbindlichkeiten", "lagerbestand"]

print("Datenbank wurde erstellt:")
print(DB_PATH)

print("\nTabellenübersicht:")
for table in tables:
    count = pd.read_sql_query(f"SELECT COUNT(*) AS zeilen FROM {table}", conn)
    print(f"{table}: {count.loc[0, 'zeilen']} Zeilen")

conn.close()