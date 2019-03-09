# -*- coding: utf-8 -*-
"""train_initialize.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QFUF7b3o_KGZGhTsudK4J8ZaKK86jPzy
"""

!pip install rasa-nlu==0.13.2 
!pip install rasa_core==0.11.1 
!pip install sklearn_crfsuite
!pip install Action
!git clone https://github.com/RasaHQ/rasa_core.git
!pip install -r requirements.txt 
!pip install -e

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals 
from rasa_core import utils 
from rasa_core.agent import Agent 
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.sklearn_policy import SklearnPolicy

from google.colab import files

uploaded = files.upload()

from google.colab import files

uploaded = files.upload()

if __name__ == '__main__':  
  utils.configure_colored_logging(loglevel="DEBUG") 
  training_data_file = 'stories.md'
  model_path = './models/dialogue' 
  agent = Agent("horoscope_domain.yml",policies=[MemoizationPolicy(), KerasPolicy()])     
  training_data = agent.load_data(training_data_file) 
  agent.train(training_data,augmentation_factor=50,epochs=500,batch_size=10,validation_split=0.2) 
  agent.persist(model_path)



