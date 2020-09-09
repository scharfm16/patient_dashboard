from utils import id_check, build_fig
import pandas as pd
import plotly.express as px
from app import run_server
import sys

if __name__ == '__main__':
    df = pd.read_csv('phq_all_final.csv',
        parse_dates=["date","patient_date_created"])

    valid_ids = id_check(sys.argv[1:],df)

    if len(valid_ids) == 0:
        print("No patient records found")
    
    else:
    	fig = build_fig(df,valid_ids)
    	run_server(fig)