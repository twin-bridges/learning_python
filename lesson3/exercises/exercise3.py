import time

start_time = time.time()
timeout = 5

print("\nEntering while loop")
while time.time() - start_time < timeout:
    time.sleep(1)
    elapsed_time = time.time() - start_time
    print(f" ...elapsed time: {elapsed_time:.4f}")

elapsed_time = time.time() - start_time
print(f"\nTimeout expired: {elapsed_time:.4f}\n")
