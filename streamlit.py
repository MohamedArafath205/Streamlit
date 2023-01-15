import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

# loading the models
model = pickle.load(open('model.sav', 'rb'))

# Title of the page
st.title('Rock or Mine Prediction')

input_data = st.text_input("Enter the values ")

import numpy as np
input_data_array = np.asarray(input_data)
input = input_data_array.reshape(1,-1)
prediction = model.predict(input)
print(prediction)
    
st.success(model_predict)
