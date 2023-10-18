def best_fit(memory_blocks, process_sizes):
    allocation = [-1] * len(process_sizes)

    for i in range(len(process_sizes)):
        best_fit_idx = -1
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= process_sizes[i]:
                if best_fit_idx == -1 or memory_blocks[j] < memory_blocks[best_fit_idx]:
                    best_fit_idx = j
        if best_fit_idx != -1:
            allocation[i] = best_fit_idx
            memory_blocks[best_fit_idx] -= process_sizes[i]

    return allocation

def first_fit(memory_blocks, process_sizes):
    allocation = [-1] * len(process_sizes)

    for i in range(len(process_sizes)):
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= process_sizes[i]:
                allocation[i] = j
                memory_blocks[j] -= process_sizes[i]
                break

    return allocation

# Example usage:
num_memory_blocks = int(input("Enter the number of memory blocks: "))
memory_blocks = []
for i in range(num_memory_blocks):
    block_size = int(input(f"Enter the size of memory block {i + 1}: "))
    memory_blocks.append(block_size)

num_processes = int(input("Enter the number of processes: "))
process_sizes = []
for i in range(num_processes):
    size = int(input(f"Enter the size of process {i + 1}: "))
    process_sizes.append(size)

best_fit_allocation = best_fit(memory_blocks[:], process_sizes)
first_fit_allocation = first_fit(memory_blocks[:], process_sizes)

print("Best Fit Allocation:")
for i in range(len(process_sizes)):
    if best_fit_allocation[i] != -1:
        print(f"Process {i + 1} is allocated to Memory Block {best_fit_allocation[i]}")
    else:
        print(f"Process {i + 1} cannot be allocated")

print("First Fit Allocation:")
for i in range(len(process_sizes)):
    if first_fit_allocation[i] != -1:
        print(f"Process {i + 1} is allocated to Memory Block {first_fit_allocation[i]}")
    else:
        print(f"Process {i + 1} cannot be allocated")
