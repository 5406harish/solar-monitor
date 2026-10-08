import tkinter as tk
from tkinter import ttk, messagebox
import requests
import time
import threading
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation

# ================== CHANGE THIS ==================
ESP_IP = "192.168.137.60"        # ←←← PUT YOUR ESP32 IP HERE
# ================================================

root = tk.Tk()
root.title("Solar Panel Live Monitor - Harish")
root.geometry("700x600")
root.configure(bg="#f0f0f0")

# Title
tk.Label(root, text="🌞 Solar Panel Live Monitoring System", 
         font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)

# Live Values
v_label = tk.Label(root, text="Voltage: -- V", font=("Arial", 16), bg="#f0f0f0")
v_label.pack(pady=5)
i_label = tk.Label(root, text="Current: -- mA", font=("Arial", 16), bg="#f0f0f0")
i_label.pack(pady=5)
p_label = tk.Label(root, text="Power: -- W", font=("Arial", 16), bg="#f0f0f0")
p_label.pack(pady=5)

# Log Area
log_text = tk.Text(root, height=12, width=80, font=("Consolas", 10))
log_text.pack(pady=10, padx=10)

# Plot
fig, ax = plt.subplots(figsize=(6, 3.5))
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(pady=10, padx=10)

x_data, v_data, i_data = [], [], []
line_v, = ax.plot([], [], label="Voltage (V)", color="blue", linewidth=2)
line_i, = ax.plot([], [], label="Current (mA)", color="green", linewidth=2)
ax.set_xlabel("Time (seconds)")
ax.set_ylabel("Value")
ax.legend()
ax.grid(True)

def update_gui():
    try:
        r = requests.get(f"http://{ESP_IP}/data", timeout=2)
        data = r.json()
        
        v = data["voltage"]
        i = data["current"]
        p = data["power"]
        
        v_label.config(text=f"Voltage: {v} V")
        i_label.config(text=f"Current: {i} mA")
        p_label.config(text=f"Power: {p} W")
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_text.insert("end", f"{timestamp} | V: {v}V | I: {i}mA | P: {p}W\n")
        log_text.see("end")
        
        # Auto save to CSV
        with open("solar_log.csv", "a", newline="") as f:
            csv.writer(f).writerow([timestamp, v, i, p])
            
        return v, i, p
        
    except Exception as e:
        v_label.config(text="Voltage: Error")
        i_label.config(text="Current: Error")
        p_label.config(text="Power: Error")
        log_text.insert("end", f"[{datetime.now().strftime('%H:%M:%S')}] Connection Error - Check ESP32 IP/WiFi\n")
        log_text.see("end")
        return 0, 0, 0

def periodic_update():
    while True:
        update_gui()
        time.sleep(1)

def animate(frame):
    try:
        v_str = v_label["text"].split(": ")[1].replace(" V", "")
        i_str = i_label["text"].split(": ")[1].replace(" mA", "")
        
        current_v = float(v_str) if v_str.replace(".", "").isdigit() else 0
        current_i = float(i_str) if i_str.replace(".", "").isdigit() else 0
        
        x_data.append(frame)
        v_data.append(current_v)
        i_data.append(current_i)
        
        # Keep only last 60 points
        if len(x_data) > 60:
            x_data.pop(0)
            v_data.pop(0)
            i_data.pop(0)
        
        line_v.set_data(x_data, v_data)
        line_i.set_data(x_data, i_data)
        ax.relim()
        ax.autoscale_view()
    except:
        pass
    return line_v, line_i

# Start everything
ani = FuncAnimation(fig, animate, interval=1000, blit=False, cache_frame_data=False)

threading.Thread(target=periodic_update, daemon=True).start()

# Buttons
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Save Log Now", command=lambda: messagebox.showinfo("Saved", "All data saved in solar_log.csv")).pack(side="left", padx=10)
tk.Button(btn_frame, text="Clear Log", command=lambda: log_text.delete(1.0, tk.END)).pack(side="left", padx=10)

# Initial message
log_text.insert("end", "Waiting for ESP32... Make sure ESP32 is powered ON and connected to same WiFi.\n")
log_text.insert("end", f"Target IP: {ESP_IP}\nChange ESP_IP in the code if needed.\n\n")

root.mainloop()