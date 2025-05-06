import os
import urllib.request as requests    
from src.data_science_project import logger
import zipfile


from src.data_science_project.entity.config_entity import DataIngestionConfig


class Dataingestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    #download the file from the source URL and save it to local path

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            file_name,header = requests.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{file_name} downloaded successfully")
        else:
            logger.info(f"File already exists at {self.config.local_data_file}")
        


    def extract_zip_file(self):
        unzib_path=self.config.unzip_dir
        os.makedirs(unzib_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzib_path)
        
