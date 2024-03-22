import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import streamlit as st
import joblib 


df = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
model = joblib.load('Sleep_Health_model.pkl')
encoder = joblib.load('Sleep_Health_encoder.pkl')
df.drop('Person ID', axis=1, inplace = True)


st.image('osborne.png')
st.markdown("<br>", unsafe_allow_html= True)


st.markdown("<h1 style = 'color: #0C2D57; text-align: center; font-family: helvetica'>Osborne Health Care</h1>", unsafe_allow_html = True)
st.markdown("<h4 style = 'margin: -30px; color: #F11A7B; text-align: center; font-family: cursive '> Sleep Disorder Specialist </h4>", unsafe_allow_html = True)
st.markdown("<br>", unsafe_allow_html= True)


st.image('doctors.png')
st.markdown("<br>", unsafe_allow_html= True)
st.markdown("<h4 style = 'margin: -30px; color: green; text-align: center; font-family: helvetica '>Project Overview</h4>", unsafe_allow_html = True)   
st.write("Join us on a journey into the world of sleep disorders. From insomnia to sleep apnea, we explore the causes, symptoms, and treatments of these conditions. Our project aims to raise awareness, provide resources, and offer support for those affected by sleep disorders, helping them on their path to better sleep and overall health.")


st.markdown("<br>",unsafe_allow_html = True)
st.dataframe(df, use_container_width = True)


st.sidebar.image('heart-health.png', 'Welcome Dear User')

Age = st.sidebar.number_input('Age')
Sleep_Duration = st.sidebar.number_input('Sleep Duration')
Systolic = st.sidebar.number_input('Systolic')
Diastolic= st.sidebar.number_input('Diastolic')
Daily_Steps = st.sidebar.number_input('Daily Steps')
Heart_Rate = st.sidebar.number_input('Heart Rate')
QoS = st.sidebar.number_input('Quality of Sleep')
PaL= st.sidebar.number_input('Physical Activity Level')

st.markdown("<br>",unsafe_allow_html = True)
st.markdown("<br>",unsafe_allow_html = True)
st.markdown("<br>",unsafe_allow_html = True)

st.markdown("<h4 style = 'margin: -30px; color: green; text-align: center; font-family: helvetica '> Input Variable </h4>", unsafe_allow_html = True)   

inputs = pd.DataFrame()

inputs['Age'] = [Age]
inputs['Sleep Duration'] = [Sleep_Duration]
inputs['Systolic'] = [Systolic]
inputs['Diastolic'] = [Diastolic]
inputs['Daily Steps'] = [Daily_Steps]
inputs['Heart Rate'] = [Heart_Rate]
inputs['Quality of Sleep'] = [QoS]
inputs['Physical Activity Level'] = [PaL]



st.dataframe(inputs, use_container_width= True)




prediction_button = st.button('Predict sleep disorder')
if prediction_button:
    predicted = model.predict(inputs)

    if predicted[0]==0:
        st.success(f'Your predicted Sleep Disorder is; Insomnia')
    elif predicted[0]==1:
        st.success(f'Your predicted Sleep Disorder is; None')
    else:
        st.success(f'Your predicted Sleep Disorder is; Sleep Apnea')

# 0 = 'Insomnia'
# 1 = 'None'
# 2 = 'Sleep Apnea'
