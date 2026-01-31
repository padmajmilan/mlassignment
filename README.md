# Machine Learning Assignment 2: UCI Banking Dataset Classification

## Problem Statement

This assignment implements a comprehensive machine learning classification pipeline on the UCI Bank Marketing dataset. The objective is to develop and evaluate multiple classification models to predict binary outcomes (customer subscription to term deposit). The project demonstrates end-to-end ML workflow including data preprocessing, model training, evaluation, and deployment via a web-based application.

## Dataset Description

**Dataset Name:** UCI Bank Marketing Dataset (Synthetic)
- **Source:** UCI Machine Learning Repository / Generated from UCI specifications
- **Total Instances:** 1000
- **Total Features:** 21
- **Target Variable:** Binary Classification (y: 'no' = 0, 'yes' = 1)
- **Class Distribution:** 
  - Negative Class (no): 896 instances (89.6%)
  - Positive Class (yes): 104 instances (10.4%)

### Feature Categories

**Categorical Features (9):**
- job: Type of job
- marital: Marital status
- education: Education level
- default: Has credit in default? (yes/no)
- housing: Has housing loan? (yes/no)
- loan: Has personal loan? (yes/no)
- contact: Contact communication type
- month: Last contact month of year
- poutcome: Outcome of previous campaign

**Numerical Features (5):**
- age: Age of client
- day: Last contact day of the month
- duration: Last contact duration in seconds
- campaign: Number of contacts performed during this campaign
- pdays: Number of days that passed since previous campaign contact

**Economic Features (6):**
- emp.var.rate: Employment variation rate
- cons.price.idx: Consumer price index
- cons.conf.idx: Consumer confidence index
- euribor3m: 3-month Euribor rate
- nr.employed: Number of employees

### Data Preprocessing

1. **Train-Test Split:** 80-20 stratified split
   - Training Set: 800 instances (80%)
   - Test Set: 200 instances (20%)
   
2. **Categorical Encoding:** Label Encoding for categorical variables
3. **Feature Scaling:** StandardScaler for numerical features
4. **Stratification:** Class-aware splitting to maintain class distribution

## Models Implemented

### 1. Logistic Regression
- **Type:** Linear Classification
- **Description:** Logistic regression uses a sigmoid function to model the probability of binary outcomes
- **Parameters:** max_iter=1000
- **Advantages:** Fast, interpretable, probabilistic outputs
- **Disadvantages:** Limited for non-linear relationships

### 2. Decision Tree Classifier
- **Type:** Tree-based Classification
- **Description:** Decision tree recursively splits features to minimize impurity
- **Parameters:** Default parameters with random_state=42
- **Advantages:** Non-parametric, interpretable, handles non-linear relationships
- **Disadvantages:** Prone to overfitting

### 3. K-Nearest Neighbors (kNN)
- **Type:** Instance-based Learning
- **Description:** Classifies instances based on majority vote of k nearest neighbors
- **Parameters:** n_neighbors=5
- **Advantages:** Simple, no training phase, flexible decision boundaries
- **Disadvantages:** Computationally expensive, sensitive to feature scaling

### 4. Naive Bayes Classifier
- **Type:** Probabilistic Classifier
- **Description:** Uses Bayes' theorem with strong independence assumption
- **Implementation:** Gaussian Naive Bayes
- **Advantages:** Fast, works well with small datasets, probabilistic framework
- **Disadvantages:** Independence assumption often violated in real data

### 5. Random Forest
- **Type:** Ensemble (Bagging)
- **Description:** Ensemble of decision trees with random feature selection
- **Parameters:** n_estimators=100, random_state=42
- **Advantages:** Reduces overfitting, handles non-linear relationships, feature importance
- **Disadvantages:** Less interpretable, higher computational cost

### 6. XGBoost
- **Type:** Ensemble (Gradient Boosting)
- **Description:** Sequential ensemble that minimizes residuals at each stage
- **Implementation:** GradientBoostingClassifier
- **Parameters:** n_estimators=100, random_state=42
- **Advantages:** High performance, handles complex relationships, regularization built-in
- **Disadvantages:** Harder to interpret, longer training time

## Model Performance Comparison

