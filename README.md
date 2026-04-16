👨‍💻 Naved Shaikh

📧 navedrys@gmail.com
 | 📱 7414991107
🔗 LinkedIn: https://linkedin.com/in/your-link

💻 GitHub: https://github.com/your-link

💳 Credit Risk Prediction using ANN

✨ A production-ready Machine Learning Web App that predicts whether a customer is a credit risk using an Artificial Neural Network (ANN).

🚀 Built with a complete pipeline: Data → Model → Deployment

🌟 Why This Project Stands Out
✔ Real-world financial use case
✔ End-to-End ML pipeline
✔ Deep Learning (ANN) implementation
✔ Deployed using Streamlit
✔ Handles preprocessing + prediction
🌳 Workflow (Tree Structure)
📦 Credit Risk Prediction System
│
├── 📥 Data Layer
│   ├── Load Dataset (German Credit Data)
│   ├── Data Cleaning
│   └── Missing Value Handling
│
├── 🔄 Preprocessing Layer
│   ├── Encoding (Categorical → Numeric)
│   ├── Feature Selection
│   └── Feature Scaling (StandardScaler)
│
├── ✂️ Data Split
│   ├── Training Data (80%)
│   └── Testing Data (20%)
│
├── 🧠 Model Layer (ANN)
│   ├── Input Layer
│   ├── Dense Layer (64, ReLU)
│   ├── Dense Layer (32, ReLU)
│   ├── Dense Layer (16, ReLU)
│   └── Output Layer (Sigmoid)
│
├── 📊 Evaluation Layer
│   ├── Accuracy
│   ├── Confusion Matrix
│   ├── Precision / Recall
│   └── Loss Analysis
│
├── 🔮 Prediction Layer
│   ├── User Input (Streamlit UI)
│   ├── Feature Scaling
│   └── Model Prediction
│
└── 🌐 Deployment Layer
    ├── Streamlit Web App
    ├── Clean UI
    └── Real-time Prediction
🧠 Model Architecture
Input Features → Dense(64) → Dense(32) → Dense(16) → Output(1)

Activation Functions:

ReLU → Hidden Layers
Sigmoid → Output Layer
🎯 Output
Prediction	Meaning
1	✅ Low Risk (Loan Approved)
0	❌ High Risk (Loan Rejected)
⚙️ Tech Stack
🐍 Python
🧠 TensorFlow / Keras
📊 Pandas, NumPy
⚙️ Scikit-learn
🌐 Streamlit
💡 App Features
✨ Simple and clean UI
⚡ Fast predictions
📊 Real-time results
🧠 Deep learning powered
📈 Model Performance
Accuracy: ~75–85%
Improvements applied:
Class imbalance handling
Feature scaling
Optimized ANN architecture
🚀 Run Locally
pip install -r requirements.txt
streamlit run streamlit_app.py
🔮 Future Improvements
Hyperparameter tuning
UI/UX enhancements
Cloud deployment (AWS / Render)
More feature inputs
⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
