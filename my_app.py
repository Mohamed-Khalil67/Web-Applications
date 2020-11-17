import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import plotly.express as px

st.header('User Input ')
st.markdown("CSV input file")
uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    @st.cache
    def get_data():
        return pd.read_csv(uploaded_file)
    df = get_data()


st.title("Streamlit Web Application")
st.markdown("Welcome to this in-depth introduction to how to Use diabetes Dataset")
st.header("Diabetes Patients Listings: data at a glance")

if st.checkbox("Show DataSet Rows of header"):
    number = st.number_input("Number of Rows to View")
    st.dataframe(df.head(int(number)))

selec = []
for col in df.columns:
   selec.append(col)
option = st.multiselect("Selectionner les colonnes",(selec))
st.table(df[option].head())

st.header("Discription Choices Boxes")

if st.button("Dataset Columns Chosen to Display Characteritics"):
    st.table(df[option].head())
if st.button("Afficher le type des colonnes du dataset"):
    st.table(df[option].dtypes)
if st.button("La shape du dataset, par lignes et par colonnes"):
    st.write(df[option].shape)
if st.button("Afficher les statistiques descriptives du dataset"):
    st.write(df[option].describe())

#graph = []
#graph = st.multiselect("What kind of graph ?",("Boxplot","Correlation"))
#st.write("You selected",len(graph),"graph")
#if 'Boxplot' in graph:
#    df[option].boxplot()
#    st.title("Distribution des Variables d'intérêt")
#    st.pyplot()
#elif 'Correlation' in graph:
#    st.write(sns.heatmap(df[option].corr(), annot=True))
#    st.pyplot()

st.header("What kind of graph ?")
status = st.radio("Choose ur way of drawing :",('Boxplot','Correlation','Distplot'))
if status == 'Boxplot':
    df[option].boxplot()
    st.title("Distribution des Variables d'intérêt")
    st.pyplot()
elif status == 'Correlation':
    st.write(sns.heatmap(df[option].corr(), annot=True))
    st.pyplot()
elif status == 'Distplot':
    st.write(sns.distplot(df[option]))
    st.pyplot()