| ML Model Name | Accuracy | AUC | Precision | Recall | F1 | MCC |
|---|---|---|---|---|---|---|
| Logistic Regression | 0.8950 | 0.5560 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| Decision Tree | 0.8250 | 0.4819 | 0.0625 | 0.0476 | 0.0541 | -0.0409 |
| kNN | 0.8950 | 0.5557 | 0.5000 | 0.0476 | 0.0870 | 0.1295 |
| Naive Bayes | 0.8950 | 0.5770 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| Random Forest | 0.8950 | 0.4977 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| XGBoost | 0.8700 | 0.4874 | 0.0000 | 0.0000 | 0.0000 | -0.0548 |

### Evaluation Metrics Description

1. **Accuracy:** Proportion of correct predictions among total predictions
   - Formula: (TP + TN) / (TP + TN + FP + FN)

2. **AUC (Area Under ROC Curve):** Measures model's ability to distinguish between classes
   - Range: 0 to 1 (0.5 = random, 1.0 = perfect)

3. **Precision:** Of predicted positives, how many are actually positive
   - Formula: TP / (TP + FP)
   - Important when false positives are costly

4. **Recall:** Of actual positives, how many did model identify
   - Formula: TP / (TP + FN)
   - Important when false negatives are costly

5. **F1 Score:** Harmonic mean of Precision and Recall
   - Formula: 2 × (Precision × Recall) / (Precision + Recall)
   - Balanced metric for imbalanced datasets

6. **MCC (Matthews Correlation Coefficient):** Correlation coefficient between predicted and actual
   - Range: -1 to 1 (0 = random, 1 = perfect)
   - Works well for imbalanced datasets

## Model Observations and Analysis

### Logistic Regression
- **Strengths:** Good accuracy (89.50%), reasonable AUC (0.5560)
- **Weaknesses:** Precision and Recall both 0, indicating conservative predictions (predicting only majority class)
- **Observation:** Model struggles with imbalanced data, biased towards predicting 'no'
- **Use Case:** Fast baseline model, but needs class balancing techniques

### Decision Tree
- **Strengths:** Interpretable, handles non-linear relationships
- **Weaknesses:** Lowest accuracy (82.50%), lowest AUC (0.4819)
- **Observation:** Overfitting or underfitting issues visible in poor generalization
- **Use Case:** Not suitable for this imbalanced dataset without pruning/balancing

### K-Nearest Neighbors
- **Strengths:** Best Precision (0.5000), non-zero F1 and MCC scores (0.0870, 0.1295)
- **Weaknesses:** Low Recall (0.0476), struggles with imbalance despite better precision
- **Observation:** Very conservative in predicting positive class; better discrimination than others
- **Use Case:** When false positives must be minimized

### Naive Bayes
- **Strengths:** Good Accuracy (89.50%), best AUC (0.5770) among all models
- **Weaknesses:** Zero Precision and Recall (predicting only majority class)
- **Observation:** AUC suggests good probabilistic ranking despite poor hard predictions
- **Use Case:** Probabilistic predictions useful even when hard predictions fail

### Random Forest
- **Strengths:** Good accuracy (89.50%), handles non-linear relationships
- **Weaknesses:** Zero Precision and Recall, predicting majority class only
- **Observation:** Even ensemble approach struggles with extreme imbalance
- **Use Case:** Requires sampling techniques (SMOTE, class weights) to be effective

### XGBoost
- **Strengths:** Sequential learning approach, handles feature interactions
- **Weaknesses:** Lowest F1 score (-0.0548 MCC), some overfitting
- **Observation:** Strong baseline but needs hyperparameter tuning and class balancing
- **Use Case:** With proper tuning and balanced data, typically highest performer

## Key Findings

1. **Class Imbalance Impact:** Dataset's 90-10 class distribution severely affects model performance
2. **Majority Class Bias:** Most models default to predicting majority class
3. **AUC vs Accuracy:** AUC scores more useful than accuracy for this imbalanced dataset
4. **kNN Performance:** Best discriminative ability despite low recall
5. **Ensemble Methods Need Tuning:** Random Forest and XGBoost need class weighting or SMOTE for improvement

## Recommendations for Future Work

1. **Address Class Imbalance:**
   - Apply SMOTE (Synthetic Minority Oversampling)
   - Use class weights in loss function
   - Adjust decision threshold

2. **Feature Engineering:**
   - Feature selection to reduce noise
   - Create interaction features
   - Temporal feature extraction

3. **Hyperparameter Tuning:**
   - Grid/Random search for optimal parameters
   - Cross-validation for robust evaluation

4. **Ensemble Stacking:**
   - Combine models for better performance
   - Meta-learner for optimal predictions

