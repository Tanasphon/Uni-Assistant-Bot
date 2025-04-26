import streamlit.web.cli as stcli
import sys
import os

def main():
    # Add the project root directory to Python path
    project_root = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(project_root)
    
    # Get the absolute path to the app.py file
    app_path = os.path.join(project_root, "src", "app.py")
    
    # Set up the command line arguments for Streamlit
    sys.argv = [
        "streamlit",
        "run",
        app_path,
        "--global.developmentMode=false",
    ]
    
    # Run the Streamlit app
    sys.exit(stcli.main())

if __name__ == "__main__":
    main() 