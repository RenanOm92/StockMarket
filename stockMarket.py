'''MktCapM is >= US$ 3 billion

1. RoE% latest FY                                                  # Return on Equity lastest Financial Year
+1 point: >20%
-1 point: <10%
0 points: otherwise

2. Latest FY trailing 12M EBIT Margin                              # EBIT Margin = (EBIT) / Total Revenue last 12M
+1 point: >12%
-1 point: <6%
0 points: otherwise

3. Common Equity to total asset ratio latest FY 
+1 point: >25%
-1 point: <15%
0 points: otherwise

4. P/E ratio 5y average
+1 point: <12
-1 point: >16
0 points: otherwise

5. Current P/E
+1 point: <12
-1 point: >16
0 points: otherwise

6. Est. Analyst Rating 2 weeks ago
+1 point: 1.0-2.0 (sell recommendation)
-1 point: 4.0-5.0 (buy recommendation)
0 points: otherwise

7. Rel. Price reaction in % on quarterly EPS reports
+1 point: >+1%
-1 point: <-1%
0 points: otherwise

8. Current FQ Est. EPS % change
+1 point: >+5%
-1 point: <-5%
0 points: otherwise

9. Price change 6 months
+1 point: >5%
-1 point: <-5%
0 points: otherwise

10. Price change 12 months
+1 point: >5%
-1 point: <-5%
0 points: otherwise

11. Price Momentum :
+1 point: 6-month price change > 5% and 12-month price change <= 5%
-1 point: 6-month price change < -5% and 12-month price change >= -5%
0 points: otherwise

12. 3-months Reversal 
+1 point: Performance in each of the last 3 months < performance of relative index
-1 point: Performance in each of the last 3 months > performance of relative index
0 points: otherwise 

13. EPS growth % from current to next FY (Est. EPS)
+1 point: > 5%
-1 point: < -5%
0 points: otherwise

Stocks with >= 4 points pass the test.
'''

#Trying with APPLE STOCKS, INPUT BY ME, DATA from http://www.wikinvest.com/stock/Apple_(AAPL)/

totalPoints = 0;

#1
roe = 39.1;                                        #http://www.wikinvest.com/stock/Apple_(AAPL)/Data/ROE

if (roe > 10):
    totalPoints += 1;
elif (roe < 10):
    totalPoints -= 1;
    
#2
ebit=68.53;                                         #http://www.wikinvest.com/stock/Apple_(AAPL)/Data/EBIT
revenue=227.54;                                     #http://www.wikinvest.com/stock/Apple_(AAPL)/Data/Total_Revenues
ebitMargin = (ebit / revenue) * 100;

if (ebitMargin > 12):
    totalPoints += 1;
elif (ebitMargin < 6):
    totalPoints -= 1;

#3
commonEquity = 119.36                              #http://www.wikinvest.com/stock/Apple_(AAPL)/Data/Common_Stock_Equity/2015
totalAssets = 290.48                               #http://www.wikinvest.com/stock/Apple_(AAPL)/Data/Total_Assets/2015
ratio= (commonEquity/totalAssets) * 100;
if (ratio > 25):
    totalPoints += 1;
elif (ratio < 15):
    totalPoints -= 1;
    

#end
    
print('Total Points: '+repr(totalPoints));
if (totalPoints > 4):
    print('Approved');
else: print ('Disapproved')

