# Importing necessary libraries
import boto3
import json
import datetime
# Import yfinance package
import yfinance as yf

def lambda_handler(event, context):
    
    # Initialize boto3 client
    fh = boto3.client("kinesis", "us-east-2")
    
    # Define required variables and arrays for compamny stocks we will analyze
    sdate = '2020-12-01'
    edate = '2020-12-02'
    granuality = '1m'
    stocks = ['fb', 'shop', 'bynd', 'nflx', 'pins', 'sq', 'ttd', 'okta', 'snap', 'ddog']
    
    # Fetch stock values for each company
    for stock in range(len(stocks)):
        records = yf.download(stocks[stock], start = sdate, end = edate, interval = granuality)
        
        
        # Cleaning the data and store them as a dict
        for i in range(len(records)):
            output = {"high":records['High'][i],"low":records['Low'][i],"ts":records.index[i].strftime('%m/%d/%Y %X'),"name":stocks[stock]}
            
            # Convert the data into JSON
            as_jsonstr = json.dumps(output)

            print(as_jsonstr)
    
            # Pass the stream info where the data should be stored as a single batch
            fh.put_record(
                StreamName="sta9760f2020_stream1", 
                Data = as_jsonstr,
                PartitionKey="partitionkey")
            
            
    # Return the JSON file dump    
    return {
        'statusCode': 200,
        'body': as_jsonstr
    }


lambda_handler({}, {})
