import queue

class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time

def srt_scheduling(processes):
    current_time = 0
    remaining_processes = queue.PriorityQueue()
    waiting_time = 0
    current_process = None

    while not remaining_processes.empty() or current_process:
        for process in processes:
            if process.arrival_time <= current_time and process.remaining_time > 0:
                if current_process:
                    if process.remaining_time < current_process.remaining_time:
                        remaining_processes.put((current_process.remaining_time, current_process))
                        current_process = process
                else:
                    current_process = process
        if current_process:
            current_process.remaining_time -= 1
            if current_process.remaining_time == 0:
                waiting_time += current_time - current_process.arrival_time - current_process.burst_time
                current_process = None
        else:
            current_time += 1

    average_waiting_time = waiting_time / len(processes)
    return average_waiting_time

# Example usage:
num_processes = int(input("Enter the number of processes: "))
processes = []

for i in range(num_processes):
    name = input(f"Enter the name of process {i + 1}: ")
    arrival_time = int(input(f"Enter the arrival time for process {name}: "))
    burst_time = int(input(f"Enter the burst time for process {name}: "))
    processes.append(Process(name, arrival_time, burst_time))

average_waiting_time = srt_scheduling(processes)
print(f"Average Waiting Time: {average_waiting_time}")
