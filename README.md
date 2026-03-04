# 🔢 MNIST Digit Classification with Neural Networks

A complete deep learning project featuring EDA, model training, and an interactive web application for handwritten digit recognition.

## 🎨 Features

### Web Application

- **Interactive Drawing Canvas**: Draw digits with your mouse
- **Real-time Prediction**: Instant AI predictions with confidence scores
- **Modern UI**: Beautiful neon-themed design with smooth animations
- **Probability Distribution**: View prediction probabilities for each digit

### Machine Learning Pipeline

- **Exploratory Data Analysis**: Complete data quality and distribution analysis
- **Two Model Architectures**: Baseline Dense NN and optimized CNN
- **Data Augmentation**: Rotation, zoom, and shift transformations
- **Model Evaluation**: Comprehensive metrics including confusion matrix and classification report

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd app
pip install -r requirements.txt
```

### 2. Train the Model

Open and run the Jupyter notebook:

```bash
cd notebooks
jupyter notebook EDA_Modeling.ipynb
```

The notebook will:

- Load the MNIST dataset (70,000 images)
- Perform exploratory data analysis
- Train both Dense NN and CNN models
- Evaluate model performance (~99% accuracy with CNN)
- Save the trained model to `model/mnist_model.pkl`

### 3. Run the Streamlit App

```bash
cd app
streamlit run app.py
```

The app will open at `http://localhost:8501`

## 📱 How to Use

1. **Draw** a digit (0-9) on the canvas
2. **Click "🎯 Predict"** to get the prediction
3. **View** the result with confidence score
4. **Click "🗑️ Clear"** to draw another digit

## 🔧 Technical Details

- **Framework**: TensorFlow/Keras
- **Dataset**: MNIST (60,000 training + 10,000 test images)
- **Image Size**: 28×28 pixels (grayscale)
- **Accuracy**: ~99% on test set (CNN model)
- **Web Framework**: Streamlit

## 📊 Model Architectures

### Baseline Dense Neural Network

```text
Input (28×28) → Flatten (784)
    ↓
Dense (128 neurons) + ReLU + Dropout (30%)
    ↓
Dense (64 neurons) + ReLU + Dropout (30%)
    ↓
Output (10 classes) + Softmax
```

### CNN with Data Augmentation (Production Model)

```text
Block 1: Conv2D(32) → BatchNorm → Conv2D(32) → BatchNorm → MaxPool → Dropout(25%)
    ↓
Block 2: Conv2D(64) → BatchNorm → Conv2D(64) → BatchNorm → MaxPool → Dropout(25%)
    ↓
Flatten → Dense(128) → BatchNorm → Dropout(50%) → Softmax(10)
```

### Data Augmentation

| Transformation | Range | Purpose |
|----------------|-------|---------|
| Rotation | ±10° | Handle tilted digits |
| Zoom | ±10% | Handle size variations |
| Width Shift | ±10% | Handle horizontal positioning |
| Height Shift | ±10% | Handle vertical positioning |

## 💡 Tips for Best Results

- Write **large, clear digits**
- Leave **some margin** around the digit
- Use **dark pen on white background**
- Stay within the canvas area

## 📁 Project Structure

```text
├── app/
│   ├── app.py              # Main Streamlit application entry point
│   ├── components.py       # HTML template components (header, footer, widgets)
│   ├── prediction.py       # Image processing & model prediction logic
│   ├── styles.py           # CSS styles and theming
│   └── requirements.txt    # Python dependencies
├── assets/                 # Static assets
├── model/
│   └── mnist_model.pkl     # Trained CNN model
├── notebooks/
│   ├── EDA_Modeling.ipynb  # Complete ML pipeline notebook
│   └── utils.py            # Helper functions for visualization & metrics
└── README.md
```

## 🐛 Troubleshooting

**"Model not found" error?**

- Run the `EDA_Modeling.ipynb` notebook and uncomment the model save cell

**Drawing isn't working?**

- Ensure `streamlit-drawable-canvas` is installed: `pip install streamlit-drawable-canvas`

**Port already in use?**

- Run: `streamlit run app.py --server.port 8502`

## 📝 Requirements

- Python 3.8+
- TensorFlow 2.x
- See [requirements.txt](app/requirements.txt) for full list

## 📚 Key Dependencies

| Package | Purpose |
|---------|---------|
| TensorFlow/Keras | Deep learning framework |
| Streamlit | Web application |
| NumPy/Pandas | Data manipulation |
| Matplotlib/Seaborn | Visualization |
| scikit-learn | Metrics and evaluation |
| joblib | Model serialization |

---

**Enjoy predicting!** 🎉
