# Python-Challenge: PyBank and PyPoll
Using the os and csv modules in Python, a financial dataset (budget_data.csv in the 'Resources' folder of PyBank) and election poll dataset (election_data.csv in the 'Resources' folder of PyPoll) were analyzed. The findings were printed out in a text file ('output.txt' in the 'Analysis' folder) within their respective directories. 

## PyBank

From the [financial dataset](PyBank/Resources/budget_data.csv) consisting of columns 'Date' and 'Profit/Losses,' a Python script was made to identify:
  - The total number of months encompassed 
  - The total Profit/Losses
  - The changes in Profit/Losses and average of the changes
  - The date and amount of the greatest increase in profits
  - The date and amount of the greatest decrease in profits

Running the script produced the following, and saved the contents as a [text file](PyBank/Analysis/output.txt).
```
Financial Analysis
----------------------
Total Months: 86
Total: $22564198
Average Change: $-8214.47
Greatest Increase in Profits: Mar-13 ($1141840)
Greatest Decrease in Profits: Dec-10 ($-1194133)
```

## PyPoll

From the [election poll dataset](PyPoll/Resources/election_data.csv), consisting of columns 'Voter ID,' 'Country,' and 'Candidate,' a Python script was made to identify:
  - The total number of votes
  - A list of candidates
  - The number of votes each candidate received 
  - The perentage of total votes each candidate received 
  - The winner of the election 

The election analysis, printed below, was saved as a [text file](PyPoll/Analysis/output.txt). 
```
Election Results
----------------------
Total Votes: 369711
----------------------
Charles Casper Stockham: 73.812% (272892
Diana DeGette: 23.049% (85213)
Raymon Anthony Doane: 3.139% (11606)
----------------------
Winner: Charles Casper Stockham
---------------------
```
