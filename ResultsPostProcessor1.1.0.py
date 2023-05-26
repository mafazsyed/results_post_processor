import os
import webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import PhotoImage
from AverageEMinforeachnode import process_files_average_emin
from Auto3mmRadius2 import process_files_auto_3mm_radius

def open_linkedin():
    webbrowser.open_new(r"https://www.linkedin.com/in/mafazsyed")

def open_github():
    webbrowser.open_new(r"https://www.github.com/mafazsyed")

def browse_folder():
    folder = filedialog.askdirectory()
    return folder

def run_average_emin():
    def browse_input_folder():
        input_folder = filedialog.askdirectory()
        input_entry.delete(0, tk.END)
        input_entry.insert(0, input_folder)

    def browse_output_folder():
        output_folder = filedialog.askdirectory()
        output_entry.delete(0, tk.END)
        output_entry.insert(0, output_folder)

    def start_processing():
        input_dir = input_entry.get()
        output_dir = output_entry.get()
        process_files_average_emin(input_dir, output_dir)
        emin_win.destroy()

    emin_win = tk.Toplevel(root)
    emin_win.title("Calculate the Average E. Min. Principal for Each Node")

    emin_frame = ttk.Frame(emin_win, padding="20 20")
    emin_frame.pack()

    emin_label = ttk.Label(emin_frame, text="Average Minimum Principal Strain for Each Node", font=("Calibri", 12, "bold"), justify=tk.CENTER)
    emin_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

    description_label = ttk.Label(emin_frame, text="Calculate the Average E. Min. Principal for Each Node from E. Min. Principal values for Each Node Obtained from Adjacent Elements. Select an Input Folder Containing E. Min. Principal Values for Each Node & Output Folder for Averaged E. Min. Principal value for Each Node.", wraplength=450, justify=tk.CENTER)
    description_label.grid(row=1, column=0, columnspan=2, pady=(0, 10))

    input_label = ttk.Label(emin_frame, text="Input Folder:")
    input_label.grid(row=2, column=0, padx=(0, 10), sticky=tk.W)
    input_entry = ttk.Entry(emin_frame, width=50)
    input_entry.grid(row=2, column=1)
    input_browse_button = ttk.Button(emin_frame, text="Browse", command=browse_input_folder)
    input_browse_button.grid(row=2, column=2, padx=(10, 0))

    output_label = ttk.Label(emin_frame, text="Output Folder:")
    output_label.grid(row=3, column=0, padx=(0, 10), sticky=tk.W)
    output_entry = ttk.Entry(emin_frame, width=50)
    output_entry.grid(row=3, column=1)
    output_browse_button = ttk.Button(emin_frame, text="Browse", command=browse_output_folder)
    output_browse_button.grid(row=3, column=2, padx=(10, 0))

    process_button = ttk.Button(emin_frame, text="Start Processing", command=start_processing)
    process_button.grid(row=4, column=1, pady=(20, 0))

def run_auto_3mm_radius():
    def browse_input_folder():
        input_folder = filedialog.askdirectory()
        input_entry.delete(0, tk.END)
        input_entry.insert(0, input_folder)

    def browse_output_folder_1():
        output_folder = filedialog.askdirectory()
        output_entry_1.delete(0, tk.END)
        output_entry_1.insert(0, output_folder)

    def browse_output_folder_2():
        output_folder = filedialog.askdirectory()
        output_entry_2.delete(0, tk.END)
        output_entry_2.insert(0, output_folder)

    def start_processing():
        input_dir = input_entry.get()
        output_dir_1 = output_entry_1.get()
        output_dir_2 = output_entry_2.get()
        process_files_auto_3mm_radius(input_dir, output_dir_1, output_dir_2)
        auto3mm_win.destroy()

    auto3mm_win = tk.Toplevel(root)
    auto3mm_win.title("Determine Average E. Min. Principal & MFS When Considering Each Node as the Center Node")

    auto3mm_frame = ttk.Frame(auto3mm_win, padding="20 20")
    auto3mm_frame.pack()

    auto3mm_label = ttk.Label(auto3mm_frame, text="Node-Centered E. Min. Principal & MFS Averaging", font=("Calibri", 12, "bold"), justify=tk.CENTER)
    auto3mm_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

    description_label = ttk.Label(auto3mm_frame, text="Determine the Average E. Min. Principal & MFS When Considering Each Node as the Center Node (of 3mm Radius). Select Input Folder Containing Files with Node ID, Node Coordinate, & E. Min. Principal value for Each Node & Output Folders for Simple & Detailed Results.", wraplength=450, justify=tk.CENTER)
    description_label.grid(row=1, column=0, columnspan=2, pady=(0, 10))

    input_label = ttk.Label(auto3mm_frame, text="Input Folder:")
    input_label.grid(row=2, column=0, padx=(0, 10), sticky=tk.W)
    input_entry = ttk.Entry(auto3mm_frame, width=50)
    input_entry.grid(row=2, column=1)
    input_browse_button = ttk.Button(auto3mm_frame, text="Browse", command=browse_input_folder)
    input_browse_button.grid(row=2, column=2, padx=(10, 0))

    output_label_1 = ttk.Label(auto3mm_frame, text="Output Folder 1, for Simple Results:")
    output_label_1.grid(row=3, column=0, padx=(0, 10), sticky=tk.W)
    output_entry_1 = ttk.Entry(auto3mm_frame, width=50)
    output_entry_1.grid(row=3, column=1)
    output_browse_button_1 = ttk.Button(auto3mm_frame, text="Browse", command=browse_output_folder_1)
    output_browse_button_1.grid(row=3, column=2, padx=(10, 0))

    output_label_2 = ttk.Label(auto3mm_frame, text="Output Folder 2, for Detailed Results:")
    output_label_2.grid(row=4, column=0, padx=(0, 10), sticky=tk.W)
    output_entry_2 = ttk.Entry(auto3mm_frame, width=50)
    output_entry_2.grid(row=4, column=1)
    output_browse_button_2 = ttk.Button(auto3mm_frame, text="Browse", command=browse_output_folder_2)
    output_browse_button_2.grid(row=4, column=2, padx=(10, 0))

    process_button = ttk.Button(auto3mm_frame, text="Start Processing", command=start_processing)
    process_button.grid(row=5, column=1, pady=(20, 0))

