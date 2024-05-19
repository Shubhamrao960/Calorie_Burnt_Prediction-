
import streamlit as st
import numpy as np
import pandas as pd
import pickle

# laoding the model
rfr = pickle.load(open('rfr.pkl','rb'))
X_train = pd.read_csv('X_train.csv')

def pred(Gender,Age,Height,Weight,Duration,Heart_rate,Body_temp):
    features = np.array([[Gender,Age,Height,Weight,Duration,Heart_rate,Body_temp]])
    prediction = rfr.predict(features).reshape(1,-1)
    return prediction[0]


# web app
st.title("Calories Burn Prediction")
Gender = st.selectbox('Gender(Male:1 ,Female:0)', X_train['Gender'])
Age = st.selectbox('Age', X_train['Age'])
Height = st.selectbox('Height', X_train['Height'])
Weight = st.selectbox('Weight', X_train['Weight'])
Duration = st.selectbox('Duration (minutes)', X_train['Duration'])
Heart_rate = st.selectbox('Heart Rate (bpm)', X_train['Heart_Rate'])
Body_temp = st.selectbox('Body Temperature', X_train['Body_Temp'])

result = pred(Gender,Age,Height,Weight,Duration,Heart_rate,Body_temp)

if st.button('predict'):
    if result:
        st.write("You have consumed this calories :",result)
