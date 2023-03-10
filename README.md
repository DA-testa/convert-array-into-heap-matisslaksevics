[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-f4981d0f882b2a3f0472912d15f9806d57e124e0fc890972558857b51b24a6f9.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=10410889)
#  Problem: Convert array into heap
In this problem you will convert an array of integers into a heap. This is the crucial step of the sorting
algorithm called HeapSort. It has guaranteed worst-case running time of π(π log π) as opposed to QuickSortβs
average running time of π(π log π). QuickSort is usually used in practice, because typically it is faster, but
HeapSort is used for external sort when you need to sort huge files that donβt fit into memory of your
computer.

# Problem description
## Task. 
The first step of the HeapSort algorithm is to create a heap from the array you want to sort. By the
way, did you know that algorithms based on Heaps are widely used for external sort, when you need
to sort huge files that donβt fit into memory of a computer?
Your task is to implement this first step and convert a given array of integers into a heap. You will
do that by applying a certain number of swaps to the array. Swap is an operation which exchanges
elements ππ and ππ of the array π for some π and π. You will need to convert the array into a heap using
only π(π) swaps, as was described in the lectures. Note that you will need to use a min-heap instead
of a max-heap in this problem.
## Input Format. 
The first line of the input contains single integer π. The next line contains π space-separated
integers ππ.
## Constraints. 
1 β€ π β€ 100 000; 0 β€ π, π β€ π β 1; 0 β€ π0, π1, . . . , ππβ1 β€ 109. All ππ are distinct.

## Output Format. 
The first line of the output should contain single integer π β the total number of swaps.
π must satisfy conditions 0 β€ π β€ 4π. The next π lines should contain the swap operations used
to convert the array π into a heap. Each swap is described by a pair of integers π, π β the 0-based
indices of the elements to be swapped. After applying all the swaps in the specified order the array
must become a heap, that is, for each π where 0 β€ π β€ π β 1 the following conditions must be true:
1. If 2π + 1 β€ π β 1, then ππ < π2π+1.
2. If 2π + 2 β€ π β 1, then ππ < π2π+2.
3. 
Note that all the elements of the input array are distinct. Note that any sequence of swaps that has
length at most 4π and after which your initial array becomes a correct heap will be graded as correct.

## Sample 
Input:
5

5 4 3 2 1

Output:
3
1 4
0 1
1 3

After swapping elements 4 in position 1 and 1 in position 4 the array becomes 5 1 3 2 4.
2
After swapping elements 5 in position 0 and 1 in position 1 the array becomes 1 5 3 2 4.

After swapping elements 5 in position 1 and 2 in position 3 the array becomes 1 2 3 5 4, which is
already a heap, because π0 = 1 < 2 = π1, π0 = 1 < 3 = π2, π1 = 2 < 5 = π3, π1 = 2 < 4 = π4.


## Sample
Input:
5

1 2 3 4 5

Output:
0

The input array is already a heap, because it is sorted in increasing order.
