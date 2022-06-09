import numpy as np
import pickle
import pandas as pd
import streamlit as st 
st.title("ENERGY CONSUMPTION PREDICTION FOR INDIA,USA AND CHINA")
option = st.selectbox(
     'Which country you want to select?',
     ('India', 'USA', 'China'))

year = st.text_input("year")



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
	
	st.success('The predicted energy consumption is {} KwH'.format(round(result[0],3)))







    
