import json

class Question:
    # Question's constructor
    def __init__(self, id, title, username):
        self.id = id

        self.title = title
        self.username = username
    
    # Showing attributes (in pretty format)
    def pshow(self):
        print(30 * "=")
        print(f"ID: {self.id}\nTITLE: {self.title}\nUSER: {self.username}")
