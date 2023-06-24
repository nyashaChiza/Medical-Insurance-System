import os
import joblib
from django.conf import settings
import pandas as pd

class Classification:
    def __init__(self, parameters: dict):
        self.parameters = parameters
        self.model = None #or joblib.load(os.path.join(settings.BASE_DIR, 'claims\\models_and_pipelines\\model.pkl'))
        self.pipeline = None #or joblib.load(os.path.join(settings.BASE_DIR, 'claims\\models_and_pipelines\\pipeline.pkl'))

    def classify_with_model(self):
        try:
            data_frame = pd.DataFrame(self.parameters, index=[0])
            transformed_parameters = self.pipeline.transform(data_frame)
            claim_classification = self.model.predict(transformed_parameters)

            return claim_classification[0]

        except Exception as e:
            settings.LOGGER.error(e)
            return None

    def classify_without_model(self):
        try:
            # Implement your classification logic here
            # You can access the parameters using self.parameters dictionary
            # Perform any necessary calculations or checks

            # Example logic:
            if self.parameters['Fee Charged'] > 1000 and self.parameters['number_of_dependants'] < 5:
                return 0  # Fraud
            elif self.parameters['number_of_claims'] > 3:
                return 0  # Fraud
            else:
                return 1  # Clean

        except Exception as e:
            settings.LOGGER.error(e)
            return None