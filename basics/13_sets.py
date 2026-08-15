# Creation
set1 = {1, 2, 3, 4}
set2 = set([3, 4, 5, 6])

# Operations
union = set1 | set2
intersection = set1 & set2
difference = set1 - set2
symmetric = set1 ^ set2

# Methods
set1.add(5)
set1.remove(1)
set1.discard(10)
set1.pop()
set1.clear()

# Set comprehension
even_set = {x for x in range(10) if x % 2 == 0}