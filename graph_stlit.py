import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

st.title("Maniplulation de données et création de graphiques")

data_choice = st.selectbox(label= "Quel data set veux tu utiliser ?", options= ["flights.csv","anscombe.csv", "attention.csv","diamonds.csv","car_crashes.csv"])

if data_choice == "flights.csv":
    data = pd.read_csv("flights.csv")
    st.dataframe(data)
    liste_col_x = data.columns.tolist()
    liste_col_y = data.columns.tolist()
if data_choice == "anscombe.csv":
    data = pd.read_csv("anscombe.csv")
    st.dataframe(data)
    liste_col_x = data.columns.tolist()
    liste_col_y = data.columns.tolist()
if data_choice == "attention.csv":
    data = pd.read_csv("attention.csv")
    st.dataframe(data)
    liste_col_x = data.columns.tolist()
    liste_col_y = data.columns.tolist()
if data_choice == "diamonds.csv":
    data = pd.read_csv("diamonds.csv")
    st.dataframe(data)
    liste_col_x = data.columns.tolist()
    liste_col_y = data.columns.tolist() 
if data_choice == "car_crashes.csv":
    data = pd.read_csv("car_crashes.csv")
    st.dataframe(data)
    liste_col_x = data.columns.tolist()
    liste_col_y = data.columns.tolist() 
    
col_choice_X = st.selectbox(label= "Quelle colonne pour les X", options= liste_col_x)
col_choice_y = st.selectbox(label= "Quelle colonne pour les Y", options= liste_col_y)

if col_choice_X == col_choice_y:
    st.text("Choisissez une colonne différente de votre X !")
    
graphs = ["bar_chart","scatter_chart","line_chart"]   
graph_choice = st.selectbox(label= "Choisissez un graphique", options= graphs)

if graph_choice == "bar_chart":
    sns.barplot(x= col_choice_X, y= col_choice_y, data= data)
    st.pyplot(plt.gcf())

if graph_choice == "scatter_chart":
    sns.scatterplot(x= col_choice_X, y= col_choice_y, data= data)
    st.pyplot(plt.gcf())

if graph_choice == "line_chart":
    sns.lineplot(x= col_choice_X, y= col_choice_y, data= data)
    st.pyplot(plt.gcf())
    
matrix = st.checkbox("Matrice de corrélation", value= False)
if matrix == True:
    corr = data[[col_choice_X, col_choice_y]]
    st.dataframe(corr)
    sns.heatmap(corr.corr())
    st.pyplot(plt.gcf())
    
