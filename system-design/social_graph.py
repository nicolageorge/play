from collections import deque
class Person(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.friends_ids = []

class LookupService(object):
    def __init__(self):
        self.lookup = {} # key : person_id, value : person_server

    def get_person(self, person_id):
        person_server = self.lookup[person_id]
        return person_server.people[person_id]

class PersonServer(object):
    def __init__(self):
        self.people = {}

    def get_people(self, ids):
        results = []
        for id in ids:
            if id in self.people:
                results.append(self.people[id])
        return results

class Graph(object):
    def bfs(self, source, dest):
        if source is None:
            return false
        queue = deque()
        queue.apend(source)
        source.visit_state = State.visited
        while queue:
            node = queue.popleft()
            print node
            if dest is node:
                return True
            for adj_node in node.adj_nodes.values():
                if adj_node.visit_state == State.unvisited:
                    queue.append(adj_node)
                    adj_node.visit_state = State.visited
        return False

class UserGraphService(object):
    def __init__(self, person_ids, lookup):
        self.lookup = lookup
        self.person_ids = person_ids
        self.visited_ids = set()

    def bfs(self, source, dest):
        # Use self.visited_ids to track visited nodes
        # use self.lookup to translate a person_id to a person
