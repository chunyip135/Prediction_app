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
    train = pd.read_csv("train_file.csv")
    test = pd.read_csv("test_file.csv")
    full = train.append(test) 
    return full

def train_model(df, random_state = 123):
    model = RandomForestClassifier(random_state = random_state)
