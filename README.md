# K6 POC

### Python minimum version required
 
 Python 3.10.13^

### Install

`pip install -r requirements.txt`

Don't forget set .env file if required!

### Run

`uvicorn app.main:app --reload --port 5000`

### Tests

`k6 run k6poc.js`

`behave`

#
That's all! :D
