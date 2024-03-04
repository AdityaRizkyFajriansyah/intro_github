import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title('Bike Sharing Data Analysis')

# Baca data
df = pd.read_csv('day.csv')

# Widget untuk memilih jenis plot
plot_type = st.selectbox('Select plot type', ['Timeseries', 'Histogram', 'Correlation Heatmap'])

# Plot berdasarkan pilihan
if plot_type == 'Timeseries':
    plt.figure()
    plt.plot(df['dteday'], df['registered'], label='Registered')
    plt.plot(df['dteday'], df['casual'], label='Casual')
    plt.legend()
    st.pyplot()

elif plot_type == 'Histogram':
    plt.figure()
    plt.hist(df['cnt'], bins=20)
    st.pyplot()
    
else:
    corr = df[['cnt', 'temp', 'hum', 'windspeed']].corr()
    plt.figure()
    plt.pcolor(corr)
    st.pyplot()
