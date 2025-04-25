import sys

from src.exception import CustomException
from src.logger import logging

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_training import ModelTrainer





def main():
    
    try:
        logging.info("Train Pipeline Started")

        # Craete Objects
        data_ingestion_obj = DataIngestion()
        data_transformation_obj = DataTransformation()
        model_trainer_obj = ModelTrainer()

        # Data Ingestion
        train_file, test_file = data_ingestion_obj.split_data()

        # Data Transformation
        train_data, test_data = data_transformation_obj.apply_transformation(train_file, test_file)

        # Model Training
        model_trainer_obj.initiate_model_training(train_data, test_data)

        logging.info("Train Pipeline Completed")

    except Exception as e:
        raise CustomException(e, sys)