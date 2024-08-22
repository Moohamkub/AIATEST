# Problem Overview
This project aims to develop a solution that extracts the IDs of the N highest values from an input file. Each row in the input file contains a unique ID and an integer value, separated by a space. The goal is to print the extracted IDs. The order of the output IDs does not matter.

## Design and Data Structure
Use min-heap to track the largest values efficiently. A min-heap is well-suited for this task because the smallest value is always at the root, making it quick to drop the smallest value and replace it with a larger one.

Example:
For a dataset data = [100, 90, 80, 85, 120, 70], and if we want to find the top 3 largest values, we can use a min-heap as follows:

1. Step 1: Insert the first 3 values into the heap: [80, 100, 90] (heap maintains smallest value at root).

2. Step 2: Compare 85 with the smallest value (80), since 85 > 80, replace 80 with 85. Now the heap becomes: [85, 100, 90].

3. Step 3: Compare 120 with the smallest value (85), since 120 > 85, replace 85 with 120. The heap now becomes: [90, 120, 100].

4. Step 4: Compare 70 with the smallest value (90), but since 70 < 90, it is ignored. The final heap contains the top 3 largest values: [90, 120, 100].

## Complexity Analysis
Time Complexity
Reading all lines in the file: This takes O(M), where M is the number of lines in the file.
Heap Operations: Inserting or replacing an element in the heap takes O(log N), and for M lines, the total time complexity is O(M log N).

Thus, the overall time complexity is O(M log N).

Space Complexity
The space complexity is O(N), where N is the number of top values to extract and store in the heap.

## Deployment Steps

1. Clone the Repository: `git clone https://github.com/Moohamkub/AIATEST.git`

2. Change directory to the Project Directory : `cd AIATEST`

3. Run the following command to build the Docker image : `docker build -t your_image_name .`

4. After building the Docker image, you can run the container using : `docker run --rm your_image_name` (**The default setup executes is python my_solution.py testdata.txt 2**)

5. If you want to use a custom testdata and specify the number of top values to extract, run the following: 
`docker run --rm somename python my_solution.py <your_data_file> <N>`

## Running Unit Tests
The unit tests are currently in progress. You can check for updates regarding the testing process through pull requests in the repository.












