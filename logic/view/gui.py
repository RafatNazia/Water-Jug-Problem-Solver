import tkinter as tk
from tkinter import messagebox
from logic.solver import bfs

class WaterJugGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Water Jug Problem Solver")

        tk.Label(self.root, text="Jug 1 Capacity").pack()
        self.cap1 = tk.Entry(self.root)
        self.cap1.pack()

        tk.Label(self.root, text="Jug 2 Capacity").pack()
        self.cap2 = tk.Entry(self.root)
        self.cap2.pack()

        tk.Label(self.root, text="Target").pack()
        self.target = tk.Entry(self.root)
        self.target.pack()

        tk.Button(
            self.root,
            text="Solve",
            command=self.solve
        ).pack(pady=10)

        self.result = tk.Text(self.root, height=15, width=40)
        self.result.pack()

    def solve(self):
        try:
            c1 = int(self.cap1.get())
            c2 = int(self.cap2.get())
            target = int(self.target.get())

            path = bfs(c1, c2, target)

            self.result.delete("1.0", tk.END)

            if path:
                for step in path:
                    self.result.insert(tk.END, str(step) + "\n")
            else:
                messagebox.showinfo("Result", "No Solution Found")

        except:
            messagebox.showerror("Error", "Enter valid numbers")

    def run(self):
        self.root.mainloop()
