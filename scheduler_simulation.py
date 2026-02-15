from priority_queue import Task, PriorityQueueMaxHeap

pq = PriorityQueueMaxHeap()

# Insert tasks
pq.insert(Task("1", 3))
pq.insert(Task("2", 10))
pq.insert(Task("3", 5))
pq.insert(Task("4", 8))

print("Task Execution Order (Highest Priority First):")

while not pq.is_empty():
    print(pq.extract_max())