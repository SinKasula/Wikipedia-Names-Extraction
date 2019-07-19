How the extraction works:
-	The code uses regex and find to get elements related to people from the page.
-	If element is found then people tag is updated to true 
-	If the people tag is true then we extract the title to a file.
How the Visualization works:
(We have plotted using sample data)
-	The code gets value from the file as a tuple.
-	The common names are then grouped.
-	The code uses matplotlib library to plot the data.

Reference for visualization:
https://github.com/norvig/pytudes/blob/master/ipynb/xkcd-Name-Dominoes.ipynb
Precision Recall and F-Measure:
We took a sample of 500 records to calculate precision:
Precision : 493/500 = 0.986 
Recall: 
Step 1: No of names/No of titles = 
Step 2:  Total titles in file (including redirect pages) = 12162695
               Total names in file = 1014959
               Expected Names in file = 2432539
               Recall = 0.4172
              
[Wikipedia pages about living people :  ~15%
(Wikipedia living people pages: https://en.wikipedia.org/wiki/Category:Living_people)
(Wikipedia total pages: https://en.wikipedia.org/wiki/Wikipedia:Size_of_Wikipedia) 
Roughly 20-25% of Wikipedia articles are related to people 
(https://www.quora.com/How-many-people-have-a-Wikipedia-page-about-them-regardless-if-they-are-living-or-dead) ]
F-measure: 2PR/(P+R)
                   = 0.8177/1.3972
                   = 0.5852

