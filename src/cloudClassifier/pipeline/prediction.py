import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import os


class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self):
        ## load model
        
        model = load_model(os.path.join("artifacts","training", "model.keras"))
        # model = load_model(os.path.join("model", "model.keras"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'AltoCumulus'
            return [{ "image" : prediction}]
        elif result[0] == 2:
            prediction = 'AltoStratus'
            return [{ "image" : prediction}]
        elif result[0] == 3:
            prediction = 'CirroCumulus'
            return [{ "image" : prediction}]
        elif result[0] == 4:
            prediction = 'CirroStratus'
            return [{ "image" : prediction}]
        elif result[0] == 5:
            prediction = 'Cirrus'
            return [{ "image" : prediction}]
        elif result[0] == 6:
            prediction = 'Contrail'
            return [{ "image" : prediction}]
        elif result[0] == 7:
            prediction = 'CumuloNimbus'
            return [{ "image" : prediction}]
        elif result[0] == 8:
            prediction = 'Cumulus'
            return [{ "image" : prediction}]
        elif result[0] == 9:
            prediction = 'NimboStratus'
            return [{ "image" : prediction}]
        elif result[0] == 10:
            prediction = 'StratoCumulus'
            return [{ "image" : prediction}]
        elif result[0] == 11:
            prediction = 'Stratus'
            return [{ "image" : prediction}]