class Profile:
    def __init__(self, id, username, bio, registeredAt, followers, nq, na, pts, coverurl, ppurl):
        self.id = id
        self.username = username

        self.bio = bio
        self.registeredAt = registeredAt

        self.followers = followers

        self.nquestions = nq
        self.nanswers = na
        
        self.score = pts

        self.cover_url = coverurl
        self.ppic_url = ppurl

    def pshow(self):
        print(f"ID: {self.id}\nUSERNAME: {self.username}\nBIO: {self.bio}\nREGISTERED AT: {self.registeredAt}\nFOLLOWERS: {self.followers}\nQUESTIONS: {self.nquestions}\nANSWERS: {self.nanswers}\nSCORE: {self.score}\nCOVER URL: https://asker.fun/{self.cover_url}\nPROFILE PIC URL: {self.ppic_url}")
