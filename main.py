from src.data_science_project import logger

from src.data_science_project.pipeline.dataingestionpipeline import DataIngestionTrainingPipeline




STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    dataingestion = DataIngestionTrainingPipeline()
    dataingestion.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e