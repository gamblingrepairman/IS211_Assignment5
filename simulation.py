import argparse
import csv
import itertools


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items)-1]


class Server:
    def __init__(self, name=str()):
        self.current_task = None
        self.time_remaining = 0
        self.name = name

    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task is not None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task


class Request:
    def __init__(self, request_inst):
        self.server_query_time = int(request_inst[0])
        self.request_timestamp = int(request_inst[2])
        self.current_request = request_inst

    def get_requesttime(self):
        return self.request_timestamp

    def get_current_request(self):
        return self.current_request

    def wait_time(self):
        return self.request_timestamp


def main():
    server_queue = Queue()
    parser = argparse.ArgumentParser()
    parser.add_argument("--fileloc", type=str, help="this is the file you wish to use for the parser")
    parser.add_argument("--servers", type=int, default=1, help="this is for how many servers you wish to use")
    args = parser.parse_args()

    if args.servers == 1:
        simulateOneServer(args)
    elif args.servers > 1:
        simulateManyServers(args)
    else:
        print('an error has occurred, servers value must be greater than 0')


def simulateOneServer(args):
    #def simulation(num_seconds, pages_per_minute):
       #lab_printer = Printer(pages_per_minute)

    def queuepull():
        with open(args.fileloc, newline='') as csvfile:
            current_list = []
            reader = csv.reader(csvfile, delimiter=' ')
            for row in reader:
                current_list.append(tuple(', '.join(row).split(',')))
            return current_list

    current_queue = Queue()
    waiting_times = []
    queue_list = queuepull()
    for cs in range(len(queue_list)): #TODO: need to replace range with better way to get current second
        for number_of_line, lineitem in enumerate(queue_list):
            #print('item is type', type(item), 'lineitem is type', type(lineitem), lineitem)
            #print(lineitem[0], cs)
            if int(lineitem[0]) == cs:
                print(cs, int(lineitem[0]))
                request = Request(lineitem)
                current_queue.enqueue(request)
                print(current_queue.size())

"""        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
        waiting_times.append(next_task.wait_time(current_second))
        lab_printer.start_next(next_task)
        lab_printer.tick()
        average_wait = sum(waiting_times) / len(waiting_times)
        print("Average Wait %6.2f secs %3d tasks remaining."
              % (average_wait, print_queue.size()))

        def new_print_task():
            num = random.randrange(1, 181)

        if num == 180:
            return True
        else:
            return False
    for i in range(10):
        simulation(3600, 5)
"""
main()