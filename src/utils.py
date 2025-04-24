import os
import sys
import pickle
import pandas as pd


from src.exception import CustomException
from src.logger import logging


from sklearn.metrics import accuracy_score, recall_score, f1_score





# Save Pickle Object
def save_pickle_obj(model_obj, file_path):
    '''
    This function dump any ML object into pkl file
    '''
    try:
        dir_name = os.path.dirname(file_path)
        os.makedirs(dir_name, exist_ok=True)

        with open(file_path, 'wb') as file:
            pickle.dump(model_obj, file)
        
        logging.info('Transformation Pipeline Dump into PKL file')

    except Exception as e:
        raise CustomException(e, sys)
    


# Load Pickle Object
def load_pickle_obj(file_path):

    try:
        with open(file_path, 'rb') as file:
            file_obj = pickle.load(file=file)

            logging.info("Pickle Object Load Successfully")
            return file_obj

    except Exception as e:
        raise CustomException(e, sys)
    





def model_evaluation(models, X_train, X_test, y_train, y_test):

    try: 
        logging.info('Model Evaluation Start')
        scores = []

        for key, value in models.items():

            model = value
            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)

            recall = recall_score(y_test, y_pred)
            f1 = f1_score(y_test, y_pred)
            accuracy = accuracy_score(y_test, y_pred)

            results = {
                'Model': key,
                'Recall Score': recall,
                'F1 Score': f1,
                'Accuracy': accuracy
            }
            scores.append(results)
        
        evaluation_data = pd.DataFrame(scores)
        evaluation_data = evaluation_data.sort_values(by='Accuracy')
        return evaluation_data

    
    except Exception as e:
        raise CustomException(e, sys)