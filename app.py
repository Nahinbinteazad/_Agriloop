import streamlit as st
from agents.orchestrator import AgriLoopOrchestrator

st.title("🌾 AgriLoop Farmer Dashboard")

# File uploader
uploaded_file = st.file_uploader("Upload waste image", type=["jpg", "png"])

# Input fields
location = st.text_input("Location", "Chattogram, Bangladesh")
quantity = st.number_input("Quantity (kg)", min_value=1, value=25)

# Generate report button
if st.button("Generate Report") and uploaded_file is not None:
    # Save the uploaded file temporarily
    image_path = f"temp_{uploaded_file.name}"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Run AgriLoop orchestrator
    orchestrator = AgriLoopOrchestrator()
    summary = orchestrator.run({
        "image_path": image_path,
        "location": location,
        "quantity_kg": quantity
    })
    
    # Display summary
    st.subheader("📄 Farmer Report")
    st.text_area("Report", summary, height=300)
