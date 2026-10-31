import csv

FILE = "dati/ricette-cucine-del-mondo.csv"


def carica(nomefile):
    """Legge il file, converte i numeri, scarta le righe sporche.
    Restituisce la lista delle righe buone e il numero di righe scartate."""

    dati_buoni = []
    righe_scartate = 0

    with open(nomefile, "r", encoding="utf-8", newline="") as f:
         for ricetta in csv.DictReader(f):
             try:
                 if ricetta["calories"] == "NA" or ricetta["calories"].strip() == "":
                     righe_scartate = righe_scartate + 1
                     continue
                 
                 if ricetta["avg_rating"] == "NA" or ricetta["avg_rating"].strip() == "":
                     voto = None
                 else:
                     voto = float(ricetta["avg_rating"])
                
                 ricetta_pulita = {
                     "name": ricetta["name"],
                     "country": ricetta["country"],
                     "calories": int(ricetta["calories"]),
                     "avg_rating": voto,
                     "total_time": int(ricetta["total_time"]),
                     "ingredients": ricetta["ingredients"]
                 }
                 
                 
                 dati_buoni.append(ricetta_pulita)
                 
             except ValueError:
                 
                 righe_scartate = righe_scartate + 1

    return dati_buoni, righe_scartate


def domanda1(dati):
    """Risponde alla domanda 1 della scheda."""
    return None


def domanda2(dati):
    """Risponde alla domanda 2."""
    return None


def domanda3(dati):
    """Risponde alla domanda 3. Restituisce la tabella
    che finirà in risultati.csv: una lista di righe."""
    return []


def domanda_nostra(dati):
    """La domanda inventata dal gruppo."""
    return None


def scrivi_risultati(nomefile, intestazione, tabella):
    """Scrive la tabella in un CSV con csv.writer."""
    pass


def main():
    dati, scartate = carica(FILE)
    print(f"Righe buone: {len(dati)}, scartate: {scartate}")
    print("Domanda 1:", domanda1(dati))
    print("Domanda 2:", domanda2(dati))
    tabella = domanda3(dati)
    scrivi_risultati("risultati.csv", ["colonna1", "colonna2"], tabella)
    print("Domanda nostra:", domanda_nostra(dati))


main()