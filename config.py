import os


class Settings:
    __OUTPUT_DATA_DIR_NAME = 'data'
    __OUTPUT_FILE_FORMAT = "json"

    @property
    def output_file_format(self):
        return self.__OUTPUT_FILE_FORMAT

    @property
    def output_data_dir_path(self) -> str:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir_path = os.path.join(current_dir, self.__OUTPUT_DATA_DIR_NAME)
        if not os.path.exists(data_dir_path):
            os.makedirs(data_dir_path)
        return data_dir_path


settings = Settings()
