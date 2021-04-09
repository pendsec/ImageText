import joblib
import pandas as pd
import numpy as np
from keras.preprocessing import sequence
from keras.preprocessing import image
from keras.preprocessing.sequence import pad_sequences

class GAN:
    def __init__(self):
        path_to_artifacts = "../../research/"
        self.model_new = joblib.load(path_to_artifacts + "encoders.joblib")
        self.model = joblib.load(path_to_artifacts + "random_forest.joblib")


    def preprocess(img):
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        return x

    def encode(image):
        image = self.preprocess(image) 
        fea_vec = self.model_new.predict(image) 
        fea_vec = np.reshape(fea_vec, fea_vec.shape[1])
        return fea_vec

    def beam_search_predictions(image, beam_index = 3):
        start = [wordtoix["startseq"]]
        start_word = [[start, 0.0]]
        while len(start_word[0][0]) < max_length:
            temp = []
            for s in start_word:
                par_caps = sequence.pad_sequences([s[0]], maxlen=max_length, padding='post')
                preds = self.model.predict([image,par_caps], verbose=0)
                word_preds = np.argsort(preds[0])[-beam_index:]
                # Getting the top <beam_index>(n) predictions and creating a 
                # new list so as to put them via the model again
                for w in word_preds:
                    next_cap, prob = s[0][:], s[1]
                    next_cap.append(w)
                    prob += preds[0][w]
                    temp.append([next_cap, prob])
                        
            start_word = temp
            # Sorting according to the probabilities
            start_word = sorted(start_word, reverse=False, key=lambda l: l[1])
            # Getting the top words
            start_word = start_word[-beam_index:]
        
        start_word = start_word[-1][0]
        intermediate_caption = [ixtoword[i] for i in start_word]
        final_caption = []
    
        for i in intermediate_caption:
            if i != 'endseq':
                final_caption.append(i)
            else:
                break

        final_caption = ' '.join(final_caption[1:])
        return final_caption

    def greedySearch(photo):
        in_text = 'startseq'
        for i in range(max_length):
            sequence = [wordtoix[w] for w in in_text.split() if w in wordtoix]
            sequence = pad_sequences([sequence], maxlen=max_length)
            yhat = self.model.predict([photo,sequence], verbose=0)
            yhat = np.argmax(yhat)
            word = ixtoword[yhat]
            in_text += ' ' + word
            if word == 'endseq':
                break

        final = in_text.split()
        final = final[1:-1]
        final = ' '.join(final)
        return final

    def compute_prediction(self, img, model_type, beam_index):
        try:
            photo = self.encode(img).reshape(1, 2048)
            prediction = None
            if model_type == "greedy":
                prediction = self.greedySearch(photo)  # only one sample
            else:
                prediction = self.beam_search_predictions(model_type, beam_index)
        except Exception as e:
            return {"status": "Error", "message": str(e)}

        return prediction