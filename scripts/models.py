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



def rf_classifier(data, device_name, scaling=False,):
    X = data.drop(['label', 'device'], axis=1)
    y = data['label']
    print(f'Original Shape:{X.shape}, {y.shape}')
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
    
    clf = RandomForestClassifier()
    model_res = clf.fit(X_train, y_train)
    y_pred = model_res.predict(X_test)
    y_pred_prob = model_res.predict_proba(X_test)
    lr_probs = y_pred_prob[:,1]
    ac = accuracy_score(y_test, y_pred)
    importances = pd.DataFrame({'feature':X.columns,'importance':np.round(clf.feature_importances_,3)})
    importances = importances.sort_values('importance',ascending=False).set_index('feature')

    f1 = f1_score(y_test, y_pred, average='weighted')
    cm = confusion_matrix(y_test, y_pred)
    print(importances.head(20))
    
    print('Random Forest: Accuracy=%.3f' % (ac))

    print('Random Forest: f1-score=%.3f' % (f1))
    print('Random Forest: Confusion Matrix', cm)
    print('Random Forest : Classification Report',classification_report(y_test, y_pred))
    
    best_model = clf
    best_model.version = 1.0
    best_model.pandas_version = pd.__version__
    best_model.numpy_version = np.__version__
    best_model.sklearn_version = sklearn_version
    #best_model.X_columns = [col for col in X_train.columns]
    best_model.build_datetime = datetime.now()
    
    modelpath = 'models'
    if not os.path.exists(modelpath):
        os.mkdir(modelpath)
    iotmodel_path = os.path.join(modelpath, model_name)
    if not os.path.exists(iotmodel_path):
        with open(iotmodel_path, 'wb') as f:
            pickle.dump(best_model, f)
    
    print('---------------------- Done ---------------------')