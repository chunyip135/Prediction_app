import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier

# import data
# ML model train
# input data
# convert into dataframe
# output prediction

st.title("Loan Prediction")

@st.cache
def load_data():
    train = pd.read_csv("https://raw.githubusercontent.com/chunyip135/Prediction_app/main/train_file.csv")
    return  train

def train_model(df, random_state = 123):
    model = RandomForestClassifier(random_state = random_state)
    
