import os
import sys
import pandas as pd

from src.exception import CustomException
from src.logger import logging
from src.utils import load_pickle_obj






class PredictPipeline:

    def __init__(self):
        pass


    # Load the model for prediction
    def load_models(self):
        try:
            

            transformer_path = os.path.join('artifacts', 'transformer.pkl')
            model_path = os.path.join('artifacts', 'model.pkl')

            transformer = load_pickle_obj(transformer_path)
            model = load_pickle_obj(model_path)

            return transformer, model

        except Exception as e:
            raise CustomException(e, sys)
        

    
    def make_prediction(self, data):

        try:
            logging.info("Making Prediction for New Data Point")

            transformer, model = self.load_models()

            # Apply Transformation on New Data Point
            transform_data = transformer.transform(data)

            # Make Prediction
            prediction = model.predict(transform_data)

            return prediction

        except Exception as e:
            raise CustomException(e, sys)
        




class CustomData:

    def __init__(self, age, bmi, menstrual_irregularity, testosterone_level, antral_follicle_count):

        self.age = age
        self.bmi = bmi
        self.menstrual_irregularity = menstrual_irregularity
        self.testosterone_level = testosterone_level
        self.antral_follicle_count = antral_follicle_count


    def data_transform_in_df(self):

        try:
            new_data_point = {
                'Age': self.age,
                'BMI': self.bmi,
                'Menstrual_Irregularity': self.menstrual_irregularity,
                'Testosterone_Level(ng/dL)': self.testosterone_level,
                'Antral_Follicle_Count': self.antral_follicle_count
            }

            new_df = pd.DataFrame(new_data_point)   
            return new_df

        except Exception as e:
            raise CustomException(e, sys)
