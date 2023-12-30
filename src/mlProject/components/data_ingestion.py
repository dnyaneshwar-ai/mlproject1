# Import necessary libraries and modules
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
# from src.components.data_transformation import DataTransformation
# from src.components.data_transformation import DataTransformationConfig
# from src.components.model_trainer import ModelTrainerConfig
# from src.components.model_trainer import ModelTrainer


# note: define varibles fror data_paths using dataclass decorador
@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join("artifacts", "train.csv")
    test_data_path : str = os.path.join("artifacts", "test.csv")
    row_data_path: str = os.path.join("artifacts", "data.csv")

# now define class for dataingestion
class DataIngestion:
    def __init__(self):
        # here store all path variables in ingestion_config from DataIngestionConfig dataclass
        self.ingestion_config = DataIngestionConfig()    

    # method for data ingetion
    def initiate_data_ingestion(self):
            logging.info('enter into initiate data ingestion')
            try:
                df = pd.read_csv('notebook\data\winequality-red.csv')
                logging.info('read dataset as dataframe completed')
                
                # save all data in data.csv file in artifact folder
                df.to_csv(self.ingestion_config.row_data_path, index=False, header=True)

                # split data
                logging.info("ingestion of data started")
                train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

                # save test and train set in artifact folder
                train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
                test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
                logging.info('ingestion of data completed')

                return (
                        self.ingestion_config.train_data_path,
                        self.ingestion_config.test_data_path

                )
                
            except Exception as e:
                raise CustomException(e, sys)


# # to check script, it running or not, run into main.py file
            


# if __name__=='__main__':
#      # create object of dtaingestion class
#      obj = DataIngestion()
     
#      # call initiate_data_ingestion function, and save results in variable train_data, test_data.
#      train_data, test_data = obj.initiate_data_ingestion()

    # # Data Transformation
    # # Create an instance of the DataTransformation class
    # data_transformation = DataTransformation()
    # # Call the initiate_data_transformation method to transform the training and test datasets
    # train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

    # # Model Trainer
    # # Create an instance of the ModelTrainer class
    # modeltrainer = ModelTrainer()
    # # Print the result of the initiate_model_trainer method
    # print(modeltrainer.initiate_model_trainer(train_arr, test_arr))
