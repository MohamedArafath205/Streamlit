import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

# loading the models
model = pickle.load(open('model.sav', 'rb'))

# Title of the page
st.title('Rock or Mine Prediction')


# Get input array from user
input_array = st.text_input("Enter the elements of the array, separated by commas: ")

# Convert input string to list of integers
input_list = [float(x) for x in input_array.split(",")]

# Convert list to numpy array
input_np = np.array(input_list)

# Reshape array to (1,-1) format
output_np = input_np.reshape(1,-1)

if st.button('Predict'):
    model_predict = model.predict(output_np)
    
    if(model_predict[0] == 'M'):
        prediction = 'Mine'
    else:
        prediction = 'Rock'
    
st.success(prediction)
