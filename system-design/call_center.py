# my implementation
from uuid import uuid4
from enum import Enum
from collections import deque

import unittest
import sys

class EmployeeType(Enum):
    AGENT = 0
    SUPERVISOR = 1
    DIRECTOR = 2

class Employee(object):
    _id = uuid4()
    _current_call = None
    _type = None

    def take_call(self, call):
        self._current_call = call

class Agent(Employee):
    _type = EmployeeType.AGENT

    def __init__(self):
        super(Agent, self).__init__()

class Supervisor(Employee):
    _type = EmployeeType.SUPERVISOR

    def __init__(self):
        super(Supervisor, self).__init__()

class Director(Employee):
    _type = EmployeeType.DIRECTOR

    def __init__(self):
        super(Director, self).__init__()

class EmployeeService(object):
    _free_agents, _free_supervisors, _free_directors = 0, 0, 0
    _available_agents, _available_supervisors, _available_directors = deque(), deque(), deque()

    def add(self, employee):
        if employee is Agent:
            self._available_agents.append(employee)
            self._free_agents += 1
        elif employee is Supervisor:
            self._available_supervisors.append(employee)
            self._free_supervisors += 1
        elif employee is Director:
            self._available_directors.append(employee)
            self._free_directors += 1
        else:
            raise ValueError("you have to add agents, supervisors or directors")

    def get_next_free_employee(self):
        if self._free_agents > 0:
            self._free_agents -= 1
            return self._available_agents.popleft()
        elif self._free_supervisors > 0:
            self._free_supervisors -= 1
            return self._available_supervisors.popleft()
        elif self._free_directors > 0:
            self._free_directors -= 1
            return self._available_directors.popleft()
        else:
            raise IndexError("No free agents")
            return None

class Call:
    _id = uuid4()
    _handler = None

    def set_handler(self, handler):
        self._handler = handler

    @property
    def id():
        return self._id


class CallService(object):
    _call_queue = deque()
    _finished_calls = []
    _active_calls = {}

    def _queue_call(self, call):
        if call is Call:
            self._call_queue.append(call)
        else:
            raise ValueError("you should be appending calls to the call queue")

    def _get_next_waiting_call(self):
        return self._call_queue.popleft()

    def check_for_waiting_calls(self):
        return len(self._call_queue) != 0

    def handle_call(self, call):
        self._active_calls[call.id] = call

    def add_call(self, call, employee):
        if employee == None:
            self._queue_call(call)
        else:
            call.set_handler(employee)
            call.handle_call(call)

    def end_call(self, call_id):
        if call_id in self._active_calls:
            call = self._active_calls.pop(call_id)
            self._finished_calls.append(call)
        else:
            raise IndexError("call not found in active call list")

class CallCenter(object):
    _call_service = CallService()
    _employee_service = EmployeeService()

    def new_call(self, call=None):
        if call is None:
            call = Call()
        try:
            employee = self._employee_service.get_next_free_employee()
        except IndexError:
            print "no free employees, queuing call"
            employee = None

        self._call_service.add_call(call, employee)

    def add_employee(self, employee):
        try:
            self._employee_service.add(employee)
        except ValueError:
            print "I said it before and I say it again, no other employees"

    def add_call(self, call=None):
        try:
            self._call_service.new_call(call)
        except ValueError:
            print "I said it before and I say it again, no other calls"


class TestInit(unittest.TestCase):
    def test1(self):
        try:
            a1 = Agent()
            a2 = Agent()
            cc = CallCenter()
            cc.add_employee(a1)
        except Exception as e:
            # e = sys.exc_info()[0]
            print str(e)

if __name__ == '__main__':
    unittest.main()
