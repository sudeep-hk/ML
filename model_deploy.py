import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

#load saved model
load_model=pickle.load(open('trained_model_log.sav','rb'))

input_data=(57,0,0,120,354,0,1,163,1,0.6,2,0,2)
#change input data into array
input_data_as_array=np.asarray(input_data)

#reshape the np array 
input_data_reshape=input_data_as_array.reshape(1,-1)
prediction=load_model.predict(input_data_reshape)

if prediction[0]==1:
    print('The Person has heart disease')
else:
    print('The person is healthy')