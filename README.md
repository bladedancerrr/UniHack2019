# UniHack2019
Bayleef's project for UniHack 2019

# Tech stack
Using chalice aws framework to host API with AWS Services including Lambda, API Gateway

# Directory information

Note: resources folder has the old implementation of getstudyspace without using chalice, now the .py files are in chalice/getstudyspace/chalicelib

tree:
.
├── README.md
├── chalice
│   ├── getstudyspace
│   │   ├── __pycache__
│   │   │   └── app.cpython-36.pyc
│   │   ├── app.py
│   │   ├── chalicelib
│   │   │   ├── __pycache__
│   │   │   │   ├── busytimes.cpython-36.pyc
│   │   │   │   ├── nearBySearch.cpython-36.pyc
│   │   │   │   └── timeAndDistance.cpython-36.pyc
│   │   │   ├── busytimes.py
│   │   │   ├── checkPlatform.py
│   │   │   ├── nearBySearch.py
│   │   │   ├── numDevices.py
│   │   │   └── timeAndDistance.py
│   │   ├── requirements.txt
│   │   └── vendor
│   │       └── populartimes
│   │           ├── __init__.py
│   │           └── crawler.py
│   └── test_post
└── resources
    ├── busytimes.py
    ├── checkPlatform.py
    ├── function.zip
    ├── lambda_function.py
    ├── nearBySearch.py
    ├── numDevices.py
    ├── populartimes
    │   ├── LICENSE.md
    │   ├── README.md
    │   ├── content
    │   │   └── bars_visualization.gif
    │   ├── populartimes
    │   │   ├── __init__.py
    │   │   └── crawler.py
    │   ├── setup.cfg
    │   ├── setup.py
    │   └── tests
    │       ├── __init__.py
    │       └── test_get_circle_centers.py
    ├── rooms_data
    │   ├── convert_json_to_csv.py
    │   ├── data
    │   │   ├── rooms_all.csv
    │   │   ├── rooms_data.csv
    │   │   ├── subject_data.csv
    │   │   └── subject_data2.csv
    │   ├── ignore_sem2.py
    │   ├── reformat_locations.py
    │   ├── room_data.py
    │   ├── test_api.json
    │   ├── test_api_data.csv
    │   └── uni_subjs.json
    └── timeAndDistance.py