5. **Alternative Algorithms:**
   - LightGBM, CatBoost for faster training
   - SVM with appropriate kernel
   - Neural Networks for complex patterns

## Project Structure

```
ML_Assignment_2_Project/
├── app.py                          # Streamlit application
├── train_models.py                 # Model training script
├── requirements.txt                # Project dependencies
├── README.md                       # This file
└── model/                          # Trained models directory
    ├── Logistic_Regression.pkl
    ├── Decision_Tree.pkl
    ├── kNN.pkl
    ├── Naive_Bayes.pkl
    ├── Random_Forest.pkl
    ├── XGBoost.pkl
    ├── scaler.pkl
    ├── label_encoders.pkl
    ├── test_data.csv
    └── metrics.csv
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd ML_Assignment_2_Project
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Method 1: Streamlit Local Server
```bash
streamlit run app.py
```
The app will open at `http://localhost:8501`

### Method 2: Train Models
```bash
python train_models.py
```
This regenerates all models with fresh training data

## Using the Streamlit Application

### Features Available

1. **📈 Model Performance Dashboard**
   - View all models' evaluation metrics
   - Identify best models for each metric
   - Compare performance with visualizations

2. **🎯 Prediction Interface**
   - Upload custom test data (CSV)
   - Select specific model for predictions
   - Get prediction probabilities and confidence scores
   - View confusion matrix and classification report
   - Download prediction results

3. **📋 Detailed Model Comparison**
   - Side-by-side metrics comparison
   - Radar chart visualization
   - Individual model insights and rankings

4. **📚 About Section**
   - Dataset documentation
   - Model descriptions
   - Evaluation metrics explanation
   - Usage guidelines

## Deployment on Streamlit Community Cloud

1. **Prepare Repository:**
   - Push code to GitHub
   - Ensure `requirements.txt` is up-to-date
   - Verify all model files are included

2. **Deploy on Streamlit Cloud:**
   - Go to https://streamlit.io/cloud
   - Sign in with GitHub account
   - Click "New App"
   - Select repository and branch
   - Set main file to `app.py`
   - Click Deploy

3. **Share Live Link:**
   - Live app available immediately
   - Share URL for evaluation

## Performance Testing

### Test Data Characteristics
- **Size:** 200 instances (20% of full dataset)
- **Class Distribution:** 179 negative, 21 positive instances
- **Features:** Scaled and encoded identical to training data

### Expected Performance Range
- **Accuracy:** 82-90% (mainly due to class imbalance)
- **AUC:** 0.48-0.58 (moderate discrimination ability)
- **F1 Score:** 0.0-0.1 (affected by low recall of minority class)

## Technical Stack

- **Language:** Python 3.9+
- **ML Framework:** Scikit-learn, XGBoost
- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Web Framework:** Streamlit
- **Model Serialization:** Joblib

## Troubleshooting

### Issue: Models not found
**Solution:** Run `train_models.py` to generate model files

### Issue: CSV upload error
**Solution:** Ensure CSV format with same features as training data

### Issue: Streamlit connection error
**Solution:** Check internet connection, restart streamlit server

## References

1. [UCI Machine Learning Repository - Bank Marketing Dataset](https://archive.ics.uci.edu/ml/datasets/bank+marketing)
2. [Scikit-learn Documentation](https://scikit-learn.org/)
3. [XGBoost Documentation](https://xgboost.readthedocs.io/)
4. [Streamlit Documentation](https://docs.streamlit.io/)

## Assignment Evaluation Criteria

- ✅ 6 classification models implemented
- ✅ All evaluation metrics calculated (Accuracy, AUC, Precision, Recall, F1, MCC)
- ✅ 80-20 train-test split applied
- ✅ GitHub repository with complete source code
- ✅ Requirements.txt with all dependencies
- ✅ README.md with comprehensive documentation
- ✅ Streamlit app with required features:
  - Data upload capability
  - Model selection dropdown
  - Metrics display
  - Confusion matrix and classification report
- ✅ Deployed on Streamlit Community Cloud

## Submission Details

- **Repository Link:** [Add GitHub repository URL here]
- **Live Streamlit App:** [Add Streamlit deployment URL here]
- **BITS Lab Screenshot:** [Add screenshot path here]

---

**Submitted for:** Machine Learning Assignment 2  
**Course:** M.Tech AIML / DSE  
**Institution:** BITS Pilani  
**Deadline:** 15-Feb-2026  

*Last Updated: January 31, 2026*
