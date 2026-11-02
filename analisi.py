import csv

FILE = "dati/ricette-cucine-del-mondo.csv"

def carica(nomefile):
    """Legge il file, converte i numeri, scarta le righe sporche. Restituisce la lista delle righe buone e il numero di righe scartate."""
    buone = []
    scartate = 0
    
    with open(nomefile, "r", encoding="utf-8", newline="") as f:
        lettore = csv.DictReader(f)
        
        for riga in lettore:
            if not riga.get("name") or not riga.get("country"):
                scartate += 1
                continue

            
            try:
                riga["calories"] = int(riga["calories"])
            except (ValueError, TypeError):
                riga["calories"] = None
                
            
            try:
                riga["avg_rating"] = float(riga["avg_rating"].replace(",", "."))
            except (ValueError, TypeError):
                riga["avg_rating"] = None
                
           
            try:
                riga["total_time"] = int(riga["total_time"])
            except (ValueError, TypeError):
                riga["total_time"] = None
                
            buone.append(riga)
            
    return buone, scartate

def domanda1(dati):
    """Risponde alla domanda 1 della scheda."""
    cucine = set()
    senza_calorie = 0
    senza_voto = 0
    
    for riga in dati:
        cucine.add(riga["country"])
        if riga["calories"] is None:
            senza_calorie += 1
        if riga["avg_rating"] is None:
            senza_voto += 1
            
    return f"Ricette totali: {len(dati)}, Cucine: {len(cucine)}, Senza calorie: {senza_calorie}, Senza voto: {senza_voto}"



def domanda2(dati):
    """Risponde alla domanda 2 usando cicli standard senza funzioni avanzate."""
    tempi_validi = []
    for r in dati:
        if r["total_time"] is not None:
            if r["total_time"] > 0:
                tempi_validi.append(r)
   
    if len(tempi_validi) == 0:
        return "Nessun tempo valido trovato"
       
    ricetta_minima = tempi_validi[0]
    ricetta_massima = tempi_validi[0]
    somma_tempi = 0
    superano_24h = 0
   
    for riga in tempi_validi:
       
        somma_tempi = somma_tempi + riga["total_time"]
             
        if riga["total_time"] < ricetta_minima["total_time"]:
            ricetta_minima = riga
                
        if riga["total_time"] > ricetta_massima["total_time"]:
            ricetta_massima = riga
           
        if riga["total_time"] > 1440:
            superano_24h = superano_24h + 1
   
    media_minuti = somma_tempi / len(tempi_validi)
    media_arrotondata = round(media_minuti, 2)
   
    tempo_max = ricetta_massima["total_time"]
    ore_max = tempo_max // 60
    minuti_max = tempo_max % 60
    tempo_max_formattato = f"{ore_max} ore e {minuti_max} minuti"
   
    nome_max = ricetta_massima["name"]
    minimo_valore = ricetta_minima["total_time"]
   
    return (f"Minimo: {minimo_valore} min, "
            f"Massimo: {tempo_max_formattato} ({nome_max}), "
            f"Media: {media_arrotondata} min, "
            f"Oltre 24 ore: {superano_24h}")
 


def domanda3(dati):    
    """Risponde alla domanda 3. Calcola la media dei voti per ogni cucina."""
    somma = {}    
    conteggi = {}          
   
    for riga in dati:        
        if riga["avg_rating"] is not None:            
            cucina = riga["country"]                          
            if cucina not in somma:                
                somma[cucina] = 0.0                
                conteggi[cucina] = 0                            
            somma[cucina] = somma[cucina] + riga["avg_rating"]            
            conteggi[cucina] = conteggi[cucina] + 1
       
    tabella_risultati = []    
    for cucina in somma:        
        voto_medio = somma[cucina] / conteggi[cucina]        
        voto_arrotondato = round(voto_medio, 2)        
        tabella_risultati.append([voto_arrotondato, cucina, conteggi[cucina]])              
       
    tabella_risultati.sort(reverse=True)    
   
    tabella_finale = []
    for riga in tabella_risultati:
        tabella_finale.append([riga[1], riga[2], riga[0]])
       

    return tabella_finale
 
 

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
    scrivi_risultati("risultati.csv", ["cucina", "numero_ricette", "voto_medio"], tabella)
    print("Domanda nostra:", domanda_nostra(dati))

main()