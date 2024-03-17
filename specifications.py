class User:
    def __init__(self, idu, name, username, password):
        self.name = name
        self.idu = idu
        self.username = username
        self.password = password

    def userlong(self, username, password):
        return self.password == password and self.username == username

