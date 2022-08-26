# env setting 

python -m venv env
# python3 -m venv env if on an older system where python 2.7
# is the default version used when calling "python"

# Activate Virtual Environment
# Windows
env\Scripts\activate

# Unix-based
source env/bin/activate

# app Start 
uvicorn main:app --reload

# PORT ver App Start 
uvicorn main:app --reload --port <PORT>

