import datetime
from logger import logger
from configs import pipeline_config
from configs import config
from measurement_set import MeasurementSet
from terminal_color import Color
from pipeline_stage import PipelineStage


def main(dataset_path):
    start_time = datetime.datetime.now()
    measurement_set = MeasurementSet(dataset_path, config.OUTPUT_PATH)
    measurement_set.quack()

    pipeline_stages = PipelineStage(measurement_set)
    pipeline_stages.flux_calibration()
    pipeline_stages.bandpass_calibration()
    pipeline_stages.phase_calibration()
    pipeline_stages.target_source()

    end_time = datetime.datetime.now()
    logger.info(Color.UNDERLINE + 'Total time =' + str(abs((end_time - start_time).seconds)) + " seconds" + Color.ENDC)