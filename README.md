# Automated-Quora-Answer-Scraper

This is a basic web scraper which when given a quora webpage of specific topic, scrapes questions, their answers as well as the tag associated with the questions and number of answers that have been written for that question and saves them into csv format.


The program mimics scrolling to find links of more questions that are present in the root/main webpage related to some topic. 
It is written in Python using the Selenium framework.

The user is required to enter the link of the root/main webpage. The scraper then searches it on the Chrome web-browser and extracts the links of all the questions that are present that page. To extract as many links as possible, we need to mimic scrolling.

The links of all the questions are saved into a python list. Then we loop through each of these link and open them on our browser. 


On automatic opening each of these links on the Chrome browser, various details are extracted. To extract the details, I inspected the webpage to know about the tags that cover the necessary details I needed.

The details are :
1. Question on the webpage
2. Tags associated with the question
3. No. of answers of that question
4. Top 4 answers of that question in the order they appear on the webpage



After that Later, Inspected the root page of both the links and found the tags that are associated with each question. 

The find_elements_by_xpath() function of driver is used to find the content for each of the above elements.

Then I saved each of the above elements into a .CSV file named as submission.csv. 
The sample is also present in the repository.

 
 
