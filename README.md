<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=200&section=header&text=OS%20Paging%20%26%20Virtual%20Memory%20Simulator&fontSize=34&fontColor=ffffff&fontAlignY=38&desc=FIFO%20%C2%B7%20LRU%20%C2%B7%20Address%20Translation%20%C2%B7%20CLI%20%26%20GUI&descAlignY=58&descColor=a0a0ff&animation=fadeIn" width="100%"/>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=1000&color=7C8CF8&center=true&vCenter=true&width=600&lines=Simulating+Virtual+Memory+Management...;FIFO+%E2%86%92+First+In%2C+First+Out+Replacement;LRU+%E2%86%92+Least+Recently+Used+Replacement;Logical+%E2%86%92+Physical+Address+Translation" alt="Typing SVG" />

<br/><br/>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-FF6B6B?style=for-the-badge&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Graphs-Matplotlib-11557C?style=for-the-badge&logo=plotly&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-00C853?style=for-the-badge&logo=checkmarx&logoColor=white)

![Type](https://img.shields.io/badge/Type-PBL%20Project-FF9800?style=for-the-badge)
![Course](https://img.shields.io/badge/Course-Operating%20Systems-8A2BE2?style=for-the-badge)
![University](https://img.shields.io/badge/University-Woxsen-0D47A1?style=for-the-badge)

</div>

---

## 📑 Table of Contents

<div align="center">

| Section | Description |
|:---|:---|
| [🧠 Overview](#-overview) | What this project does and why |
| [⚙️ How Virtual Memory Works](#%EF%B8%8F-how-virtual-memory-works) | Full memory management flow |
| [🔷 FIFO Algorithm](#-fifo--first-in-first-out) | First-In First-Out walkthrough |
| [🔶 LRU Algorithm](#-lru--least-recently-used) | Least Recently Used walkthrough |
| [📊 Algorithm Comparison](#-algorithm-comparison) | FIFO vs LRU head-to-head |
| [🔄 Address Translation](#-address-translation) | Logical → Physical with examples |
| [✨ Features](#-features) | All capabilities at a glance |
| [📁 Project Structure](#-project-structure) | File tree and descriptions |
| [🛠️ Installation](#%EF%B8%8F-requirements--installation) | Setup guide |
| [🚀 Usage](#-usage--modes) | CLI and GUI walkthrough |
| [📋 Sample Run](#-full-sample-walkthrough) | End-to-end example |
| [📚 Glossary](#-concepts-quick-reference) | OS terms explained |

</div>

---

## 🧠 Overview

<div align="center">

> **A full-featured Python simulation of Virtual Memory Management in Operating Systems.**  
> Demonstrates FIFO & LRU page replacement step-by-step, generates performance graphs, and simulates logical-to-physical address translation — through both **CLI** and **GUI** modes.

</div>

<br/>

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│   ┌─────────┐    Logical     ┌──────────┐   Frame#   ┌──────────────┐   │
│   │   CPU   │ ─────────────► │   MMU    │ ──────────► │     RAM      │   │
│   │         │    Address     │          │            │  ┌──────────┐ │   │
│   │ Page No.│                │  Page    │            │  │ Frame 0  │ │   │
│   │ Offset  │                │  Table   │            │  │ Frame 1  │ │   │
│   └─────────┘                │  Lookup  │            │  │ Frame 2  │ │   │
│                               └──────────┘            │  └──────────┘ │   │
│                                    │                  └──────────────┘   │
│                               Page Fault?                                │
│                              /           \                               │
│                            YES            NO                             │
│                             │              │                             │
│                    Run Replacement     Return Physical                   │
│                    Algorithm           Address to CPU                    │
│                 (FIFO / LRU)                                             │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## ⚙️ How Virtual Memory Works

```
  PROCESS REQUESTS PAGE
          │
          ▼
  ┌───────────────┐
  │ Is page in    │──── YES ──► HIT ✅ → Return data to CPU
  │ RAM (frames)? │
  └───────────────┘
          │
         NO
          │
          ▼
  ┌───────────────┐
  │  PAGE FAULT   │  ← OS interrupted, begins handling
  └───────────────┘
          │
          ▼
  ┌──────────────────┐
  │ Free frame        │──── YES ──► Load page into free frame
  │ available?        │             Update page table → Resume
  └──────────────────┘
          │
         NO
          │
          ▼
  ┌──────────────────────────┐
  │   Page Replacement       │
  │   Algorithm Selected     │
  │                          │
  │   FIFO → Evict oldest    │
  │   LRU  → Evict LRU page  │
  └──────────────────────────┘
          │
          ▼
  Victim page written to disk (if dirty)
          │
          ▼
  New page loaded → Page table updated → Resume process
```

---

## 🔷 FIFO — First In, First Out

<details open>
<summary><b>Click to expand FIFO trace table</b></summary>

<br/>

**Reference String:** `7  0  1  2  0  3  0  4` &nbsp;&nbsp; | &nbsp;&nbsp; **Frames:** `3`

```
╔══════╦══════╦═════════╦═════════╦═════════╦══════════╦══════════╗
║ Step ║ Page ║ Frame 0 ║ Frame 1 ║ Frame 2 ║  Evicted ║  Result  ║
╠══════╬══════╬═════════╬═════════╬═════════╬══════════╬══════════╣
║  1   ║  7   ║    7    ║    —    ║    —    ║    —     ║ FAULT ❌ ║
║  2   ║  0   ║    7    ║    0    ║    —    ║    —     ║ FAULT ❌ ║
║  3   ║  1   ║    7    ║    0    ║    1    ║    —     ║ FAULT ❌ ║
║  4   ║  2   ║    2    ║    0    ║    1    ║    7     ║ FAULT ❌ ║
║  5   ║  0   ║    2    ║    0    ║    1    ║    —     ║  HIT  ✅ ║
║  6   ║  3   ║    2    ║    3    ║    1    ║    0     ║ FAULT ❌ ║
║  7   ║  0   ║    2    ║    3    ║    0    ║    1     ║ FAULT ❌ ║
║  8   ║  4   ║    4    ║    3    ║    0    ║    2     ║ FAULT ❌ ║
╠══════╬══════╩═════════╩═════════╩═════════╩══════════╬══════════╣
║      ║          Total Page Faults (FIFO) = 7          ║  📉 7/8  ║
╚══════╩═════════════════════════════════════════════════╩══════════╝
```

**FIFO Queue Progression:**
```
Start:  [ ]
Step 1: [ 7 ]            ← 7 enters rear
Step 2: [ 7 → 0 ]        ← 0 enters rear
Step 3: [ 7 → 0 → 1 ]    ← 1 enters rear, queue full
Step 4: [ 0 → 1 → 2 ]    ← 7 evicted from front, 2 enters rear
Step 5: [ 0 → 1 → 2 ]    ← 0 is HIT, no change
Step 6: [ 1 → 2 → 3 ]    ← 0 evicted from front, 3 enters rear
Step 7: [ 2 → 3 → 0 ]    ← 1 evicted from front, 0 enters rear
Step 8: [ 3 → 0 → 4 ]    ← 2 evicted from front, 4 enters rear
```

</details>

<br/>

| ✅ Advantages | ❌ Disadvantages |
|---|---|
| Dead simple to implement | Suffers from **Belady's Anomaly** |
| No extra hardware required | Ignores access frequency completely |
| Predictable, queue-based | May evict critical, frequently used pages |
| Low overhead | Worst average performance of common algorithms |

---

## 🔶 LRU — Least Recently Used

<details open>
<summary><b>Click to expand LRU trace table</b></summary>

<br/>

**Reference String:** `7  0  1  2  0  3  0  4` &nbsp;&nbsp; | &nbsp;&nbsp; **Frames:** `3`

```
╔══════╦══════╦═════════╦═════════╦═════════╦══════════╦══════════╗
║ Step ║ Page ║ Frame 0 ║ Frame 1 ║ Frame 2 ║  Evicted ║  Result  ║
╠══════╬══════╬═════════╬═════════╬═════════╬══════════╬══════════╣
║  1   ║  7   ║    7    ║    —    ║    —    ║    —     ║ FAULT ❌ ║
║  2   ║  0   ║    7    ║    0    ║    —    ║    —     ║ FAULT ❌ ║
║  3   ║  1   ║    7    ║    0    ║    1    ║    —     ║ FAULT ❌ ║
║  4   ║  2   ║    2    ║    0    ║    1    ║    7  🕐  ║ FAULT ❌ ║
║  5   ║  0   ║    2    ║    0    ║    1    ║    —     ║  HIT  ✅ ║
║  6   ║  3   ║    2    ║    0    ║    3    ║    1  🕐  ║ FAULT ❌ ║
║  7   ║  0   ║    2    ║    0    ║    3    ║    —     ║  HIT  ✅ ║
║  8   ║  4   ║    4    ║    0    ║    3    ║    2  🕐  ║ FAULT ❌ ║
╠══════╬══════╩═════════╩═════════╩═════════╩══════════╬══════════╣
║      ║          Total Page Faults (LRU) = 6           ║  📉 6/8  ║
╚══════╩══════════════════════════════════════════════════╩══════════╝
```
> 🕐 = Evicted because it was Least Recently Used

**LRU Stack Progression (MRU → LRU):**
```
Start:  [ ]
Step 1: [ 7 ]               → Most Recent: 7
Step 2: [ 0 | 7 ]           → Most Recent: 0
Step 3: [ 1 | 0 | 7 ]       → Most Recent: 1
Step 4: [ 2 | 1 | 0 ]       → 7 evicted (bottom/LRU), 2 added
Step 5: [ 0 | 2 | 1 ]       → 0 moved to top on HIT
Step 6: [ 3 | 0 | 2 ]       → 1 evicted (LRU), 3 added
Step 7: [ 0 | 3 | 2 ]       → 0 moved to top on HIT
Step 8: [ 4 | 0 | 3 ]       → 2 evicted (LRU), 4 added
```

</details>

<br/>

| ✅ Advantages | ❌ Disadvantages |
|---|---|
| Exploits **temporal locality** | More complex to implement |
| **No Belady's Anomaly** | Requires usage tracking (timestamps/counters) |
| Closest to Optimal (OPT) | May need hardware reference bits |
| Retains hot pages effectively | Higher overhead than FIFO |

---

## 📊 Algorithm Comparison

### Head-to-Head

| Property | 🔷 FIFO | 🔶 LRU |
|:---|:---:|:---:|
| Eviction Policy | Oldest loaded page | Least recently accessed |
| Belady's Anomaly | ✅ Affected | ❌ Immune |
| Implementation Complexity | 🟢 Simple | 🟡 Moderate |
| Hardware Needed | None | Reference bit / counter |
| Temporal Locality Aware | ❌ No | ✅ Yes |
| Performance (example) | **7 faults** | **6 faults** |
| Best for | Teaching / toy OS | Production systems |
| Hit Rate (example) | 12.5% | 25.0% |

### Visual Performance Chart

```
  Page Faults
  │
8 ┤
7 ┤  ████████████████████
6 ┤  ████████████████████  ██████████████████
5 ┤  ████████████████████  ██████████████████
4 ┤  ████████████████████  ██████████████████
3 ┤  ████████████████████  ██████████████████
2 ┤  ████████████████████  ██████████████████
1 ┤  ████████████████████  ██████████████████
  └──────────────────────────────────────────────
         FIFO (7)               LRU (6)

   ⬆️ FIFO: 7 faults    LRU: 6 faults  →  LRU wins ✅
               Lower Bar = Better Algorithm
```

> 💡 **Why LRU wins:** When page `0` was referenced at step 5, FIFO had already queued it for near-term eviction. LRU recognised it was recently used and kept it — saving 1 fault. This is **temporal locality** in action.

---

## 🔄 Address Translation

```
┌──────────────────────────────────────────────────────────────────┐
│                  LOGICAL → PHYSICAL ADDRESS MAP                  │
│                                                                  │
│   CPU generates Logical Address                                  │
│   ┌──────────────────────────────┐                               │
│   │  Logical Address = 350       │  (Page Size = 100 bytes)      │
│   │  Page Number = 350 ÷ 100 = 3 │                               │
│   │  Offset      = 350 mod 100 = 50│                              │
│   └──────────────────────────────┘                               │
│                    │                                             │
│                    ▼                                             │
│              ┌─────────────┐                                     │
│              │  Page Table │                                     │
│              ├──────┬──────┤                                     │
│              │ P.No │ Frame│                                     │
│              ├──────┼──────┤                                     │
│              │  0   │  2   │                                     │
│              │  1   │  0   │                                     │
│              │  2   │  4   │                                     │
│              │  3   │  1   │ ← Page 3 is in Frame 1             │
│              └──────┴──────┘                                     │
│                    │                                             │
│                    ▼                                             │
│   Physical Address = (Frame × Page Size) + Offset               │
│                    = (1 × 100) + 50 = 150                        │
│                                                                  │
│   ┌─────────────────────────────────────────────────────────┐    │
│   │  Logical 350  →  Page 3, Offset 50  →  Physical 150    │    │
│   └─────────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────────┘
```

### Translation Formula

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│   Page Number = ⌊ Logical Address ÷ Page Size ⌋    │
│   Offset      = Logical Address mod Page Size       │
│                                                     │
│   Physical Address = (Frame Number × Page Size)     │
│                    +  Offset                        │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Example Lookups

| Logical Address | Page Size | Page No. | Offset | Frame (Table) | Physical Address |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `100` | 100 | 1 | 0 | 0 | **0** |
| `350` | 100 | 3 | 50 | 1 | **150** |
| `275` | 100 | 2 | 75 | 4 | **475** |
| `0`   | 100 | 0 | 0  | 2 | **200** |

---

## ✨ Features

<div align="center">

| # | Feature | Description |
|:---:|:---|:---|
| 🖥️ | **Dual Mode Interface** | Full CLI mode or Tkinter-based GUI — user's choice at startup |
| 🔷 | **FIFO Simulation** | Queue-based page replacement with step-by-step trace |
| 🔶 | **LRU Simulation** | Counter/timestamp-based tracking with detailed output |
| 📊 | **Bar Graph** | Matplotlib pop-up comparing page fault counts visually |
| 🔢 | **Address Translation** | Full logical → physical mapping with formula explanation |
| 📋 | **Step Trace** | Every page access shown with HIT ✅ / FAULT ❌ labels |
| 🧮 | **Hit Rate Reporting** | Calculates and displays efficiency percentage per algorithm |
| 📂 | **Study Materials** | Includes project report, viva Q&A, and output guide |

</div>

---

## 📁 Project Structure

```
📦 OS-Paging-Virtual-Memory-Simulation/
│
├── 🐍 paging_simulator.py     ← Core application — CLI + GUI in one file
│                                 ├─ FIFO algorithm
│                                 ├─ LRU algorithm
│                                 ├─ Address Translation module
│                                 ├─ Matplotlib graph generator
│                                 └─ Tkinter GUI window
│
├── 📋 requirements.txt        ← Python dependencies (matplotlib)
│
├── 📄 PROJECT_REPORT.md       ← Formal report: abstract → conclusion
├── 📄 VIVA_QUESTIONS.md       ← Q&A for viva voce exam prep
├── 📄 OUTPUT_GUIDE.md         ← Explains every line of output in detail
└── 📄 README.md               ← You are here
```

---

## 🛠️ Requirements & Installation

### Prerequisites

| Tool | Version | Install |
|:---|:---:|:---|
| Python | ≥ 3.x | [python.org](https://python.org) |
| pip | Latest | Bundled with Python |
| `matplotlib` | Latest | `pip install matplotlib` |
| `tkinter` | Built-in | No install needed |

### Quick Setup

```bash
# Step 1 — Clone the repository
git clone https://github.com/RishvinReddy/OS-Paging-Virtual-Memory-Simulation.git

# Step 2 — Move into the project directory
cd OS-Paging-Virtual-Memory-Simulation

# Step 3 — Install dependencies
pip install -r requirements.txt

# Step 4 — Launch the simulator
python paging_simulator.py
```

---

## 🚀 Usage & Modes

### Startup Menu

```
╔══════════════════════════════════════╗
║    Paging & Virtual Memory Simulator ║
╠══════════════════════════════════════╣
║  1.  CLI (Command Line Interface)    ║
║  2.  GUI (Graphical User Interface)  ║
║  3.  Exit                            ║
╠══════════════════════════════════════╣
║  Enter your choice (1–3): _          ║
╚══════════════════════════════════════╝
```

### 🖤 Mode 1 — CLI

- Runs entirely in terminal
- Prompts: reference string → number of frames
- Outputs step-by-step trace for both FIFO and LRU
- Address translation with formula shown inline

### 🪟 Mode 2 — GUI

```
┌─────────────────────────────────────────────────────┐
│  🖥️  Paging & Virtual Memory Simulator              │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Page Reference String:  [ 7 0 1 2 0 3 0 4      ]  │
│  Number of Frames:       [ 3                     ]  │
│                                                     │
│  ┌─────────┐  ┌─────────┐  ┌──────────────────┐    │
│  │ Run FIFO│  │ Run LRU │  │   Show Graph 📊  │    │
│  └─────────┘  └─────────┘  └──────────────────┘    │
│                                                     │
├─────────────────────────────────────────────────────┤
│  Output:                                            │
│  ─────────────────────────────────────────────────  │
│  Page 7 → FAULT | Memory: [7]                      │
│  Page 0 → FAULT | Memory: [7, 0]                   │
│  Page 1 → FAULT | Memory: [7, 0, 1]                │
│  Page 2 → FAULT | Memory: [0, 1, 2]                │
│  Page 0 → HIT   | Memory: [0, 1, 2]                │
│  ...                                               │
│  Total Page Faults: 7                              │
└─────────────────────────────────────────────────────┘
```

---

## 📋 Full Sample Walkthrough

<details>
<summary><b>🔷 FIFO Full Output — click to expand</b></summary>

```
Reference String : 7  0  1  2  0  3  0  4
Frames           : 3
Algorithm        : FIFO
─────────────────────────────────────────────────
 Step 1  │  Page  7  │  FAULT ❌  │  Memory: [ 7 ]
 Step 2  │  Page  0  │  FAULT ❌  │  Memory: [ 7, 0 ]
 Step 3  │  Page  1  │  FAULT ❌  │  Memory: [ 7, 0, 1 ]
 Step 4  │  Page  2  │  FAULT ❌  │  Memory: [ 0, 1, 2 ]   ← 7 evicted
 Step 5  │  Page  0  │  HIT   ✅  │  Memory: [ 0, 1, 2 ]
 Step 6  │  Page  3  │  FAULT ❌  │  Memory: [ 1, 2, 3 ]   ← 0 evicted
 Step 7  │  Page  0  │  FAULT ❌  │  Memory: [ 2, 3, 0 ]   ← 1 evicted
 Step 8  │  Page  4  │  FAULT ❌  │  Memory: [ 3, 0, 4 ]   ← 2 evicted
─────────────────────────────────────────────────
 Total Faults : 7   │   Total Hits : 1   │   Hit Rate : 12.5%
─────────────────────────────────────────────────
```

</details>

<details>
<summary><b>🔶 LRU Full Output — click to expand</b></summary>

```
Reference String : 7  0  1  2  0  3  0  4
Frames           : 3
Algorithm        : LRU
─────────────────────────────────────────────────
 Step 1  │  Page  7  │  FAULT ❌  │  Memory: [ 7 ]
 Step 2  │  Page  0  │  FAULT ❌  │  Memory: [ 7, 0 ]
 Step 3  │  Page  1  │  FAULT ❌  │  Memory: [ 7, 0, 1 ]
 Step 4  │  Page  2  │  FAULT ❌  │  Memory: [ 0, 1, 2 ]   ← 7 evicted (LRU)
 Step 5  │  Page  0  │  HIT   ✅  │  Memory: [ 0, 1, 2 ]   ← 0 refreshed
 Step 6  │  Page  3  │  FAULT ❌  │  Memory: [ 0, 2, 3 ]   ← 1 evicted (LRU)
 Step 7  │  Page  0  │  HIT   ✅  │  Memory: [ 0, 2, 3 ]   ← 0 refreshed
 Step 8  │  Page  4  │  FAULT ❌  │  Memory: [ 0, 3, 4 ]   ← 2 evicted (LRU)
─────────────────────────────────────────────────
 Total Faults : 6   │   Total Hits : 2   │   Hit Rate : 25.0%
─────────────────────────────────────────────────
```

</details>

<br/>

```
  Final Score
  ═══════════════════════════════════════════════
  FIFO  →  7 faults  │  1 hit  │  12.5% hit rate
  LRU   →  6 faults  │  2 hits │  25.0% hit rate
  ───────────────────────────────────────────────
  Winner: LRU — saves 1 fault by exploiting
          temporal locality of page 0 ✅
  ═══════════════════════════════════════════════
```

---

## 📚 Concepts Quick Reference

<details open>
<summary><b>Core OS / Memory Terms</b></summary>

<br/>

| Term | Definition |
|:---|:---|
| **Virtual Memory** | OS abstraction allowing processes to use more memory than physically available in RAM |
| **Paging** | Memory management that divides logical & physical memory into fixed-size **pages** and **frames** |
| **Page** | Fixed-size block of logical (process) memory |
| **Frame** | Fixed-size block of physical (RAM) memory — same size as a page |
| **Page Fault** | Exception raised when CPU accesses a page not currently in RAM |
| **Page Table** | OS data structure mapping page numbers → frame numbers |
| **MMU** | Memory Management Unit — hardware chip that translates logical → physical addresses |
| **Logical Address** | Address generated by CPU: `[Page No. | Offset]` |
| **Physical Address** | Actual RAM address: `[Frame No. | Offset]` |
| **Demand Paging** | Pages loaded into RAM only when first accessed — not at process start |
| **FIFO** | Evicts the page that has been in memory the **longest** (oldest) |
| **LRU** | Evicts the page that was **used least recently** (stale) |
| **Belady's Anomaly** | FIFO bug where adding **more frames** causes **more page faults** |
| **Temporal Locality** | Recently used pages are statistically likely to be used again soon |
| **Spatial Locality** | Pages near recently accessed addresses are likely to be accessed soon |
| **Thrashing** | System spends more time paging than executing — caused by insufficient frames |
| **Working Set** | Set of pages actively used by a process in a time window |
| **Dirty Page** | A page modified in RAM that must be written to disk before eviction |

</details>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=120&section=footer&text=Operating%20Systems%20PBL%20%E2%80%94%20Woxsen%20University&fontSize=16&fontColor=a0a0ff&fontAlignY=65&animation=fadeIn" width="100%"/>

**Made with 🧠 + Python | FIFO · LRU · Address Translation**

</div>
