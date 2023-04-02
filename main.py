import requests
from bs4 import BeautifulSoup
from question import Question
import json

'''
AskerScraper - Retrieve Asker Q&A Community content
https://github.com/0xyp1e/AskerScraper

Written by 0xyp1e, https://github.com/0xyp1e
DISCLAIMER: I don't own any website's resources and if it's the case I can delete all of this.
'''

'''
Gets a question's id from a li question item.
'''
def getq_id(liq):
    return int(liq["data-id"])

'''
Gets the user's username who asked a question from a li question item.
'''
def getq_username(liq):
    return liq.find("span", class_="qcreator-small").string.strip()

'''
Gets the question's title from a li question item.
'''
def getq_title(liq):
    return liq.find("a", class_="q-title").text.strip()

'''
Transforms a liq into a Question obj.
'''
def transformliq(liq):
    return Question(getq_id(liq), getq_title(liq), getq_username(liq))

'''
Gets 'n' questions.
'''
def get_questions(n, fid = 0):
    questions = []

    getted = 0
    nextfqid = fid

    while getted < n:
        # Getting questions
        url = f"https://asker.fun/more_questions?maxid={nextfqid}&order=c&cat=0&max_questions=1"
        html = requests.get(url).text

        # "Souping it"
        soup = BeautifulSoup(html, "html.parser")

        # Getting questions links
        questions_links = soup.find_all("li", class_="list-group-item")

        # Retrieving only remaining questions
        questions_links = questions_links[0:n - getted]
        
        # Saving them
        for q in questions_links:
            question = transformliq(q)
            questions.append(question)

        # Getting next question's id to retrieve
        nextfqid = getq_id(questions_links[len(questions_links) - 1]) - 1

        # Increasing number of getted questions
        getted += len(questions_links)
        print(f"Getted {getted} questions!")
    
    print()
    return questions

'''
App's entry point.
'''
def main(n, fid = 0):
    questions = get_questions(n, fid)

    # Printing all questions in JSON format:
    print(json.dumps([q.__dict__ for q in questions]))

main(50, 0)
