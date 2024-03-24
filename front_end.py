import streamlit as st
import subprocess

def run_yadfs_cli_command(command):
    try:
        result = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True, shell=True)
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.strip()}"

def main():
    st.title("YADFS CLI Web Interface")

    
    st.sidebar.header("Commands")

   
    st.sidebar.subheader("File Management")
    file_operation = st.sidebar.selectbox("Select File Operation", ["List Files", "Move File", "Upload File", "Download File"])

    if file_operation == "List Files":
        st.subheader("List Files")
        list_files_command = "yadfs_cli list_files"  
        result = run_yadfs_cli_command(list_files_command)
        st.text_area("Result", result, height=200)
    elif file_operation == "Move File":
        st.subheader("Move File")
        source_path = st.text_input("Source Path", "/path/to/source_file")
        destination_path = st.text_input("Destination Path", "/path/to/destination_file")
        move_file_command = f"yadfs_cli move_file {source_path} {destination_path}"  
        result = run_yadfs_cli_command(move_file_command)
        st.text_area("Result", result, height=200)
    elif file_operation == "Upload File":
        st.subheader("Upload File")
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            upload_command = f"yadfs_cli upload_file {uploaded_file.name}"  
            result = run_yadfs_cli_command(upload_command)
            st.text_area("Result", result, height=200)
    elif file_operation == "Download File":
        st.subheader("Download File")
        file_to_download = st.text_input("Enter File Path to Download", "/path/to/file")
        download_command = f"yadfs_cli download_file {file_to_download}" 
        result = run_yadfs_cli_command(download_command)
        st.text_area("Result", result, height=200)

if __name__ == "__main__":
    main()
