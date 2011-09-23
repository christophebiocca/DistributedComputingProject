class DistributableTask:
    """the info kept by the server about each work unit"""

    def __init__(self, newTask):
        self.task = newTask
        self.activeWorkers = 0
        self.finishedWorkers = 0
