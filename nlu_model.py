from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config

def train_nlu(data,config,model_dir):
	training_data=load_data(data)
	trainer=Trainer(RasaNLUModelConfig(config))
	trainer.train(training_data)
	model_directory=trainer.persist(model_dir,fixed_model_name='weathernlu')
	
if name =='main':
	train_nlu('./data/data.json','config_spacy.json','./models/nlu')