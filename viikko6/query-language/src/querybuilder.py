from matchers import And, All, PlaysIn, HasAtLeast, HasFewerThan


class Query:
    def __init__(self):
        self.matchers = []

    def push(self, matcher):
        self.matchers.append(matcher)

    def pop(self):
        return self.matchers.pop()


class QueryBuilder:
    def __init__(self, query=Query()):
        self.query = query

    def playsIn(self, team: str):
        self.query.push(PlaysIn(team))
        return QueryBuilder(self.query)

    def hasAtLeast(self, value: int, attr: str):
        self.query.push(HasAtLeast(value, attr))
        return QueryBuilder(self.query)

    def hasFewerThan(self, value: int, attr: str):
        self.query.push(HasFewerThan(value, attr))
        return QueryBuilder(self.query)

    def build(self):
        return And(*self.query.matchers, All())
