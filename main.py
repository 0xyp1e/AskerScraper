import requests
from bs4 import BeautifulSoup
from question import Question
import json
import os
import sys

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
def get_recent_questions(n, fid = 0, verbose = False):
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
        
        if verbose:
            print(f"Getted {getted} questions!")
    
    print()
    return questions

'''
Show help
'''
def showh():
    print("\nAskerScraper - Retrieve Asker Q&A Community content!")
    print("Usage: ./<binary> <COMMAND> [OPTIONS]\n")

    print("[] means optional and it will be replaced by some default value; <> means mandatory.")

    print("The default command is '--get-recent 10', and its output will be displayed in the default format 'pretty'. See formats for more information.\n")
    print("Available commands:")

    print("\t-h, --help - Show this help")
    print("\t-g, --get-recent [n questions] - Get n last questions")

    print("\nAvailable options:")

    print("\t-f, --format <specified format> - Format the output")
    print("\t-v, --verbose - *be careful when redirecting output: not only the default output will be displayed.")

    print("\nAvailable formats:")
    
    print("\tpretty")
    print("\tjson")

    die("")

'''
Outputs a message and finish the application.
'''
def die(msg, status = 0):
    print(msg)
    print()

    exit(status)

def hasformat():
    return ("-f" or "--format") in sys.argv 

def getformat(defaultf = "pretty"):
    # By -f alias
    if "-f" in sys.argv:
        if not sys.argv.index("-f") + 1 >= len(sys.argv):
            return sys.argv[sys.argv.index("-f") + 1]

    # By --format fullname
    elif "--format" in sys.argv:
        if not sys.argv.index("--format") + 1 >= len(sys.argv):
            return sys.argv[sys.argv.index("--format") + 1]

    # Not specified, using default format
    return defaultf

def getverbose():
    return "-v" in sys.argv or "--verbose" in sys.argv

def validc(command):
    return command in [ "g", "--get-recent", "h", "--help" ]

def valido(option):
    return option in [ "v", "--verbose", "f", "--format" ]

def validf(format):
    return format in [ "pretty", "json" ]

def validUsage(cmd, format):
    return validc(cmd) and validf(format)

def getcmdi(cmd):
    if cmd == ("-h") or cmd == "--help":
        return "h"
    elif cmd == "-g" or cmd == "--get-recent":
        return "g"
    
    return ""

def main():
    # Validating command
    if len(sys.argv) <= 1:
        die("No command provided. Use --help for more information.")

    # Global variables    
    COMMAND = getcmdi(sys.argv[1])
    VERBOSE = getverbose()
    FORMAT = getformat()
    
    # Validating usage
    if not validUsage(COMMAND, FORMAT):
        die("Invalid usage. Use --help for more information.")
    
    # Doing what it should do
    if COMMAND == "h":
        showh()
    elif COMMAND == "g":
        qs = get_recent_questions(10, verbose=VERBOSE)

        if FORMAT == "pretty":
            for q in qs:
                q.pshow()
        elif FORMAT == "json":
            print(json.dumps([q.__dict__ for q in qs]))

main()
