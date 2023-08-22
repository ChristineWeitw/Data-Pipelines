# Building a DAG (Directed Acyclic Graph) class 
class DAG:
    def __init__(self):
        self.root = Vertex()
    def add(self, node, to=None):
        if not node in self.graph:
            self.graph[node] = []
        if to:
            if not to in self.graph:
                self.graph[to] = []
            self.graph[node].append(to)

class Vertex:
    def __init__(self):
        self.to = []
        self.data = None

# Integrating a DAG into a pipeline
class Pipeline:
    def __init__(self):
        self.tasks = DAG()
    def task(self, depends_on=None):
        def inner(f):
            self.tasks.add(f)
            if depends_on:
                self.tasks.add(depends_on, f)
            return f
        return inner
    
def run(self):
    scheduled = self.tasks.sort()
    # Initialize a dictionary
    completed = {}
    # Check every node in the graph, and if the task is referenced, run the task with the proper input and add it to completed
    for task in scheduled:
        for node, values in self.tasks.graph.items():
            if task in values:
                completed[task] = task(completed[node])
        # If the task is not referenced, run the task without arguments and add it to completed.

        if task not in completed:
            completed[task] = task()
    return completed