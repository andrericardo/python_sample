# Environment

`python3 --version`

Python 3.7.6
## Create Python environment

`python3 -m venv ~/.venv/python_sample`

## Source the environment

`source ~/.venv/python_sample/bin/activate`

Optional, check it's clean
`pip freeze --local`

# Install dependencies

`pip install requests`

`pip freeze --local > requirements.txt`