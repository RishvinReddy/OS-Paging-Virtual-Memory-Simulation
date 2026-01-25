# Paging & Virtual Memory Simulator

**Project:** PBL (Project Based Learning) - Operating Systems  
**Language:** Python 3  

## Overview
This project is a simulation of **Virtual Memory Management** using **Paging**. It demonstrates how an Operating System handles memory allocation, page faults, and address translation. The simulator includes two popular page replacement algorithms: **FIFO (First-In-First-Out)** and **LRU (Least Recently Used)**.

## Features
- **Dual Mode:** Choose between **Command Line Interface (CLI)** or **Graphical User Interface (GUI)**.
- **Page Replacement:** Simulates FIFO and LRU algorithms step-by-step.
- **Visual Comparison:** Generates a bar graph comparing page faults for both algorithms.
- **Address Translation:** Simulates Logical to Physical address translation using a Page Table.
- **Interactive:** User-friendly menus and input prompts.

## Requirements
- Python 3.x
- `matplotlib` (for graphing)
- `tkinter` (included with standard Python, for GUI)

## Installation
1. Clone or download this repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the main script:
```bash
python paging_simulator.py
```

You will be prompted to select a mode:
1. **CLI Mode:** Runs in the terminal.
2. **GUI Mode:** Opens a graphical window.

### Sample Input
- **Page Reference String:** `7 0 1 2 0 3 0 4`
- **Number of Frames:** `3`

## Project Structure
- `paging_simulator.py`: Main application code (CLI + GUI).
- `PROJECT_REPORT.md`: Formal project report.
- `VIVA_QUESTIONS.md`: Q&A for viva voce.
- `OUTPUT_GUIDE.md`: Detailed guide on understanding the output.
- `requirements.txt`: Python dependencies.

## Credits
Developed for the Operating Systems Laboratory course.
