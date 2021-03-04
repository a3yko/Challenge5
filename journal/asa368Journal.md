# asa368 Journal


## Link to Instance <br>
http://www.adrianatanasov.com/ <br> <br>

## Crawler Purpose <br>
The crawler grabs data from tech crunch startups webpage and can be used to create an rss feed for useful articles. It would be fairly easy to filter for specific articles to make a specific list or a top 10 of the day. The crawler currently pulls all articles for 10 pages. <br><br>

## Running the Crawler <br>

Make sure you have python,pymongo,and scrapy installed on your system, then make sure Mongodb setup and running in the background <br><br>

 1. Copy the reddit folder to a pc/server with scrapy and python installed. <br>
 2. Change directory to the reddit folder on your system
 3. you can run "scrapy crawl postcrawler"<br>
 
 
 <b>Note:</b> If you would like to use the interface, go to the instance link and press the get data button. The data is updated every day so webcrunch doesn't get overloaded. <br><br>


## Problems I ran into <br><br>

https://crontab.guru/ <br>

https://m-t-a.medium.com/running-scrapy-spiders-locally-in-a-cron-job-4ce49f42678b <br>

https://serverfault.com/questions/157705/how-can-i-run-mongod-in-the-background-on-unix-mac-osx <br>

https://blog.dipasquale.fr/en/2018/12/17/incremental-scraping-with-scrapy-and-mongo/ <br> <br>


I had a really hard time with getting php to run the script locally and had no time to rewrite the whole project in angular again. I intially had written the project in angular for the UI but I couldn't get nodejs to work with mongodb. I simplified the UI into a an organized table built with PHP and a single file and it worked without a problem. The biggest issue I had was that the scrapy script would not run from a php post call no matter what I did so instead I setup a cronjob which is included in the screenshot below. <br><br>


![UI](../screenshots/cron.png) <br><br>


The image below shows the data pulled from mongodb and the code is in index.php for the mongodb connection<br>


![UI](../screenshots/uifilled.png) <br><br>

This shows the output after running the crawler, whcih successfully pulls data from the website

![output](../screenshots/output.png) <br><br>