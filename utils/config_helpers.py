def parse_list(x):
    return [int(i.strip()) for i in x.split(',')]


class MainConfig:

    def __init__(self, main_config):
        self.num_epochs = int(main_config['TRAINING']['num_epochs'])
        self.batch_size = int(main_config['TRAINING']['batch_size'])
        self.eval_every = int(main_config['TRAINING']['eval_every'])
        self.checkpoints_to_keep = int(main_config['TRAINING']['checkpoints_to_keep'])
        self.save_every = int(main_config['TRAINING']['save_every'])
        self.eval_size = int(main_config['TRAINING']['eval_size'])
        self.log_device_placement = bool(main_config['TRAINING']['log_device_placement'])

        self.num_tests = int(main_config['DATA']['num_tests'])
        self.data_fn = str(main_config['DATA']['file_name'])
        self.logs_path = str(main_config['DATA']['logs_path'])
        self.model_dir = str(main_config['DATA']['model_dir'])
