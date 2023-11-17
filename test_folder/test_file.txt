from collections import deque

ada = deque([])

ada.append(1)
ada.append(2)
ada.append(3)

ada.popleft() # removes the item at the first index
print(ada)
