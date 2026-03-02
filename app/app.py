from streamlit_drawable_canvas import st_canvas
import streamlit as st
from PIL import Image
import numpy as np
import joblib

# ===================== Page Config =====================
st.set_page_config(
    page_title="MNIST Digit Predictor",
    page_icon="🔢",
    layout="centered"
)

# ===================== Styling =====================
st.markdown("""
<style>
[data-testid="stMainBlockContainer"] {
    max-width: 800px;
}
.stApp {
    background: linear-gradient(135deg, #0f0f1e 0%, #1a1a2e 100%);
    color: #ffffff;
}
.stButton>button {
    width: 100%;
    padding: 0.75rem 1rem;
    font-size: 1rem;
    border: none;
    border-radius: 12px;
    font-weight: 600;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}
.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
}
.result-box {
    text-align: center;
    padding: 2.5rem;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 20px;
    color: white;
    margin-top: 2rem;
    box-shadow: 0 10px 40px rgba(102, 126, 234, 0.4);
    animation: slideIn 0.5s ease-out;
}
@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
.prediction {
    font-size: 4rem;
    font-weight: 900;
    margin: 1rem 0;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}
.confidence {
    font-size: 1.2rem;
    opacity: 0.95;
    font-weight: 500;
}
.title-text {
    text-align: center;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.5rem;
}
.caption-text {
    text-align: center;
    color: #999;
    font-size: 1rem;
    margin-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)

# ===================== Session State =====================
if "canvas_key" not in st.session_state:
    st.session_state.canvas_key = 0

if "processed_image" not in st.session_state:
    st.session_state.processed_image = None

if "prediction_result" not in st.session_state:
    st.session_state.prediction_result = None

# ===================== Title =====================
st.markdown('<div class="title-text"><h1>🔢 MNIST Digit Predictor</h1></div>', unsafe_allow_html=True)
st.markdown('<div class="caption-text">Draw a digit and see how the model interprets it</div>', unsafe_allow_html=True)

# ===================== Load Model =====================
MODEL_PATH = "../model/mnist_model.pkl"
model = joblib.load(MODEL_PATH)

# ===================== Layout =====================
col_canvas, col_preview = st.columns([2, 1])

with col_canvas:
    canvas_result = st_canvas(
        fill_color="rgba(0, 0, 0, 1)",
        stroke_width=18,
        stroke_color="rgba(0, 0, 0, 1)",
        background_color="rgba(255, 255, 255, 1)",
        height=280,
        width=280,
        drawing_mode="freedraw",
        display_toolbar=True,
        key=f"canvas_{st.session_state.canvas_key}",
    )

with col_preview:
    st.markdown("### 🖼 Processed (28×28)")
    preview_container = st.empty()

# ===================== Buttons =====================
col1, col2 = st.columns(2)

with col1:
    predict_button = st.button("🎯 Predict", use_container_width=True)

with col2:
    clear_button = st.button("🗑️ Clear", use_container_width=True)

# ===================== Clear =====================
if clear_button:
    # Force canvas reset by incrementing key
    st.session_state.canvas_key += 1
    st.session_state.processed_image = None
    st.session_state.prediction_result = None
    # Clear any temporary state
    st.session_state.pop("canvas_image_data", None)
    st.rerun()

# ===================== Predict =====================
if predict_button and canvas_result.image_data is not None:

    canvas_array = canvas_result.image_data[:, :, :3].astype("uint8")
    gray = np.dot(canvas_array[..., :3], [0.299, 0.587, 0.114]).astype("uint8")
    gray = 255 - gray

    gray[gray < 50] = 0
    gray[gray >= 50] = 255

    coords = np.column_stack(np.where(gray > 0))
    if coords.size != 0:
        y_min, x_min = coords.min(axis=0)
        y_max, x_max = coords.max(axis=0)
        digit = gray[y_min:y_max+1, x_min:x_max+1]
    else:
        digit = gray

    h, w = digit.shape
    if h > w:
        new_h = 20
        new_w = int(w * (20 / h))
    else:
        new_w = 20
        new_h = int(h * (20 / w))

    digit_resized = Image.fromarray(digit).resize(
        (new_w, new_h),
        Image.Resampling.LANCZOS
    )
    digit_resized = np.array(digit_resized)

    final_img = np.zeros((28, 28), dtype=np.uint8)
    y_offset = (28 - new_h) // 2
    x_offset = (28 - new_w) // 2
    final_img[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = digit_resized

    st.session_state.processed_image = final_img

    image_array = final_img.astype("float32") / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    prediction = model.predict(image_array)
    predicted_class = np.argmax(prediction)
    confidence = float(prediction[0][predicted_class]) * 100

    st.session_state.prediction_result = (predicted_class, confidence)

# ===================== Update Preview =====================
if st.session_state.processed_image is not None:
    preview_container.image(
        st.session_state.processed_image,
        clamp=True,
        width=180
    )

# ===================== Result =====================
if st.session_state.prediction_result is not None:
    digit, conf = st.session_state.prediction_result

    st.markdown(f"""
        <div class='result-box'>
            <p>Your digit is:</p>
            <p class='prediction'>{digit}</p>
            <p class='confidence'>Confidence: {conf:.1f}%</p>
        </div>
    """, unsafe_allow_html=True)