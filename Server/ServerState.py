class ServerState():
    """Captures the state of the server, such as what data needs processing"""
    def __init__(self):
        self.processed = 0
        self.results = []

    def aggregateResults(self, data):
        self.results.extend(list(map(int, data)))

    def nextData(self):
        self.processed += 10
        return (self.processed - 10, self.processed)

    def displayData(self):
        return str(self.results)