import os
import sys

from src.exception import CustomException
from src.logger import logging
from src.utils import save_pickle_obj, model_evaluation

# ML Models
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from catboost import CatBoostClassifier
from xgboost import XGBClassifier





# Configure Model Training File
class ModelTrainerConfig:
    model_file = os.path.join('artifact', 'model.pkl')



# Peroform Model Training
class ModelTrainer:

    def __init__(self):
        self.model_file_obj = ModelTrainerConfig()


    def initiate_model_training(self, train_data, test_data):

        try:
            logging.info('Model Traing Start')

            X_train = train_data[:, :-1]
            X_test = test_data[:, :-1]
            y_train = train_data[:,-1]
            y_test = test_data[:,-1]


            models = {
                'Logistic Regression': LogisticRegression(),
                'KNN Classifier': KNeighborsClassifier(),
                'Support Vector Classifier': SVC(),
                'Random Forest Classifier': RandomForestClassifier(),
                'Gradient Boosting Classifier': GradientBoostingClassifier(),
                'CatBoost Classifier': CatBoostClassifier(),
                'XGBoost Classifier': XGBClassifier()
            }

            model_results = model_evaluation(models, X_train, X_test, y_train, y_test)

            # Get Best Model
            model_name = model_results.iloc[-1, :]['Model']
            model_obj = models[model_name]
            model_accuracy = model_results.iloc[-1, :]['Accuracy']

            if model_accuracy < 0.6:
                raise CustomException('No best model found')

            save_pickle_obj(
                model_obj=model_obj,
                file_path=self.model_file_obj.model_file
            )

            logging.info(f'Best Model Found: [{model_name}] with accuracy: [{model_accuracy}]')
            logging.info('Model Traing Complete')

        except Exception as e:
            raise CustomException(e, sys)