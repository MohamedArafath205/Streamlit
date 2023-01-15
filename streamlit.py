import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

# loading the models
model = pickle.load(open('model.sav', 'rb'))

# Title of the page
st.title('Rock or Mine Prediction')

input_ = st.text_input("Enter the values ")

import numpy as np
input_data = [0.0491,0.0279,0.0592,0.127,0.1772,0.1908,0.2217,0.0768,0.1246,0.2028,0.0947,0.2497,0.2209,0.3195,0.334,0.3323,0.278,0.2975,0.2948,0.1729,0.3264,0.3834,0.3523,0.541,0.5228,0.4475,0.534,0.5323,0.3907,0.3456,0.4091,0.4639,0.558,0.5727,0.6355,0.7563,0.6903,0.6176,0.5379,0.5622,0.6508,0.4797,0.3736,0.2804,0.1982,0.2438,0.1789,0.1706,0.0762,0.0238,0.0268,0.0081,0.0129,0.0161,0.0063,0.0119,0.0194,0.014,0.0332]
input_data_array = np.asarray(input_data)
input = input_data_array.reshape(1,-1)
prediction = model.predict(input)
print(prediction)
    
st.success(model_predict)
