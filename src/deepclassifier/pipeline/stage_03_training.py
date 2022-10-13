from deepclassifier.config import ConfigurationManager
from deepclassifier.components import PrepareCallBack, Training
from deepclassifier import logger

STAGE_NAME= "Training"

def main():
    config = ConfigurationManager()
    prepare_callbacks_config = config.get_prepare_callback_config()
    prepare_callbacks = PrepareCallBack(config=prepare_callbacks_config)
    callback_list = prepare_callbacks.get_tb_ckpt_callback()
    
    training_config = config.get_training_config()
    training = Training(config=training_config)
    training.get_base_model()
    training.train_valid_generator() #training and validation generators being created
    training.train(
        callback_list=callback_list
    )
    
if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e