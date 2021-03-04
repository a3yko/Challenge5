# Challenge 6: Web Crawlers and Scrapers

_Due Sunday, November 8 at 11:59:00pm_

_Submit through GitHub Classroom **AND** Canvas_

GitHub Classroom Link: [https://classroom.github.com/a/fjHDqQWr](https://classroom.github.com/a/fjHDqQWr)

For this challenge, I want you to use Scrapy, or another popular framework, to go to the web, scrape data, crawl to different pages, store the data in a database like MongoDB, and then display the results on a webpage hosted on your server. The project must be the same technical level or higher and meet the same requirements or better as listed here: [Web Scraper Idea](https://missouri.instructure.com/courses/42879/pages/web-scraper-idea?module_item_id=2199263)

**Help with Decision:** If you need help on making a decision then let us know. The best project idea is something that interests you!

## Getting Started and GitHub Submission Link

To start the challenge, go to the link listed above.

`Link` your account, `clone` the repository, make a new `branch`, go into the `code` directory, and `create` your application

Make sure you start a new `development` branch. The `master` branch will be the production branch. At the end, when you are finished, do the final `commit` to `development`, and the final `merge` to `master` then `push` the `master` **_and_** `development` branch back up for grading.

**If you work the entire time on master, you will get points deducted.** This is not a good industry practice.

After pushing back to `origin` for the final submission, I recommend to go to your remote repository on GitHub, download the repository which will give you a zip file of your repo on your local machine, then submit that zip to canvas. The challenge submission will require both on GitHub and Canvas.

**Note:** Make sure the Canvas submission has all of the elements that are included in your GitHub submission which includes a link to the server, the raw code, the journal, and screenshots of the application. **Make sure the canvas submission is up-to-date.**

## Overview

- These are some popular web scraping frameworks and tools available: [https://www.scrapehero.com/open-source-web-scraping-frameworks-and-tools/](https://www.scrapehero.com/open-source-web-scraping-frameworks-and-tools/)
  - We used Python Scrapy in class
- For this challenge, I want you to use Scrapy, or another popular framework, to go to the web, scrape data, crawl to different pages, store the data in database like MongoDB, and then display the results on a webpage hosted on your server
- Scrapy has good tutorials here:
  - [https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3](https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3)
  - [https://realpython.com/web-scraping-with-scrapy-and-mongodb/](https://realpython.com/web-scraping-with-scrapy-and-mongodb/)

## Requirements

Your challenge is to:

- Design and develop a web scraper that will crawl and scrape data from a website, that will allow such actions, while crawling and scraping multiple pages from that site.
  - You can crawl multiple websites, however the minimum requirements is to at least crawl and scrape one.
- The project must be at the same technical level or higher meeting the following requirements or better, which are listed here: [Web Scraper Idea](https://missouri.instructure.com/courses/42879/pages/web-scraper-idea?module_item_id=2199263)
- You must post your idea and resources you used to help you form your idea here in this discussion: [Shared Web Scraper Ideas](https://missouri.instructure.com/courses/42879/discussion_topics/752614?module_item_id=2341266) (20 points)
- The goal of this project is for you to combine the things that you have learned this semester into a working and useful application.
  - Usually the best project ideas are something that interest you or help you solve a problem you are facing!
  - This is also an opportunity to develop something that you can put in your portfolio to show a prospective employer.
- The application should not be trivial, but it should also not be so big and complex that you are not able to finish and test it.
- Now take your idea and build a web scrapping application that users can see the results on a webpage hosted on your server. Use Scrapy and other tutorials online to help you get the environment setup.
  - The TAs will run your code and watch it fill MongoDB
  - The best scenario would be for you to have your scraper setup on the server, we click a button which will run your scraper, and then we can see the results on the same page. If your scraper needs inputs like a search string, then you can include a way for us to input the search before we click the button (like a form).
    - If you do have inputs, it would be nice for you to provide a help button which will fill a default value for us (the user) and to make sure you include examples in your journal
  - **Note:** Clicking a button to run your scraper is not required but your scraper running correctly is ... so if we need to download your code, install all the proper module and dependency versions, and get everything setup correctly, then there is a high chance for error. Therefore, if we are able to run your scraper on your server where everything is already setup correctly by you, the probability of you not loosing points significantly reduces.
    - Making a server side script to run your scraper is not difficult, just a few lines of code. For example, if you plan to use a Node or PHP script to run a python script then below are some good examples:
      - Node: [https://www.npmjs.com/package/node-cmd](https://www.npmjs.com/package/node-cmd)
      - Node: [https://www.geeksforgeeks.org/run-python-script-node-js-using-child-process-spawn-method/](https://www.geeksforgeeks.org/run-python-script-node-js-using-child-process-spawn-method/)
      - PHP: [https://www.tutorialspoint.com/How-to-call-Python-file-from-within-PHP](https://www.tutorialspoint.com/How-to-call-Python-file-from-within-PHP)
      - PHP: [https://forum.freecodecamp.org/t/run-a-python-script-from-php/168433/4](https://forum.freecodecamp.org/t/run-a-python-script-from-php/168433/4)
      - Note: You can even include the search string that the user inputs as a command line argument
        - [https://stackoverflow.com/questions/23450534/how-to-call-a-python-function-from-node-js](https://stackoverflow.com/questions/23450534/how-to-call-a-python-function-from-node-js)
    - If you want us to run your scraper on our machine, your documentation should be `crystal` clear on how to set everything up so there are no errors. If we are not able to run your scraper because of poor documentation, then points will be deducted. You have been warned.
  - Then we will then go to your server and see if your site will display the results from your crawler
- The output should be in a nicely formatted view. You can use responsive designs such as no tables, or you can use frameworks to help you display the data nicely.
  - A good idea would be to use Angular with an `*ngFor` directive in order to loop through the contents and display it nicely on the page
    - Although using Angular is not required it is recommended you use a framework to help you display the contents
    - What is required is to display the output nicely ... not just a `JSON` string or a `CSV`
    - The displayed results do not need to be super fancy, but they should be readable. I recommend using a table but other HTML elements can be used.
- Lastly, you will run your code on a few examples (the minimum will be one URL with multiple pages on that URL ... just like we did in class ... by either going to the next page or going to another year), show the results from your instance, then submit your code and a markdown document, which explains how to run your code and how to setup your environment.
  - The document will contain:
    - The overall idea of what you are crawling and scraping and why that would be a valuable product
    - How to setup the environment
    - Some default examples that we can test your result with
    - The trials you face and how you were able to solve them
    - If you used something other than Scrapy, do a small comparison from the tool/framework you used versus Scrapy
      - What are the pros and cons for each
      - Why did you decided to use the other one
      - Etc.
    - Note: Make sure the document is a markdown document

**Note:** If you need help selecting an idea, you can look here for help: [Web Scraper Idea](https://missouri.instructure.com/courses/42879/pages/web-scraper-idea?module_item_id=2199263)

**If you plan on us running your scraper on `our` server:** When we are grading the assignments, if you do not provide a way for us to run your scraper, the one you built on your server, then we will be running your code on our server, so you will want to make sure you build your code to work on the default server we built in class (Either the MEAN stack with Ubuntu 18.04, MongoDB, Express, Angular, and Node or the LAMP stack with Ubuntu 18.04, Apache, Mysql, PHP). After we run your code, we will see if it lines up with what you have stored in the database. So you will want to put default queries that we can test your scraper with in the document you submit.

**If you plan on us running your scraper on `your` server:** If you built the site where we can run the scraper the way you set it up, by clicking a button to run the scraper, then you will guarantee your grade by ensuring the scraper runs correctly. You can clear all or some of the records in the database before you submit so we can see the scraper working in real time. After we run your code, we will see if it lines up with the JSON you submitted as the example with the default query. So you will want to put default queries that we can test your scraper with in the document you submit.

**Note:** Make sure you test your scraper and make sure it works ... Either run through the document that you created (act like you are the person grading the assignment) to make sure the document is crystal clear and there will be no mistakes made to ensure your scraper runs ... or make sure the scraper runs correctly on your server by testing the site throughly. My recommendation is to let us run the scraper on your server the way you set it up, which will guarantee your grade by making sure everything works correctly. Either way, make sure you test and verify everything works correctly and is good.

## What and Where to Submit

**For GitHub:**

1. Raw Code that contains:
   - Scraper code
     - Crawls webpages
     - Scrapes data
     - Uploads to Database
   - Server side code that pulls data from database
   - Front end code that displays the data
2. Journal with URL to your instance and:
   - The overall idea of what you are crawling and scraping and why that would be a valuable product
   - How to setup the environment so we can run your code
   - Some default examples that we can test your result with
   - The trials you face and how you were able to solve them
   - If you used something other than Scrapy, do a small comparison from the tool/framework you used versus scrapy
3. Screenshots of your application running with the system clock.
   - Take screenshots of ALL your finished code
   - The system clock must contain the date/time to be valid
   - **Note:** Link the screenshots in your journal as in previous challenges

**For Canvas:**

4.  Submit your URL to your instance using a "URL Submission" type
5.  Then click on `Resubmit`, download your GitHub repository after your final submission and submit that zip file on Canvas and named it `<Pawprint>WebCrawlerF20.zip` where you replace `<Pawprint>` with your actual pawprint

**NOTE:** For canvas, you cannot submit different types of submissions at the same time. Therefore, you may submit two different submissions, the first submission will be a `URL submission`, where you will copy and paste your URL to your output on the instance, then click submit. After the submission is successful, you will click on the big blue button called `Re-submit assignment`, then do a second submission for a `file upload`. You will upload a zip file from your final GitHub submission. On your end it will look like you only submitted the zip file but on our end we will see both submissions.

## Notes:

1. There is a `code` directory in the GitHub classroom template, this is where your raw code will go. Make sure you do not submit any build code here.
2. There is a `journal` directory, this is where your markdown `.md` file will go for the journal. Please link your screenshots in the journal as in previous challenges. Place your URL link in the journal. As well as the information that was asked of you in the requirements.
3. There is a `screenshots` directory, you can place your screenshots there, but please link them in your journal.

## Help

If there is anything unclear about what you need to do please let me or the TAs know. If you need help, office hours are located under `Modules` -> `Course Information` -> `Office Hours and TA Information`

## Due Date/Time

This challenge will be **due at 11:59:00PM on Sunday, November 8**. Therefore, you will have approximately 1 week to complete this assignment. This includes pushing everything to GitHub classroom, submitting the downloaded zip from GitHub on Canvas, and posting the discussion.

**NOTE:** Remember to complete the discussion board.
**NOTE:** Remember to submit link and zip file on Canvas

---

> © 2020 Professor Wergeles. All rights reserved.
> _This document is provided with the materials for an educational course and are meant for personal use by the student while participating in the course and is not to be distributed to others._
