# Dashboard and analysis for data from 'phq_all_final.csv'. 
First, run ```pip install -r requirements.txt``` in the file directory to download dependencies.

## 'GAD-7 Data Analysis.ipynb' is a python notebook with my analysis and ideas.

## 'app.py', 'main.py', and 'utils' are code for a dashboard displaying score timelines for requested patients.

To run the dashboard: run ```python3 main.py patient_id1 patient_id2 patient_id3..``` in the command line
for the patient id's you wish to see. For example, run
```python3 main.py 1 2 3 4 5 6 7 8 9 10``` in the command line to build a dashboard for patients 1-10.