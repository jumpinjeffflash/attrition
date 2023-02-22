import streamlit as st
import tensorflow as tf

import numpy as np
import pandas as pd

#Loading up the model we created
model = tf.keras.models.load_model('hr-model.h5')

def main():
    #Setting Application title
    st.title('uShipper Attrition Dashboard')

      #Setting Application description
    st.subheader("""This Streamlit Dashboard predicts employee churn using a fictional HR dataset created by IBM Data Scientists""")
    st.markdown("<h3></h3>", unsafe_allow_html=True)
      
    #Setting Application sidebar default

    add_selectbox = st.sidebar.selectbox(
    "Would you like to predict churn for an individual employee or multiple employees?", ("Individual Employee", "Batch file"))

    if add_selectbox == "Individual Employee":
        st.info("""NOTE: None of the data is saved and nobody can see what data is being entered (I promise!)""")
        st.write("""If we decide to analyze our own data, we'll probably find that some of the data points below don't have any impact on retention/attrition - in which case we wouldn't ask for them to power predictions in a dashboard.""")
         #Based on our optimal features selection
        age = st.slider('Age of the Employee:', min_value=18, max_value=65, value=35)
        education=st.number_input('Education: KEY 1=No College, 2=Some College, 3=Bachelors Degree, 4=Masters Degree, 5=Doctorate', min_value=1, max_value=5, value=1)
        joblevel = st.number_input('Job Level: KEY 1=Junior/Graduate, 2=Individual Contributor, 3=Manager, 4=Senior Management, 5=VP/C-Level', min_value=1, max_value=5, value=1)
        monthlyrate = st.slider('Monthly Salary (USD):', min_value=3000, max_value=15000, value=8000)
        percentsalaryhike = st.number_input('% Salary increase in last 12 months:', min_value=0, max_value=20, value=0)
        performancerating = st.number_input('Performance Rating: KEY 1=Rubbish 2=Improvement needed 3=Good 4=Really good', min_value=1, max_value=4, value=1)
        stockoptionlevel = st.number_input('Stock options: KEY 0=No stock options, 1=Has options but none vested, 2=Partially vested, 3=Fully vested', min_value=0, max_value=3, value=0)
        yearsatcompany = st.slider('Number of years with the company', min_value=1, max_value=15, value=5)
        yearsincurrentrole = st.slider('Number of years in current role', min_value=1, max_value=15, value=5)
        yearssincelastpromotion = st.slider('Years since last promotion:', min_value=1, max_value=15, value=5)
        yearswithcurrentmanager = st.slider('Years with current manager:', min_value=1, max_value=15, value=5)

        data = {
                'age': age,
                'education': education,
                'joblevel': joblevel,
                'monthlyrate': monthlyrate,
                'percentsalaryhike': percentsalaryhike,
                'performancerating': performancerating,
                'stockoptionlevel': stockoptionlevel,
                'yearsatcompany': yearsatcompany,
                'yearsincurrentrole': yearsincurrentrole,
                'yearssincelastpromotion': yearssincelastpromotion,
                'yearswithcurrmanager': yearswithcurrentmanager,
                }
            
        features_df = pd.DataFrame.from_dict([data])
        
        st.write("""Now all you have to do is click to Predict!""")
        
        if st.button('Predict'):
            if monthlyrate <= 5000 or yearssincelastpromotion >= 5 or performancerating <= 2 or percentsalaryhike <= 5:
                st.warning('This employee is probably going to leave the Ship. This is probably due to lack of promotions/salary raises and/or they have a low performance rating')
            elif age > 30 and joblevel <= 2 and education >= 3:
                st.warning('This employee is probably going to leave the Ship. They are probably seeking a more senior role.')
            elif monthlyrate > 5000 or yearssincelastpromotion < 3 or percentsalaryhike > 5 or performancerating >=3:
                st.success('This employee will most likely stay with uShip. Hooray! This is probably due to pay (rises) and/or they are high performers')

    else:
        st.info("Coming Soon! Well... if you want it...")
        st.warning("""NOTE: this is NOT BUILT YET, but this is how we'd upload the data (see below)...""")
        uploaded_file = st.file_uploader("Please choose a file")
        st.markdown("""...and then the app would read that file and get the model to make churn predictions. As with the individual employee prediction, the data isn't saved anywhere.""")
        
        if uploaded_file is not None:
            data = pd.read_csv(uploaded_file)
            #Get overview of data
            st.write(data.head(5))
            st.markdown("<h3></h3>", unsafe_allow_html=True)
            
            if st.button('Predict'):
                st.warning('CONGRATULATIONS! You get bonus points for being curious and uploading a file!! You can trade them in for Dogecoins, if you like')
        
if __name__ == '__main__':
        main()
