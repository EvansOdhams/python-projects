# Python Iterators

Iterators are objects that allow us to traverse through a collection of data, such as lists, tuples, and dictionaries, and access their elements one at a time. In Python, an iterator is an object that implements the iterator protocol, which consists of the __iter__() and __next__() methods

## Iterator Protocol
The __iter__() method returns the iterator object itself and is called when an iterator is required for a collection. The __next__() method returns the next item in the sequence and is called every time the iterator is used


Here's an example of how to use an iterator in Python:
	my_list = [1, 2, 3]
my_iter = iter(my_list)

	print(next(my_iter))  # Output: 1
	print(next(my_iter))  # Output: 2
	print(next(my_iter))  # Output: 3

	In this example, we first create a list my_list and then create an iterator my_iter using the iter() function. We then use the next() function to get the next item in the sequence until the iterator is exhausted
	1
	.
	Building Custom Iterators
	Building a custom iterator in Python is easy. We just have to implement the __iter__() and the __next__() methods in our class. The __iter__() method should return the iterator object itself, and the __next__() method should return the next item in the sequence and raise the StopIteration exception when there are no more items to return
	1
	3
	.
	Here's an example of how to create a custom iterator in Python:

	class MyIterator:
		def __init__(self, start, end):
			self.current = start
			self.end = end

			def __iter__(self):
				return self

				def __next__(self):
					if self.current > self.end:
					raise StopIteration
					else:
					self.current += 1
					return self.current - 1

					In this example, we define a custom iterator MyIterator that takes two arguments start and end. The __iter__() method returns the iterator object itself, and the __next__() method returns the next item in the sequence until the iterator is exhausted
=======

An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
