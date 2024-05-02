from time import time

import requests
import streamlit as st

from src.frontend.config.iris import settings

st.title("Iris Model Training")

st.info(
    "This button allows you to update the performance of our machine learning model using the most recent data. By clicking here, you initiate the retraining process, which will enhance the accuracy and relevance of our predictions. Make sure you have updated data before proceeding.",
    icon="ℹ️",
)

retrain_button = st.button("Re-Train Model")

if retrain_button:
    now = time()
    requests.post(f"{settings.BACKEND_URL}{settings.TRAIN_ROUTE}")
    st.info(f"Model was retrained in {time() - now:.2f} seconds", icon="🎉")
