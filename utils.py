import pandas as pd
import plotly.express as px

def id_check(id_list,df):
	valid_ids = set()
	
	for item in id_list:
		try:
			_id = int(item)
			if _id  in list(df.patient_id):
				valid_ids.add(_id)
			else:
				print('{} is not in the patient record'.format(item))
				pass
		except ValueError:
			print("Patient ids must be numeric types- {} is not a numeric type".format(item))
			pass

	return valid_ids

def build_fig(df,valid_ids):

    df_select = df[df.patient_id.isin(valid_ids)]
    fig = px.line(df_select,title='GAD7 Test Results',x='date',y='score',color='patient_id')
    fig.update_traces(mode='markers+lines')
    
    return fig