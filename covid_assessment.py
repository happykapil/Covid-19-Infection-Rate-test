import streamlit as st

def calculate_infection_risk(answers, temperature):
    count = sum(answers)
    if temperature >= 100:
        count += 1
    risk_percentage = count * 10
    return risk_percentage

def main():
    st.title('COVID-19 Infection Rate Test Tool')

    with st.form(key='covid_form'):
        st.subheader("Personal Information")
        name = st.text_input("Name", placeholder="Enter your name")
        age = st.number_input("Age", min_value=0, step=1)
        state = st.text_input("State", placeholder="Enter your state")

        st.subheader("Health and Travel History")
        traveled = st.checkbox("Traveled in the past 14 days to any other state")
        contact_with_infected = st.checkbox("Contact with any COVID-19 infected person")
        patient_in_vicinity = st.checkbox("COVID-19 patient within 1 km range")

        st.subheader("Pre-existing Conditions")
        col1, col2, col3 = st.columns(3)
        with col1:
            diabetes = st.checkbox("Diabetes")
            hypertension = st.checkbox("Hypertension")
        with col2:
            lung_disease = st.checkbox("Lung Disease")
            heart_disease = st.checkbox("Heart Disease")
        with col3:
            kidney_disorder = st.checkbox("Kidney Disorder")
            asthma = st.checkbox("Asthma")

        pre_existing_conditions = any([diabetes, hypertension, lung_disease, heart_disease, kidney_disorder, asthma])

        st.subheader("Current Symptoms")
        col4, col5 = st.columns(2)
        with col4:
            dry_cough = st.checkbox("Dry Cough")
            breath_shortness = st.checkbox("Shortness of Breath")
            headache = st.checkbox("Headache")
        with col5:
            aches_pains = st.checkbox("Aches and Pains")
            sore_throat = st.checkbox("Sore Throat")
            fatigue = st.checkbox("Fatigue")

        symptoms = any([dry_cough, breath_shortness, headache, aches_pains, sore_throat, fatigue])

        st.subheader("Other Health Information")
        bp_sugar_problem = st.checkbox("Suffering from BP or sugar problem")
        not_vaccinated = not st.checkbox("Vaccinated for COVID-19")

        temperature = st.number_input("Body Temperature (in F)", min_value=95.0, max_value=110.0, step=0.1, format="%.1f")

        answers = [traveled, contact_with_infected, patient_in_vicinity, pre_existing_conditions, symptoms, bp_sugar_problem, not_vaccinated]
        submit_button = st.form_submit_button(label='Submit')

    if submit_button and name and state:
        risk_percentage = calculate_infection_risk(answers, temperature)
        st.markdown("## COVID-19 Risk Assessment Report")
        st.markdown(f"#### Name: {name}")
        st.markdown(f"#### Age: {age}")
        st.markdown(f"#### State: {state}")
        st.markdown(f"#### Estimated Infection Risk: {risk_percentage}%")
        st.progress(risk_percentage / 100)

        if risk_percentage <= 20:
            st.success("You are in the green zone. Your infection rate is low.")
        elif risk_percentage <= 40:
            st.warning("You are in the orange zone. Please be cautious.")
        else:
            st.error("Alert! You are in the red zone. Consider seeking medical advice.")

if __name__ == "__main__":
    main()
