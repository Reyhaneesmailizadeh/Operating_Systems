import socket
import threading
import signal
import os
# Constants
HOST = '127.0.0.1'
PORT = 8080
MAX_THREADS = 5
QUEUE_SIZE = 10

# Shared queue for requests
request_queue = []
queue_lock = threading.Lock()
exit_event = threading.Event()

# Function to handle SIGINT signal
def signal_handler(sig, frame):
    print("Received SIGINT. Exiting gracefully.")
    os._exit(0)

# Function to handle client requests
def handle_request(client_socket):
    print("now the request is being handled")
    request = client_socket.recv(1024).decode('utf-8')
    print("Received request:", request)
    print("filename")
    filename = request.split(' ')[1][1:].strip()
    
    
    print("filename",filename)
    pro = 1
    if not filename:
        # Invalid request (400)
        response = "HTTP/1.1 400 Bad Request\r\n\r\nInvalid Request"
    elif os.path.exists(filename):
        print("heloo")
        with open(filename, 'r') as file:
            content = file.read()
            response = f"HTTP/1.1 200 OK\r\n\r\n Here You are!{content}"
            
    else:
        # File not found (404)
        if(pro == 1):
            response = "HTTP/1.1 404 Not Found\r\n\r\nFile NNot Found"
        else:
            response = "NO"
            pro = 2
    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()





# Function to enqueue a request
def enqueue_request(client_socket):
    with queue_lock:
        if len(request_queue) < QUEUE_SIZE:
            request_queue.append(client_socket)
            print("request is appended to the queue.")
        else:
            # Queue is full
            client_socket.sendall("HTTP/1.1 503 Service Unavailable\r\n\r\nServer Busy".encode('utf-8'))
            client_socket.close()

# Function to process requests from the queue
def process_requests():
    print("now the request is being processed")
    while not exit_event.is_set():
        if not request_queue:
            continue

        # Dequeue a request
        with queue_lock:
            client_socket = request_queue.pop(0)

        # Process the request
        handle_request(client_socket)

    print("Thread exiting.")

# Function to create and start worker threads
def start_threads():
    print("now threads are working")
    threads = []
    for _ in range(MAX_THREADS):
        thread = threading.Thread(target=process_requests)
        thread.start()
        threads.append(thread)
    return threads

# Main server function
def main():
    # Set up the signal handler for SIGINT
    signal.signal(signal.SIGINT, signal_handler)

    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))

    try:
        server_socket.listen()
        print("Server is now listening on", (HOST, PORT))

        # Start worker threads
        threads = start_threads()

        # Inside the main loop of the main function
        while True:
            try:
                # Accept a connection
                client_socket, addr = server_socket.accept()
                print(f"Accepted connection from {addr}")

                # Enqueue the client socket
                enqueue_request(client_socket)

            except Exception as e:
                print("Error accepting connection:", e)
                break

    except KeyboardInterrupt:
        exit_event.set()

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

    except Exception as e:
        print("Error while setting up the server:", e)

    finally:
        # Close the server socket
        server_socket.close()
        print("Server socket closed.")

if __name__ == "__main__":
    main()


