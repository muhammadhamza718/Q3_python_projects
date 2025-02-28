import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Set page configuration
st.set_page_config(page_title="💿 Data Sweeper", layout="wide")

st.title("💿 Data Sweeper")
st.write("Transform your files between CSV and Excel format with built-in data cleaning and visualization!")

# File Uploader
uploaded_files = st.file_uploader("Upload files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

# Process uploaded files
if uploaded_files:
    for file in uploaded_files:
        file_name = file.name
        file_size = file.size / 1024  # Convert bytes to KB
        file_ext = os.path.splitext(file_name)[-1].lower()

        # Read file into a dataframe
        if file_ext == ".csv":
            df = pd.read_csv(file) if file.size > 0 else None
        elif file_ext == ".xlsx":
            df = pd.read_excel(file) if file.size > 0 else None
        else:
            st.error(f"❌ Unsupported file type: {file_ext}")
            continue

        # Handle empty files
        if df is None:
            st.error(f"❌ The file {file_name} is empty.")
            continue

        # Display file info
        st.write(f"**📂 File Name:** {file_name}")
        st.write(f"**📏 File Size:** {file_size:.2f} KB")

        # Show DataFrame Preview
        st.write("🔍 **Preview of Dataframe**")
        st.dataframe(df.head())

        # Data Cleaning Options
        st.subheader("🧹 **Data Cleaning Options**")
        col1, col2 = st.columns(2)

        if st.checkbox(f"Enable Cleaning for {file_name}"):
            with col1:
                if st.button(f"Remove Duplicates ({file_name})"):
                    df.drop_duplicates(inplace=True)
                    st.success("✅ Duplicates Removed!")

            with col2:
                if st.button(f"Fill Missing Values ({file_name})"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.success("✅ Missing Values Filled!")

        # Column Selection
        st.subheader("🎯 **Select Columns to Keep**")
        selected_columns = st.multiselect(f"Choose Columns for {file_name}", df.columns, default=df.columns)
        df = df[selected_columns]

        # Data Visualization
        st.subheader("📊 **Data Visualization**")
        if st.checkbox(f"Show Bar Chart for {file_name}"):
            numeric_df = df.select_dtypes(include='number')
            if not numeric_df.empty:
                st.bar_chart(numeric_df.iloc[:, :2])  # Show first two numeric columns
            else:
                st.warning("⚠️ No numeric columns available for visualization.")

        # File Conversion Options
        st.subheader("🔄 **File Conversion**")
        conversion_type = st.radio(f"Convert {file_name} to:", ["CSV", "Excel"], key=file_name)

        if st.button(f"Convert {file_name}"):
            buffer = BytesIO()
            new_extension = ".csv" if conversion_type == "CSV" else ".xlsx"
            mime_type = "text/csv" if conversion_type == "CSV" else "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
            else:
                df.to_excel(buffer, index=False)

            buffer.seek(0)

            st.download_button(
                label=f"🔽 Download {file_name.replace(file_ext, new_extension)}",
                data=buffer,
                file_name=file_name.replace(file_ext, new_extension),
                mime=mime_type
            )

st.success("🎉✨ All files processed successfully!")
