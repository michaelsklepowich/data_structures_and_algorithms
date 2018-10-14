

# FIFO Animal Shelter

This animal shelter class contains two lists of "dogs" and "cats" which users can take from or add to using the dequeue and enqueue methods. The shelter is a first-in-first-out structure, so the user must take the animal from the front of the queue and any animal enqueued gets added to the end of the queue

## Methods

### Enqueue
The enqueue method take an animal in the form of a species name, which creates a node based on the input. If the input is either "cat" or "dog" an animal is added to its respective queue

### Dequeue
The dequeue method takes an animal in the form of species name, which removes the first animal from its respective queue. If no animal species is specified, the animal with the lowest .tag property is removed from its respective queue