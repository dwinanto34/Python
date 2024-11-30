from collections import deque
import heapq

########################
# Queue
print("\n\n# Queue")
queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

print(queue[0])  # Peek the first element of a queue without pop the data, output : 1
print(queue[-1])  # Peek the last element of a queue without pop the data, output : 3
print(queue.popleft())  # Pop the last element of a queue, output : 1
print(queue.pop())  # Pop the first element of a queue, output : 3

# Check if queue is empty
print(len(queue) == 0)  # Output: False
# Check if queue is not empty
print(len(queue) > 0)  # Output: True

########################
# Stack
print("\n\n# Stack")
stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print(stack[0])  # Peek the last element of a stack without pop the data, output : 1
print(stack[-1])  # Peek the first element of a stack without pop the data, output : 3
print(stack.pop(0))  # Pop the last element of a stack, output : 1
print(stack.pop())  # Pop the first element of a stack, output : 3

# Check if stack is empty
print(len(stack) == 0)  # Output: False
# Check if stack is not empty
print(len(stack) > 0)  # Output: True

########################
# Heap
print("\n\n# Heap")
print("\n\n# Min heap")
heap = []
for i in range(1, 4): # 1 to 3
    heapq.heappush(heap, i)  # Push

print(heap[0])  # Peek (smallest element), Output : 1
print(heapq.heappop(heap))  # Pop (smallest element), Output : 1
print(heapq.heappop(heap))  # Pop (smallest element), Output : 2
print(heapq.heappop(heap))  # Pop (smallest element), Output : 3

print("\n\n# Max heap (the key here is to negate the value)")
heap = []
for i in range(1, 4): # 1 to 3
    heapq.heappush(heap, -i)  # Negate and Push

print(-heap[0])  # Peek (smallest element), Output : 1
print(-heapq.heappop(heap))  # Pop (smallest element), Output : 1
print(-heapq.heappop(heap))  # Pop (smallest element), Output : 2
print(-heapq.heappop(heap))  # Pop (smallest element), Output : 3
