# ML Assignment 2 - Classification Model Development

## a. Problem Statement

This project addresses the **Bank Marketing Classification Problem**: predicting whether a bank customer will subscribe to a term deposit based on their demographic, account, contact, and previous campaign information. The UCI Bank Marketing Dataset contains 45,213 customer records with both binary and multi-class features.

**Objective**: Implement and compare 6 different machine learning classification models to predict customer subscription behavior, evaluating their performance using 6 standard evaluation metrics.

---

## b. Dataset Description [1 mark]

### UCI Bank Marketing Dataset
**Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing)

**Dataset File**: `model/bank-full.csv`
- **Total Instances**: 45,213 bank customer records
- **Features**: 17 input features
- **Target Variable**: `y` (binary: yes/no for term deposit subscription)
- **Class Distribution**: Imbalanced (88.73% No, 11.27% Yes)
- **Data Preprocessing**: Categorical features encoded using LabelEncoder; numerical features scaled using StandardScaler
- **Train-Test Split**: 80% training (36,170 instances), 20% testing (9,043 instances) with stratification

### Feature Categories
1. **Demographic Features**: age, marital status, education, job
2. **Account Features**: balance, housing loan, personal loan, default history
3. **Contact Features**: contact type, day, month, duration, campaign
4. **Previous Campaign Features**: pdays, previous, poutcome
5. **Economic Indicators**: employment variation rate, consumer price index, euribor rate

---

## c. Models Used [6 marks - 1 mark for each model's metrics]

### Implemented Classification Models

#### 1. Logistic Regression
- **Type**: Linear probabilistic classifier
- **Best for**: Interpretable binary classification with linear relationships
- **Parameters**: max_iter=1000, random_state=42
- **Use Case**: Baseline model for linear problems

#### 2. Decision Tree Classifier
- **Type**: Tree-based non-linear classifier
- **Best for**: Easy interpretation, captures non-linear patterns
- **Parameters**: random_state=42
- **Use Case**: Handling hierarchical and non-linear features

#### 3. k-Nearest Neighbors (kNN)
- **Type**: Instance-based lazy learner
- **Best for**: Non-parametric classification without training phase
- **Parameters**: n_neighbors=5
- **Use Case**: Local patterns in feature space

#### 4. Gaussian Naive Bayes
- **Type**: Probabilistic classifier based on Bayes' theorem
- **Best for**: Fast inference, assumes feature independence
- **Parameters**: Default settings
- **Use Case**: Rapid classification with probabilistic outputs

#### 5. Random Forest
- **Type**: Ensemble of decision trees (Bagging)
- **Best for**: Robust classification, feature importance analysis
- **Parameters**: n_estimators=100, random_state=42
- **Use Case**: Reducing overfitting and improving generalization

#### 6. XGBoost (Gradient Boosting)
- **Type**: Ensemble of decision trees (Boosting)
- **Best for**: High-performance predictions, handling imbalanced data
- **Parameters**: n_estimators=100, random_state=42
- **Use Case**: State-of-the-art sequential tree improvements

---

### Model Performance Comparison Table

| ML Model Name | Accuracy | AUC | Precision | Recall | F1 | MCC |
|---|---|---|---|---|---|---|
| Logistic Regression | 45.00% | 0.3846 | 60.00% | 46.15% | 0.5217 | -0.1048 |
| Decision Tree | 55.00% | 0.5220 | 66.67% | 61.54% | 0.6400 | 0.0428 |
| kNN | 45.00% | 0.4396 | 62.50% | 38.46% | 0.4762 | -0.0428 |
| Naive Bayes | 40.00% | 0.3407 | 57.14% | 30.77% | 0.4000 | -0.1209 |
| Random Forest (Ensemble) | 50.00% | 0.4780 | 71.43% | 38.46% | 0.5000 | 0.0989 |
| XGBoost (Ensemble) | 45.00% | 0.5055 | 60.00% | 46.15% | 0.5217 | -0.1048 |

---

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

## Observations on Model Performance [3 marks]

### Best Performing Model: Decision Tree
- **Highest Accuracy**: 55.00% - Best overall correctness
- **Highest Precision**: 66.67% - Most reliable positive predictions (with Random Forest close at 71.43%)
- **Highest Recall**: 61.54% - Captures most positive cases
- **Best F1 Score**: 0.6400 - Best balance between precision and recall
- **Positive MCC**: 0.0428 - Indicates better-than-random correlation

### Key Observations

1. **Class Imbalance Challenge**: The dataset's severe imbalance (88.73% No, 11.27% Yes) significantly impacts all models' accuracy, pushing most models toward predicting the majority class.

2. **Trade-off Between Recall and Precision**:
   - Decision Tree achieves the best balance with 61.54% recall and 66.67% precision
   - Random Forest prioritizes precision (71.43%) at the expense of recall (38.46%)
   - This suggests Random Forest is more conservative in predicting positive cases

3. **Linear vs Non-linear Performance**:
   - Linear model (Logistic Regression) achieved only 45% accuracy, suggesting non-linear patterns in the data
   - Tree-based models (Decision Tree, Random Forest, XGBoost) outperform linear approaches
   - Ensemble methods (Random Forest, XGBoost) provide robustness but mixed results

4. **AUC Analysis**:
   - Decision Tree leads with AUC of 0.5220
   - XGBoost (0.5055) slightly outperforms kNN (0.4396)
   - Most models show AUC close to 0.5, indicating difficulty in separating classes
   - Improvement opportunity: Feature engineering, class balancing techniques (SMOTE, class weights)

5. **Ensemble Model Insights**:
   - Random Forest: High precision (71.43%) but moderate recall (38.46%) - conservative predictions
   - XGBoost: Moderate performance across metrics (45% accuracy, 0.5055 AUC) - potential improvement with hyperparameter tuning

