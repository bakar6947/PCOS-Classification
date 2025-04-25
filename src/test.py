import sys


from src.exception import CustomException
from src.logger import logging

from src.pipeline.train_pipeline import main
from src.pipeline.predict_pipeline import CustomData, PredictPipeline







# Test Train and Predict Pipelines
if __name__ == '__main__':

    try:
        logging.info("Testing Satrt")
        
        # call train pipeline
        main()

        # Create New Data Point for Prediction
        data = CustomData(
            age=42,
            bmi=15.5,
            menstrual_irregularity=0,
            testosterone_level=40.6,
            antral_follicle_count=8
        )
        df = data.data_transform_in_df()

        predict = PredictPipeline()
        pcos_prediction = predict.make_prediction(df)

        print(f'PCOS Prediction: {pcos_prediction}')

        logging.info('Testing Complete')

    except Exception as e:
        raise CustomException(e, sys)