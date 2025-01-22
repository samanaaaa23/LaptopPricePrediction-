import streamlit as st
import pickle
import numpy as np
import pandas as pd  # Import pandas for DataFrame creation

# Load Model and Data
df = pickle.load(open('df.pkl', 'rb'))
pipe = pickle.load(open('pipe.pkl', 'rb'))

st.title("Laptop Price Predictor")

# For Laptop Brand
Company = st.selectbox('Company Brand', df['Company'].unique())

# For Laptop Type
Type = st.selectbox('Types of Laptop', df['TypeName'].unique())

# For RAM
Ram = st.selectbox('RAM of Laptop (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])

# For Weight of the Laptop
weight = st.number_input('Weight of Laptop (in KG)')

# For Touchscreen
Touchscreen = st.selectbox('Is Laptop Touchscreen?', ['No', 'Yes'])
Touchscreen = 1 if Touchscreen == 'Yes' else 0

# For IPS
IPS = st.selectbox('IPS Display?', ['No', 'Yes'])
IPS = 1 if IPS == 'Yes' else 0

# For Screen Size
Screen_Size = st.number_input('Screen Size of Laptop')

# For Screen Resolution
Screen_Resolution = st.selectbox(
    'Screen Resolution',
    ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440']
)

# For CPU Brand
Cpu_Brand = st.selectbox('CPU Brand', df['Cpu Brand'].unique())

# For HDD
HDD = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])

# For SSD
SSD = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])

# For GPU
GPU = st.selectbox('GPU', df['Gpu Brand'].unique())

# For Operating System
Operating_System = st.selectbox('Operating System', df['Operating System'].unique())

# Predict Button
if st.button('Predict Laptop Price'):
    # Calculate PPI
    X_resolution = int(Screen_Resolution.split('x')[0])
    Y_resolution = int(Screen_Resolution.split('x')[1])
    PPI = ((X_resolution ** 2) + (Y_resolution ** 2)) ** 0.5 / Screen_Size

    # Create a pandas DataFrame with user inputs
    query = pd.DataFrame([{
        'Company': Company,
        'TypeName': Type,
        'Ram': Ram,
        'Weight': weight,
        'Touchscreen': Touchscreen,
        'IPS': IPS,
        'PPI': PPI,
        'Cpu Brand': Cpu_Brand,
        'HDD': HDD,
        'SSD': SSD,
        'Gpu Brand': GPU,
        'Operating System': Operating_System
    }])

    # Make the prediction
    try:
        predicted_price = int(np.exp(pipe.predict(query)[0]))
        st.title(f"The predicted price of this Laptop = {predicted_price} euros")
    except Exception as e:
        st.error(f"Error: {str(e)}")
