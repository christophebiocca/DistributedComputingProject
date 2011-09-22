class WorkUnit:
    """The data to sent to a node to process"""
    def __init__(self, start, end):
        self.workUnitProtocolVersion = 1

        self.rangeStart = start
        self.rangeEnd = end
