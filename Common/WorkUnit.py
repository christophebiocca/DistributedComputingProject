class WorkUnit:
    """The data to sent to a node to process"""
    def init(self, start, end):
        self.workUnitProtocolVersion = 1

        self.rangeStart = start
        self.rangeEnd = end
