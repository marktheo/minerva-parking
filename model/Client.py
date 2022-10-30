class Client():
    def __init__(self, id, name, phone, email, password, state):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
        self.state = state

    def getId(self):
        return str(self.id)

    def setId(self, id):
        self.id = id

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPhone(self):
        return self.phone
    
    def setPhone(self, phone):
        self.phone = phone

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state


client = Client(0, 'name', 'phone', 'email', 'password', False)