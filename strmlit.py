import numpy as np
import pickle
import streamlit as st

load_model=load_model=pickle.load(open('C:/Users/sudee/Desktop/Learning/ML/trained_model_log.sav','rb'))

#creating a function for pred
def prediction(input_data):
#change input data into array
    input_data_as_array=np.asarray(input_data)
#reshape the np array 
    input_data_reshape=input_data_as_array.reshape(1,-1)
    prediction=load_model.predict(input_data_reshape)

    if prediction[0]==1:
        return 'The Person has heart disease'
    else:
        return 'The person is healthy'

def main():
    #title for the web page
    st.title('Heart Disease Prediciton web app')

    #getting the input data from the user
    age=st.text_input('age: ')
    sex=st.text_input('sex')
    cp=st.text_input('cp')
    trestbps=st.text_input('trestbps')
    chol=st.text_input('chol')
    restecg=st.text_input('restecg')
    fbs=st.text_input('fbs')
    thalach=st.text_input('thalach')
    exang=st.text_input('exang')
    oldpeak=st.text_input('oldpeak')
    slope=st.text_input('slope')
    ca=st.text_input('ca')
    thal=st.text_input('thal')

    #code for the pred
    diagnosis=''

    #creating a button for the prediction
    if st.button('Test Result'):
        diagnosis=prediction([int(age),int(sex),int(cp),int(trestbps),int(chol),int(fbs),int(restecg),int(thalach),int(exang),int(oldpeak),int(slope),int(ca),int(thal)])
    
    st.success(diagnosis)

if __name__=='__main__':
    main()