def about_window():
    about_win = tk.Toplevel(root)
    about_win.title("About")

    about_frame = ttk.Frame(about_win, padding="20 20 20 20")
    about_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    about_label = ttk.Label(about_frame, text="Results Post Processor", font=("Calibri", 12, "bold"))
    about_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

    description_label = ttk.Label(about_frame, text="This application:\n" "Calculates the Average of the E. Min. Principal values produced from Adjacent Elements for Each Node;\nDetermines the Average E. Min. Principal and MFS When Considering Each Node as the Center Node (of a 3mm Radius);\nFor More than One Simulation Result", wraplength=450, justify=tk.CENTER)
    description_label.grid(row=1, column=0, columnspan=2, pady=(0, 10))

    version_label = ttk.Label(about_frame, text="Version: 1.1.0", font=('Calibri', 9, 'italic'))
    version_label.grid(row=2, column=0, columnspan=2, pady=(0, 10))

    created_by_label = ttk.Label(about_frame, text="Created by Mafaz Syed", font=('Calibri', 9, 'italic'))
    created_by_label.grid(row=3, column=0, columnspan=2, pady=(0, 10))

    linkedin_logo = PhotoImage(file=r"C:\Users\mafaz\OneDrive\Desktop\ResultsPostProcessor - Copy\linkedin_logo.png.png")
    linkedin_logo = linkedin_logo.subsample(3)  # Make the image 2 times smaller
    linkedin_button = tk.Button(about_frame, image=linkedin_logo, command=open_linkedin, bd=0) # borderwidth set to 0
    linkedin_button.image = linkedin_logo  # keep a reference
    linkedin_button.grid(row=4, column=0, sticky='e')

    github_logo = PhotoImage(file=r"C:\Users\mafaz\OneDrive\Desktop\ResultsPostProcessor - Copy\github_logo.png.png")
    github_logo = github_logo.subsample(3)  # Make the image 2 times smaller
    github_button = tk.Button(about_frame, image=github_logo, command=open_github, bd=0) # borderwidth set to 0
    github_button.image = github_logo  # keep a reference
    github_button.grid(row=4, column=1, sticky='w')

    close_button = ttk.Button(about_frame, text="Close", command=about_win.destroy)
    close_button.grid(row=5, column=0, columnspan=2, pady=(10, 0))

root = tk.Tk()
root.title("Results Post Processor")

# Use ttk style
style = ttk.Style()
style.theme_use("xpnative") # choose a modern theme
style.configure("TButton", padding=4, relief="flat",)

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

# Add a heading to the application
heading_label = ttk.Label(frame, text="Results Post Processor", font=("Calibri", 12, "bold"))
heading_label.pack()

description_text = ("This application calculates the Average E. Min. Principal values from Adjacent Elements for Each Node, & Determines the Average E. Min. Principal & MFS When Each Node is Considered as the Center Node of a 3mm Radius, for Several Files at the Same Time. Specify Input & Output Folder Paths for Each Task.")
description_label = ttk.Label(frame, text=description_text, wraplength=500, justify=tk.CENTER)
description_label.pack()

btn_average_emin = ttk.Button(frame, text="Calculate the Average E. Min. Principal for Each Node", command=run_average_emin)
btn_average_emin.pack(pady=5)

btn_auto_3mm_radius = ttk.Button(frame, text="Determine the Average E. Min. Principal & MFS When Considering Each Node as the Center Node (of 3mm Radius)", command=run_auto_3mm_radius)
btn_auto_3mm_radius.pack(pady=5)

about_button = ttk.Button(frame, text="About", command=about_window)
about_button.pack(pady=5)

root.mainloop()