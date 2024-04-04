import rbloom
import time

def run_python_benchmark(size):
    bf = rbloom.Bloom(size, 0.01)
    print(f"{bf=}")
    start = time.time()
    for i in range(size):
        bf.add(i + 0.5)  
    
    add_time = time.time() - start
    for i in range(size):
        assert i + 0.5 in bf
    
    total_time = time.time() - start

    print(f"{add_time=}\n{total_time=}\n\n", flush=True)