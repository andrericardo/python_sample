# Environment

`python3 --version`

`pip install pytest`
`pytest --version`
This is pytest version 5.3.5

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

To restore dependencies
`pip install -r requirements.txt`

# Run tests
With pytest

`pytest application_test.py`

or with default unittest runner

`python application_test.py`
