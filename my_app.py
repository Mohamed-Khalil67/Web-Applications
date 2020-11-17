import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import plotly.express as px


@st.cache
def get_data():
    return pd.read_csv("https://raw.githubusercontent.com/Mohamed-Khalil67/Machine-Learning-Mini-Project/main/diabetes.csv")

df = get_data()

st.title("Streamlit 101: An in-depth introduction")
st.markdown("Welcome to this in-depth introduction to how to Use diabetes Dataset")
st.header("Diabetes Patients Listings: data at a glance")

if st.checkbox("Show DataSet Rows of header"):
    number = st.number_input("Number of Rows to View")
    st.dataframe(df.head(int(number)))

#selec = []
#for col in df.columns:
#    selec.append(col)
#location = set.multiselect("Selectionner les colonnes",(selec))
#st.table(ds[location].head())

option = st.multiselect('What Columns to choose?',('Pregnancies', 'Glucose', 'BloodPressure', 'Insulin','BMI','DiabetesPedigreeFunction', 'Age','Outcome'))

if st.button("Columns Chosen to Display"):
    st.table(df[option].head())
    st.markdown("Afficher le type des colonnes du dataset")
    st.table(df[option].dtypes)
    st.markdown("La shape du dataset, par lignes et par colonnes")
    st.write(df[option].shape)
    st.markdown("Afficher les statistiques descriptives du dataset")
    st.write(df[option].describe())

if st.button("Show Boxplot"):
    df.boxplot()
    st.title("Distribution des Variables d'intérêt")
    st.pyplot()

if st.button("Show Correlation"):
    st.write(sns.heatmap(df.corr(), annot=True))
    st.pyplot()
