# UTS 36104 Data Visualisation and Narratives - Session 2 Part E (Multipage App)

This repository contains the completed multi-page Streamlit application developed according to the official Streamlit tutorial: [Create a multipage app](https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app).

## Features
- **Main Entrypoint (`streamlit_app.py`)**: Landing page with introduction, documentation links, and sidebar demo navigation.
- **Plotting Demo (`pages/1_📈_Plotting_Demo.py`)**: Interactive streaming line chart animation with animated progress bar.
- **Mapping Demo (`pages/2_🌍_Mapping_Demo.py`)**: 3D geospatial visualization of San Francisco bike rides and BART routes powered by Pydeck.
- **DataFrame Demo (`pages/3_📊_DataFrame_Demo.py`)**: Interactive Gapminder dataset exploration with dynamic country multiselection and Altair area chart visualization.

## Running Locally
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```
