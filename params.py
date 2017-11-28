
import os

default_class_names = 'bicycle, bus, car, motorbike, person, train'
default_num_class = len(default_class_names.split(','))
default_data_shape = 512
default_model_dir = os.path.join(os.getcwd(), 'model')
default_network = 'resnet50'
default_lr = 1.0
default_batch_size = 128
