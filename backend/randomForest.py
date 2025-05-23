import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn .metrics import accuracy_score, precision_score, recall_score, confusion_matrix
import joblib
import os


# function for training the random forest model
def trainTestModelRF(csv):
    df = pd.read_csv(csv)

    # splitting the data
    X = df[['country_encoded', 'isp_encoded', 'is_proxy', 'is_hosting']]
    y = df['is_suspicious']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # training the model
    modelObject = RandomForestClassifier()
    modelObject.fit(X_train, y_train)

    # testing the model
    y_pred = modelObject.predict(X_test)

    # evaluation metrics
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    print(f"Accuracy: {acc:.2f}")
    print(f"Precision: {prec:.2f}")
    print(f"Recall: {rec:.2f}")
    print("Confusion Matrix:")
    print(cm)

    # saving the model
    os.makedirs("models", exist_ok=True)
    model_path = "models/vpn_rf_model.pkl"
    joblib.dump(modelObject, model_path)
    print(f"Model saved to {model_path}")