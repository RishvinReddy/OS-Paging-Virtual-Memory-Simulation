# Output & Usage Guide

## How to Run
1. Ensure Python 3 is installed.
2. Install the required library:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the simulator:
   ```bash
   python paging_simulator.py
   ```
   *You will be prompted to choose between CLI (1) and GUI (2).*

## Understanding the Output

### Menu
### Mode Selection
```text
====================================
  Paging & Virtual Memory Simulator
====================================
1. CLI (Command Line Interface)
2. GUI (Graphical User Interface)
3. Exit

Enter your choice (1-3):
```

### GUI Interface
If you select **2 (GUI)**, a window will appear.
1. Enter the **Page Reference String** (e.g., `7 0 1 2 0 3 0 4`).
2. Enter the **Number of Frames** (e.g., `3`).
3. Click the buttons to run **FIFO**, **LRU**, or show the **Graph**.

The results will be displayed in the text area at the bottom.

### 1. FIFO Output
Shows the state of memory after every step.
- **FAULT**: Page was not in memory, loaded it.
- **HIT**: Page was already there.
- **Memory**: Current pages in the frames.

### 2. LRU Output
Similar to FIFO, but replacements happen based on "least recently used".
- **Comparison**: Typically, you will see fewer faults here for the same input.

### 3. Graph
A pop-up window will appear showing a bar chart.
- **X-axis**: Algorithm (FIFO vs LRU)
- **Y-axis**: Number of Page Faults
- **Observation**: The lower bar is the more efficient algorithm.

### 4. Address Translation
You will be asked for:
- **Logical Addresses**: e.g., `100 350`
- **Page Size**: e.g., `100`
- **Frames**: e.g., `3`

**Explanation:**
- `Logical 100` (Page Size 100) -> Page 1, Offset 0.
- If Page 1 is put in Frame 0 => Physical Address = `0 * 100 + 0 = 0`.
- This simulates the hardware MMU calculation.
