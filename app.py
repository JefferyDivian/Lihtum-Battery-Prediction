import streamlit as st
import pickle

model_linear=open("finalized_model.pickle",'rb')
linear_reg = pickle.load(model_linear)
model_scaling = pickle.load(open("finalized_scaling.pickle",'rb'))

st.title("Battery analysis")

st.header("Get input:")
soc = st.text_input('State of charge of the Battery')
soh = st.text_input('State of health of the Battery')
power = st.text_input('Power')

if soc and soh and power:
    print(soc)
    print(soh)
    print(power)

    scaled=model_scaling.transform([[soc,soh,power]])
    a = linear_reg.predict(scaled)
    st.header("Predicted value {}".format(a))

