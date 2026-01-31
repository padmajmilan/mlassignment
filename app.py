"""
Streamlit Application for ML Classification Model Evaluation
Assignment 2: UCI Banking Dataset Classification
Uses Python code models instead of pickle files
"""

import streamlit as st
import pandas as pd
import numpy as np
import os
import sys
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, roc_auc_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import base64

# Add model directory to path for importing model modules
sys.path.insert(0, 'model')

# Set page configuration
st.set_page_config(
    page_title="ML Model Evaluation - Banking Dataset",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_models():
    """Load all trained models from Python code"""
    models = {}
    
    # Import model modules dynamically
    try:
        import LogisticRegression
        models['Logistic Regression'] = LogisticRegression.model
    except Exception as e:
        st.warning(f"Could not load Logistic Regression: {e}")
    
    try:
        import DecisionTree
        models['Decision Tree'] = DecisionTree.model
    except Exception as e:
        st.warning(f"Could not load Decision Tree: {e}")
    
    try:
        import kNN
        models['kNN'] = kNN.model
    except Exception as e:
        st.warning(f"Could not load kNN: {e}")
    
    try:
        import NaiveBayes
        models['Naive Bayes'] = NaiveBayes.model
    except Exception as e:
        st.warning(f"Could not load Naive Bayes: {e}")
    
    try:
        import RandomForest
        models['Random Forest'] = RandomForest.model
    except Exception as e:
        st.warning(f"Could not load Random Forest: {e}")
    
    try:
        import XGBoost
        models['XGBoost'] = XGBoost.model
    except Exception as e:
        st.warning(f"Could not load XGBoost: {e}")
    
    return models

@st.cache_resource
def load_scaler():
    """Load scaler from Python code"""
    try:
        import scaler
        return scaler.scaler_model
    except Exception as e:
        st.warning(f"Could not load scaler: {e}")
        return None

@st.cache_resource
def load_label_encoders():
    """Load label encoders from Python code"""
    try:
        import label_encoders
        return label_encoders.label_encoders_model
    except Exception as e:
        st.warning(f"Could not load label encoders: {e}")
        return None

@st.cache_data
def load_metrics():
    """Load pre-calculated metrics"""
    if os.path.exists('model/metrics.csv'):
        return pd.read_csv('model/metrics.csv')
    return None

@st.cache_data
def load_test_data():
    """Load test data"""
    if os.path.exists('model/test_data.csv'):
        return pd.read_csv('model/test_data.csv')
    return None

def preprocess_data(data, categorical_cols, scaler):
    """Preprocess input data"""
    data_processed = data.copy()
    
    # The data is already scaled if from CSV, but we'll handle both cases
    if data_processed.isnull().any().any():
        st.warning("Data contains missing values. Filling with mean...")
        data_processed = data_processed.fillna(data_processed.mean())
    
    return data_processed

# Main App
st.title("🤖 ML Classification Model Evaluation")
st.markdown("**UCI Banking Dataset - Binary Classification**")
st.markdown("---")

# Load all resources
models = load_models()
scaler = load_scaler()
label_encoders = load_label_encoders()
metrics_df = load_metrics()
test_data = load_test_data()

if not models or metrics_df is None:
    st.error("❌ Models not found. Please ensure all model files are in the 'model/' directory.")
    st.stop()

# Sidebar Navigation
st.sidebar.title("📊 Navigation")
page = st.sidebar.radio(
    "Choose a section:",
    ["📈 Model Performance", "🎯 Make Predictions", "📋 Model Comparison", "📚 About"]
)

# ============================================================================
# PAGE 1: MODEL PERFORMANCE
# ============================================================================
if page == "📈 Model Performance":
    st.header("Model Performance Metrics")
    
    # Display metrics table
    st.subheader("Evaluation Metrics (Test Set)")
    
    # Format the dataframe for display
    display_df = metrics_df.copy()
    display_df = display_df.round(4)
    st.dataframe(display_df, use_container_width=True, hide_index=True)
    
    # Best model highlights
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        best_accuracy = metrics_df['Accuracy'].max()
        best_model_acc = metrics_df[metrics_df['Accuracy'] == best_accuracy]['Model'].values[0]
        st.metric("🏆 Best Accuracy", f"{best_accuracy:.4f}", best_model_acc)
    
    with col2:
        best_auc = metrics_df['AUC'].max()
        best_model_auc = metrics_df[metrics_df['AUC'] == best_auc]['Model'].values[0]
        st.metric("📊 Best AUC", f"{best_auc:.4f}", best_model_auc)
    
    with col3:
        best_f1 = metrics_df['F1'].max()
        best_model_f1 = metrics_df[metrics_df['F1'] == best_f1]['Model'].values[0]
        st.metric("⭐ Best F1 Score", f"{best_f1:.4f}", best_model_f1)
    
    with col4:
        best_mcc = metrics_df['MCC'].max()
        best_model_mcc = metrics_df[metrics_df['MCC'] == best_mcc]['Model'].values[0]
        st.metric("✅ Best MCC", f"{best_mcc:.4f}", best_model_mcc)
    
    # Visualization - Bar charts
    st.subheader("Metrics Comparison")
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Model Performance Comparison', fontsize=16, fontweight='bold')
    
    metrics_to_plot = ['Accuracy', 'AUC', 'Precision', 'Recall', 'F1', 'MCC']
    colors = plt.cm.Set3(np.linspace(0, 1, len(metrics_df)))
    
    for idx, metric in enumerate(metrics_to_plot):
        ax = axes[idx // 3, idx % 3]
        bars = ax.barh(metrics_df['Model'], metrics_df[metric], color=colors)
        ax.set_xlabel(metric, fontweight='bold')
        ax.set_title(metric, fontweight='bold')
        ax.set_xlim(0, 1)
        
        # Add value labels on bars
        for i, bar in enumerate(bars):
            width = bar.get_width()
            ax.text(width, bar.get_y() + bar.get_height()/2, 
                   f'{width:.3f}', ha='left', va='center', fontsize=8)
    
    plt.tight_layout()
    st.pyplot(fig)

# ============================================================================
# PAGE 2: MAKE PREDICTIONS
# ============================================================================
elif page == "🎯 Make Predictions":
    st.header("Model Prediction Interface")
    
    # Data upload section
    st.subheader("Upload Test Data")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        uploaded_file = st.file_uploader(
            "Upload your test data (CSV format)",
            type=['csv'],
            help="Upload a CSV file with test instances for prediction"
        )
    
    with col2:
        if st.button("📥 Load Sample Test Data", key="sample_data"):
            uploaded_file = None
    
    # Model selection
    st.subheader("Select Model for Prediction")
    selected_model = st.selectbox(
        "Choose a classification model:",
        list(models.keys()),
        help="Select which model to use for predictions"
    )
    
    # Handle data input
    if uploaded_file is not None:
        # User uploaded file
        try:
            input_data = pd.read_csv(uploaded_file)
            
            # Remove target column if present
            if 'y' in input_data.columns:
                y_true = input_data['y'].values
                X_data = input_data.drop('y', axis=1)
                has_labels = True
            else:
                X_data = input_data
                has_labels = False
            
            st.success(f"✓ Data loaded successfully! Shape: {X_data.shape}")
            
        except Exception as e:
            st.error(f"Error reading file: {e}")
            st.stop()
    else:
        # Use sample test data
        if test_data is not None:
            input_data = test_data.sample(min(20, len(test_data)))
            y_true = input_data['y'].values
            X_data = input_data.drop('y', axis=1)
            has_labels = True
            st.info(f"📊 Using sample test data. Showing first {len(X_data)} instances.")
        else:
            st.warning("No test data available. Please upload a CSV file.")
            st.stop()
    
    # Make predictions
    if st.button("🔮 Generate Predictions", key="predict_btn"):
        try:
            st.subheader("Prediction Results")
            
            # Get selected model
            model = models[selected_model]
            
            # Make predictions
            predictions = model.predict(X_data)
            probabilities = model.predict_proba(X_data)[:, 1]
            
            # Display results table
            results_df = pd.DataFrame({
                'Instance': range(len(predictions)),
                'Prediction': ['Yes' if p == 1 else 'No' for p in predictions],
                'Probability (Yes)': probabilities.round(4),
                'Confidence': np.maximum(probabilities, 1 - probabilities).round(4)
            })
            
            if has_labels:
                results_df['Actual'] = ['Yes' if y == 1 else 'No' for y in y_true]
                results_df['Correct'] = results_df['Prediction'] == results_df['Actual']
            
            st.dataframe(results_df, use_container_width=True, hide_index=True)
            
            # Metrics if labels available
            if has_labels:
                st.subheader("Evaluation Metrics (Test Set)")
                
                col1, col2, col3, col4 = st.columns(4)
                
                accuracy = accuracy_score(y_true, predictions)
                auc = roc_auc_score(y_true, probabilities)
                
                with col1:
                    st.metric("Accuracy", f"{accuracy:.4f}")
                with col2:
                    st.metric("AUC Score", f"{auc:.4f}")
                with col3:
                    st.metric("Total Predictions", len(predictions))
                with col4:
                    correct_preds = (predictions == y_true).sum()
                    st.metric("Correct Predictions", f"{correct_preds}/{len(predictions)}")
                
                # Confusion Matrix
                st.subheader("Confusion Matrix")
                cm = confusion_matrix(y_true, predictions)
                
                fig, ax = plt.subplots(figsize=(8, 6))
                sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                           xticklabels=['No', 'Yes'],
                           yticklabels=['No', 'Yes'],
                           ax=ax, cbar_kws={'label': 'Count'})
                ax.set_xlabel('Predicted Label', fontweight='bold')
                ax.set_ylabel('True Label', fontweight='bold')
                ax.set_title(f'Confusion Matrix - {selected_model}', fontweight='bold')
                st.pyplot(fig)
                
                # Classification Report
                st.subheader("Classification Report")
                report = classification_report(y_true, predictions, target_names=['No', 'Yes'])
                st.text(report)
            
            # Download predictions
            csv = results_df.to_csv(index=False)
            st.download_button(
                label="📥 Download Predictions (CSV)",
                data=csv,
                file_name=f"predictions_{selected_model.replace(' ', '_')}.csv",
                mime="text/csv"
            )
            
        except Exception as e:
            st.error(f"Error during prediction: {e}")
            st.info("Please ensure your data format matches the training data.")

# ============================================================================
# PAGE 3: MODEL COMPARISON
# ============================================================================
elif page == "📋 Model Comparison":
    st.header("Detailed Model Comparison")
    
    st.subheader("Overview")
    st.write("""
    This section compares all 6 classification models trained on the UCI Banking Dataset.
    """)
    
    # Metrics table with better formatting
    st.subheader("Complete Metrics Table")
    
    # Create a styled dataframe
    comparison_df = metrics_df.copy()
    comparison_df = comparison_df.round(6)
    
    # Apply conditional formatting
    st.dataframe(
        comparison_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            'Model': st.column_config.TextColumn(width=150),
            'Accuracy': st.column_config.NumberColumn(format="%.4f", width=120),
            'AUC': st.column_config.NumberColumn(format="%.4f", width=120),
            'Precision': st.column_config.NumberColumn(format="%.4f", width=120),
            'Recall': st.column_config.NumberColumn(format="%.4f", width=120),
            'F1': st.column_config.NumberColumn(format="%.4f", width=120),
            'MCC': st.column_config.NumberColumn(format="%.4f", width=120),
        }
    )
    
    # Radar chart for model comparison
    st.subheader("Model Performance Radar Chart")
    
    from math import pi
    
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
    
    categories = ['Accuracy', 'AUC', 'Precision', 'Recall', 'F1', 'MCC']
    num_vars = len(categories)
    angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
    angles += angles[:1]
    
    colors_list = plt.cm.Set3(np.linspace(0, 1, len(metrics_df)))
    
    for idx, row in metrics_df.iterrows():
        values = row[categories].values.tolist()
        values += values[:1]
        ax.plot(angles, values, 'o-', linewidth=2, label=row['Model'], color=colors_list[idx])
        ax.fill(angles, values, alpha=0.15, color=colors_list[idx])
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, size=10)
    ax.set_ylim(0, 1)
    ax.set_title('Model Performance Comparison (Radar Chart)', size=14, weight='bold', pad=20)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    ax.grid(True)
    
    st.pyplot(fig)
    
    # Model-specific insights
    st.subheader("Model Insights")
    
    for model_name in metrics_df['Model']:
        with st.expander(f"📌 {model_name}"):
            model_metrics = metrics_df[metrics_df['Model'] == model_name].iloc[0]
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Accuracy", f"{model_metrics['Accuracy']:.4f}")
            with col2:
                st.metric("F1 Score", f"{model_metrics['F1']:.4f}")
            with col3:
                st.metric("MCC", f"{model_metrics['MCC']:.4f}")
            
            # Relative performance
            st.write("**Relative Performance:**")
            accuracy_rank = (metrics_df['Accuracy'] >= model_metrics['Accuracy']).sum()
            f1_rank = (metrics_df['F1'] >= model_metrics['F1']).sum()
            
            col1, col2 = st.columns(2)
            with col1:
                st.caption(f"Accuracy Rank: {accuracy_rank}/6")
            with col2:
                st.caption(f"F1 Score Rank: {f1_rank}/6")

