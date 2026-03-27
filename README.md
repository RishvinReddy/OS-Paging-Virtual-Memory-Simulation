<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=220&section=header&text=OS%20Paging%20%26%20Virtual%20Memory%20Simulator&fontSize=30&fontColor=ffffff&fontAlignY=36&desc=FIFO%20%E2%80%A2%20LRU%20%E2%80%A2%20Address%20Translation%20%E2%80%A2%20CLI%20%26%20GUI&descAlignY=55&descColor=b0b0ff&animation=fadeIn" width="100%" alt="header"/>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=16&pause=1200&color=7C8CF8&center=true&vCenter=true&width=620&lines=Simulating+Virtual+Memory+Management+in+Python...;FIFO+%E2%86%92+Evicts+the+Oldest+Page+in+Memory;LRU+%E2%86%92+Evicts+the+Least+Recently+Used+Page;Logical+Address+%E2%86%92+Physical+Address+Translation" alt="Typing SVG"/>

<br/><br/>

<a href="https://www.python.org"><img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/></a>
<a href="#"><img src="https://img.shields.io/badge/GUI-Tkinter-FF6B6B?style=for-the-badge&logo=python&logoColor=white" alt="Tkinter"/></a>
<a href="#"><img src="https://img.shields.io/badge/Graphs-Matplotlib-11557C?style=for-the-badge&logo=plotly&logoColor=white" alt="Matplotlib"/></a>
<img src="https://img.shields.io/badge/Status-Complete-00C853?style=for-the-badge&logo=github&logoColor=white" alt="Status"/>

<br/>

<img src="https://img.shields.io/badge/Type-PBL%20Project-FF9800?style=for-the-badge" alt="Type"/>
<img src="https://img.shields.io/badge/Course-Operating%20Systems-8A2BE2?style=for-the-badge" alt="Course"/>
<img src="https://img.shields.io/badge/University-Woxsen-0D47A1?style=for-the-badge" alt="University"/>
<img src="https://img.shields.io/badge/Language-Python%203-yellow?style=for-the-badge&logo=python&logoColor=white" alt="Language"/>

<br/><br/>

> **A full-featured simulation of Virtual Memory Management in Operating Systems.**
> Demonstrates FIFO and LRU page replacement step-by-step, generates a visual comparison graph,
> and simulates logical-to-physical address translation — with both **CLI** and **GUI** modes.

</div>

---

## Table of Contents

<div align="center">

