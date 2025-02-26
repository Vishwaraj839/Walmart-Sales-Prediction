import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model_filename = 'final_model.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# Streamlit App
def main():
    st.title("Walmart Sales Prediction")
    st.write("Enter the details to predict weekly sales")
    
    # Input fields
    store = st.number_input("Store ID", min_value=1, step=1)
    dept = st.number_input("Department ID", min_value=1, step=1)
    is_holiday = st.selectbox("Is Holiday", [0, 1])
    size = st.number_input("Store Size", min_value=1000, step=100)
    week = st.number_input("Week Number", min_value=1, max_value=52, step=1)
    year = st.number_input("Year", min_value=2010, max_value=2025, step=1)
    
    # Predict button
    if st.button("Predict Sales"):
        input_data = pd.DataFrame({
            'Store': [store],
            'Dept': [dept],
            'IsHoliday': [is_holiday],
            'Size': [size],
            'Week': [week],
            'Year': [year]
        })
        prediction = model.predict(input_data)[0]
        st.success(f"Predicted Weekly Sales: ${prediction:,.2f}")

if __name__ == "__main__":
    main()
