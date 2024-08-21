Problem Overview: Develop a solution to extract ids of the N highest values from the input file, then print the extracted ids to stdout. The order of the output ids does not matter.

Design :
- Data structure that I used in this project is min_heap this data structure is good for tracking the largest value because the smallest value is always at the first so it quick for drop smallest value in list and replace with large one.

for example -> data = [100,90,80,85,120,70] if we want to find 3 largest values
-step 1 insert 3 values in heap [80,100,90] first index is smallest

-step 2 if 85 > 80 SO 80 is replaced by 85 heap = [85,100,90]

-step 3 check 120 > 85 SO 85 is replaced by 120 heap = [90,120,100]

-step 4 70 is lower than 90(lowest value) SO result is [90,120,100]

Time Complexity : Reading all lines in file = O(M) (M=Number of lines) , Inserting or Replace an value in a heap O(log N) time and there are M lines in file so time complexity = O(M Log N) SO O(M) + O(M Log N) = O(M Log N) ; N is Number to extract

Space Complexity = O(N) N is Number to extract

Deploy step:

-git clone https://github.com/Moohamkub/AIATEST.git

-cd to project

-Build docker image by this command = docker build -t somename .

-After building the Docker image, run the container:
    docker run --rm somename
    default setup is this command 
        -python my_solution.py input.txt 2

    If you want to use your custom testdata and number of highest values
        -docker run --rm somename python my_solution.py (your path to data) (N)

Run Unit Tests:
    Unit Tests is currently in the process push and pull request.









