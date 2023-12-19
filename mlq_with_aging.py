class Process:
    def __init__(self, process_id, priority, burst_time):
        self.process_id = process_id
        self.priority = priority
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.waiting_time = 0  # For aging

def enqueue(queue, process):
    queue.append(process)

def dequeue(queue):
    return queue.pop(0)

def multilevel_queue_scheduling(processes, time_quantum, aging_threshold):
    high_priority = []
    medium_priority = []
    low_priority = []

    print("\nMultilevel Queue Scheduling Output:")

    for process in processes:
        # Enqueue processes based on priority
        if process.priority == 0:
            enqueue(high_priority, process)
        elif process.priority == 1:
            enqueue(medium_priority, process)
        else:
            enqueue(low_priority, process)

    # Process each queue with priority and limited time quantum
    while high_priority or medium_priority or low_priority:
        # Priority order: High > Medium > Low
        if high_priority:
            current_process = dequeue(high_priority)
        elif medium_priority:
            current_process = dequeue(medium_priority)
        else:
            current_process = dequeue(low_priority)

        # Simulate execution using time quantum
        time_slice = time_quantum

        while time_slice > 0 and current_process.remaining_time > 0:
            current_process.remaining_time -= 1
            time_slice -= 1

            # Aging: Increase waiting time for priority processes
            current_process.waiting_time += 1

        print(f"Executing Process {current_process.process_id} (Priority {current_process.priority}) with Remaining Time {current_process.remaining_time} and Waiting Time {current_process.waiting_time}")

        # Check if process is completed or needs to be enqueued again
        if current_process.remaining_time > 0:
            # Enqueue the process back to its priority queue
            if current_process.priority == 0:
                # Check if the waiting time exceeds the threshold for high-priority process
                if current_process.waiting_time >= aging_threshold:
                    current_process.waiting_time = 0  # Reset waiting time after priority increase
                    enqueue(low_priority, current_process)
                else:
                    enqueue(high_priority, current_process)
            elif current_process.priority == 1:
                # Check if the waiting time exceeds the threshold for medium-priority process
                if current_process.waiting_time >= aging_threshold:
                    current_process.waiting_time = 0  # Reset waiting time after priority increase
                    enqueue(low_priority, current_process)
                else:
                    enqueue(medium_priority, current_process)
            else:
                # Check if the waiting time exceeds the threshold for low-priority process
                if current_process.waiting_time >= aging_threshold:
                    current_process.waiting_time = 0  # Reset waiting time after priority increase
                    enqueue(high_priority, current_process)
                else:
                    enqueue(low_priority, current_process)
                
        else:
            print(f"Process {current_process.process_id} completed.")

# Example usage
if __name__ == "__main__":
    n = int(input("Enter the number of processes: "))
    processes = []

    for i in range(n):
        process_id = i + 1
        priority = int(input(f"Enter priority for Process {process_id}: "))
        burst_time = int(input(f"Enter burst time for Process {process_id}: "))
        processes.append(Process(process_id, priority, burst_time))

    time_quantum = int(input("Enter time quantum: "))
    aging_threshold = int(input("Enter aging threshold: "))

    multilevel_queue_scheduling(processes, time_quantum, aging_threshold)
