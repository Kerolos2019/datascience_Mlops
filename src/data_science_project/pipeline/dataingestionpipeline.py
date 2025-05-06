

from src.data_science_project.config.configuration import ConfigurationManager
from src.data_science_project.components.data_ingestion import Dataingestion
from src.data_science_project import logger



STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    
    def __init__(self):
        pass
    def initiate_data_ingestion(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        dataingestion = Dataingestion(config=data_ingestion_config)
        dataingestion.download_file()
        dataingestion.extract_zip_file()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        dataingestion = DataIngestionTrainingPipeline()
        dataingestion.initiate_data_ingestion()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n")
    except Exception as e:
        logger.exception(e)
        raise e