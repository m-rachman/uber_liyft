import streamlit as st
import pandas as pd
import pickle
from PIL import Image

def run():
# Load All Files

    with open('pipeline_model.pkl', 'rb') as file:
        full_process = pickle.load(file)


    distance = st.number_input(label='input your distance here',min_value=0.0,max_value=7.5)
    surge_multiplier = st.selectbox(label='choose your surge_multiplier here',options=[1.  , 1.25, 2.5 , 2.  , 1.75, 1.5 , 3.  ])
    name = st.selectbox(label='choose your cab name here',options=['Shared', 'Lux', 'Lyft', 'Lux Black XL', 'Lyft XL', 'Lux Black',
       'UberXL', 'Black', 'UberX', 'WAV', 'Black SUV', 'UberPool'])
    product_id = st.selectbox(label='choose your product id here',options=['lyft_line', 'lyft_premier', 'lyft', 'lyft_luxsuv', 'lyft_plus',
       'lyft_lux', 'uber_line', 'uber_premier', 'uber', 'uber_luxsuv',
       'uber_plus', 'uber_lux'])
    
    st.write('In the following is the result of the data you have input : ')
    
    data_inf = pd.DataFrame({
         'distance' : distance,
        'surge_multiplier' : surge_multiplier,
        'name' : name ,
        'product_id' : product_id,
        }, index=[0])

    st.table(data_inf)


    if st.button(label='predict'):
    
        # Melakukan prediksi data dummy
        y_pred_inf = full_process.predict(data_inf)

        
        st.metric(label="Here is a prediction of your travel costs : ", value = y_pred_inf[0])

    # If your data is a classification, you can follow the example below 
        # if y_pred_inf[0] == 0:
        #     st.write('Pasien tidak terkena jantung')
        #     st.markdown("[Cara Cegah Serangan Jantung](https://www.siloamhospitals.com/informasi-siloam/artikel/cara-cegah-serangan-jantung-di-usia-muda)")

        # else:
        #     st.write('Pasien kemungkinan terkena jantung')
        #     st.markdown("[Cara Hidup Sehat Sehabis Terkena Serangan Jantung](https://lifestyle.kompas.com/read/2021/11/09/101744620/7-pola-hidup-sehat-setelah-mengalami-serangan-jantung?page=all)")
