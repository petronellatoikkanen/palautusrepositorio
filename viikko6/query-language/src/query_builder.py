from player_reader import PlayerReader

from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, matcher = None):
        self.matcher = matcher or All()
    
    def playsIn(self, team):
        return QueryBuilder(And(self.matcher, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.matcher, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.matcher, HasFewerThan(value, attr)))

    def oneOf(self, q1, q2):
        return QueryBuilder(Or(q1, q2))

    def build(self):
        return self.matcher
    