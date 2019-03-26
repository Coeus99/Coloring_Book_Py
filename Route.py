class Route:
    def __init__(self):
        self.name = "Unnamed"
        self.holds = []
        self.grade = ("V",0,"")
        self.tags = []

class standardRoute(Route):
    def __init__(self):
        Route.__init__(self)

class sequenceRoute(Route):
    def __init__(self):
        Route.__init__(self)
        self.sequence = []      #a parallel list to self.holds
