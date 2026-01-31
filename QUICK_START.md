# QUICK START GUIDE - ML ASSIGNMENT 2

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
streamlit run app.py
```

### Step 3: Open in Browser
Navigate to: `http://localhost:8501`

---

## 📊 What You Can Do

### 1. View Model Performance
- See all 6 models' evaluation metrics
- Identify best performing models
- Compare models visually

### 2. Make Predictions
- Upload test data (CSV format)
- Select a model
- Get predictions with probabilities
- View confusion matrix
- Download results

### 3. Compare Models
- Radar chart comparison
- Detailed model insights
- Performance rankings

---

## 📁 Project Files

```
├── app.py                      # Main Streamlit application
├── train_models.py             # Script to train models
├── requirements.txt            # Project dependencies
├── README.md                   # Full documentation
├── ASSIGNMENT_COMPLETION_SUMMARY.txt  # This assignment's status
└── model/                      # Trained models directory
    ├── *.pkl files            # Trained model files
    ├── metrics.csv            # Performance metrics
    └── test_data.csv          # Test data for predictions
```

---

## 🔄 Regenerate Models

To retrain all models with fresh data:

```bash
python train_models.py
```

This will:
- Generate synthetic banking dataset
- Train all 6 models
- Calculate metrics
- Save all artifacts

---

## 🌐 Deploy to Streamlit Cloud

1. Push code to GitHub
2. Go to https://streamlit.io/cloud
3. Sign in with GitHub
4. Click "New App"
5. Select this repository
6. Set main file to: `app.py`
7. Click Deploy

---

## 📊 Dataset Information

- **Instances:** 1000
- **Features:** 21
- **Target:** Binary (Yes/No)
- **Train/Test Split:** 80/20
- **Models:** 6 Classification Models
- **Metrics:** Accuracy, AUC, Precision, Recall, F1, MCC

---

## 🎯 Models Included

1. **Logistic Regression** - Linear baseline
2. **Decision Tree** - Tree-based classification
3. **K-Nearest Neighbors** - Instance-based learning
4. **Naive Bayes** - Probabilistic classifier
5. **Random Forest** - Ensemble (Bagging)
6. **XGBoost** - Ensemble (Gradient Boosting)

---

## 💡 Tips

- For custom predictions, prepare CSV with same features as training data
- Use sample test data to see example predictions
- Check Model Comparison page for radar chart visualization
- All metrics saved in `model/metrics.csv`

---

## ❓ Help

For full documentation: See `README.md`
For completion status: See `ASSIGNMENT_COMPLETION_SUMMARY.txt`

---

**Status:** ✅ All requirements met and tested
**Ready for:** GitHub submission & Streamlit deployment
