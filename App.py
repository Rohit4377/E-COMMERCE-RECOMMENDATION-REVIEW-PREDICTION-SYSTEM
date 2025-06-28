# import streamlit as st
# import pandas as pd
# import requests

# # Mock prediction function (replace with actual ML model integration)
# def predict_values(product_id):
#     return {"Value 1": product_id * 1.1, "Value 2": product_id * 1.2, "Value 3": product_id * 1.3, "Value 4": product_id * 1.4, "Value 5": product_id * 1.5}

# # Power BI Embedded Report URL (replace with your actual Power BI report URL)
# POWER_BI_URL = "https://app.powerbi.com/view?r=eyJrIjoiZWIzYmJmOTMtMjg0MC00YzQ5LTlkMmYtZDBhYmEwZWI5OGIxIiwidCI6IjNjYjkxMTI3LTkyNDMtNGQ1Yy04NWJiLTM2Zjc4YTIwMDA2MiJ9"

# # Streamlit UI
# st.set_page_config(page_title="Product Prediction Dashboard", layout="wide")


# # Sidebar navigation
# page = st.sidebar.selectbox("Select Page", ["Predict Product Values", "Power BI Dashboard"])

# if page == "Predict Product Values":
#     st.title("Product Prediction System")
    
#     product_id = st.number_input("Enter Customer ID", min_value=1, step=1)
#     if st.button("Predict"):
#         predictions = predict_values(product_id)
#         st.write("### Predicted Values")
#         st.dataframe(pd.DataFrame(predictions.items(), columns=["Metric", "Value"]))
        
#         # Simulate updating Power BI (you'd likely send data via API to update it)
#         st.success("Power BI dashboard updated with new predictions!")

# elif page == "Power BI Dashboard":
#     st.title("Live Power BI Dashboard")
#     st.markdown(f'<iframe src="{POWER_BI_URL}" width="100%" height="600"></iframe>', unsafe_allow_html=True)


import streamlit as st
import pandas as pd
import requests

# Mock prediction function (replace with actual ML model integration)
def predict_values(product_id):
    return {"Value 1": product_id * 1.1, "Value 2": product_id * 1.2, "Value 3": product_id * 1.3, "Value 4": product_id * 1.4, "Value 5": product_id * 1.5}

# Power BI Embedded Report URL (replace with your actual Power BI report URL)
POWER_BI_URL = "https://app.powerbi.com/view?r=eyJrIjoiZWIzYmJmOTMtMjg0MC00YzQ5LTlkMmYtZDBhYmEwZWI5OGIxIiwidCI6IjNjYjkxMTI3LTkyNDMtNGQ1Yy04NWJiLTM2Zjc4YTIwMDA2MiJ9"

# Streamlit UI
st.set_page_config(page_title="Product Prediction Dashboard", layout="wide")

# Set Background Image
page_bg_img = '''
<style>
.stApp {
    background-image: url("https://source.unsplash.com/1600x900/?technology,abstract");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Product Prediction and Power BI Dashboard")

# Prediction Section
st.header("Product Prediction System")
product_id = st.number_input("Enter Product ID", min_value=1, step=1)
if st.button("Predict"):
    predictions = predict_values(product_id)
    st.write("### Predicted Values")
    st.dataframe(pd.DataFrame(predictions.items(), columns=["Metric", "Value"]))
    st.success("Power BI dashboard updated with new predictions!")

# Power BI Dashboard Section
st.header("Live Power BI Dashboard")
st.markdown(f'<iframe src="{POWER_BI_URL}" width="100%" height="600"></iframe>', unsafe_allow_html=True)
