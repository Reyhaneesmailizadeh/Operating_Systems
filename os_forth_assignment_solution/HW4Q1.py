import threading
import time
import random

# Define the number of philosophers and forks
num_philosophers = 5
num_forks = num_philosophers

# Define semaphores for the forks and the mutex

mmutex = threading.Semaphore(1)
forks = [threading.Semaphore(1) for i in range(num_forks)]

# Define the philosopher thread function
def philosopher(i):
	while True:
		#before eating the philosopher is doing nothing
		print(f"Philosopher {i} is contemplating...")
		#we add this part to avoid rapid continuous printing in terminal
		time.sleep(random.randint(2, 6))
		#when a philisopher wants to enter the critical section tries to acquire the mutex, 
        # if another philosopher has already been in critical section, the new philosofer should wait, 
        # here the critical section is the shared fork between each pair of philosofers.
		mmutex.acquire()
		#here is the critical section
		#we have i forks and i philosofers so we can assign i as the left or right fork, 
        # and then for the other fork, we should assign i+1
		left_fork_index = i
		right_fork_index = (i + 1) % num_forks
		#having been able to acquire mutex and entering the critical section, 
        # the philosofer i then has to acquire the left and right forks, 
        # here if the cpu is taken from philosofer i and be granted to another one, 
        # nothing will happen because mutex has already been aquired by philosofer i and whenever 
        # the cpu is given back to phillosofer i, he or she will aquire the other fork,
        #  so no deadlock would happen beacuse it is inpossible that one philosofer acquire one fork and so does the another philosofer another fork
		forks[right_fork_index].acquire()
		forks[left_fork_index].acquire()
		
		#after philosofer i has taken his/her forks, they will let other philosofers to enter to the 
        # critical section beacuse the resources or the forks have already been taken
		mmutex.release()
		
		
		print(f"Philosopher {i} is eating...")
		time.sleep(random.randint(2, 7))
		
        #after philosopher i has eaten for a random tim ebetween 2 and 7, 
        # they will put down the forks, so another philosofer which is waiting in critical section 
        # will immediately acquirte the forks
		forks[right_fork_index].release()
		forks[left_fork_index].release()
		

# Create a thread for each philosopher
philosopher_threads = []
for i in range(num_philosophers):
	philosopher_threads.append(threading.Thread(target=philosopher, args=(i,)))
	
# Start the philosopher threads
for thread in philosopher_threads:
	thread.start()
	
# Wait for the philosopher threads to complete
for thread in philosopher_threads:
	thread.join()
