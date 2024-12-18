import pandas as pd
import plotly.express as px
import streamlit as st

# Dataset Reading (CSV)
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

# Renaming Columns
df = df.rename(columns={
    'newDeaths': 'Novos Óbitos',
    'newCases': 'Novos Casos',
    'deaths_per_100k_inhabitants': 'Óbitos por 100 mil hab',  
    'totalCases_per_100k_inhabitants' : 'Casos por 100 mil hab'  
})

# State Select
states = sorted(list(df['state'].unique()))
state = st.sidebar.selectbox('Selecione o Estado:', states)

# Column Select 
columns = [
    'Novos Óbitos',
    'Novos Casos',
    'Óbitos por 100 mil hab',
    'Casos por 100 mil hab'
]
column = st.sidebar.selectbox('Selecione o Campo:', columns)

# Select Rows from State
df = df[df['state'] == state]

# FIGURE
fig = px.line(df, x="date", y=column, title=column + ' - ' + state)
fig.update_layout(xaxis_title='Data', yaxis_title=column.upper(), title = {'x':0.5})

st.title('DADOS COVID - BRASIL')
st.plotly_chart(fig, use_container_width=True)
st.caption('Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br')