import tkinter as tk

# window
window = tk.Tk()
window.title("Pavan's App")
window.minsize(width=500, height=300)

# Label component
my_label = tk.Label(text="I am a label", font=("Ariel", 12, "italic"))
my_label.pack(anchor='w')


# keep last 
window.mainloop()