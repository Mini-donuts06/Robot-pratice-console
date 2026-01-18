import tkinter as tk

# create the main window
window = tk.Tk()
window.title("Robot Console")
window.geometry("500x400") # width x height

# Create the output area
output_area = tk.Text(window, height =15, width=60)
output_area.pack(pady=10)

# Create the input box
input_box = tk.Entry(window, width = 50)
input_box.pack(pady = 10)

# Define the function BEFORE using it in the button
def sub_command():
    command = input_box.get()
    input_box.delete(0, tk.END)    # clears input box
    
    # For now, just echo the command 
    output_area.insert(tk.END, f"You: {command}\n")
    output_area.insert(tk.END, f"Robot: You said '{command}'\n\n")
    output_area.see(tk.END)  # auto-scroll to the bottom

# Create the button the calls the function
submit_button = tk.Button(window, text="Send", command=sub_command)
submit_button.pack()

# Run the window loop
window.mainloop()
