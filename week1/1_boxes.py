from dataclasses import dataclass
import math

def min_count(product_count, box_size):
    
    return math.ceil(product_count / box_size)
  # return (product_count + box_size - 1) // box_size

if __name__ == "__main__":
    print(min_count(10, 3)) # 4
    print(min_count(10, 4)) # 3
    print(min_count(100, 1)) # 100
    print(min_count(100, 100)) # 1
    print(min_count(100, 99)) # 2
    print(min_count(5, 5)) # 1
    print(min_count(5, 6)) # 1