# Python-Sorting-Algorithm-Visualizer (WIP)

I built this application in order to get much more accommodated with Python and Pygame and to have a much better understanding of the nature of various sorting algorithms through visualization.

## The Project

The project is implemented in Python using Pygame. The program allows the user to choose from a selection of sorting algorithms, select the number of elements to be sorted and also input the speed at which the visualization process will execute.

## The Algorithms

**Bubble Sort** - is one of the simpler sorting algorithms as it repeatedly steps through the list comparing adjacent elements and swapping them in case they are not in ascending order. Worst case performance will be met when the array is entirely reversed so we would get O(n^2) comparisons and swaps. Best case would be if the array would be already sorted and it would amount to O(n) comparisons and O(1) swaps.

**Insertion Sort** - is also a pretty simple sorting algorithm that builds the sorted array one element at a time by removing the probed element and inserting it in the place it needs to be in the final sorted array. It performs well on small lists but it is not efficient on large lists and has much lower performance than more advanced algorithms such as quicksort, heapsort or merge sort. Worst case performance is just like Bubble Sort, having O(n^2) comparisons and swaps when the array is completely reversed and also a best case performance of O(n) comparisons and O(1) swaps.

**Selection Sort** - also inefficient on large lists. It divides the input list into two sublists. The first sublist starts from the left and contains the sorted elements and the second sublist contains only the unsorted elements. Once we find the minimum element from the unsorted array during an interation we remove it from the second sublist and insert it in the sorted one. Because of this the worst case performance is O(n^2) comparisons and O(n) swaps and best case is O(n^2) comparisons and O(1) swaps. So even in the best case scenario the complexity of this algorithm is quadratic. The only advantage of this algorithm is that it has the minimum number of swaps possible, n-1 in the worst case.

**Quick Sort** - just like Merge Sort, it is a Divide and Conquer algorithm. It picks an element as a pivot (first, last, random) and partitions the given array around the picked pivot. In most cases the complexity is O(n * log(n)), but in the worst case scenario it is O(n^2). Regardless, Quick Sort is in practice faster than all other O(n * log(n)) algorthitms, because the inner loop is efficiently implemented.

**Merge Sort** - is a Divine and Conquer algorithm. It divides the array in two halves, calls itself for the two halves and then merges the two sorted halves. The merge() function is used for merging two halves. The worst case complexity is O(n * log(n)). It can perform better than Quick Sort.

**Heap Sort** - also a comparison based sorting technique based on the Binary Heap data strucutre. It is similar to selection sort where we first find the maximum element and place it at the end. We repeat the process for the remaining elements. We build a max heap from the input array. At this point the largest item is stored at the root of the heap. We replace it with the last item of the heap followed by reducing the size of the heap by 1. Finally, we heapify the root of tree. We repeat the previous step until size of heap is greater than 1. Worst case complexity is O(n * log(n)).

**Radix Sort** - is a non-comparative sorting algorithm. It avoids comparison by creating and distributing elements into buckets according to their radix. For elements with more than one significant digit, this process is repeated for each digit, while preserving the ordering of the prior step, until all the digits have been considered. Worst case complexity is O(n * w), where w is the number of bits required to store each key.

## The Application

The user is able to select an algorithm from a selection to visualize and also customize the number of elements in the list to be sorted and the speed at which the visualization to run. After selecting all the necessary parametes the user can choose to start the algorithm visualization. After the algorithm has finished, the user can choose to reset the application in order to select different parameters to test.

![](https://github.com/andreidumitrescu95/Python-Sorting-Algorithm-Visualizer/blob/master/sorting_visualization.gif)

## WIP features and functionalities

At the current stage all but one sorting algorithms have been implemented and the flow of the application is complete enough so that a user may be able to visualize all algorithms and reset the visualization easily. Further adjustments can be made in the optimization department. I am considering switching from lists and arrays to numpy arrays which should make the app run a bit faster, seeing as numpy data structures are linear and they take less time to swap and compare values.
