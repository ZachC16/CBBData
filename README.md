# CBBModel
A simple linear regression model to predict the point spread of a college basketball game.

If you have stumbled upon this repository in search of a starting point to build your own model, know that this model is largely untested and **I would not recommend using it for actual betting on college basketball games**. 

However, while building and testing my own model, I did scrape large amounts of game data from https://sports-reference.com that may be helpful to you. This is also available here.

Here are the coefficients from a linear regression on the game data in cleanedupgames.csv with Point.Diff as the dependent variable:

|Variables     | ...         | ...          | ...          | ...          | ...           | ...         |
|--------------|-------------|--------------|--------------|--------------|---------------|-------------|
|(Intercept)   |   Home.FG.  |    Home.2P.  |    Home.3P.  |     Home.FT  |    Home.FT.   |   Home.TRB  |
|110.197477744 | 39.958407730|  -6.924359372|   1.357944717|   0.094048031|   1.731358859 |  0.214890065| 
|     Home.TOV |      Home.PF|      Home.TS.|     Home.eFG.|     Home.3PAr|     Home.ORB. |    Home.DRB.| 
|  0.017006711 |  0.016947938| -33.832822924|  -6.565778424|   6.807511746|  -0.191335441 | -1.091333419| 
|    Home.STL. |    Home.BLK.|     Home.ORtg|     Home.DRtg|      Away.FG.|      Away.2P. |     Away.3P.| 
| -0.001131857 | -0.000849520|   0.696900058|  -0.581323619| -17.024425138|   2.801990591 | -1.246147741| 
|      Away.FT |     Away.FT.|      Away.TRB|      Away.TOV|       Away.PF|      Away.TS. |    Away.eFG.| 
| -0.066948867 | -0.277151241|  -0.173227310|   0.256102450|  -0.042516982|   6.228891463 | -0.523711747| 
|    Away.3PAr |    Away.ORB.|     Away.DRB.|     Away.STL.|     Away.BLK.|     Away.ORtg |    Away.DRtg| 
| -3.870558531 | -1.035833715|  -0.072820947|   0.010039467|  -0.007490804|            NA |           NA| 
