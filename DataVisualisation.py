import csv
import pandas as pd
import plotly.express as px

df = pd.read_csv('Data.csv')
averageScore = df.groupby(['student_id','level'],as_index = False)['attempt'].mean() 
fig  = px.scatter(averageScore , x = 'student_id', y = 'level',size = 'attempt' , color = 'attempt')
fig.show()