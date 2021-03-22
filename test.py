import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
st.text_input("User name")
uploaded_file = st.file_uploader("Choose a file",type=['csv'])
click= st.button('submit')

if click ==True:
    df=pd.read_csv(uploaded_file)
    st.write(df.head())
    fig = plt.figure()
    ax = fig.add_subplot(2,2,1)

    ax.scatter(df["petal.length"],df["sepal.length"])

    ax.set_xlabel("petal.length")
    ax.set_ylabel("sepal.length")

    st.write(fig)
