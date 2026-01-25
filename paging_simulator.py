import sys
import matplotlib.pyplot as plt

# Check for tkinter availability
try:
    import tkinter as tk
    from tkinter import messagebox
    TKINTER_AVAILABLE = True
except ImportError:
    TKINTER_AVAILABLE = False


# ==========================================
#              CLI IMPLEMENTATION
# ==========================================

def cli_fifo_page_replacement(pages, frames):
    memory = []
    page_faults = 0

    print("\nFIFO Page Replacement")
    print("----------------------")

    for page in pages:
        if page not in memory:
            page_faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            print(f"Page {page} → FAULT | Memory: {memory}")
        else:
            print(f"Page {page} → HIT   | Memory: {memory}")

    return page_faults


def cli_lru_page_replacement(pages, frames):
    memory = []
    recent_use = {}
    page_faults = 0
    time = 0

    print("\nLRU Page Replacement")
    print("----------------------")

    for page in pages:
        time += 1
        if page not in memory:
            page_faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                lru_page = min(recent_use, key=recent_use.get)
                memory.remove(lru_page)
                del recent_use[lru_page]
                memory.append(page)
            print(f"Page {page} → FAULT | Memory: {memory}")
        else:
            print(f"Page {page} → HIT   | Memory: {memory}")

        recent_use[page] = time

    return page_faults


def cli_plot_graph(fifo_faults, lru_faults):
    algorithms = ['FIFO', 'LRU']
    faults = [fifo_faults, lru_faults]

    plt.figure()
    plt.bar(algorithms, faults)
    plt.xlabel('Page Replacement Algorithm')
    plt.ylabel('Number of Page Faults')
    plt.title('FIFO vs LRU Page Fault Comparison')
    plt.show()


def cli_address_translation(frames):
    logical_addresses = list(map(int, input("\nEnter logical addresses: ").split()))
    page_size = int(input("Enter page size: "))

    page_table = {}
    memory = []
    frame_number = 0

    print("\n🔁 Address Translation")
    print("----------------------")

    for addr in logical_addresses:
        page = addr // page_size
        offset = addr % page_size

        if page not in page_table:
            if len(memory) < frames:
                page_table[page] = frame_number
                memory.append(page)
                frame_number += 1
            else:
                removed_page = memory.pop(0)
                del page_table[removed_page]
                page_table[page] = frame_number
                memory.append(page)
                frame_number += 1

            print(f"Logical Addr {addr} → Page {page} | PAGE FAULT")
        else:
            print(f"Logical Addr {addr} → Page {page} | HIT")

        physical_addr = page_table[page] * page_size + offset
        print(f"   Physical Address: {physical_addr}")


def run_cli():
    print("\n🔹 Running CLI Mode...")
    pages = list(map(int, input("Enter page reference string: ").split()))
    frames = int(input("Enter number of frames: "))

    fifo_faults = 0
    lru_faults = 0

    while True:
        print("\n📘 Paging Simulator Menu")
        print("1. FIFO Page Replacement")
        print("2. LRU Page Replacement")
        print("3. FIFO vs LRU Graph")
        print("4. Address Translation")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            fifo_faults = cli_fifo_page_replacement(pages, frames)
            print(f"FIFO Page Faults: {fifo_faults}")

        elif choice == "2":
            lru_faults = cli_lru_page_replacement(pages, frames)
            print(f"LRU Page Faults: {lru_faults}")

        elif choice == "3":
            if fifo_faults == 0 and lru_faults == 0:
                print("⚠️ Run FIFO and LRU first!")
            else:
                cli_plot_graph(fifo_faults, lru_faults)

        elif choice == "4":
            cli_address_translation(frames)

        elif choice == "5":
            print("Exiting Paging Simulator. Thank you!")
            break

        else:
            print("❌ Invalid choice. Try again.")


# ==========================================
#              GUI IMPLEMENTATION
# ==========================================

