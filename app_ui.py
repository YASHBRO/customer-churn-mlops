import streamlit as st
import requests

# FastAPI Endpoint (Ensure FastAPI is running)
API_URL = "http://127.0.0.1:8000/predict"

# Streamlit UI
st.title("Customer Churn Prediction App")

st.markdown("### Enter Customer Details")

# Collect user inputs
Call_Failure = st.number_input("Call Failures", min_value=0, step=1)
Complains = st.number_input("Complains", min_value=0, step=1)
Subscription_Length = st.number_input(
    "Subscription Length (months)", min_value=1, step=1
)
Charge_Amount = st.number_input("Charge Amount ($)", min_value=1, step=1)
Seconds_of_Use = st.number_input("Seconds of Use", min_value=0, step=1)
Frequency_of_use = st.number_input("Frequency of Use", min_value=0, step=1)
Frequency_of_SMS = st.number_input("Frequency of SMS", min_value=0, step=1)
Distinct_Called_Numbers = st.number_input(
    "Distinct Called Numbers", min_value=0, step=1
)
Age_Group = st.number_input("Age Group", min_value=0, step=1)
Tariff_Plan = st.number_input("Tariff Plan", min_value=0, step=1)
Status = st.number_input("Status", min_value=0, step=1)
Age = st.number_input("Age", min_value=18, step=1)
Customer_Value = st.number_input(
    "Customer Value", min_value=0.0, max_value=5000.0, step=0.01
)

# Submit button
if st.button("Predict Churn"):
    # Prepare input data
    input_data = {
        "Call_Failure": Call_Failure,
        "Complains": Complains,
        "Subscription_Length": Subscription_Length,
        "Charge_Amount": Charge_Amount,
        "Seconds_of_Use": Seconds_of_Use,
        "Frequency_of_use": Frequency_of_use,
        "Frequency_of_SMS": Frequency_of_SMS,
        "Distinct_Called_Numbers": Distinct_Called_Numbers,
        "Age_Group": Age_Group,
        "Tariff_Plan": Tariff_Plan,
        "Status": Status,
        "Age": Age,
        "Customer_Value": Customer_Value,
    }

    # Send request to FastAPI
    response = requests.post(API_URL, json=input_data)

    if response.status_code == 200:
        result = response.json()
        churn_prediction = result["churn_prediction"]

        # Display result
        if churn_prediction == 1:
            st.error("🚨 The customer is likely to churn.")
        else:
            st.success("✅ The customer is NOT likely to churn.")
    else:
        st.error(
            "⚠ Error fetching prediction. Make sure the FastAPI server is running."
        )
