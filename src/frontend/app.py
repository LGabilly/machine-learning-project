import requests  # type: ignore
import streamlit as st
from st_pages import show_pages_from_config

from src.frontend.config.iris import settings

show_pages_from_config("src/frontend/.streamlit/pages.toml")
st.title("Iris Species Prediction")

sepal_length = st.slider("Sepal Length", 4.0, 8.0)
sepal_width = st.slider("Sepal Width", 2.0, 5.0)
petal_length = st.slider("petal Length", 1.0, 6.9)
petal_width = st.slider("petal Width", 0.0, 2.5)

params = {
    "sepal_length_cm": sepal_length,
    "sepal_width_cm": sepal_width,
    "petal_length_cm": petal_length,
    "petal_width_cm": petal_width,
}


response = requests.post(f"{settings.BACKEND_URL}{settings.API_ROUTE}", params=params)
if response.status_code == 200:
    prediction = response.json()
    predicted_species = prediction.get("species")
    st.write("Predicted Species :")
    path = str(settings.IMG_DIR / f"iris_{predicted_species}.jpeg")
    st.image(
        path,
        caption=predicted_species.title(),
        width=400,
    )
else:
    st.write("Something went wrong : 🫡")
