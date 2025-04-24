import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import logging







# Confugure Data Ingestion Files
class DataIngestionConfig:
    raw_data_file = os.path.join('artifact', 'raw.csv')
    train_data_file = os.path.join('artifact', 'train.csv')
    test_data_file = os.path.join('artifact', 'test.csv')




# Perform Data Ingestion
class DataIngestion:

    def __init__(self):
        self.ingestion_config_obj = DataIngestionConfig()

    
    def split_data(self):

        try:
            logging.info('Data Ingestion Start')

            # Load Data Set
            df = pd.read_csv('notebook\data\pcos_rotterdam_balanceado.csv')

            # Create artifact Directory
            artifact_path = os.path.dirname(self.ingestion_config_obj.raw_data_file)
            os.makedirs(artifact_path, exist_ok=True)

            # Save Raw DataFrames as CSV into Artifact
            df.to_csv(self.ingestion_config_obj.raw_data_file, index=False)

            # Perform Train Test Split
            train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

            # Save Test and Train DataFrames as CSV into Artifact
            train_df.to_csv(self.ingestion_config_obj.train_data_file, index=False)
            test_df.to_csv(self.ingestion_config_obj.test_data_file, index=False)


            logging.info("Data Ingestion Complete")
            return(
                self.ingestion_config_obj.train_data_file,
                self.ingestion_config_obj.test_data_file
            )

        except Exception as e:
            raise CustomException(e, sys)