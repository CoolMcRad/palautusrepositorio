from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

class Pino:
    def __init__(self):
        self.query = All()

class QueryBuilder:
    def __init__(self, pino = Pino()):
        self.pino_olio = pino

    def playsIn(self, team):
        return QueryBuilder(PlaysInPino(self.pino_olio, team))

    def hasAtLeast(self, value, attribute):
        return QueryBuilder(HasAtLeastPino(self.pino_olio, value, attribute))

    def hasFewerThan(self, value, attribute):
        return QueryBuilder(HasFewerThanPino(self.pino_olio, value, attribute))

    def oneOf(self, m1, m2):
        return QueryBuilder(OrPino(m1, m2))
    
    def notOne(self, m1, m2):
        return QueryBuilder(NotPino(m1, m2))

    def build(self):
        return self.pino_olio.query

class PlaysInPino:
    def __init__(self, pino, team):
        self.query = pino.query
        self.query = And(self.query, PlaysIn(team))

class AllPino:
    def __init__(self, pino):
        self.query = pino.query
        self.query = And(self.query, All())

class HasAtLeastPino:
    def __init__(self, pino, value, attribute):
        self.query = pino.query
        self.query = And(self.query, HasAtLeast(value, attribute))

class HasFewerThanPino:
    def __init__(self, pino, value, attribute):
        self.query = pino.query
        self.query = And(self.query, HasFewerThan(value, attribute))

class NotPino:
    def __init__(self, m1, m2):
        self.query = m1
        self.query = Not(self.query, m2)

class OrPino:
    def __init__(self, m1, m2):
        self.query = m1
        self.query = Or(self.query, m2)