| # | Section |
|:---:|:---|
| 01 | [Overview](#overview) |
| 02 | [Virtual Memory Architecture](#virtual-memory-architecture) |
| 03 | [Page Replacement Flow](#page-replacement-flow) |
| 04 | [FIFO Algorithm](#fifo--first-in-first-out) |
| 05 | [LRU Algorithm](#lru--least-recently-used) |
| 06 | [Belady's Anomaly Demo](#beladys-anomaly-demonstration) |
| 07 | [Algorithm Comparison](#algorithm-comparison) |
| 08 | [Address Translation](#address-translation) |
| 09 | [Features](#features) |
| 10 | [Project Structure](#project-structure) |
| 11 | [Installation](#installation) |
| 12 | [Usage and Modes](#usage-and-modes) |
| 13 | [Full Sample Walkthrough](#full-sample-walkthrough) |
| 14 | [Performance Analysis](#performance-analysis) |
| 15 | [Glossary](#glossary) |

</div>

---

<a name="overview"></a>
## Overview

```
╔══════════════════════════════════════════════════════════════════════════╗
║                      WHAT THIS PROJECT SIMULATES                        ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║   Modern OS kernels manage memory using VIRTUAL MEMORY + PAGING.        ║
║   This simulator reproduces the exact behaviour of that system:          ║
║                                                                          ║
║   1. CPU generates a logical address  →  [Page Number | Offset]          ║
║   2. MMU looks up the Page Table      →  finds Frame Number              ║
║   3. If page is in RAM                →  HIT, return data                ║
║   4. If page is NOT in RAM            →  PAGE FAULT                      ║
║   5. OS runs replacement algorithm    →  FIFO or LRU picks victim        ║
║   6. Victim evicted, new page loaded  →  page table updated              ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

This is a **PBL (Project-Based Learning)** submission for the **Operating Systems** course.

---

<a name="virtual-memory-architecture"></a>
## Virtual Memory Architecture

```
  PROCESS ADDRESS SPACE              PHYSICAL RAM
  ┌─────────────────┐                ┌─────────────────┐
  │   Page  0       │                │   Frame  0      │ ← Page 2 loaded
  │   Page  1       │                │   Frame  1      │ ← Page 5 loaded
  │   Page  2  ─────┼──────┐         │   Frame  2      │ ← Page 0 loaded
  │   Page  3       │      │         │   Frame  3      │ ← Page 7 loaded
  │   Page  4       │      │         └─────────────────┘
  │   Page  5  ─────┼──────┼──┐
  │   Page  6       │      │  │      PAGE TABLE
  │   Page  7  ─────┼──────┼──┼──┐  ┌────────┬─────────┐
  │    ...          │      │  │  │  │ Page # │ Frame # │
  └─────────────────┘      │  │  │  ├────────┼─────────┤
                           │  │  │  │   0    │    2    │
         DISK / SWAP       │  │  │  │   2    │    0    │
  ┌─────────────────┐      │  │  │  │   5    │    1    │
  │   Page  1  ◄────┼──────┘  │  └─►│   7    │    3    │
  │   Page  3  ◄────┼─────────┘     └────────┴─────────┘
  │   Page  4       │   (not yet
  │   Page  6       │    loaded)          MMU translates:
  └─────────────────┘              Logical → Frame → Physical
```

---

<a name="page-replacement-flow"></a>
## Page Replacement Flow

```
  CPU requests Page N
         │
         ▼
  ┌──────────────────┐
  │  Check Page Table │
  └──────────────────┘
         │
    ┌────┴─────┐
   YES         NO
    │           │
    ▼           ▼
  HIT ✅     PAGE FAULT ❌
  Return      OS takes control
  data             │
                   ▼
          ┌─────────────────┐
          │ Free frame in   │
          │ RAM available?  │
          └─────────────────┘
               │       │
              YES      NO
               │       │
               ▼       ▼
           Load page  Run Replacement Algorithm
           directly   ┌────────────────────────┐
                      │  FIFO → evict oldest   │
                      │  LRU  → evict stale    │
                      └────────────────────────┘
                               │
                               ▼
                    Write dirty page to disk (if modified)
                               │
                               ▼
                    Load new page into freed frame
                               │
                               ▼
                    Update page table entry
                               │
                               ▼
                    Resume CPU execution ✅
```

---

<a name="fifo--first-in-first-out"></a>
## FIFO — First In, First Out

> The **oldest** page in memory — the one loaded first — is evicted when a replacement is needed.

<details>
<summary><strong>Click to expand — Full FIFO Trace</strong></summary>

<br>

**Input:** Reference String `7 0 1 2 0 3 0 4` · Frames `3`

```
┌──────┬──────┬─────────┬─────────┬─────────┬──────────┬───────────┐
│ Step │ Page │ Frame 0 │ Frame 1 │ Frame 2 │  Evicted │  Result   │
├──────┼──────┼─────────┼─────────┼─────────┼──────────┼───────────┤
│  1   │  7   │    7    │    -    │    -    │    -     │ FAULT  ❌ │
│  2   │  0   │    7    │    0    │    -    │    -     │ FAULT  ❌ │
│  3   │  1   │    7    │    0    │    1    │    -     │ FAULT  ❌ │
│  4   │  2   │    2    │    0    │    1    │    7     │ FAULT  ❌ │
│  5   │  0   │    2    │    0    │    1    │    -     │ HIT    ✅ │
│  6   │  3   │    2    │    3    │    1    │    0     │ FAULT  ❌ │
│  7   │  0   │    2    │    3    │    0    │    1     │ FAULT  ❌ │
│  8   │  4   │    4    │    3    │    0    │    2     │ FAULT  ❌ │
├──────┴──────┴─────────┴─────────┴─────────┴──────────┼───────────┤
│         Total FIFO Faults = 7   │   Hits = 1          │ Rate 12.5%│
└─────────────────────────────────────────────────────────────────────┘
```

**FIFO Queue State at Each Step (front → rear):**

```
Step 1:  [ 7 ]                  ← 7 enters
Step 2:  [ 7 → 0 ]              ← 0 enters
Step 3:  [ 7 → 0 → 1 ]          ← 1 enters  (queue FULL)
Step 4:  [ 0 → 1 → 2 ]          ← 7 evicted (front), 2 enters rear
Step 5:  [ 0 → 1 → 2 ]          ← 0 HIT, no queue change
Step 6:  [ 1 → 2 → 3 ]          ← 0 evicted (front), 3 enters rear
Step 7:  [ 2 → 3 → 0 ]          ← 1 evicted (front), 0 enters rear
Step 8:  [ 3 → 0 → 4 ]          ← 2 evicted (front), 4 enters rear
```

> **Note at Step 6:** Page `0` was just used at Step 5, yet FIFO evicts it because it was loaded earliest. This is the core weakness — FIFO is completely blind to usage recency.

</details>

<br>

| Advantages | Disadvantages |
|:---|:---|
| Extremely simple to implement | Suffers from **Belady's Anomaly** |
| No hardware support needed | Ignores access frequency entirely |
| Predictable, deterministic | May evict heavily-used pages |
| Minimal runtime overhead | Worst average performance of all common algorithms |

---

<a name="lru--least-recently-used"></a>
## LRU — Least Recently Used

> The page that has **not been used for the longest time** is chosen as the eviction victim.

<details>
<summary><strong>Click to expand — Full LRU Trace</strong></summary>

<br>

**Input:** Reference String `7 0 1 2 0 3 0 4` · Frames `3`

```
┌──────┬──────┬─────────┬─────────┬─────────┬───────────┬───────────┐
│ Step │ Page │ Frame 0 │ Frame 1 │ Frame 2 │  Evicted  │  Result   │
├──────┼──────┼─────────┼─────────┼─────────┼───────────┼───────────┤
│  1   │  7   │    7    │    -    │    -    │     -     │ FAULT  ❌ │
│  2   │  0   │    7    │    0    │    -    │     -     │ FAULT  ❌ │
│  3   │  1   │    7    │    0    │    1    │     -     │ FAULT  ❌ │
│  4   │  2   │    2    │    0    │    1    │  7 (LRU)  │ FAULT  ❌ │
│  5   │  0   │    2    │    0    │    1    │     -     │ HIT    ✅ │
│  6   │  3   │    2    │    0    │    3    │  1 (LRU)  │ FAULT  ❌ │
│  7   │  0   │    2    │    0    │    3    │     -     │ HIT    ✅ │
│  8   │  4   │    4    │    0    │    3    │  2 (LRU)  │ FAULT  ❌ │
├──────┴──────┴─────────┴─────────┴─────────┴───────────┼───────────┤
│         Total LRU Faults = 6   │   Hits = 2            │ Rate 25.0%│
└───────────────────────────────────────────────────────────────────┘
```

**LRU Stack State at Each Step (MRU ← top, LRU ← bottom):**

```
Step 1:  [ 7 ]               ← Most Recent = 7
Step 2:  [ 0 | 7 ]           ← Most Recent = 0
Step 3:  [ 1 | 0 | 7 ]       ← Most Recent = 1  (stack FULL)
Step 4:  [ 2 | 1 | 0 ]       ← 7 evicted (bottom/LRU), 2 at top
Step 5:  [ 0 | 2 | 1 ]       ← 0 HIT: moved to top, stack reordered
Step 6:  [ 3 | 0 | 2 ]       ← 1 evicted (bottom/LRU), 3 at top
Step 7:  [ 0 | 3 | 2 ]       ← 0 HIT: moved to top, stack reordered
Step 8:  [ 4 | 0 | 3 ]       ← 2 evicted (bottom/LRU), 4 at top
```

> **Why LRU wins at Step 6:** Page `0` was used at Step 5, so it sits at the top of the LRU stack — protected. LRU correctly identifies page `1` (unused since Step 3) as the real victim. FIFO evicts `0` instead — a recently active page.

</details>

<br>

| Advantages | Disadvantages |
|:---|:---|
| Exploits **temporal locality** | More complex to implement |
| **Immune to Belady's Anomaly** | Needs usage tracking (timestamps / counters) |
| Closest to the theoretical Optimal (OPT) | May require hardware reference bits |
| Retains hot/active pages | Higher overhead than FIFO |

---

<a name="beladys-anomaly-demonstration"></a>
## Belady's Anomaly Demonstration

> **Belady's Anomaly:** With FIFO, adding *more* physical frames can sometimes cause *more* page faults. LRU is immune.

**Reference String:** `1 2 3 4 1 2 5 1 2 3 4 5`

```
┌─────────────────────────────────────────────────────────────────┐
│                        FIFO — 3 Frames                          │
├──────┬──────┬─────────┬─────────┬─────────┬────────────────────┤
│ Step │ Page │ Frame 0 │ Frame 1 │ Frame 2 │ Result             │
├──────┼──────┼─────────┼─────────┼─────────┼────────────────────┤
│  1   │  1   │    1    │    -    │    -    │ FAULT ❌           │
│  2   │  2   │    1    │    2    │    -    │ FAULT ❌           │
│  3   │  3   │    1    │    2    │    3    │ FAULT ❌           │
│  4   │  4   │    4    │    2    │    3    │ FAULT ❌           │
│  5   │  1   │    4    │    1    │    3    │ FAULT ❌           │
│  6   │  2   │    4    │    1    │    2    │ FAULT ❌           │
│  7   │  5   │    5    │    1    │    2    │ FAULT ❌           │
│  8   │  1   │    5    │    1    │    2    │ HIT   ✅           │
│  9   │  2   │    5    │    1    │    2    │ HIT   ✅           │
│ 10   │  3   │    5    │    3    │    2    │ FAULT ❌           │
│ 11   │  4   │    5    │    3    │    4    │ FAULT ❌           │
│ 12   │  5   │    5    │    3    │    4    │ HIT   ✅           │
├──────┴──────┴─────────┴─────────┴─────────┴────────────────────┤
│                            FIFO 3 Frames = 9 faults            │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                       FIFO — 4 Frames  (MORE frames = MORE faults!) │
├──────┬──────┬─────────┬─────────┬─────────┬─────────┬─────────────┤
│ Step │ Page │ Frame 0 │ Frame 1 │ Frame 2 │ Frame 3 │ Result      │
├──────┼──────┼─────────┼─────────┼─────────┼─────────┼─────────────┤
│  1   │  1   │    1    │    -    │    -    │    -    │ FAULT ❌    │
│  2   │  2   │    1    │    2    │    -    │    -    │ FAULT ❌    │
│  3   │  3   │    1    │    2    │    3    │    -    │ FAULT ❌    │
│  4   │  4   │    1    │    2    │    3    │    4    │ FAULT ❌    │
│  5   │  1   │    1    │    2    │    3    │    4    │ HIT   ✅    │
│  6   │  2   │    1    │    2    │    3    │    4    │ HIT   ✅    │
│  7   │  5   │    5    │    2    │    3    │    4    │ FAULT ❌    │
│  8   │  1   │    5    │    1    │    3    │    4    │ FAULT ❌    │
│  9   │  2   │    5    │    1    │    2    │    4    │ FAULT ❌    │
│ 10   │  3   │    5    │    1    │    2    │    3    │ FAULT ❌    │
│ 11   │  4   │    4    │    1    │    2    │    3    │ FAULT ❌    │
│ 12   │  5   │    4    │    5    │    2    │    3    │ FAULT ❌    │
├──────┴──────┴─────────┴─────────┴─────────┴─────────┼─────────────┤
│                            FIFO 4 Frames = 10 faults ← MORE FAULTS │
└─────────────────────────────────────────────────────────────────────┘
```

```
  Belady's Anomaly Summary
  ┌──────────────┬──────────────┬──────────────┐
  │  Algorithm   │   3 Frames   │   4 Frames   │
  ├──────────────┼──────────────┼──────────────┤
  │  FIFO        │  9 faults    │  10 faults   │  ← ANOMALY (more frames = more faults)
  │  LRU         │  8 faults    │   6 faults   │  ← NORMAL  (more frames = fewer faults)
  └──────────────┴──────────────┴──────────────┘

  FIFO: Adding 1 frame caused +1 extra fault  [BUG IN FIFO]
  LRU:  Adding 1 frame saved  -2 faults       [CORRECT BEHAVIOUR]
```

---

<a name="algorithm-comparison"></a>
## Algorithm Comparison

### Head-to-Head Property Table

| Property | FIFO | LRU | Optimal (OPT) |
|:---|:---:|:---:|:---:|
| Eviction Rule | Oldest loaded | Least recently used | Furthest future use |
| Belady's Anomaly | Affected | Immune | Immune |
| Implementation | Simple queue | Counter / stack | Not implementable |
| Hardware Support Needed | None | Reference bits | Future knowledge |
| Temporal Locality | Ignored | Exploited | Exploited |
| Page Faults (example 8 refs, 3 frames) | 7 | 6 | 5 (theoretical) |
| Hit Rate (example) | 12.5% | 25.0% | 37.5% (theoretical) |
| Complexity | O(1) | O(n) | N/A |

### Visual Fault Comparison

```
  Page Faults (Reference: 7 0 1 2 0 3 0 4, Frames: 3)
  ════════════════════════════════════════════════════

  10 ┤
   9 ┤
   8 ┤
   7 ┤  ████████████████
   6 ┤  ████████████████  ██████████████
   5 ┤  ████████████████  ██████████████
   4 ┤  ████████████████  ██████████████
   3 ┤  ████████████████  ██████████████
   2 ┤  ████████████████  ██████████████
   1 ┤  ████████████████  ██████████████
     └──────────────────────────────────────
             FIFO              LRU
             (7)               (6)

       ↑ Lower bar = Better  ↑

   FIFO hit rate:  1/8 = 12.5%  ████░░░░░░░░░░░░░░░░
   LRU  hit rate:  2/8 = 25.0%  ████████░░░░░░░░░░░░
```

---

<a name="address-translation"></a>
## Address Translation

```
╔══════════════════════════════════════════════════════════════════════╗
║              LOGICAL  →  PHYSICAL  ADDRESS  TRANSLATION             ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║   CPU  ──── generates ────►  Logical Address                         ║
║                              │                                       ║
║                         ┌────┴────────────────────┐                 ║
║                         │  Split by Page Size      │                 ║
║                         │  Logical = 350           │                 ║
║                         │  Page Size = 100 bytes   │                 ║
║                         │                          │                 ║
║                         │  Page No = 350 ÷ 100 = 3 │                 ║
║                         │  Offset  = 350 mod 100= 50│                ║
║                         └────┬────────────────────┘                 ║
║                              │                                       ║
║                              ▼                                       ║
║                         Page Table                                   ║
║                    ┌───────────────────┐                             ║
║                    │  Page 0 → Frame 2 │                             ║
║                    │  Page 1 → Frame 0 │                             ║
║                    │  Page 2 → Frame 4 │                             ║
║                    │  Page 3 → Frame 1 │  ← lookup Page 3           ║
║                    └───────────────────┘                             ║
║                              │  Frame = 1                            ║
║                              ▼                                       ║
║   Physical Address = (Frame × Page Size) + Offset                   ║
║                    = (  1   ×    100   ) +   50                      ║
║                    =   150                                           ║
║                                                                      ║
║   Result: Logical 350  →  Physical 150                              ║
╚══════════════════════════════════════════════════════════════════════╝
```

### Translation Formula

```
  ┌────────────────────────────────────────────────────────────┐
  │                                                            │
  │   Page Number  =  floor( Logical Address  ÷  Page Size )  │
  │   Offset       =         Logical Address mod Page Size     │
  │                                                            │
  │   Physical Address  =  (Frame Number × Page Size)          │
  │                     +   Offset                             │
  │                                                            │
  └────────────────────────────────────────────────────────────┘
```

### Worked Examples

| Logical Address | Page Size | Page No | Offset | Frame | Physical Address |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `100` | 100 | 1 | 0 | 0 | **0** |
| `350` | 100 | 3 | 50 | 1 | **150** |
| `275` | 100 | 2 | 75 | 4 | **475** |
| `0` | 100 | 0 | 0 | 2 | **200** |
| `499` | 100 | 4 | 99 | 3 | **399** |

---

<a name="features"></a>
## Features

| Feature | Details |
|:---|:---|
| Dual Interface | Full **CLI** terminal mode OR **Tkinter GUI** window — selected at startup |
| FIFO Simulation | Queue-based replacement with step-by-step HIT/FAULT trace printed per access |
| LRU Simulation | Counter-based tracking; evicts stale page with detailed trace output |
| Bar Graph | Matplotlib pop-up comparing FIFO vs LRU page fault counts side by side |
| Address Translation | Takes logical addresses + page size, outputs physical addresses with formula |
| Hit Rate Report | Calculates and displays efficiency percentage for each algorithm |
| Study Materials | Includes formal project report, viva Q&A guide, and output explanation doc |

---

<a name="project-structure"></a>
## Project Structure

```
OS-Paging-Virtual-Memory-Simulation/
│
├── paging_simulator.py     ←  Core application (CLI + GUI in one file)
│                               ├─ simulate_fifo()     FIFO replacement engine
│                               ├─ simulate_lru()      LRU replacement engine
│                               ├─ translate_address() Logical → Physical
│                               ├─ plot_comparison()   Matplotlib bar chart
│                               └─ run_gui()           Tkinter window
│
├── requirements.txt        ←  Python dependencies  (matplotlib)
│
├── PROJECT_REPORT.md       ←  Formal report: Abstract → System Analysis → Conclusion
├── VIVA_QUESTIONS.md       ←  Common viva Q&A for OS exam prep
├── OUTPUT_GUIDE.md         ←  Explains every line of simulator output in detail
└── README.md               ←  This file
```

---

<a name="installation"></a>
## Installation

### Prerequisites

| Tool | Version | Notes |
|:---|:---:|:---|
| Python | 3.x | [python.org/downloads](https://python.org/downloads) |
| pip | Latest | Bundled with Python 3 |
| matplotlib | Latest | Graph generation |
| tkinter | Built-in | No install required — ships with Python |

### Setup Steps

```bash
# 1. Clone the repository
git clone https://github.com/RishvinReddy/OS-Paging-Virtual-Memory-Simulation.git

# 2. Enter the project folder
cd OS-Paging-Virtual-Memory-Simulation

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the simulator
python paging_simulator.py
```

---

<a name="usage-and-modes"></a>
## Usage and Modes

### Startup Menu

```
╔══════════════════════════════════════════╗
║   Paging and Virtual Memory Simulator   ║
╠══════════════════════════════════════════╣
║                                          ║
║   1.  CLI  (Command Line Interface)      ║
║   2.  GUI  (Graphical User Interface)    ║
║   3.  Exit                               ║
║                                          ║
║   Enter your choice (1-3):  _            ║
╚══════════════════════════════════════════╝
```

### Mode 1 — CLI

```
  Enter page reference string : 7 0 1 2 0 3 0 4
  Enter number of frames      : 3

  Running FIFO...
  ──────────────────────────────────────────
  Page  7  FAULT   Memory: [7]
  Page  0  FAULT   Memory: [7, 0]
  Page  1  FAULT   Memory: [7, 0, 1]
  Page  2  FAULT   Memory: [0, 1, 2]   (evicted: 7)
  Page  0  HIT     Memory: [0, 1, 2]
  Page  3  FAULT   Memory: [1, 2, 3]   (evicted: 0)
  Page  0  FAULT   Memory: [2, 3, 0]   (evicted: 1)
  Page  4  FAULT   Memory: [3, 0, 4]   (evicted: 2)
  ──────────────────────────────────────────
  Total Faults: 7   Hits: 1   Hit Rate: 12.50%
```

### Mode 2 — GUI

```
  ┌────────────────────────────────────────────────────────┐
  │   Paging and Virtual Memory Simulator                  │
  ├────────────────────────────────────────────────────────┤
  │                                                        │
  │   Page Reference String:  [ 7 0 1 2 0 3 0 4        ]  │
  │   Number of Frames:       [ 3                       ]  │
  │                                                        │
  │   [ Run FIFO ]    [ Run LRU ]    [ Show Graph ]        │
  │                                                        │
  ├────────────────────────────────────────────────────────┤
  │   Output                                               │
  │   ────────────────────────────────────────────────     │
  │   Page 7  FAULT   Memory: [7]                          │
  │   Page 0  FAULT   Memory: [7, 0]                       │
  │   Page 1  FAULT   Memory: [7, 0, 1]                    │
  │   Page 2  FAULT   Memory: [0, 1, 2]                    │
  │   Page 0  HIT     Memory: [0, 1, 2]                    │
  │   ...                                                  │
  │   Total Faults: 7   Hit Rate: 12.50%                   │
  └────────────────────────────────────────────────────────┘
```

### Mode 2 — Graph Output

```
  A Matplotlib pop-up window appears:

  ┌─────────────────────────────────────────┐
  │   Page Fault Comparison                 │
  │                                         │
  │  8 ┤                                    │
  │  7 ┤  ███                               │
  │  6 ┤  ███  ███                          │
  │  5 ┤  ███  ███                          │
  │  4 ┤  ███  ███                          │
  │  3 ┤  ███  ███                          │
  │  2 ┤  ███  ███                          │
  │  1 ┤  ███  ███                          │
  │    └──────────────                      │
  │       FIFO  LRU                         │
  │       (7)   (6)                         │
  └─────────────────────────────────────────┘
```

---

<a name="full-sample-walkthrough"></a>
## Full Sample Walkthrough

**Reference String:** `7 0 1 2 0 3 0 4` · **Frames:** `3`

<details>
<summary><strong>FIFO Full Output</strong></summary>

<br>

```
Reference String : 7  0  1  2  0  3  0  4
Algorithm        : FIFO
Frames           : 3
────────────────────────────────────────────────────────
Step 1   Page 7   FAULT    Memory: [ 7 ]
Step 2   Page 0   FAULT    Memory: [ 7, 0 ]
Step 3   Page 1   FAULT    Memory: [ 7, 0, 1 ]
Step 4   Page 2   FAULT    Memory: [ 0, 1, 2 ]    evicted: 7
Step 5   Page 0   HIT      Memory: [ 0, 1, 2 ]
Step 6   Page 3   FAULT    Memory: [ 1, 2, 3 ]    evicted: 0
Step 7   Page 0   FAULT    Memory: [ 2, 3, 0 ]    evicted: 1
Step 8   Page 4   FAULT    Memory: [ 3, 0, 4 ]    evicted: 2
────────────────────────────────────────────────────────
Total Faults : 7    Hits : 1    Hit Rate : 12.50%
```

</details>

<details>
<summary><strong>LRU Full Output</strong></summary>

<br>

```
Reference String : 7  0  1  2  0  3  0  4
Algorithm        : LRU
Frames           : 3
────────────────────────────────────────────────────────
Step 1   Page 7   FAULT    Memory: [ 7 ]
Step 2   Page 0   FAULT    Memory: [ 7, 0 ]
Step 3   Page 1   FAULT    Memory: [ 7, 0, 1 ]
Step 4   Page 2   FAULT    Memory: [ 0, 1, 2 ]    evicted: 7  (LRU)
Step 5   Page 0   HIT      Memory: [ 0, 1, 2 ]    0 refreshed
Step 6   Page 3   FAULT    Memory: [ 0, 2, 3 ]    evicted: 1  (LRU)
Step 7   Page 0   HIT      Memory: [ 0, 2, 3 ]    0 refreshed
Step 8   Page 4   FAULT    Memory: [ 0, 3, 4 ]    evicted: 2  (LRU)
────────────────────────────────────────────────────────
Total Faults : 6    Hits : 2    Hit Rate : 25.00%
```

</details>

---

<a name="performance-analysis"></a>
## Performance Analysis

```
  ┌────────────────────────────────────────────────────────────┐
  │                  FINAL SCORE SUMMARY                       │
  ├────────────────┬──────────────┬──────────────┬────────────┤
  │  Algorithm     │  Page Faults │  Page Hits   │  Hit Rate  │
  ├────────────────┼──────────────┼──────────────┼────────────┤
  │  FIFO          │     7        │     1        │   12.50%   │
  │  LRU           │     6        │     2        │   25.00%   │
  │  OPT (theory)  │     5        │     3        │   37.50%   │
  ├────────────────┼──────────────┼──────────────┼────────────┤
  │  Winner        │    LRU       │    LRU       │    LRU     │
  └────────────────┴──────────────┴──────────────┴────────────┘

  Why LRU beats FIFO here:
  → Page 0 is accessed at Step 5 (HIT under both).
  → At Step 6, FIFO still treats 0 as old (entered early) → evicts it.
  → LRU sees 0 was just refreshed at Step 5 → keeps it, evicts 1.
  → This saves exactly 1 fault, and doubles the hit rate.
  → Root cause: temporal locality of page 0.
```

---

<a name="glossary"></a>
## Glossary

<details open>
<summary><strong>Core OS and Memory Management Terms</strong></summary>

<br>

| Term | Definition |
|:---|:---|
| **Virtual Memory** | OS abstraction that lets processes use more memory than physically exists in RAM |
| **Paging** | Divides both logical and physical memory into equal fixed-size chunks (pages / frames) |
| **Page** | Fixed-size block of a process's logical address space |
| **Frame** | Fixed-size block of physical RAM — same size as a page |
| **Page Fault** | Interrupt raised when the CPU requests a page not currently resident in RAM |
| **Page Table** | OS data structure mapping each page number to its physical frame number |
| **MMU** | Memory Management Unit — hardware that performs logical-to-physical address translation |
| **Logical Address** | Address generated by the CPU: composed of Page Number and Offset |
| **Physical Address** | Actual memory address in RAM: Frame Number combined with Offset |
| **Demand Paging** | Pages are only loaded into RAM when first accessed, not at process startup |
| **Page Replacement** | Process of choosing a victim page to evict when RAM is full |
| **FIFO** | Evicts the page that has been resident in RAM the longest |
| **LRU** | Evicts the page that was accessed least recently |
| **Belady's Anomaly** | FIFO defect: more frames can paradoxically cause more page faults |
| **Temporal Locality** | A page used recently is statistically very likely to be used again soon |
| **Spatial Locality** | Pages near a recently accessed address are also likely to be accessed soon |
| **Working Set** | The set of pages actively being used by a process within a time window |
| **Thrashing** | Pathological state where the system spends more time paging than executing code |
| **Dirty Page** | A modified page that must be written back to disk before its frame is reused |
| **OPT / Optimal** | Theoretical algorithm that evicts the page used furthest in the future — not implementable |

</details>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=130&section=footer&text=Operating%20Systems%20PBL%20%E2%80%94%20Woxsen%20University&fontSize=15&fontColor=a0a0ff&fontAlignY=65&animation=fadeIn" width="100%" alt="footer"/>

**Built with Python · FIFO · LRU · Address Translation · Tkinter · Matplotlib**

</div>
