import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
        f1_score, classification_report, 
        confusion_matrix, roc_curve, 
        roc_auc_score, accuracy_score,
        log_loss)
from sklearn import __version__ as sklearn_version
from sklearn.neighbors import KNeighborsClassifier
from imblearn.under_sampling import NearMiss
from datetime import datetime
import os
import pickle



def rf_classifier(data, device_name, scaling=False):

    # Split some data for validation
    validation_data = data.sample(frac=0.30)

    # Removing Validation data from dataframe
    data_df = data.drop(validation_data.index)

    # New Dict for storing Results
    results = {}

    # X & Y Variables from dataframe
    X = data_df.drop(['label', 'device'], axis=1)
    y = data_df['label']

    results['original_shape'] = [X.shape, y.shape]

    # Check data needs to be scaled or not
    if scaling == False:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=47)
        model_name = f'{device_name}_without_scaling_unbalanced_model.pkl'
    else:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=47)
        scaler = StandardScaler()
        scaler.fit(X_train)
        X_train = scaler.transform(X_train)
        X_test = scaler.transform(X_test)
        model_name = f'{device_name}_with_scaling_unbalanced_model.pkl'

    # Define Classifier
    clf = RandomForestClassifier()

    # Fit the model classifier into training data
    model_res = clf.fit(X_train, y_train)

    # Predict with Test Data
    y_pred = model_res.predict(X_test)
    y_pred_prob = model_res.predict_proba(X_test)
    lr_probs = y_pred_prob[:,1]

    # Accuracy Score
    ac = accuracy_score(y_test, y_pred)

    # Calculate F1 Score
    f1 = f1_score(y_test, y_pred, average='weighted')

    # Calculate Confusion Matrix, classification Report
    cm = confusion_matrix(y_test, y_pred)
    cr = classification_report(y_test, y_pred)


    # Feature Importance
    importances = pd.DataFrame({'feature':X.columns,'importance':np.round(clf.feature_importances_,3)})
    importances = importances.sort_values('importance',ascending=False).set_index('feature')

   
    results['feature_importance'] = [importances.head(20)]
    results['Accuracy Test Data'] = ac
    results['F1 Score Test Data'] = f1

    # Saving Model
    
    best_model = clf
    best_model.version = 1.0
    best_model.pandas_version = pd.__version__
    best_model.numpy_version = np.__version__
    best_model.sklearn_version = sklearn_version
    best_model.build_datetime = datetime.now()
    
    modelpath = f'models/{device_name}'
    if not os.path.exists(modelpath):
        os.mkdir(modelpath)
    iotmodel_path = os.path.join(modelpath, model_name)
    if not os.path.exists(iotmodel_path):
        with open(iotmodel_path, 'wb') as f:
            pickle.dump(best_model, f)
    
    f = open(f'models/{device_name}/report.txt', 'w')
    f.write(f'''Classification Report on Test Set 
                    \n \n {cr}\n \n 
                Confusion Matrix on Test Set
                    \n \n {cm} \n \n''')
    f.close()

    validation_data.to_csv(f'{modelpath}/{device_name}_validation_data.csv')
    return f'Model trained and saved successfully \n {results}'