# StockMarket

Software desenvolvido até metade, escassez de obter alguns dados das empresas nas bolsas de valores que seriam necessários para fazer o uso da estratégia resultaram no travamento do desenvolvimento. Contornável. Criado na linguagem Python por causa da facilidade de extração de dados da web e necessidade do desenvolvedor (eu hahaha) em treinar tal linguagem. Software até o presente momento só tem  regras implementadas, nenhuma GUI (mas o planejamento era criar em etapas posteriores)

Ideia de criar um software que usa a estratégia de Susan Levermann para avaliar se uma ação é recomendada para investir. A estratégia é composta por 12 regras, que envolvem vários indicadores da empresa, gerando um parecer final.

"Susan Levermann is known as one of Germany's best funds managers. She earned this reputation over eight years at Germany's largest and best investment company, the DWS. In 2008 she got the award for "Best German Funds Manager over three years" from the highly respected rating agency Lipper.
This success was based on a stock-picking technique that she developed herself. A technique that allows profitable stocks to be selected quickly and reliably. With her book "The Relaxed Way to Richness" she presented this groundbreaking investment technique to a broader audience."

Regras:

MktCapM is >= US$ 3 billion

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

