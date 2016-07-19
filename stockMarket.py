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

import requests
from bs4 import BeautifulSoup

totalPoints = 0;
#stockName = raw_input("Enter the stock name.");
stockName = "Apple_(AAPL)";

#1

url_to_scrape = 'http://www.wikinvest.com/stock/%s/Data/ROE' % stockName ;

r = requests.get(url_to_scrape)
 
soup = BeautifulSoup(r.text)

roe = soup.find( id = "nv_value")
roe = float(roe.string.strip("%"))

#roe = 39.1;                                        #http://www.wikinvest.com/stock/Apple_(AAPL)/Data/ROE

if (roe > 10):
    totalPoints += 1;
elif (roe < 10):
    totalPoints -= 1;
    
print(totalPoints);

#2

#ebit=68.53;                                        #http://www.wikinvest.com/stock/Apple_(AAPL)/Data/EBIT
url_to_scrape = 'http://www.wikinvest.com/stock/%s/Data/EBIT' % stockName ;
#url_to_scrape = 'http://www.wikinvest.com/stock/Continental_Resources_(CLR)/Data/EBIT'
r = requests.get(url_to_scrape) 
soup = BeautifulSoup(r.text)
ebit = soup.find( id = "nv_value")

#revenue=227.54;                                     #http://www.wikinvest.com/stock/Apple_(AAPL)/Data/Total_Revenues
url_to_scrape = 'http://www.wikinvest.com/stock/%s/Data/Total_Revenues' % stockName ;
#url_to_scrape = 'http://www.wikinvest.com/stock/Continental_Resources_(CLR)/Data/Total_Revenues'
r = requests.get(url_to_scrape)
soup = BeautifulSoup(r.text)
revenue = soup.find( id = "nv_value")    

ebit = ebit.string.replace("$","")
revenue = revenue.string.replace("$","")

if (ebit.find("million") > 0 and revenue.find("million") > 0):
    ebit = float(ebit.replace("million",""))
    revenue = float(revenue.replace("million",""))
elif (ebit.find("million") > 0 and revenue.find("billion") > 0):
    ebit = float(ebit.replace("million",""))
    ebit = ebit / 1000
    revenue = float(revenue.replace("billion",""))
elif (ebit.find("billion") > 0 and revenue.find("million") > 0):
    ebit = float(ebit.replace("billion",""))
    revenue = float(revenue.replace("million",""))
    revenue = revenue / 1000
else:
    ebit = float(ebit.replace("billion",""))
    revenue = float(revenue.replace("billion",""))
    
print "Ebit value: ",ebit
print "Revenue value: ",revenue
ebitMargin = (ebit / revenue) * 100;

if (ebitMargin > 12):
    totalPoints += 1;
elif (ebitMargin < 6):
    totalPoints -= 1;

print(totalPoints);
#3
commonEquity = 119.36                              #http://www.wikinvest.com/stock/Apple_(AAPL)/Data/Common_Stock_Equity/2015
totalAssets = 290.48                               #http://www.wikinvest.com/stock/Apple_(AAPL)/Data/Total_Assets/2015
ratio= (commonEquity/totalAssets) * 100;
if (ratio > 25):
    totalPoints += 1;
elif (ratio < 15):
    totalPoints -= 1;
    
print(totalPoints);
#4
pe = [11.98,15.67,12.00,15.10,13.78];              #http://www.gurufocus.com/term/pe/AAPL/PE-Ratio/Apple-Inc
average = sum(pe)/float(len(pe));
if (average < 12):
    totalPoints += 1;
elif (average > 16):
    totalPoints -= 1;

print(totalPoints);
#5
currentPE = 10.81;                               #http://www.gurufocus.com/term/pe/AAPL/PE-Ratio/Apple-Inc
if (currentPE < 12):
    totalPoints += 1;
elif (currentPE > 16):
    totalPoints -= 1;

print(totalPoints);
#6
#Est. Analyst Rating ?????

#7 Rel. Price reaction in % on quarterly EPS reports

#8 Current FQ Est. EPS % change
epsCurrent = 2.27                               #http://www.wikinvest.com/stock/Apple_(AAPL)/Data/Earnings_Per_Share
epsPrevious = 2.38

changeEPS = epsCurrent / epsPrevious;

if (changeEPS >= 1.05):
    totalPoints += 1;
elif (changeEPS <= 0.95):
    totalPoints -= 1;
    
print(totalPoints);

#9 Price change 6 months                    #http://www.gurufocus.com/stock/AAPL
price6monthsCurrent = 98.78;
price6monthsPrevious = 97.13;

changePrice6months = price6monthsCurrent/ price6monthsPrevious;

if (changePrice6months >= 1.05):
     totalPoints += 1;
elif (changePrice6months <= 0.95):
    totalPoints -= 1;
    
print(totalPoints);

#10 Price change 12 months                  #http://www.gurufocus.com/stock/AAPL
price12monthsCurrent = 98.78;
price12monthsPrevious = 132.07;

changePrice12months = price12monthsCurrent / price12monthsPrevious;

if (changePrice12months >= 1.05):
     totalPoints += 1;
elif (changePrice12months <= 0.95):
    totalPoints -= 1;
    
print(totalPoints);

#11 Price Momentum

if (changePrice6months > 1.05 and changePrice12months <= 1.05 ):
    totalPoints += 1;
elif (changePrice6months < 0.95 and changePrice12months >= 0.95):
    totalPoints -= 1;
    
print(totalPoints);

#12 3-months Reversal 


#end
    
print('Total Points: '+repr(totalPoints));
if (totalPoints >= 4):
    print('Approved');
else: print ('Disapproved')
