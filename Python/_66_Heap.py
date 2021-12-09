import heapq

heap = list()
heapq.heapify(heap)
heapq.heappush(heap, 2)
heapq.heappush(heap, 0)
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)
heapq.heappush(heap, 4)

while len(heap) > 0:
  min = heapq.heappop(heap)
  print(min)

heap = [8,5,4,1,9,0,3,2,6]
heapq.heapify(heap)
print(heap)
largest3 = heapq.nlargest(3, heap)
smallest3 = heapq.nsmallest(3, heap)
print(largest3)
print(smallest3)

# Using heap with objects
heap = list()
heapq.heapify(heap)
heapq.heappush(heap, (3, "Three"))
heapq.heappush(heap, (4, "Four"))
heapq.heappush(heap, (1, "One"))
heapq.heappush(heap, (2, "Two"))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))