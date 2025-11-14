import streamlit as st
import pickle
import numpy as np
import pandas as pd   # <-- REQUIRED to load df.pkl

# load data + model
df = pickle.load(open("df.pkl", "rb"))
pipe = pickle.load(open("pipe.pkl", "rb"))

st.title("Car Price Predictor App ")

company = st.selectbox("Car Brand", df['Company'].unique())
fuel = st.selectbox("Fuel Type", df['fuel'].unique())
seller_type = st.selectbox("Seller Type", df['seller_type'].unique())
transmission = st.selectbox("Transmission", df['transmission'].unique())
owner = st.selectbox("Previous Owners", df['owner'].unique())

km_driven = st.slider(
    "Kilometers Driven",
    min_value=int(df['km_driven'].min()),
    max_value=int(df['km_driven'].max()),
    value=int(df['km_driven'].median())
)

car_age = st.slider(
    "Car Age (Years)",
    min_value=0,
    max_value=int(df['car_age'].max()),
    value=5
)

if st.button("PREDICT PRICE"):

    query = np.array([[company, km_driven, fuel, seller_type,
                       transmission, owner, car_age]])

    output = pipe.predict(query)[0]
    output = int(round(output, -3))

    st.subheader("Estimated Selling Price:")
    st.subheader("₹ " + str(output))
