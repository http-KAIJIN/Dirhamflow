from pathlib import Path
import logging
from typing import Final #kat
## Chemin du dossier principal du projet
BASE_DIR = Final[Path] =Path(__fils__).resolve().parent.partent
#data directories 
DATA_DIR: Final[Path] = BASE_DIR / "data
RAW_DIR : Final[Path]= BASE_DIR / "raw" /"raw_data"
STRAGING_DIR: Final[Path] = BASE_DIR / "staging"
CURATED_DIR: Final[Path]= BASE_DIR / "curated"
QUARANTINE_DIR: Final[Path] = BASE_DIR / "quarantine"

for _dir in [STRAGING_DIR , CURATED_DIR , QUARANTINE_DIR]:
    _dir.mkdir(parents = True , exist_ok=True)

RAW_FILES: Final[dict[str , Path]] ={
    "customers":RAW_DIR /"customers.csv",
    "accounts":RAW_DIR /"accounts.csv",
    "cards":RAW_DIR /"cards.csv",
    "transactions": RAW_DIR / "transactions.csv",
        "payment_errors": RAW_DIR / "payment_errors.csv",
        "support_tickets": RAW_DIR / "support_tickets.csv",
        "credit_risk_bureau": RAW_DIR / "credit_risk_bureau.csv",
}
#Normalisation dyal les villes marocaines
 CITY_MAPPING : Final[dict[str , str]] = {
     "casa" : "Casablanca",
     "casablanca" :"Casablanca",
     "kech" "Marrakech",
     "marrakech" "Marrakech",
     "rabat" : "Rabat",
     "tanger" : "Tangier",
     "tangier" :"Tangier",
     "fes" : "Fes" ,
     "agadir" : "Agadir", }

#limite dl Age 
MIN_LEGAL_AGE : Final[int] = 18
MAX_CREDIT_SCORE : Final[int] = 100
# Limites dyal Credit Bureau (Standard international)
MIN_CREDIT_SCORE : Final[int] = 300
MAX_CREDIT_SCORE : Final[int] = 850

VALID_CURRENCIRES :Final[set[str]] = {"MAD" ,"EUR","USD"}
VALID_KYC_STATION :Final[set[str]] ={"VERIFIED","PENDING","REJ