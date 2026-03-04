"""
Neural Canvas - MNIST Digit Recognition Web Application
========================================================
A Streamlit app for real-time handwritten digit prediction
using a trained CNN model on the MNIST dataset.

Author: Osama Abd El Mohsen
Version: 2.0.0
"""

import streamlit as st
from streamlit_drawable_canvas import st_canvas

from styles import CSS
from components import (
    get_header,
    get_flow_arrow,
    get_preview_placeholder,
    get_result_display,
    get_waiting_state,
    get_probability_bars,
    get_pipeline_widget,
    get_model_architecture,
    get_footer,
)
from prediction import load_model, process_canvas_image, predict_digit


# ===================== Page Config =====================
st.set_page_config(
    page_title="MNIST Digit Classification | CNN",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://github.com',
        'Report a bug': 'https://github.com',
        'About': '# MNIST Digit Classification\nCNN-powered handwritten digit recognition.'
    }
)

# Apply custom CSS
st.markdown(CSS, unsafe_allow_html=True)


# ===================== Session State =====================
if "canvas_key" not in st.session_state:
    st.session_state.canvas_key = 0
if "processed_image" not in st.session_state:
    st.session_state.processed_image = None
if "prediction_result" not in st.session_state:
    st.session_state.prediction_result = None
if "all_probabilities" not in st.session_state:
    st.session_state.all_probabilities = None


# ===================== Load Model =====================
model = load_model()


# ===================== Header =====================
st.markdown(get_header(), unsafe_allow_html=True)


# ===================== Main Layout =====================
st.markdown(
    '<p class="section-label">Draw a Digit. Let the AI Recognize It</p>',
    unsafe_allow_html=True
)

# 5-column layout: Canvas | Arrow | Preview | Arrow | Prediction
col_canvas, col_arrow1, col_preview, col_arrow2, col_prediction = st.columns(
    [1, 0.2, 1, 0.2, 1.2], gap="small"
)

with col_canvas:
    st.markdown('<p class="step-label"><span class="step-num">01</span>Draw Digit</p>', unsafe_allow_html=True)
    canvas_result = st_canvas(
        fill_color="rgba(0, 0, 0, 1)",
        stroke_width=18,
        stroke_color="#FFFFFF",
        background_color="#0a0a1a",
        height=280,
        width=280,
        drawing_mode="freedraw",
        display_toolbar=True,
        key=f"canvas_{st.session_state.canvas_key}",
    )

with col_arrow1:
    st.markdown(get_flow_arrow("Resize"), unsafe_allow_html=True)

with col_preview:
    st.markdown('<p class="step-label"><span class="step-num">02</span>(28×28) Preprocessed Image</p>', unsafe_allow_html=True)
    preview_placeholder = st.container()

with col_arrow2:
    st.markdown(get_flow_arrow("CNN"), unsafe_allow_html=True)

with col_prediction:
    st.markdown('<p class="step-label"><span class="step-num">03</span>Model Prediction</p>', unsafe_allow_html=True)
    result_container = st.empty()
    prob_container = st.empty()


# ===================== Predict Button =====================
st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)

_, btn_col, _ = st.columns([2, 1, 2])
with btn_col:
    predict_button = st.button(
        "⚡ Predict Digit",
        use_container_width=True,
        key="predict_btn"
    )


# ===================== Prediction Logic =====================
if predict_button and canvas_result.image_data is not None:
    # Process and predict
    processed_img = process_canvas_image(canvas_result.image_data)
    predicted_digit, confidence, all_probs = predict_digit(model, processed_img)
    
    # Store in session state
    st.session_state.processed_image = processed_img
    st.session_state.prediction_result = (predicted_digit, confidence)
    st.session_state.all_probabilities = all_probs


# ===================== Display Updates =====================
# Preview image
with preview_placeholder:
    if st.session_state.processed_image is not None:
        st.image(st.session_state.processed_image, width=280, clamp=True)
    else:
        st.markdown(get_preview_placeholder(), unsafe_allow_html=True)

# Result display
if st.session_state.prediction_result is not None:
    digit, conf = st.session_state.prediction_result
    result_container.markdown(get_result_display(digit, conf), unsafe_allow_html=True)
    
    if st.session_state.all_probabilities is not None:
        prob_container.markdown(
            get_probability_bars(st.session_state.all_probabilities, digit),
            unsafe_allow_html=True
        )
else:
    result_container.markdown(get_waiting_state(), unsafe_allow_html=True)


# ===================== Pipeline & Architecture Widgets =====================
widget_col1, widget_col2 = st.columns(2, gap="medium")
with widget_col1:
    st.markdown(get_pipeline_widget(), unsafe_allow_html=True)
with widget_col2:
    st.markdown(get_model_architecture(), unsafe_allow_html=True)

# ===================== Footer =====================
st.markdown(get_footer(), unsafe_allow_html=True)