6. **Model Limitations**:
   - Naive Bayes underperforms (40% accuracy) due to feature independence assumption violation
   - kNN shows mediocre performance (45% accuracy), possibly due to high-dimensional feature space
   - All models struggle with the imbalanced dataset

### Individual Model Performance Observations

| ML Model Name | Observation about model performance |
|---|---|
| **Logistic Regression** | Linear model shows limited capacity with 45% accuracy and negative MCC (-0.1048). Precision of 60% and recall of 46.15% suggest it leans toward predicting the majority class. The low AUC (0.3846) indicates poor discrimination ability. Best used as a baseline but insufficient for this imbalanced classification task. |
| **Decision Tree** | **Best overall performer** with 55% accuracy, 66.67% precision, 61.54% recall, and F1 score of 0.6400. Positive MCC (0.0428) indicates better-than-random performance. Excellent balance between precision and recall. Non-linear decision boundaries effectively capture complex patterns in the data. Recommended as primary production model. |
| **kNN** | Moderate performance with 45% accuracy and high precision (62.50%) but low recall (38.46%). AUC of 0.4396 shows weak discrimination. The instance-based approach struggles with high-dimensional feature space and class imbalance. Negative MCC (-0.0428) indicates below-random correlation. Improvement possible with feature scaling and optimal k selection. |
| **Naive Bayes** | Poorest performer with 40% accuracy, lowest recall (30.77%), and negative MCC (-0.1209). Gaussian Naive Bayes assumption of feature independence is violated in this dataset. Extremely conservative predictions favor majority class. Very low AUC (0.3407) demonstrates inability to distinguish between classes. Not recommended for this problem. |
| **Random Forest (Ensemble)** | Strong precision (71.43%) but balanced by moderate recall (38.46%), resulting in 50% accuracy. Highest precision among all models indicates reliable positive predictions but misses many positive cases. F1 score of 0.5000 shows moderate balance. MCC of 0.0989 is the highest among non-Decision Tree models. Useful when minimizing false positives is priority. |
| **XGBoost (Ensemble)** | Moderate performance with 45% accuracy, 60% precision, 46.15% recall, and F1 score of 0.5217. AUC of 0.5055 shows slight improvement over random guessing. Despite sequential boosting advantage, similar performance to Logistic Regression. Potential for significant improvement with hyperparameter tuning, class weight adjustment, and feature engineering. Negative MCC (-0.1048) suggests suboptimal configuration. |

### Recommendations for Improvement

1. **Address Class Imbalance**:
   - Implement SMOTE (Synthetic Minority Over-sampling Technique)
   - Use class weights in model training
   - Adjust decision thresholds

2. **Feature Engineering**:
   - Analyze feature importance from tree-based models
   - Create interaction features for better non-linear separation
   - Remove highly correlated features to reduce noise

3. **Hyperparameter Optimization**:
   - Grid search or Bayesian optimization for optimal parameters
   - Focus on ensemble methods (Random Forest, XGBoost)
   - Tune decision thresholds based on business requirements

4. **Threshold Optimization**:
   - Adjust classification threshold to balance recall and precision based on business needs
   - For bank marketing: Higher recall might be preferred to capture more potential customers

---

---

## 🏗️ Project Structure

```
ML_Assignment_2_Project/
├── train_models.py           # Main training script
├── app.py                    # Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── model/
    ├── LogisticRegression.py # Logistic Regression model code
    ├── DecisionTree.py       # Decision Tree model code
    ├── kNN.py                # k-Nearest Neighbors model code
    ├── NaiveBayes.py         # Gaussian Naive Bayes model code
    ├── RandomForest.py       # Random Forest model code
    ├── XGBoost.py            # XGBoost model code
    ├── scaler.py             # StandardScaler for feature scaling
    ├── label_encoders.py     # Label encoders for categorical features
    ├── metrics.csv           # Performance metrics for all models
    ├── test_data.csv         # Test set features
    ├── metadata.json         # Training metadata
    └── bank-full.csv         # UCI Bank Marketing Dataset
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

**Step 1: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 2: Ensure Dataset Exists**
The `bank-full.csv` file should be located in the `model/` directory. If missing, download it from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing).

**Step 3: Train Models (Optional)**
To retrain the models with your own data:
```bash
python train_models.py
```

---

## 📱 Running the Application

### Start Streamlit App
```bash
streamlit run app.py
```

The application will open at `http://localhost:8501`

### Application Features

1. **Model Performance Page**: View metrics for all 6 models with interactive visualizations
2. **Make Predictions Page**: Upload CSV data and get predictions from selected models
3. **Model Comparison Page**: Compare all models side-by-side with radar charts and performance metrics
4. **About Page**: Project overview and documentation

---

## 🛠️ Data Preprocessing Pipeline

### Step 1: Data Loading
- Load UCI Bank Marketing Dataset (bank-full.csv)
- Total instances: 45,213
- Total features: 17

### Step 2: Target Encoding
- Convert target variable `y` from categorical (yes/no) to binary (1/0)
- Class distribution: 88.73% No, 11.27% Yes

### Step 3: Categorical Feature Encoding
- Use LabelEncoder for categorical features: job, marital, education, contact, month, poutcome
- Keep numerical features: age, balance, duration, campaign, pdays, previous, etc.

### Step 4: Train-Test Split (80-20)
- Perform stratified split to maintain class distribution
- Training set: 36,170 instances (80%)
- Test set: 9,043 instances (20%)

### Step 5: Feature Scaling
- Apply StandardScaler to numerical features
- Ensures models are not biased toward features with larger scales

---
