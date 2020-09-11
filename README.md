## Everis Python Challenge

In this test, we implement a simple python application following OOPs and PEP guidelines.

The structure of the project is as follows:
root_dir: everis_test
```
.
├── core.py
├── data
│   ├── output
│   │   └── 12254943.csv
│   └── store_transactions.csv
├── dockerfile
├── LICENSE
├── README.md
├── requirements.txt
├── src
│   ├── classify.py
│   ├── config.py
│   └── __init__.py
└── test
    ├── __init__.py
    └── test_classify.py

```

### Setup

It is highly advised to setup a virtual environment, this can be achieved using `virtualenv` or `pyenv`. We can install the all the required packages using `pip` python package manager, by following below commmands. 

```
virtualenv -p python3 virtpy
source virtpy/bin/activate
cd everis_test
pip install -r requirements.txt
```

### Run Python app

In order to run the python app, please make sure you are in root directory and execute
```
python core.py PRODUCT_ID
```
The `PRODUCT_ID` can be an integer, like 12254943 this will return a JSON response. 

### Run Tests 

The test are written in `pytest` in `test/` directory and can be evaluated using following command from root directory.
```
pytest -v 
```

#### Docker Setup

The repository also contains a docker file to build a docker image and run the image directory. Below commands illustrates the following.

```
cd everis_test
docker build --tag classification:1.0 .
docker run --name test classification:1.0
``` 
