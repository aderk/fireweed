# Fireweed
A toy project of trying out Mojo🔥 with a Bloom filter. Why a Bloom filter?
 * Limited API
 * Super fun w/ probability and bit operations
   * Seemingly does the impossible measuring containment w/o storing more than several bits per item
 * Useful
 * Extendable to Cuckoo, kMinHash, HyperLogLog(++), Counting Bloom Filters, etc.

# Installation And Running
1. Install Mojo
2. Install python (probably via miniconda)
3. Set MOJO_PYTHON_LIBRARY
4. pip install rbloom
5. mojo run main.🔥

# Benchmark Results
Benchmarks always have some unfairness, so take these with a grain of salt. This compares python with a rust library to mojo with a mojo library, which is very much apples-to-oranges. Disclaimers aside, for 10M insertions and membership checks. rbloom/python takes about 1.7s and this Mojo implementation takes about 0.6s.

```
alan@mbalan ~/C/fireweed (main) [1]> mojo run main.🔥           (py310) 
===rbloom/python results===
bf=<Bloom size_in_bits=95850584 approx_items=0.0>
add_time=0.9502909183502197
total_time=1.6721301078796387


num_hash_funcs= 6
filter_size_total_bits= 95850624
===mojo results===
---------------------
Benchmark Report (s)
---------------------
Mean: 0.61287924999999999
Total: 2.4515169999999999
Iters: 4
Warmup Mean: 0.61581649999999999
Warmup Total: 1.231633
Warmup Iters: 2
Fastest Mean: 0.61287924999999999
Slowest Mean: 0.61287924999999999
```

# Future work
 * Investigate TODOs/HACKs/MUSINGs
 * Currently it scales very poorly above ~100k elements on an M2 MBA, not sure what's going on there.
 * Performance profiling
 * Write a real test suite 

# Citations
This project borrows heavily from https://github.com/KenanHanke/rbloom, which is very readable and well designed. Bloom filters were originally proposed in [(Bloom, 1970)](https://dl.acm.org/doi/10.1145/362686.362692). 
