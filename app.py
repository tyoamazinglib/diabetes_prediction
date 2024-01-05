import streamlit as st
import streamlit.components.v1 as stc
import pickle

with open('models/rf_model.pkl','rb') as file:
    Random_Forest_Model = pickle.load(file)

html_temp = """
    <div style="background-color:#008000;padding:20px;border-radius:10px;box-shadow: 5px 10px 18px #888888;">
        <img src="https://stickershop.line-scdn.net/stickershop/v1/product/1006864/LINEStorePC/main.png?v=1" alt="Diabetes Prediction" style="width:50px;height:50px;">
        <h1 style="color:white;text-align:center;font-size:2.5em;">Diabetes Prediction</h1>
    </div>
"""

desc_temp = """
    ### Diabetes Prediction App
    This app will be used by the insurance team to predict diabetes of the user.
    #### Pandas Team
    - Vio W. Prinandita
    - Nugroho Budi Prasetyo
    - M. Armand Gaffar
    - M. Ridwan
    - M. Iqbal
    - Dian Retno W.
    - Azizah Nurmahdyah
    - Nabil Shaleh
    #### App Content
    - Machine Learning Section
"""

def main():
    stc.html(html_temp)

    menu = ["Home", "Machine Learning"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        st.markdown(desc_temp, unsafe_allow_html=True)
    elif choice == "Machine Learning":
        run_ml_app()

def run_ml_app():
    st.subheader("Diabetes Prediction")
    
    # Create a two-column layout
    left, right = st.columns([1, 1])
    
    # Add content to the left column
    with left:
        pregnancies = st.number_input('Pregnancies', value=0, step=1)
        glucose = st.number_input('Glucose', value=0, step=1)
        blood_pressure = st.number_input('Blood Pressure', value=0, step=1)
        skin_thickness = st.number_input('Skin Thickness', value=0, step=1)
        insulin = st.number_input('Insulin', value=0, step=1)
    
    # Add content to the right column
    with right:
        bmi = st.number_input('BMI', value=0.0, step=0.1)
        dpf = st.number_input('Diabetes Pedigree Function', value=0.0, step=0.01)
        age = st.number_input('Age', value=0, step=1)
    
    # Add a button for prediction
    button = st.button('Predict')
    
    # If button is clicked
    if button:
        # Make prediction
        result = predict(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age)
        
        # Display prediction result
        if result == 1:
            st.success('Prediction: You have diabetes')
        else:
            st.warning('Prediction: You do not have diabetes')

def predict(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age):
    # Making prediction
    prediction = Random_Forest_Model.predict([[pregnancies, glucose, blood_pressure, skin_thickness,
                                               insulin, bmi, dpf, age]])
    return prediction[0]

if __name__ == "__main__":
    main()
