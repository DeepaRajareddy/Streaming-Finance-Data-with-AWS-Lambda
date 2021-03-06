## Requirements
This project leads you through the process of consuming “real time” data, processing the data and then dumping it in a manner that facilitates querying and further analysis, either in real time or near real time capacity.
In doing so, you will familiarize yourself with a process that you can leverage in your professional or personal endeavors that require consumption of data that is “always on” and changing very quickly, in sub-hour (and typically) sub-minute intervals.

### This Project is broken into three parts:
 Infrastructure 
 Data collection
 Data analysis


### Infrastructure
This project consists of three major infrastructure elements that work in tandem:
1. A lambda function that gathers our data (DataTransformer)
2. A Kinesis stream that holds our data (DataCollector)
3. A serverless process that allows us to query our S3 data 

### DataAnalyzer
First, you will create a Kinesis Delivery Stream like we did in Lecture 12. Then, you will write a Lambda function that is triggered every 1 or 5 minutes, just like we configured in Lecture 13. On trigger, it will grab stock price data and place it into the delivery defined in the 

### DataTransformer. 
Finally, configure AWS Glue, pointing it to the S3 Bucket you created in your DataCollector. This will allow us to now interactively query the S3 files generated by the DataTransformer using AWS Athena to gain insight into our streamed data. This is what I am calling the DataAnalyzer.

In our collector lambda, using the yfinance module (documentation here), you will grab pricing information for each of the following stocks:
 Facebook (FB)
 Shopify (SHOP)
 Beyond Meat (BYND)
 Netflix (NFLX)
 Pinterest (PINS)
 Square (SQ)
 The Trade Desk (TTD)
 Okta (OKTA)
 Snap (SNAP)
 Datadog (DDOG)

We have to collect one full day’s worth of stock HIGH and LOW prices for each company listed above on Tuesday, December 1st 2020, at an one minute interval. Note that by “full day” we mean one day of stock trading, which is not 24 hours.

we have two options - you can use the `history` function and get a previous day’s data OR you can attempt to collect this data “in real time” (of course this would require usage of the Cloudwatch Events trigger on Lambda). Using the `history` function is definitely the easier approach and I would recommend starting there.
For each datapoint, generate a JSON object that looks like so:
{
  "high": 67.5, 
  "low": 64.61, 
  "ts": "2020-05-13 09:30:00-04:00", 
  "name": "DDOG"
}

This is an example of a single “record” that you would place into the kinesis stream defined in DataCollector. 

### Data Analysis
We want to prep this data gathered for analysis! To do so, set up a Glue crawler so that you can run AWS Athena queries against your data. Then, in Athena, write and run a query that gives us the highest hourly stock “high” per company from the list above.




 

