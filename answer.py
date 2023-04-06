class Answer:
    # Constructor
    def __init__(self, id, qid, username, text):
        self.id = id
        self.qid = qid

        self.username = username
        self.text = text

    # Showing attributes (in pretty format)
    def pshow(self):
        print(30 * "=")
        print(f"Id: {self.id}\nQUESTION ID: {self.qid}\nUSER: {self.username}\nTEXT: {self.text}")

