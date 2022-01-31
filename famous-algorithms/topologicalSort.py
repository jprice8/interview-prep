def topologicalSort(jobs, deps):
    # 1. Set up dictionary for adjacency list
    # 2. Iterate through length of jobs, and traverse neighbors.
    # 3. Check if already in job order array.
    # 4. Add to job order array once there's no more neighbors.
    jobOrder = []
    graph = getAdjacencyList(jobs, deps)

    for i in range(len(jobs)):
        job = jobs[i]

        if job in jobOrder:
            continue 

        # Traverse neighbors
        neighbors = graph[job]
        findJobWithNoPrereqs(neighbors, graph, job, jobOrder)
        if len(jobOrder) == len(jobs):
            return jobOrder

    # return jobOrder


def findJobWithNoPrereqs(neighbors, graph, job, jobOrder):
    while len(neighbors) > 0: # []
        currentPreReq = neighbors.pop()
        jobToComplete = currentPreReq[0]

        # Check if we've already added it to our list
        if jobToComplete in jobOrder:
            continue
        elif jobToComplete in graph:
            findJobWithNoPrereqs(graph[jobToComplete], graph, jobToComplete, jobOrder)

    if job not in jobOrder:
        jobOrder.append(job)



def getAdjacencyList(jobs, deps):
    graph = {}
    for i in range(len(jobs)):
        job = jobs[i]
        graph[job] = []
        for j in range(len(deps)):
            dep = deps[j]
            # Check if job is the second number of dep
            if job == dep[1]:
                graph[job].append(dep)
    return graph


#### AE Solution with DFS ####
def aeSolution1(jobs, deps):
    jobGraph = createJobGraph(jobs, deps)


def createJobGraph(jobs, deps):
    graph = JobGraph(jobs)
    for prereq, job in deps:
        # add edges
        graph.addPrereq(job, prereq)
    return graph


def getOrderedJobs(graph):
    orderedJobs = []
    nodes = graph.nodes
    while len(nodes):
        node = node.pop()
        containsCycle = depthFirstTraverse(node, orderedJobs)
    return orderedJobs


def depthFirstTraverse(node, orderedJobs):
    if node.visited:
        return 
    if node.visiting:
        return True


class JobGraph:
    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.addNode(job)

    def addPrereq(self, job, prereq):
        jobNode = self.getNode(job)
        prereqNode = self.getNode(prereq)
        jobNode.prereqs.append(prereqNode)

    def addNode(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])
    
    def getNode(self, job):
        if job not in self.graph:
            self.addNode(job)
        return self.graph[job]


class JobNode:
    def __init__(self, job):
        self.job = job
        self.prereqs = []
        self.visited = False 
        self.visiting = False
        



if __name__ == '__main__':
    jobs = [1, 2, 3, 4]
    deps = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
    print(topologicalSort(jobs, deps))