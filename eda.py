import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from phik.report import plot_correlation_matrix
from PIL import Image

#membuat function untuk nantinya dipanggil di app.py
def run():
    st.title('Welcome to Explaration Data Analysis')
#Memanggil data csv 
    df= pd.read_csv(r'rideshare_kaggle.csv')

#menampilakn 5 data teratas
    st.table(df.head(5))


#menampilakn phik matrix
    st.title('phik correlation matrix')
    image = Image.open('charts1.jpg')
    st.image(image, caption='figure 1')

#menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('lorem ipsum')




