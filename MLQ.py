class Process:
    def __init__(self, name, arrival_time, burst_time, priority):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.waiting_time = 0

def mlq_scheduling(processes):
    queue1 = []
    queue2 = []
    waiting_time = 0
    current_time = 0

    for process in processes:
        if process.priority == 1:
            queue1.append(process)
        else:
            queue2.append(process)

    while queue1 or queue2:
        if queue1:
            current_process = queue1.pop(0)
        elif queue2:
            current_process = queue2.pop(0)

        if current_process.arrival_time > current_time:
            current_time = current_process.arrival_time
        waiting_time += current_time - current_process.arrival_time
        current_time += current_process.burst_time

    average_waiting_time = waiting_time / len(processes)
    return average_waiting_time

# Example usage:
num_processes = int(input("Enter the number of processes: "))
processes = []

for i in range(num_processes):
    name = input(f"Enter the name of process {i + 1}: ")
    arrival_time = int(input(f"Enter the arrival time for process {name}: "))
    burst_time = int(input(f"Enter the burst time for process {name}: "))
    priority = int(input(f"Enter the priority for process {name} (1 or 2): "))
    processes.append(Process(name, arrival_time, burst_time, priority))

average_waiting_time = mlq_scheduling(processes)
print(f"Average Waiting Time: {average_waiting_time}")
