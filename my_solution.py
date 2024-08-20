import sys
from minheap import MinHeap

def extract_ids(file_path, n):
    if n <= 0:
        print("Number must be positive integer")
        return

    min_heap = MinHeap()
    line_count = 0
    line_number = 1  # start line 1
    errors = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:  # when that line is empty
                print(f"line number {line_number} is empty")
                line_number += 1
                continue
            
            line_split = line.split()
            if len(line_split) != 2:
                print(f"line number {line_number} is not in pattern unique_id and an value = {line}")
                line_number += 1
                continue

            id_str, value_str = line_split
            
            try:
                value = int(value_str)
                line_count += 1
                if len(min_heap.heap) < n:
                    min_heap.heappush((value, id_str))
                else:
                    if value > min_heap.heap[0][0]:
                        min_heap.replace((value, id_str))
            except ValueError:
                print(f"line number {line_number} is not integer value = {line}")

            line_number += 1

    if line_count == 0:
        print("no valid data found in the input file")
        return
    
    result = []
    while len(min_heap.heap) > 0:
        result.append(min_heap.heappop()[1])

    if len(result)>0:
        for id_str in result:
            print(id_str)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("command line must be : python my_solution.py <input_file path> <number of the highest values>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    try:
        n = int(sys.argv[2])
    except ValueError:
        print("Number must be integer")
        sys.exit(1)
    
    extract_ids(input_file, n)
