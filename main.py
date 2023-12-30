from src.mlProject.components.data_ingestion import DataIngestion

# ---> for data ingestion
# to check script, it running or not
if __name__=='__main__':
     # create object of dataingestion class
     obj = DataIngestion()
     
     # call initiate_data_ingestion function, and save results in variable train_data, test_data.
     train_data, test_data = obj.initiate_data_ingestion()

# ---> for data transformation