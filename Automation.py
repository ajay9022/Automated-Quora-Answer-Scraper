import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv


with open('submission.csv','w') as file:
    file.write("Question,No. of answers,Tags,4 answers")
link1='https://www.quora.com/topic/CAT-Preparation'
link2='https://www.quora.com/topic/Graduate-Record-Examination-GRE-1'
manylinks = list()
manylinks.append(link1)
manylinks.append(link2)
for olink in manylinks:
    qlinks = list()    
    browser = webdriver.Chrome(executable_path='/Users/ajay/Downloads/chromedriver')
    browser.get(olink)
    time.sleep(1)
    elem = browser.find_element_by_tag_name("body")
    #print(elem,'\n\n',elem.text)

    no_of_pagedowns = 50
    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        no_of_pagedowns-=1
    post_elems =browser.find_elements_by_xpath("//a[@class='question_link']")
    for post in post_elems:
        qlink = post.get_attribute("href")
        print(qlink)
        qlinks.append(qlink)

    for qlink in qlinks:

        append_status=0

        row = list()
        #browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
        browser.get(qlink)
        time.sleep(1)


        elem = browser.find_element_by_tag_name("body")
        #print(elem,'\n\n',elem.text)

        no_of_pagedowns = 1
        while no_of_pagedowns:
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)
            no_of_pagedowns-=1


        #Question Names
        qname =browser.find_elements_by_xpath("//div[@class='question_text_edit']")
        for q in qname:
            print(q.text)
            row.append(q.text)


        #Answer Count    
        no_ans = browser.find_elements_by_xpath("//div[@class='answer_count']")
    #    print("No. of ans :")
        for count in no_ans:
    #        print(count.text)
            append_status = int(count.text[:2])

            row.append(count.text)

        #Tags
        tags = browser.find_elements_by_xpath("//div[@class='header']")
    #    print("\nTag :")
        tag_field = list()
        for t in tags:
            tag_field.append(t.text)
    #        print(t.text,'\n')
        row.append(tag_field)


        #All answers
        all_ans=browser.find_elements_by_xpath("//div[@class='ui_qtext_expanded']")
        i=1
        answer_field = list()
        for post in all_ans:
            if i<=4:
                i=i+1
    #            print("Answer : ")
    #            print(post.text)
                answer_field.append(post.text)
            else:
                break   
        row.append(answer_field)


        print('append_status',append_status)

        if append_status >= 4:
            with open('submission.csv','a') as file:
                writer = csv.writer(file)
                writer.writerow(row)