def run_gui():
    if not TKINTER_AVAILABLE:
        print("❌ Tkinter not installed or supported. Please use CLI mode.")
        return

    # Encapsulate GUI state in a closure or class to avoid global pollution
    # Using a class is cleaner but sticking to the functional style requested by user context
    
    # Global state for GUI
    class GuiState:
        fifo_faults = 0
        lru_faults = 0
    
    state = GuiState()

    def get_pages():
        try:
            return list(map(int, pages_entry.get().split()))
        except:
            messagebox.showerror("Error", "Invalid page reference string")
            return None

    def get_frames():
        try:
            return int(frames_entry.get())
        except:
            messagebox.showerror("Error", "Invalid number of frames")
            return None

    def gui_fifo():
        pages = get_pages()
        frames = get_frames()
        if pages is None or frames is None:
            return

        memory = []
        faults = 0
        output = "FIFO Page Replacement\n--------------------\n"

        for page in pages:
            if page not in memory:
                faults += 1
                if len(memory) < frames:
                    memory.append(page)
                else:
                    memory.pop(0)
                    memory.append(page)
                output += f"Page {page} → FAULT | Memory: {memory}\n"
            else:
                output += f"Page {page} → HIT   | Memory: {memory}\n"

        output += f"\nTotal FIFO Page Faults: {faults}"
        result_text.set(output)
        state.fifo_faults = faults

    def gui_lru():
        pages = get_pages()
        frames = get_frames()
        if pages is None or frames is None:
            return

        memory = []
        recent = {}
        faults = 0
        time = 0
        output = "LRU Page Replacement\n--------------------\n"

        for page in pages:
            time += 1
            if page not in memory:
                faults += 1
                if len(memory) < frames:
                    memory.append(page)
                else:
                    lru_page = min(recent, key=recent.get)
                    memory.remove(lru_page)
                    del recent[lru_page]
                    memory.append(page)
                output += f"Page {page} → FAULT | Memory: {memory}\n"
            else:
                output += f"Page {page} → HIT   | Memory: {memory}\n"

            recent[page] = time

        output += f"\nTotal LRU Page Faults: {faults}"
        result_text.set(output)
        state.lru_faults = faults

    def gui_show_graph():
        if state.fifo_faults == 0 or state.lru_faults == 0:
            messagebox.showwarning("Warning", "Run FIFO and LRU first!")
            return

        plt.figure()
        plt.bar(["FIFO", "LRU"], [state.fifo_faults, state.lru_faults])
        plt.xlabel("Algorithm")
        plt.ylabel("Page Faults")
        plt.title("FIFO vs LRU Page Fault Comparison")
        plt.show()

    def gui_address_translation():
        try:
            addresses = list(map(int, logical_entry.get().split()))
            page_size = int(page_size_entry.get())
            frames = get_frames()
            if frames is None: return
        except:
            messagebox.showerror("Error", "Invalid address input")
            return

        page_table = {}
        memory = []
        frame_no = 0
        output = "Address Translation\n-------------------\n"

        for addr in addresses:
            page = addr // page_size
            offset = addr % page_size

            if page not in page_table:
                if len(memory) < frames:
                    page_table[page] = frame_no
                    memory.append(page)
                    frame_no += 1
                    output += f"Logical {addr} → Page {page} | FAULT\n"
                else:
                    removed = memory.pop(0)
                    del page_table[removed]
                    page_table[page] = frame_no
                    memory.append(page)
                    frame_no += 1
                    output += f"Logical {addr} → Page {page} | REPLACED\n"
            else:
                output += f"Logical {addr} → Page {page} | HIT\n"

            physical = page_table[page] * page_size + offset
            output += f"   Physical Address: {physical}\n"

        result_text.set(output)

    # GUI Setup
    print("\n🔹 Running GUI Mode...")
    root = tk.Tk()
    root.title("Paging & Virtual Memory Simulator")
    root.geometry("700x650")

    tk.Label(root, text="Page Reference String (space separated)").pack()
    pages_entry = tk.Entry(root, width=50)
    pages_entry.pack()

    tk.Label(root, text="Number of Frames").pack()
    frames_entry = tk.Entry(root)
    frames_entry.pack()

    tk.Button(root, text="Run FIFO", command=gui_fifo).pack(pady=5)
    tk.Button(root, text="Run LRU", command=gui_lru).pack(pady=5)
    tk.Button(root, text="Show Graph", command=gui_show_graph).pack(pady=5)

    tk.Label(root, text="Logical Addresses (space separated)").pack()
    logical_entry = tk.Entry(root, width=50)
    logical_entry.pack()

    tk.Label(root, text="Page Size").pack()
    page_size_entry = tk.Entry(root)
    page_size_entry.pack()

    tk.Button(root, text="Address Translation", command=gui_address_translation).pack(pady=5)

    result_text = tk.StringVar()
    tk.Label(root, textvariable=result_text, justify="left", anchor="w", font=("Courier", 10)).pack(fill="both", padx=10, pady=10)

    root.mainloop()


# ==========================================
#              MAIN ENTRY
# ==========================================

def main():
    print("====================================")
    print("  Paging & Virtual Memory Simulator")
    print("====================================")
    print("1. CLI (Command Line Interface)")
    print("2. GUI (Graphical User Interface)")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ").strip()

    if choice == '1':
        run_cli()
    elif choice == '2':
        run_gui()
    elif choice == '3':
        print("Goodbye!")
        sys.exit()
    else:
        print("❌ Invalid choice. Please restart.")

if __name__ == "__main__":
    main()
