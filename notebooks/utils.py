from sklearn.metrics import (classification_report, accuracy_score, confusion_matrix, recall_score, precision_score, f1_score, roc_auc_score)
from matplotlib import pyplot as plt
import tensorflow as tf



def show_img(pixels, label, number_of_images = 1):
    fig , ax = plt.subplots(ncols= number_of_images , nrows=1, figsize=(10,3))
    
    if number_of_images == 1:
        ax = [ax]
    
    for i in range(number_of_images):
        ax[i].imshow(pixels[i], cmap="gray")
        ax[i].set_title(f"Label: {label[i]}")
        ax[i].axis("off")
    
    plt.tight_layout()
    plt.show()


def classification_model_measurements(y_train, y_t_pred, y_test, y_pred, y_t_proba=None, y_proba=None):
    """
    Comprehensive model evaluation metrics.
    
    Parameters:
    -----------
    y_train, y_test : Ground truth labels
    y_t_pred, y_pred : Predicted binary labels
    y_t_proba, y_proba : (Optional) Predicted probabilities for ROC-AUC calculation
    """
    
    print("="*50)
    print(f"{' MODEL EVALUATION METRICS ':*^50}")
    print("="*50)
    
    # Accuracy
    print(f"\n{'ACCURACY SCORE':^50}")
    print("-"*50)
    print(f"Training  => {accuracy_score(y_train, y_t_pred)*100:.2f}%")
    print(f"Testing   => {accuracy_score(y_test, y_pred)*100:.2f}%")

    # ROC-AUC (if probabilities provided)
    if y_t_proba is not None and y_proba is not None:
        print(f"\n{'ROC-AUC SCORE':^50}")
        print("-"*50)
        print(f"Training  => {roc_auc_score(y_train, y_t_proba):.3f}")
        print(f"Testing   => {roc_auc_score(y_test, y_proba):.3f}")

    # Confusion Matrix
    print(f"\n{'CONFUSION MATRIX':^50}")
    print("-"*50)
    print(f"Training:\n{confusion_matrix(y_train, y_t_pred)}")
    print(f"\nTesting:\n{confusion_matrix(y_test, y_pred)}")

    # Classification Report
    print(f"\n{'CLASSIFICATION REPORT':^50}")
    print("-"*50)
    print(f"Training:\n{classification_report(y_train, y_t_pred)}")
    print(f"Testing:\n{classification_report(y_test, y_pred)}")
    print("="*50)
