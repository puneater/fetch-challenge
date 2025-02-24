# Receipt Processor

This is my solution to Fetch's [Receipt Processor Challenge](https://github.com/fetch-rewards/receipt-processor-challenge/).

## How to run on Docker

1. Dowload this repository as a zip file. (Defaults to fetch-challenge-main.zip)
2. Extract the zip file.
```
unzip fetch-challenge-main.zip
```
3. Change working directory to the unzipped directory
```
cd fetch-challenge-main/
```
4. Build the container image with a tagname
```
docker build -t fetch-challenge .
```
5. Start the container using the docker run command
```
docker run -dp 5000:5000 fetch-challenge
```
6. Test the deployed APIs, ```/receipts/process``` and ```/receipts/{receipt_id}/points```

## Assumptions and Notes
- Python.uuid.uuid4() is being used to generate unique IDs for receipts
- In a receipt even if some fields are missing, points will be calculated on the available fields
- For the rule to calculate reward points for Purchase Time, it strictly follows the description. The receipts with purchase time of 4:00pm and 2:00pm will not be included in reward calculation.