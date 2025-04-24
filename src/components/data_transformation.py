import os
import sys
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline



from src.exception import CustomException
from src.logger import logging
from src.utils import save_pickle_obj
from src.components.data_ingestion import DataIngestion









# Configure Data Transformation File (transform.pkl)
class DataTransformationConfig:
    data_transformation_file = os.path.join('artifact', 'data_transform.pkl')




# Perform Data Transformation
class DataTransformation:

    def __init__(self):
        self.transform_obj = DataTransformationConfig()



    def get_pipeline(self):
        '''
        This pipeline is imput missing value(if Available) and scale data
        '''
        try:
            transform_pipe = Pipeline(
                [
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler())
                ]
            )

            return transform_pipe
    
        except Exception as e:
            raise CustomException(e, sys)
    


    def apply_transformation(self, train_file_path, test_file_path):

        try:
            logging.info('Data Transformation Start')

            # Get Pipeline
            transform_pipe = self.get_pipeline()

            
            train_df = pd.read_csv(train_file_path)
            test_df = pd.read_csv(test_file_path)

            target_feature = 'PCOS_Diagnosis'

            # Separate Target and Input Features
            X_train = train_df.drop(columns=[target_feature])
            y_train = train_df[target_feature]

            X_test = test_df.drop(columns=[target_feature])
            y_test = test_df[target_feature]


            # Apply Transformation Pipeline
            X_train = transform_pipe.fit_transform(X_train)
            X_test = transform_pipe.transform(X_test)

            # Concat X and y data
            train_data = np.c_[X_train, np.array(y_train)]
            test_data = np.c_[X_test, np.array(y_test)]

            # Dump Transform Pipeline Object into pkl file
            save_pickle_obj(
                model_obj=transform_pipe,
                file_path=self.transform_obj.data_transformation_file
            )   

            logging.info('Data Transformation Complete')
            return(
                train_data,
                test_data
            )

        
        except Exception as e:
            raise CustomException(e, sys)