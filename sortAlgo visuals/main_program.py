from tkinter import *
from tkinter import messagebox
import random
import time

unsorted_data = data = []

def draw_data(data, colors):
    """
    Function that is used to draw the array of data

    Inputs:
    data => array of the data to be drawn
    colors => array carrying the corresponding color of each value in the array
    """
    canvas.delete("all")
    canvas_height = 500
    canvas_width = 800
    x_width = canvas_width / (len(data) + 1)
    offset = 20
    spacing = 10

    # Normalizing the heights of the bars
    normalize_data = [i / max(data) for i in data]

    for i, rec_height in enumerate(normalize_data):
        x_initial = i * x_width + offset + spacing
        y_initial = canvas_height - rec_height * 460

        x_final = (i+1) * x_width + offset
        y_final = canvas_height

        canvas.create_rectangle(x_initial, y_initial, x_final, y_final, fill=colors[i])
        canvas.create_text(x_initial + 2, y_initial, anchor=SW, text=str(data[i]))

    # Updating the canvas after sleep
    main_prog.update_idletasks()

def generate_array():
    """
    Function that is used to generate an array of data on clicking on the generate button in the UI_frame
    """
    global data, unsorted_data

    # Reading user inputs
    min_val = int(min_value.get())
    size_val = int(size_value.get())
    max_val = int(max_value.get())

    if min_val > max_val:
        messagebox.showwarning(message="Max. value should not be less than Min. value")
        min_val, max_val = max_val, min_val

    data = [random.randrange(min_val, max_val + 1) for _ in range(size_val)]
    unsorted_data = data.copy()
    draw_data(data, ["red" for x in range(len(data))])

def reset_array():
    """
    Function that resets the current sorted array
    """
    global data
    data = unsorted_data.copy()
    draw_data(data, ["red" for x in range(len(data))])

def bubble_sort(data, speed):
    """
    Function that performs bubble sort on the passed array

    Inputs:
    data => array to be sorted
    speed => speed of the simulation
    """
    for i in range(len(data)-1):
        for j in range(len(data) - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
            draw_data(data, ["yellow" if x == j or x == j + 1 else "red" for x in range(len(data))])
            time.sleep(speed)

    draw_data(data, ["green" for x in range(len(data))])

def insertion_sort(data, speed):
    """
    Function that performs insertion sort on the passed array

    Inputs:
    data => array to be sorted
    speed => speed of the simulation
    """
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
            draw_data(data, ["yellow" if x == j or x == j + 1 else "red" for x in range(len(data))])
            time.sleep(speed)
        data[j + 1] = key
        draw_data(data, ["yellow" if x == j + 1 else "red" for x in range(len(data))])
        time.sleep(speed)

    draw_data(data, ["green" for x in range(len(data))])

def selection_sort(data, speed):
    """
    Function that performs selection sort on the passed array

    Inputs:
    data => array to be sorted
    speed => speed of the simulation
    """
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
            draw_data(data, ["yellow" if x == j or x == min_idx else "red" for x in range(len(data))])
            time.sleep(speed)
        data[i], data[min_idx] = data[min_idx], data[i]
        draw_data(data, ["yellow" if x == i or x == min_idx else "red" for x in range(len(data))])
        time.sleep(speed)

    draw_data(data, ["green" for x in range(len(data))])

def merge_sort(data, speed):
    """
    Function that performs merge sort on the passed array

    Inputs:
    data => array to be sorted
    speed => speed of the simulation
    """
    def merge_sort_recursive(data, left, right, speed):
        if left < right:
            middle = (left + right) // 2
            merge_sort_recursive(data, left, middle, speed)
            merge_sort_recursive(data, middle + 1, right, speed)
            merge(data, left, middle, right, speed)

    def merge(data, left, middle, right, speed):
        n1 = middle - left + 1
        n2 = right - middle
        L = data[left:middle + 1]
        R = data[middle + 1:right + 1]
        i = j = 0
        k = left

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                data[k] = L[i]
                i += 1
            else:
                data[k] = R[j]
                j += 1
            draw_data(data, ["yellow" if x == k else "red" for x in range(len(data))])
            time.sleep(speed)
            k += 1

        while i < n1:
            data[k] = L[i]
            i += 1
            k += 1
            draw_data(data, ["yellow" if x == k else "red" for x in range(len(data))])
            time.sleep(speed)

        while j < n2:
            data[k] = R[j]
            j += 1
            k += 1
            draw_data(data, ["yellow" if x == k else "red" for x in range(len(data))])
            time.sleep(speed)

    merge_sort_recursive(data, 0, len(data) - 1, speed)
    draw_data(data, ["green" for x in range(len(data))])

def run_sort():
    """
    Function that runs the simulation on user click
    """
    global data
    speed = speed_scale.get()
    algorithm = algo_menu.get()

    if algorithm == 'Bubble Sort':
        bubble_sort(data, speed)
    elif algorithm == 'Insertion Sort':
        insertion_sort(data, speed)
    elif algorithm == 'Selection Sort':
        selection_sort(data, speed)
    elif algorithm == 'Merge Sort':
        merge_sort(data, speed)

# Initializing main program
main_prog = Tk()
main_prog.title("Sorting Algorithm Visualization")
main_prog.maxsize(800, 800)
main_prog.config(bg="grey")

# Creating user interface frame
UI_frame = Frame(main_prog, width=800, height=300, bg="grey")
UI_frame.grid(row=0, column=0, padx=10, pady=5)

Label(UI_frame, text="Sorting Algorithm Visualization", bg="grey", font=("Arial", 16)).grid(row=0, column=0, padx=5, pady=5, columnspan=4)
Button(UI_frame, text="Start", command=run_sort, bg="green").grid(row=1, column=1, padx=5, pady=5)

speed_scale = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed", bg="ivory")
speed_scale.grid(row=1, column=2, padx=5, pady=5)

# Creating scale for array size
size_value = Scale(UI_frame, from_=0, to=30, resolution=1, orient=HORIZONTAL, label="Select Size", bg="ivory")
size_value.grid(row=2, column=0, padx=5, pady=5, sticky=W)

# Creating scale for min. value of generated values
min_value = Scale(UI_frame, from_=0, to=100, resolution=10, orient=HORIZONTAL, label="Select Min. value", bg="ivory")
min_value.grid(row=2, column=1, padx=5, pady=5, sticky=W)

# Creating scale for max. value of generated values
max_value = Scale(UI_frame, from_=0, to=500, resolution=10, orient=HORIZONTAL, label="Select Max. value", bg="ivory")
max_value.grid(row=2, column=2, padx=5, pady=5, sticky=W)

# Generate random array button
Button(UI_frame, text="Generate", command=generate_array, bg="blue").grid(row=2, column=3, padx=5, pady=5)

# Reset the current array button
Button(UI_frame, text="Reset", command=reset_array, bg="blue").grid(row=1, column=3, padx=5, pady=5)

# Sorting algorithm menu
algo_menu = StringVar()
algo_menu.set("Bubble Sort")
algo_menu_label = Label(UI_frame, text="Select Algorithm", bg="grey")
algo_menu_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
algo_menu_dropdown = OptionMenu(UI_frame, algo_menu, "Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort")
algo_menu_dropdown.grid(row=1, column=0, padx=5, pady=5, sticky=E)

# Creating canvas for visualization
canvas = Canvas(main_prog, width=800, height=500, bg="white")
canvas.grid(row=1, column=0, padx=10, pady=5)

# Running main program
main_prog.mainloop()
# End of main program