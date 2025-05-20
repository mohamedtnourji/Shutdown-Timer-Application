import os
import tkinter as tk
import platform

def shutdown(minutes=0):
    system_platform = platform.system()
    
    if system_platform == "Windows":
        # Windows uses seconds for the timer
        os.system(f"shutdown /s /t {minutes * 60}")
    elif system_platform == "Darwin":  # macOS
        if minutes == 0:
            os.system("sudo shutdown -h now")
        else:
            os.system(f"sudo shutdown -h +{minutes}")
    elif system_platform == "Linux":
        if minutes == 0:
            os.system("shutdown now")
        else:
            os.system(f"shutdown +{minutes}")
    else:
        print("Unsupported OS")

# Create a Tkinter window
window = tk.Tk()
window.title("Shutdown Timer")
window.geometry("300x200")

# Add a label
label = tk.Label(window, text="Select shutdown time:")
label.pack(pady=10)

# Create a frame for buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# Create buttons for different timer options
now_button = tk.Button(button_frame, text="Now", command=lambda: shutdown(0))
min10_button = tk.Button(button_frame, text="10 Minutes", command=lambda: shutdown(10))
min20_button = tk.Button(button_frame, text="20 Minutes", command=lambda: shutdown(20))
min30_button = tk.Button(button_frame, text="30 Minutes", command=lambda: shutdown(30))

# Pack buttons side by side
now_button.pack(side=tk.LEFT, padx=5)
min10_button.pack(side=tk.LEFT, padx=5)
min20_button.pack(side=tk.LEFT, padx=5)
min30_button.pack(side=tk.LEFT, padx=5)

# Add a cancel button to abort shutdown
def cancel_shutdown():
    system_platform = platform.system()
    
    if system_platform == "Windows":
        os.system("shutdown /a")
    elif system_platform == "Darwin":  # macOS
        os.system("sudo killall shutdown")
    elif system_platform == "Linux":
        os.system("shutdown -c")
    else:
        print("Unsupported OS")

cancel_button = tk.Button(window, text="Cancel Shutdown", command=cancel_shutdown, bg="red", fg="white")
cancel_button.pack(pady=20)

# Run the Tkinter event loop
window.mainloop()
