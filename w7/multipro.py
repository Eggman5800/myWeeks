import hashlib
import multiprocessing

def hash_worker(string, lz, start, end, result_queue):
    target = '0' * lz

    for nonce in range(start, end):
        data = (string + str(nonce)).encode()
        hash_result = hashlib.sha256(data).hexdigest()

        if hash_result.startswith(target):
            result_queue.put((hash_result, nonce))
            return

def hashLz(string, lz, num_processes):
    # Create a Queue to get results from processes
    result_queue = multiprocessing.Queue()
    processes = []

    # Define the range of nonces
    total_nonces = 100000000  # Adjust this value based on your needs
    chunk_size = total_nonces // num_processes

    # Start processes
    for i in range(num_processes):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_processes - 1 else total_nonces
        p = multiprocessing.Process(target=hash_worker, args=(string, lz, start, end, result_queue))
        processes.append(p)
        p.start()

    # Check for results
    for _ in range(num_processes):
        result = result_queue.get()
        if result:
            # Terminate other processes if we found a result
            for p in processes:
                p.terminate()
            return result

    # Ensure all processes finish
    for p in processes:
        p.join()

    return None, None  # Return if no result is found

if __name__ == "__main__":
    string = "talha"
    lz = 16
    num_processes = multiprocessing.cpu_count()  # Use number of CPU cores

    hash_result, nonce = hashLz(string, lz, num_processes)
    if hash_result:
        print("Hash with " + str(lz) + " leading zeros: " + hash_result)
        print("Nonce:", nonce)
    else:
        print("No valid nonce found.")
