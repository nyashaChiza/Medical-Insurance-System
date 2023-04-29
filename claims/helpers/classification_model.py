import os
import joblib
from django.conf import settings
import pandas as pd

class Classification:
    def __init__(self,parameters:dict):
        self.parameters = parameters
        self.model =joblib.load(os.path.join(settings.BASE_DIR ,'claims\\models_and_pipelines\\model.pkl'))
        self.pipeline = joblib.load(os.path.join(settings.BASE_DIR , 'claims\\models_and_pipelines\\pipeline.pkl'))
        
    def classify(self):
        try:
            data_frame = pd.DataFrame(self.parameters, index=[0])
            transformed_parameters = self.pipeline.transform(data_frame)
            claim_classification = self.model.predict(transformed_parameters)
            
            return claim_classification[0]
        
        except Exception as e:
            settings.LOGGER.error(e)
            return None