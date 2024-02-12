create .vevn use "python3 -m venv .venv"

activate the .venv use 
windows: ".venv\Scripts\activate"
mac/linux: "source .venv/bin/activate"

export modules to requirements.txt use "pip freeze > requirements.txt"

install from a requirements.txt use "pip install -r requirements.txt"