import numpy as np
import pickle
import pandas as pd
import streamlit as st 
st.title("ENERGY CONSUMPTION PREDICTION FOR INDIA,USA AND CHINA")
option = st.selectbox(
     'Please select the country',
     ('India', 'USA', 'China'))

year = st.text_input("year"," Type year")



pickle_in = open("india.pkl","rb")
model_india = pickle.load(pickle_in)


pickle_in = open("usa.pkl","rb")
model_usa = pickle.load(pickle_in)

pickle_in = open("china.pkl","rb")
model_china= pickle.load(pickle_in)


if st.button("Predict"):
	if option == "India":
		result= model_india.predict([[int(year)]])

	if option == "USA":
		result= model_usa.predict([[int(year)]])

	if option == "China":
		result= model_china.predict([[int(year)]])
	
	st.success('The Predicted Electricity Consumption of {} for the year {} is {} KwH'.format(option,year,round(result[0],3)))








    