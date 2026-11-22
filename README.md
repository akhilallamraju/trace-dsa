# Trace - Data Structures & Algorithms

Trace is an interactive desktop application designed to make data
structures and algorithms easier to understand through step-by-step
visualisations. Rather than simply showing the final output, Trace aims
to illustrate how an algorithm works as it processes data.

The application is organised into three modules:

- **Searching** - explore how searching algorithms locate values.
- **Sorting** - watch sorting algorithms rearrange collections of data.
- **Binary Trees** - understand how traversal algorithms visit nodes in a tree.

> **Project status:** Trace is under active development. Features
> described below represent the planned scope and may not all be
> implemented yet.

------------------------------------------------------------------------

## 1 Modules

### 1.1 Searching Algorithms

Generate a random collection of values, choose a target and observe how
a searching algorithm works.

Planned algorithms:

- **Linear Search** - inspect elements one at a time until the target is found or the collection is exhausted.
- **Binary Search** - repeatedly divide a sorted collection to narrow down the target's position.

Planned visual features include highlighting the current element,
showing the search range, and displaying the number of comparisons.

### 1.2 Sorting

Generate a random array and watch an algorithm sort its elements.

Planned algorithms:

- **Bubble Sort**
- **Selection Sort**
- **Insertion Sort**
- **Merge Sort**

Planned visual features include animated comparisons and swaps,
adjustable animation speed, and statistics such as comparisons and
swaps.

### 1.3 Binary Trees

Explore how traversal algorithms visit nodes in a binary tree.

Planned traversals:

- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**:
    - Pre-order
    - In-order
    - Post-order

The visualiser will highlight nodes as they are visited and display the
resulting traversal sequence.

------------------------------------------------------------------------

## 2 Technology

Trace is being developed with:

-   **Python** - application and algorithm implementations.
-   **Tkinter** - desktop graphical user interface.
-   **Git & GitHub** - version control and project hosting.
-   **pytest** - planned automated testing.

The project is intended to keep algorithm implementations separate from
the user interface and visualisation code. This makes the algorithms
easier to test, reuse and extend.

------------------------------------------------------------------------

## 3 Getting Started

### 3.1 Prerequisites

-   Python 3.10 or later
-   Git

Tkinter is included with many standard Python installations. On some
Linux distributions, it may need to be installed separately.

### 3.2 Clone the repository

``` bash
git clone https://github.com/akhilallamraju/trace-dsa.git
cd trace-dsa
```

### 3.3 Run the application

``` bash
python main.py
```

OR

``` bash
python3 main.py
```

------------------------------------------------------------------------

## 4 Planned Project Structure

The codebase will be built around the following file structure:

``` text
trace-dsa/
│
├── main.py
├── theme.py
│
├── ui/
│   ├── __init__.py
│   ├── main_menu.py
│   ├── searching_screen.py
│   ├── sorting_screen.py
│   └── tree_screen.py
│
├── algorithms/
│   ├── searching/
│   ├── sorting/
│   └── trees/
│
├── visualisation/
│   ├── array_visualiser.py
│   └── tree_visualiser.py
│
├── tests/
│
└── README.md
```

------------------------------------------------------------------------

## 5 Development Goals

The project is being built incrementally, with an emphasis on:

- Clear, modular and maintainable code.
- Separating algorithm logic from visualisation.
- Showing algorithm execution step by step.
- Explaining time complexity and comparing algorithm behaviour.
- Testing algorithms against typical and edge-case inputs.
- Providing a consistent and accessible user interface.

------------------------------------------------------------------------

## 6 Roadmap

- [x] Create the application window and main menu.
- [x] Implement navigation between the three modules.
- [x] Implement and visualise Linear Search.
- [x] Implement and visualise Binary Search.
- [ ] Implement and visualise the initial sorting algorithms.
- [ ] Generate and display binary trees.
- [ ] Implement BFS and DFS traversals.
- [ ] Add execution statistics and animation controls.
- [ ] Add automated tests and complete project documentation.

------------------------------------------------------------------------

## 7 Contributing

Trace is currently a personal learning project. Suggestions and feedback
are welcome - feel free to open an issue or start a discussion in the
repository.

------------------------------------------------------------------------

## 8 Licence

See 'LICENCE'
