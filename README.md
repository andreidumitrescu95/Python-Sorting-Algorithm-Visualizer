# Python-Sorting-Algorithm-Visualizer (WIP)

I built this application in order to get much more accommodated with Python and Pygame and to have a much better understanding of the nature of various pathfinding algorithms through visualization.

## The Project

## The Algorithms

**Bubble Sort** - is one of the simpler sorting algorithms as it repeatedly steps through the list comparing adjacent elements and swapping them in case they are not in ascending order. Worst case performance will be met when the array is entirely reversed so we would get O(n^2) comparisons and swaps. Best case would be if the array would be already sorted and it would amount to O(n) comparisons and O(1) swaps.

**Insertion Sort** - is also a pretty simple sorting algorithm that builds the sorted array one element at a time by removing the probed element and inserting it in the place it needs to be in the final sorted array. It performs well on small lists but it is not efficient on large lists and has much lower performance than more advanced algorithms such as quicksort, heapsort or merge sort. Worst case performance is just like Bubble Sort, having O(n^2) comparisons and swaps when the array is completely reversed and also a best case performance of O(n) comparisons and O(1) swaps.

**Selection Sort** - also inefficient on large lists. It divides the input list into two sublists. The first sublist starts from the left and contains the sorted elements and the second sublist contains only the unsorted elements. Once we find the minimum element from the unsorted array during an interation we remove it from the second sublist and insert it in the sorted one. Because of this the worst case performance is O(n^2) comparisons and O(n) swaps and best case is O(n^2) comparisons and O(1) swaps. So even in the best case scenario the complexity of this algorithm is quadratic. The only advantage of this algorithm is that it has the minimum number of swaps possible, n-1 in the worst case.

**Merge Sort** - WIP

**Quick Sort** - WIP

**Heap Sort** - WIP

## The Application

The user is able to select an algorithm from a selection to visualize and also customize the number of elements in the list to be sorted and the speed at which the visualization to run. After selecting all the necessary parametes the user can choose to start the algorithm visualization. After the algorithm has finished, the user can choose to reset the application in order to select different parameters to test.

![](https://github.com/andreidumitrescu95/Python-Sorting-Algorithm-Visualizer/blob/master/sorting.gif)

