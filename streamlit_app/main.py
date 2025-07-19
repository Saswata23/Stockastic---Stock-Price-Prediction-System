import streamlit as st

# Set full width layout
st.set_page_config(page_title="Stockastic", layout="wide")

# Centered layout with larger image
st.markdown("""
    <div style='text-align: center; padding-top: 50px;'>
        <img src='https://plus.unsplash.com/premium_photo-1663931932651-ea743c9a0144?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' 
             alt='Stockastic logo' style='width: 500px; max-width: 90%; border-radius: 20px; margin-bottom: 10px;'/>
        <h1 style='font-size: 3em; margin-bottom: 0px;'>Stockastic</h1>
        <p style='font-size: 1.3em; max-width: 800px; margin:auto;'>
            AI-powered Stock Price Forecasting and Insights.<br><br>
            Leverage machine learning, real-time financial news, and technical indicators to forecast stock prices
            with greater confidence. Whether you're a financial analyst or a curious investor, Stockastic helps you turn market data into smarter decisions.
        </p>
    </div>
""", unsafe_allow_html=True)


