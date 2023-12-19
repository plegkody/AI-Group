## Install git on your PC (below is a link for Windows)
```
https://git-scm.com/download/win
```

## Start a command line (cmd) and clone repository to your folder. One repository will contain all scripts we will use over the next sessions:
```
git clone https://github.com/plegkody/AI-Group.git
```

## Create a .env file with variables
```
OPENAI_API_KEY=YOUR_KEY
```

## Create a data folder if you'd like to store files (can be other folder name, change in code)

## Install Python if not yet done, e.g. Python 3.9.0 (https://www.python.org/downloads/). Push button Download Python 3.XX.XX

## Open terminal in VS code or open cmd, select foldre with repository, create a virtual environment and activate it
```
cd C:\Users\YourUser\Documents\DEV\AI Group\ChatOpenAI_streamlit
python -m venv venv
venv\scripts\activate
```

## Make sure virtual environmetn is activated - (venv) in the beginning of command prompt
```
(venv) PS C:\Users\YourUser\...
```

## Install requirements.txt
```
pip install -r requirements.txt
```

## Run streamlit server (if applicable)
```
streamlit run main.py
```

## Or run a python script 
```
python main.py
```