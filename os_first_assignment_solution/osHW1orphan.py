import os
import time

def main():
    for i in range(4):
        pid = os.fork()
        
        if pid == 0:
            # Child process
            print(f"Child {i} with PID {os.getpid()} is running")
            
            if i < 2:
                # The first two children become orphan process
                time.sleep(15)  # Sleep to keep the orphan process running
                print(f"Child {i} is now an orphan process")
            else:
                # The other two children become zombie processes
                print(f"Child {i} is now a zombie process")
            return
        
    # Parent process
    time.sleep(5)  # Sleep to allow children to print their messages
    print("Parent process terminated")

if __name__ == "__main__":
    main()