# ============================================================================
# PAGE 4: ABOUT
# ============================================================================
elif page == "📚 About":
    st.header("About This Application")
    
    st.markdown("""
    ## Machine Learning Assignment 2
    **UCI Banking Dataset Classification**
    
    ### 📊 Dataset Information
    - **Dataset**: UCI Bank Marketing Dataset (Synthetic)
    - **Instances**: 1000
    - **Features**: 21
    - **Target Variable**: Binary (Yes/No for deposit subscription)
    - **Train-Test Split**: 80-20
    
    ### 🤖 Models Implemented
    1. **Logistic Regression** - Linear classification model
    2. **Decision Tree** - Tree-based classification model
    3. **K-Nearest Neighbors (kNN)** - Instance-based learning
    4. **Naive Bayes** - Probabilistic classifier based on Bayes' theorem
    5. **Random Forest** - Ensemble of decision trees
    6. **XGBoost** - Gradient boosting ensemble model
    
    ### 📈 Evaluation Metrics
    - **Accuracy**: Proportion of correct predictions
    - **AUC**: Area Under the ROC Curve
    - **Precision**: True positives / (True positives + False positives)
    - **Recall**: True positives / (True positives + False negatives)
    - **F1 Score**: Harmonic mean of Precision and Recall
    - **MCC**: Matthews Correlation Coefficient
    
    ### 🎯 How to Use This App
    
    **1. Model Performance Page:**
    - View all models' evaluation metrics
    - See best performing models for each metric
    - Compare metrics with visualizations
    
    **2. Make Predictions Page:**
    - Upload your own test data (CSV format)
    - Select a model for predictions
    - Get detailed prediction results
    - View confusion matrix and classification report
    
    **3. Model Comparison Page:**
    - Detailed comparison of all 6 models
    - Radar chart for visual comparison
    - Individual model insights
    
    ### 🔒 Model Files Location
    All trained models are saved in the `model/` directory:
    - `Logistic_Regression.pkl`
    - `Decision_Tree.pkl`
    - `kNN.pkl`
    - `Naive_Bayes.pkl`
    - `Random_Forest.pkl`
    - `XGBoost.pkl`
    - `scaler.pkl`
    - `label_encoders.pkl`
    - `test_data.csv`
    - `metrics.csv`
    
    ### 📝 Features
    ✅ Multiple ML classification models  
    ✅ Comprehensive evaluation metrics  
    ✅ Interactive prediction interface  
    ✅ Data upload functionality  
    ✅ Confusion matrix and classification reports  
    ✅ Model comparison visualizations  
    ✅ Download prediction results  
    
    ---
    **Assignment**: Machine Learning (BITS Pilani)  
    **Created**: 2026
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; font-size: 0.85rem;'>
    🤖 ML Classification Model Evaluation | Powered by Streamlit<br/>
    © 2026 Assignment 2
</div>
""", unsafe_allow_html=True)
