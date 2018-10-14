class Cat(object):
    ''' a cat node which has a "tag" which is its id 
    as to when it was added into the shelter
    '''

    def __init__(self, tag, _next=None):
        self.tag = tag
        self._next = _next

    def __data__(self):
        return f'{self}'

    def __repr__(self):
        return(
            f'<Cat | tag: {self.tag} | Next: {self._next}>'
            )


class Dog(object):
    ''' a dog node which has a "tag" which is its id 
    as to when it was added into the shelter
    '''

    def __init__(self, tag, _next=None):
        self.tag = tag
        self._next = _next

    def __data__(self):
        return f'{self}'

    def __repr__(self):
        return(
            f'<Dog | tag: {self.tag} | Next: {self._next}>'
            )


class Queue(object):
 
    def __init__(self):
        """ queue with front back and length
        """
        self._front = None
        self._back = None
        self.length = 0

    def __str__(self):
        """ returns the front-most value of the queue
        """
        return(
             f'Front: {self._front}'
             )

    def __repr__(self):
        """ returns the front-most value of the queue
        """
        return(
            f'<Queue | Front: {self._front}')

    def enq(self, animal):
        """ adds a new animal to the back of the queue
        """
        if self._front is None:
            self._front = animal
            self._back = animal
        else:
            self._back._next = animal
            self._back = animal

    def deq(self):
        """ removes and returns the front-most node from the queue
        """
        if self._front:
            adopt = self._front
            if self._front._next:
                self._front = self._front._next
            else:
                self._front = None
            adopt._next = None
            return adopt
        else:
            return False


class Shelter(object):

    def __init__(self):
        """ creates shelter with a cat and dog queue, and a tag and counter
        """
        self.cats = Queue()
        self.dogs = Queue()
        self.tags = 0
        self.count = 0

    def __str__(self):
        """ returns the number of animals that have been added, and the current number of animals
        """
        return(
            f'tags: {self.tags} | count: {self.count}'
        )

    def __repr__(self):
        """ returns the number of animals that have been added, and the current number of animals
        """
        return(
            f'tags: {self.tags} | count: {self.count}'
        )

    def __len__(self):
        """ returns the number of the current animals in the shelter
        """
        return self.count

    def enqueue(self, animal):
        """ checks to see what species the animal is and adds it to its respective queue
        """
        if animal is 'dog':
            pupper = Dog(self.tags)
            self.tags += 1
            self.count += 1
            self.dogs.enq(pupper)

        if animal is 'cat':
            kitty = Cat(self.tags)
            self.tags += 1
            self.count += 1
            self.cats.enq(kitty)
        elif animal:
            pass

    def dequeue(self, animal):
        """ checks to see what species the animal is and removes it from its respective queue
        """
        if animal is 'dog' and self.dogs._front:
            self.count -= 1
            self.dogs.deq()

        if animal is 'cat' and self.cats._front:
            self.count -= 1
            self.cats.deq()

        elif animal and (self.dogs._front or self.cats._front):
            if self.dogs._front and self.cats._front:
                if self.dogs._front.tag < self.cats._front.tag:
                    self.dogs.deq()
                    return
                else:
                    self.cats.deq()
                    return
            elif self.dogs._front:
                self.dogs.deq()
                return
            elif self.cats._front:
                self.cats.deq()
                return
            else:
                pass
        else:
            return False