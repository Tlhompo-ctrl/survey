# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 00:29:52 2025

@author: Lenovo
"""

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Set page title
st.set_page_config(page_title="Data analysis on survey dataset", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to:", ["Survey Dataset"])

if menu == "Survey Dataset":
    st.title("Doing some data analysis on the survey dataset")
    
    # Load dataset
    survey_df = pd.read_csv("surveys.csv")
    
    if st.button("Read in the csv file"):
        st.write("Dataset loaded successfully!")
    
    # Button to display the first 15 rows of the dataset
    if st.button("Show First 15 Rows"):
        st.dataframe(survey_df.head(15))
    
    # Button to drop NaN values and display first 15 and last 5 rows
    if st.button("Drop NaN and Show Cleaned Data"):
        survey_df.dropna(inplace=True)
        st.dataframe(survey_df.head(15))
        st.dataframe(survey_df.tail())
    
    # Button to show statistics of the weight column
    if st.button("Show Weight Stats"):
        st.write(survey_df["weight"].describe())
    
    # Button to show grouped stats by sex
    if st.button("Show Stats by Sex"):
        grouped_data = survey_df.groupby("sex").describe()
        st.write(grouped_data)
    
    # Button to show the mean of the grouped data
    if st.button("Show Mean of Grouped Data"):
        st.write(survey_df.groupby("sex").mean(numeric_only=True))
    
    # Button to show the number of unique values in the grouped data
    if st.button("Show Unique Counts in Grouped Data"):
        st.write(survey_df.groupby("sex").nunique())
    
    # Button to show species count
    if st.button("Show Species Count"):
        species_counts = survey_df.groupby('species_id')['record_id'].count()
        st.write(species_counts)
    
    # Button to display species count bar graph
    if st.button("Show Species Count Bar Graph"):
        species_counts = survey_df.groupby('species_id')['record_id'].count()
        fig, ax = plt.subplots()
        species_counts.plot(kind='bar', ax=ax)
        ax.set_xlabel("Species ID for the Record ID only")
        ax.set_ylabel("Number of species")
        ax.set_title("Number of species in the record ID")
        st.pyplot(fig)
    
    # Button to display average weight per plot ID bar graph
    if st.button("Show Average Weight per Plot ID"):
        fig, ax = plt.subplots()
        survey_df.groupby("plot_id")["weight"].mean().plot(kind='bar', ax=ax, color="green")
        ax.set_ylabel("Weight")
        ax.set_xlabel("Plot ID")
        ax.set_title("The average weight across all species")
        st.pyplot(fig)
