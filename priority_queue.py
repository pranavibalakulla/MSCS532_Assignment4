class Task:
    def __init__(self, task_id, priority, arrival_time=0, deadline=None):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __repr__(self):
        return f"Task(ID={self.task_id}, Priority={self.priority})"


class PriorityQueueMaxHeap:
    def __init__(self):
        self.heap = []

    # ---------- Helper index methods ----------

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def is_empty(self):
        return len(self.heap) == 0

    # ---------- Heapify (Sift Down) ----------

    def heapify(self, i):
        largest = i
        left = self.left(i)
        right = self.right(i)

        if left < len(self.heap) and self.heap[left].priority > self.heap[largest].priority:
            largest = left

        if right < len(self.heap) and self.heap[right].priority > self.heap[largest].priority:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest)

    # ---------- Core Operations ----------

    def insert(self, task):
        """
        Insert a new task into the heap.
        Time Complexity: O(log n)
        """
        self.heap.append(task)
        i = len(self.heap) - 1

        # Sift Up
        while i != 0 and self.heap[self.parent(i)].priority < self.heap[i].priority:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extract_max(self):
        """
        Remove and return the task with the highest priority.
        Time Complexity: O(log n)
        """
        if self.is_empty():
            return None

        root = self.heap[0]
        last = self.heap.pop()

        if not self.is_empty():
            self.heap[0] = last
            self.heapify(0)

        return root

    def increase_key(self, index, new_priority):
        """
        Increase priority of task at given index.
        Time Complexity: O(log n)
        """
        if new_priority < self.heap[index].priority:
            return

        self.heap[index].priority = new_priority

        while index != 0 and self.heap[self.parent(index)].priority < self.heap[index].priority:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def decrease_key(self, index, new_priority):
        """
        Decrease priority of task at given index.
        Time Complexity: O(log n)
        """
        if new_priority > self.heap[index].priority:
            return

        self.heap[index].priority = new_priority
        self.heapify(index)