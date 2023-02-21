from collections import namedtuple

# creating a structure for all the components which will be used in config to use
DataIngestionConfig = namedtuple("DataIngestionConfig",["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])

DataValidationConfig = namedtuple("DataValidationConfig",["schema_file_path"])

DataTransformconfig = namedtuple("DataTransformconfig",["add_bedroom_per_room","transformed_train_dir","transformed_test_dir","preprocessed_object_file_path"])

ModelTrainerConfig = namedtuple("ModelTrainerConfig", ["trained_model_file_path","base_accuracy"])

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig", ["model_evaluation_file_path","time_stamp"])

ModelPusherConfig = namedtuple("ModelPusherConfig", ["export_dir_path"])