from scheduler.johnson import johnsons_rule
from scheduler.timing import calculate_times
from scheduler.gantt import plot_gantt

# Sample Data
jobs = [
    {'name': 'P1', 'test': 3, 'scan': 8},
    {'name': 'P2', 'test': 6, 'scan': 2},
    {'name': 'P3', 'test': 4, 'scan': 7},
    {'name': 'P4', 'test': 5, 'scan': 3},
]

# Step 1: Get sequence
sequence = johnsons_rule(jobs)

# Step 2: Calculate timings
result, makespan, idle = calculate_times(sequence)

# Step 3: Output
print("Optimal Sequence:")
for job in sequence:
    print(job['name'], end=" -> ")

print("\n\nDetailed Schedule:")
for r in result:
    print(r)

print("\nTotal Elapsed Time:", makespan)
print("Idle Time (Scan Machine):", idle)

# Step 4: Gantt Chart
plot_gantt(result)