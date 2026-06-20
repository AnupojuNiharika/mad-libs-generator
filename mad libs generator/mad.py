import tkinter as tk
from tkinter import messagebox
import random

def generate_story():
    name = name_entry.get()
    place = place_entry.get()
    animal = animal_entry.get()
    adjective = adjective_entry.get()
    verb = verb_entry.get()

    if not all([name, place, animal, adjective, verb]):
        messagebox.showwarning("Warning", "Please fill all fields!")
        return

    stories = [
        f"One day {name} went to {place}. There, a {adjective} {animal} appeared. It started to {verb}. Everyone was surprised!",

        f"While visiting {place}, {name} found a {adjective} {animal}. Suddenly it began to {verb} and became famous overnight!",

        f"{name} was walking through {place} when a {adjective} {animal} started to {verb}. It was the funniest thing ever!"
    ]

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, random.choice(stories))

# Main Window
root = tk.Tk()
root.title("Mad Libs Generator")
root.geometry("700x650")
root.configure(bg="#E6F7FF")

# Title
title = tk.Label(
    root,
    text="✨ MAD LIBS GENERATOR ✨",
    font=("Arial", 24, "bold"),
    bg="#E6F7FF",
    fg="#003366"
)
title.pack(pady=15)

# Input Frame
frame = tk.Frame(root, bg="#E6F7FF")
frame.pack()

# Labels and Entries
labels = ["Name", "Place", "Animal", "Adjective", "Verb"]
entries = []

for label in labels:
    tk.Label(
        frame,
        text=label,
        font=("Arial", 12, "bold"),
        bg="#E6F7FF",
        fg="#004080"
    ).pack(pady=3)

    entry = tk.Entry(
        frame,
        width=35,
        font=("Arial", 12)
    )
    entry.pack(pady=3)
    entries.append(entry)

name_entry = entries[0]
place_entry = entries[1]
animal_entry = entries[2]
adjective_entry = entries[3]
verb_entry = entries[4]

# Generate Button
generate_btn = tk.Button(
    root,
    text="Generate Story",
    font=("Arial", 14, "bold"),
    bg="#28A745",
    fg="white",
    padx=10,
    pady=5,
    command=generate_story
)
generate_btn.pack(pady=20)

# Output Label
output_label = tk.Label(
    root,
    text="Generated Story",
    font=("Arial", 14, "bold"),
    bg="#E6F7FF",
    fg="#800000"
)
output_label.pack()

# Output Box
output_text = tk.Text(
    root,
    width=70,
    height=10,
    font=("Calibri", 12),
    bg="white"
)
output_text.pack(pady=10)

root.mainloop()

tk.Button(root, text="Generate Story", command=generate_story).pack(pady=10)

output_text = tk.Text(root, height=10, width=50)
output_text.pack()

root.mainloop()