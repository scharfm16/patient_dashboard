#The main file for pulling the data and generating the dashboard

from utils import id_check, build_fig
import pandas as pd
import plotly.express as px
from app import run_server
import sys

if __name__ == '__main__':
	
	#Pulling data with Pandas
    df = pd.read_csv('phq_all_final.csv',
        parse_dates=["date","patient_date_created"])

    #Checking the patient id inputs for validity-getting ids from system args.
    valid_ids = id_check(sys.argv[1:],df)

    #Checking whether there are any records for the inputted patients
    if len(valid_ids) == 0:
        print("No patient records found")
    
    else:
    	#Building the figure for the dashboard
    	fig = build_fig(df,valid_ids)

    	#Running the server and opening the dashboard in a browser
    	run_server(fig)