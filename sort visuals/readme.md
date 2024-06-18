# Sorting Algorithm Visualization

This project is a graphical tool for visualizing various sorting algorithms. The tool allows users to generate a random array and watch how different sorting algorithms work step-by-step. The visualization includes Bubble Sort, Insertion Sort, Selection Sort, and Merge Sort.

## Table of Contents

* [Features](#features)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
  * [Generate Array](#generate-array)
  * [Reset Array](#reset-array)
  * [Select Sorting Algorithm](#select-sorting-algorithm)
  * [Set Sorting Speed](#set-sorting-speed)
  * [Start Sorting](#start-sorting)
* [Sorting Algorithms Explained](#sorting-algorithms-explained)
  * [Bubble Sort](#bubble-sort)
  * [Insertion Sort](#insertion-sort)
  * [Selection Sort](#selection-sort)
  * [Merge Sort](#merge-sort)
* [Future Enhancements](#future-enhancements)
* [Contributing](#contributing)
* [License](#license)

## Features

* Generate random arrays with user-defined size and value range.
* Visualize sorting algorithms step-by-step.
* Supports multiple sorting algorithms: Bubble Sort, Insertion Sort, Selection Sort, and Merge Sort.
* Adjustable sorting speed.

## Requirements

* Python 3.x
* tkinter (Python's standard GUI package)

## Installation

1. **Clone the Repository** :

<pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg>Copy code</button></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">git clone https://github.com/yourusername/sorting-visualization.git
   cd sorting-visualization
   </code></div></div></pre>

1. **Run the Script** :

<pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg>Copy code</button></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">python sort_visualization.py
   </code></div></div></pre>

## Usage

### Generate Array

1. **Set Array Size** : Use the "Select Size" slider to choose the number of elements in the array.
2. **Set Value Range** : Use the "Select Min. value" and "Select Max. value" sliders to set the range of values for the elements.
3. **Click "Generate"** : Generates a random array with the specified size and value range.

### Reset Array

* Click the "Reset" button to reset the array to its original unsorted state.

### Select Sorting Algorithm

* Use the dropdown menu labeled "Select Algorithm" to choose the sorting algorithm you want to visualize (Bubble Sort, Insertion Sort, Selection Sort, Merge Sort).

### Set Sorting Speed

* Use the "Select Speed" slider to adjust the speed of the sorting visualization.

### Start Sorting

* Click the "Start" button to begin the visualization of the selected sorting algorithm.

## Sorting Algorithms Explained

### Bubble Sort

Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The process is repeated until the list is sorted.

### Insertion Sort

Insertion Sort builds the sorted array one item at a time, with the final sorted array being built one element at a time by comparing and inserting elements into their correct positions.

### Selection Sort

Selection Sort divides the list into two parts: the sorted part at the beginning and the unsorted part at the end. It repeatedly selects the smallest (or largest) element from the unsorted part and moves it to the end of the sorted part.

### Merge Sort

Merge Sort is a divide-and-conquer algorithm that divides the list into two halves, recursively sorts each half, and then merges the two sorted halves to produce the final sorted list.

## Future Enhancements

* Add more sorting algorithms (Quick Sort, Heap Sort, etc.).
* Improve UI with more interactive features and better visual representations.
* Include educational information about each sorting algorithm.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or new features to suggest.
