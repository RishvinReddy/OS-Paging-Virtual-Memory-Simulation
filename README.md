<div align="center">

```
╔═══════════════════════════════════════════════════════════════════╗
║        🖥️  OS PAGING & VIRTUAL MEMORY SIMULATOR                  ║
║              FIFO  ·  LRU  ·  Address Translation                ║
╚═══════════════════════════════════════════════════════════════════╝
```

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-FF6B6B?style=for-the-badge&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Graph-Matplotlib-11557C?style=for-the-badge&logo=plotly&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-00C853?style=for-the-badge)
![Type](https://img.shields.io/badge/Type-PBL_Project-FF9800?style=for-the-badge)

> **A full-featured simulation of Virtual Memory Management in Operating Systems.**  
> Demonstrates FIFO & LRU page replacement, visual graph comparison, and logical-to-physical address translation — with both CLI and GUI modes.

</div>

---

## 📑 Table of Contents

- [Overview](#-overview)
- [How Virtual Memory Works](#-how-virtual-memory-works)
- [Algorithms Explained](#-algorithms-explained)
- [Address Translation](#-address-translation)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Requirements & Installation](#-requirements--installation)
- [Usage & Modes](#-usage--modes)
- [Sample Walkthrough](#-sample-walkthrough)
- [Performance Comparison](#-performance-comparison)
- [Concepts Quick Reference](#-concepts-quick-reference)

---

## 🧠 Overview

This project is a **PBL (Project-Based Learning)** submission for the **Operating Systems** course at Woxsen University. It simulates the core virtual memory mechanism used in modern OS kernels — specifically **demand paging** and **page replacement**.

```
  CPU generates           OS manages              RAM holds
  Logical Addresses  -->  Page Table  -->  Physical Frames
       │                      │                    │
  [Page No | Offset]    [P# → Frame#]       [Frame 0..N-1]
```

When the required page is **not in RAM** → a **Page Fault** occurs → OS invokes a **Replacement Algorithm** to make room.

---

## 🏗️ How Virtual Memory Works

```
┌─────────────────────────────────────────────────────────────────┐
│                    VIRTUAL MEMORY FLOW                          │
│                                                                 │
│   Process        MMU           Page Table        RAM / Disk     │
│   ───────        ───           ──────────        ──────────     │
│   Access  ──→  Translate  ──→  Valid? ──Yes──→  Return Frame    │
│   Page N        Addr            │                               │
│                                 No                              │
│                                 ↓                               │
│                           PAGE FAULT                            │
│                                 │                               │
│                         Frames Available?                       │
│                        /              \                         │
│                      Yes              No                        │
│                       │               │                         │
│                   Load Page     Run Replacement Algo            │
│                       │        (FIFO / LRU selects victim)      │
│                       │               │                         │
│                       └──────→ Update Page Table ←─────────────┘
│                                       │                         │
│                                  Resume Process                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## ⚙️ Algorithms Explained

### 🔷 FIFO — First In, First Out

> The **oldest** page loaded into memory is the first one evicted.

```
Reference String: 7  0  1  2  0  3  0  4
Frames: 3

Step │ Page │ Frame 0 │ Frame 1 │ Frame 2 │ Result
─────┼──────┼─────────┼─────────┼─────────┼────────
  1  │  7   │    7    │    -    │    -    │ FAULT ❌
  2  │  0   │    7    │    0    │    -    │ FAULT ❌
  3  │  1   │    7    │    0    │    1    │ FAULT ❌
  4  │  2   │    2    │    0    │    1    │ FAULT ❌  (7 evicted)
  5  │  0   │    2    │    0    │    1    │ HIT   ✅
  6  │  3   │    2    │    3    │    1    │ FAULT ❌  (0 evicted)
  7  │  0   │    2    │    3    │    0    │ FAULT ❌  (1 evicted)
  8  │  4   │    4    │    3    │    0    │ FAULT ❌  (2 evicted)

                                    Total FIFO Faults: 7
```

**Pros & Cons:**

| ✅ Pros | ❌ Cons |
|--------|--------|
| Simple to implement | Suffers from Belady's Anomaly |
| No extra hardware needed | Ignores usage frequency |
| Predictable behavior | Can evict frequently-used pages |

---

### 🔶 LRU — Least Recently Used

> The page that was **used longest ago** is evicted first.

```
Reference String: 7  0  1  2  0  3  0  4
Frames: 3

Step │ Page │ Frame 0 │ Frame 1 │ Frame 2 │ LRU Victim │ Result
─────┼──────┼─────────┼─────────┼─────────┼────────────┼────────
  1  │  7   │    7    │    -    │    -    │     -      │ FAULT ❌
  2  │  0   │    7    │    0    │    -    │     -      │ FAULT ❌
  3  │  1   │    7    │    0    │    1    │     -      │ FAULT ❌
  4  │  2   │    2    │    0    │    1    │     7      │ FAULT ❌
  5  │  0   │    2    │    0    │    1    │     -      │ HIT   ✅
  6  │  3   │    2    │    0    │    3    │     1      │ FAULT ❌
  7  │  0   │    2    │    0    │    3    │     -      │ HIT   ✅
  8  │  4   │    4    │    0    │    3    │     2      │ FAULT ❌

                                    Total LRU Faults: 6
```

**Pros & Cons:**

| ✅ Pros | ❌ Cons |
|--------|--------|
| Exploits temporal locality | More complex to implement |
| Does NOT suffer Belady's Anomaly | Requires usage tracking overhead |
| Closer to Optimal algorithm | May need hardware counters |

---

### 🔁 FIFO vs LRU — Side-by-Side

| Property | FIFO | LRU |
|---|---|---|
| Eviction Policy | Oldest loaded page | Least recently accessed |
| Belady's Anomaly | ✅ Affected | ❌ Not affected |
| Implementation | Simple queue | Counter / stack tracking |
| Performance | Average | Better (locality-aware) |
| Hardware Needed | None | Reference bit / counter |
| Page Faults (example) | **7** | **6** |

---

## 🔄 Address Translation

```
┌──────────────────────────────────────────────────────────┐
│               LOGICAL → PHYSICAL TRANSLATION             │
│                                                          │
│   Logical Address  =  [ Page Number | Offset ]          │
│                              │                           │
│                         Page Table                       │
│                         ┌────────────────┐               │
│                         │ Page 0 → Frame 2│               │
│                         │ Page 1 → Frame 0│               │
│                         │ Page 2 → Frame 3│               │
│                         └────────────────┘               │
│                              │                           │
│   Physical Address =  [ Frame Number | Offset ]         │
│                                                          │
│   Formula:                                               │
│   Physical Addr = (Frame Number × Page Size) + Offset   │
└──────────────────────────────────────────────────────────┘
```

**Example Calculation:**

| Input | Value |
|---|---|
| Logical Address | `350` |
| Page Size | `100` bytes |
| Page Number | `350 ÷ 100 = 3` |
| Offset | `350 mod 100 = 50` |
| Mapped Frame (from table) | Frame `2` |
| Physical Address | `(2 × 100) + 50 = 250` |

---

## ✨ Features

| Feature | Description |
|---|---|
| 🖥️ Dual Mode | Run as CLI or GUI — your choice |
| 🔄 FIFO Simulation | Step-by-step page replacement with queue |
| 🧠 LRU Simulation | Tracks recency using counter/timestamp |
| 📊 Visual Graph | Matplotlib bar chart comparing both algorithms |
| 🔢 Address Translation | Converts logical addresses to physical addresses |
| 📋 Step Trace | Every page access shown with HIT / FAULT result |
| 🪟 GUI Window | Tkinter-based interactive window with input fields |

---

## 📁 Project Structure

```
OS-Paging-Virtual-Memory-Simulation/
│
├── 📄 paging_simulator.py     ← Main application (CLI + GUI combined)
├── 📄 requirements.txt        ← Python dependencies
│
├── 📄 PROJECT_REPORT.md       ← Formal project report (abstract → conclusion)
├── 📄 VIVA_QUESTIONS.md       ← Q&A for viva voce preparation
├── 📄 OUTPUT_GUIDE.md         ← Detailed guide to understand every output
└── 📄 README.md               ← You are here
```

---

## 🛠️ Requirements & Installation

### Prerequisites

| Requirement | Version | Purpose |
|---|---|---|
| Python | 3.x | Core runtime |
| `matplotlib` | Latest | Graph generation |
| `tkinter` | Built-in | GUI window |

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/RishvinReddy/OS-Paging-Virtual-Memory-Simulation.git

# 2. Navigate into the project
cd OS-Paging-Virtual-Memory-Simulation

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the simulator
python paging_simulator.py
```

---

## 🚀 Usage & Modes

```
====================================
  Paging & Virtual Memory Simulator
====================================
1. CLI (Command Line Interface)
2. GUI (Graphical User Interface)
3. Exit

Enter your choice (1-3):
```

### Mode 1 — CLI

- Runs entirely in the terminal
- Prompts for page reference string and number of frames
- Displays step-by-step trace for FIFO and LRU
- Shows address translation results

### Mode 2 — GUI

```
┌─────────────────────────────────────────────┐
│         Paging Simulator - GUI              │
├─────────────────────────────────────────────┤
│  Page Reference String: [7 0 1 2 0 3 0 4 ] │
│  Number of Frames:      [3               ] │
│                                             │
│  [ Run FIFO ]  [ Run LRU ]  [ Show Graph ] │
├─────────────────────────────────────────────┤
│  Output:                                    │
│  Page 7 → FAULT | Memory: [7]              │
│  Page 0 → FAULT | Memory: [7, 0]           │
│  ...                                        │
└─────────────────────────────────────────────┘
```

---

## 📋 Sample Walkthrough

**Input:**
- Reference String: `7 0 1 2 0 3 0 4`
- Frames: `3`

**FIFO Output:**
```
Page 7 → FAULT | Memory: [7]
Page 0 → FAULT | Memory: [7, 0]
Page 1 → FAULT | Memory: [7, 0, 1]
Page 2 → FAULT | Memory: [0, 1, 2]   ← 7 evicted (oldest)
Page 0 → HIT   | Memory: [0, 1, 2]
Page 3 → FAULT | Memory: [1, 2, 3]   ← 0 evicted
Page 0 → FAULT | Memory: [2, 3, 0]   ← 1 evicted
Page 4 → FAULT | Memory: [3, 0, 4]   ← 2 evicted
────────────────────────────────────
Total FIFO Page Faults: 7
```

**LRU Output:**
```
Page 7 → FAULT | Memory: [7]
Page 0 → FAULT | Memory: [7, 0]
Page 1 → FAULT | Memory: [7, 0, 1]
Page 2 → FAULT | Memory: [0, 1, 2]   ← 7 evicted (LRU)
Page 0 → HIT   | Memory: [0, 1, 2]
Page 3 → FAULT | Memory: [0, 2, 3]   ← 1 evicted (LRU)
Page 0 → HIT   | Memory: [0, 2, 3]
Page 4 → FAULT | Memory: [0, 3, 4]   ← 2 evicted (LRU)
────────────────────────────────────
Total LRU Page Faults: 6
```

> **Inference:** LRU saved 1 fault by recognising that page `0` was accessed recently (step 5) and keeping it in memory. FIFO blindly evicted it because it was "oldest" — even though it was still being used. This demonstrates **temporal locality**.

---

## 📊 Performance Comparison

```
Page Faults
│
8 │
7 │  ██████████
6 │  ██████████  ████████
5 │  ██████████  ████████
4 │  ██████████  ████████
3 │  ██████████  ████████
2 │  ██████████  ████████
1 │  ██████████  ████████
  └──────────────────────────
       FIFO (7)    LRU (6)

         ↑ Lower is Better ↑
```

| Algorithm | Page Faults | Page Hits | Hit Rate |
|---|---|---|---|
| FIFO | 7 | 1 | 12.5% |
| LRU | 6 | 2 | 25.0% |
| **Winner** | — | — | **LRU** ✅ |

> The simulator also generates this comparison as an interactive **Matplotlib bar chart** in a pop-up window.

---

## 📚 Concepts Quick Reference

| Term | Definition |
|---|---|
| **Virtual Memory** | Abstraction allowing processes to use more memory than physically available |
| **Paging** | Divides memory into fixed-size blocks (pages/frames) |
| **Page Fault** | Occurs when a requested page is not in RAM |
| **Page Table** | OS data structure mapping page numbers to frame numbers |
| **MMU** | Memory Management Unit — hardware that translates addresses |
| **Logical Address** | Address generated by CPU (Page No. + Offset) |
| **Physical Address** | Actual RAM address (Frame No. + Offset) |
| **FIFO** | Evicts the page that has been in memory the longest |
| **LRU** | Evicts the page that was used least recently |
| **Belady's Anomaly** | FIFO bug: more frames can cause *more* page faults |
| **Temporal Locality** | Recently used pages are likely to be used again soon |
| **Thrashing** | Excessive paging causing severe performance degradation |

---

<div align="center">

**Developed for the Operating Systems PBL — Woxsen University**  
Made with 🧠 + Python

</div>
