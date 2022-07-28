import csv
import os
from utils.constants import (daily_reports_processed, 
                            nominations_processed,
                            balance_data, 
                            companies,
                            oils,
                            nominations_data)

def create_csv_file(filepath, header):
    with open(filepath, "w") as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)

def init_database():
    if not os.path.exists(daily_reports_processed):
        create_csv_file(daily_reports_processed, ["fecha actualizacion", "fecha reporte"])
    if not os.path.exists(nominations_processed):
        create_csv_file(nominations_processed, ["fecha actualizacion", "fecha reporte"])
    if not os.path.exists(balance_data):
        create_csv_file(balance_data, ["fecha", "empresa", "operacion" , "tipo crudo", "GOV", "GSV", "NSV"])
    if not os.path.exists(nominations_data):
        create_csv_file(nominations_data, ["fecha", "nominados geopark"])
    if not os.path.exists(companies):
        create_csv_file(companies, ["Nombre"])
    if not os.path.exists(oils):
        create_csv_file(oils, ["Crudo", "Livianos"])