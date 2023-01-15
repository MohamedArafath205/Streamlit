import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

# loading the models
model = pickle.load(open('model.sav', 'rb'))

# Title of the page
st.title('Rock or Mine Prediction')

input_ = st.text_input("Enter the values ")

final = ''

input_array = input.asarray(input_)

input_np = input_array.reshape(1,-1)

if st.button('Predict'):
    model_predict = model.predict(input_np)
    
    if(model_predict[0] == 'M'):
        prediction = 'Mine'
    else:
        prediction = 'Rock'
    
st.success(prediction)
