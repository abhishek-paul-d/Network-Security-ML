import sys
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation


if __name__=='__main__':
    try:
        traningpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(traningpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the Data Ingestion")
        dataingestionartifact=data_ingestion.intiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact,"\n")
        datavalidationconfig=DataValidationConfig(traningpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,datavalidationconfig)
        logging.info("Initiate Data Validation")
        datavalidationartifact=data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(datavalidationartifact, "\n")
        datatransformationconfig=DataTransformationConfig(traningpipelineconfig)
        logging.info("Data Transformation initiated")
        data_transformation=DataTransformation(datavalidationartifact,datatransformationconfig)
        datatransformationartifact=data_transformation.initiate_data_transformation()
        print(datatransformationartifact, "\n")
        logging.info("Data Transformation Completed")


    except Exception as e:
        raise NetworkSecurityException(e,sys)