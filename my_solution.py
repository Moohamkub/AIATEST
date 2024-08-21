import sys
import logging
from minheap import MinHeap

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_top_n_ids(file_path, n):
    """
    Extract the top N ids with the highest integer values from the given file.

    :param file_path: Path to the input file
    :param n: Number of ids to extract
    """
    if n <= 0:
        logging.error("Number of ids to extract must be a positive integer.")
        return
    
    min_heap = MinHeap()
    line_count = 0
    line_number = 1

    try:
        with open(file_path, 'r',encoding='utf-8') as file:
            for line in file:
                line = line.strip()

                if not line:
                    logging.warning(f"Line {line_number} is empty.")
                    line_number += 1
                    continue
                
                line_split = line.split()
                if len(line_split) != 2:
                    logging.warning(f"Line {line_number} is invalid form : '{line}'.")
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
                    logging.error(f"Line {line_number} not a integer value : '{value_str}'.")
                
                line_number += 1

        if line_count == 0:
            logging.error("No valid data in this file.")
            return
        
        result = []
        while len(min_heap.heap) > 0:
            result.append(min_heap.heappop()[1])

        for id_str in result:
            print(id_str)

    except FileNotFoundError:
        logging.error(f"File not found : {file_path}")
    except Exception as e:
        logging.exception(f"An unexpected error occurred : {e}")

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Command should be python my_solution.py <input_file> <N>")
        sys.exit(1)

    input_file = sys.argv[1]
    try:
        n = int(sys.argv[2])
    except ValueError:
        print("Number must be an integer.")
        sys.exit(1)

    extract_top_n_ids(input_file, n)
