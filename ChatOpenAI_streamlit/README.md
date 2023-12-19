<!-- # Clone repository -->
<!-- git clone https://github.com/... -->

<!-- # Create a .env file with variables
VAR1 = 'smtp.gmail.com'
VAR2 = 587 -->

# Open terminal, create a virtual environment and activate it
python -m venv venv
venv\scripts\activate

# Make sure virtual environmetn is activated - (venv) in the beginning of command prompt
(venv) PS C:\Users\YourUser\...

# Install requirements.txt
pip install -r requirements.txt

# Run streamlit server
streamlit run main.py

