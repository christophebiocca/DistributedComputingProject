import WorkUnit
import DistributableTask

class ServerState():
    """Captures the state of the server, such as what data needs processing"""
    def __init__(self):
        self.processed = 0
        self.activeTasks = []
        self.completedTasks = []
        self.results = []

    def aggregateResults(self, data):
        self.results.extend(list(map(int, data)))

    def nextWorkUnit(self):
        tasks = list(filter(lambda x:x.finishedWorkers < 3, self.activeTasks))
        if len(tasks) == 0:
            nextTask = self.generateWorkUnit()
        else:
            nextTask = sorted(tasks, key=lambda x:x.finishedWorkers)[0].task

        return nextTask

    def displayData(self):
        return str(self.results)

    def generateWorkUnit(self):
        start = self.processed
        self.processed += 10
        end = self.processed

        newUnit = WorkUnit.WorkUnit(start, end)
        newTask = DistributableTask.DistributableTask(newUnit)

        self.activeTasks.append(newTask)
        return newUnit
