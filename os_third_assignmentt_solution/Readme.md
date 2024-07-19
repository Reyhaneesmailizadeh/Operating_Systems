# problem 1
. Implement how a binary semaphore can be used to do mutual exclusion among
n processes. The goal is to implement a solution that ensures mutual exclusion,
meaning that only one process can access the shared resource at any given time.
This is essential to prevent race conditions and maintain the integrity of the shared
resource. You should provide followings in your code:
• Implement a binary semaphore (using a language of choice that supports multithreading or multiprocessing).
• Develop n processes, each of which will perform some operations in a critical
section.
• Use the binary semaphore to control access to the critical section, ensuring
that only one process can execute the critical section at a time.
• The processes should be able to enter the critical section, modify the shared
resource, and exit the critical section without interference from other processes.
# problem 2
Readers-Writers Problem
In a database management system (DBMS), multiple users may simultaneously
read data from a database (readers), and some users may need to write data to
the database (writers). The challenge is to ensure that multiple readers can access
the database concurrently without conflicts, but when a writer wants to modify the
database, it needs exclusive access to prevent data inconsistencies.
Implement a program that simulates the readers-writers problem using synchronization mechanisms. Multiple readers and writers access a shared resource (e.g., file or
a data structure like an array, ...). Readers can access the resource simultaneously,
but writers must have exclusive access.
Requirements:
• Create a shared resource (e.g., a variable, data structure, or file) that readers
and writers will access.
• Implement functions for readers and writers to access the shared resource.
• Use synchronization mechanisms (e.g., locks, semaphores) to ensure exclusive
access for writers and allow concurrent access for readers.
• Simulate multiple readers and writers accessing the resource.
• Print relevant information (e.g., reader/writer activity, resource state) for each
step to demonstrate proper synchronization and clearly comment your code to
explain the use of synchronization mechanisms.
