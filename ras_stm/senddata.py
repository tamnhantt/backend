import serial
import time
import threading    
import tkinter as tk

port = '/dev/ttyS0'
baudrate = 115200

running = False
data_value = 1
thread = None

def send_data_to_stm32():
    global running, data_value
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        print(f"Serial port {port} opened successfully.")

        while running:
            ser.write(str(data_value).encode())
            print(f"Data sent: {data_value}")
            time.s  leep(1)  # Gửi mỗi giây
        
        ser.close()
        print("Serial port closed.")
    except serial.SerialException as e:
        print(f"Error: {e}")

def toggle_transmission():
    global running, data_value, thread

    if not running:
        running = True
        thread = threading.Thread(target=send_data_to_stm32, daemon=True)
        thread.start()
    else:
        data_value = 1 if data_value == 0 else 0

    button.config(text=f"Send {1 if data_value == 0 else 0}")

root = tk.Tk()
root.title("Serial Transmission Control")

button = tk.Button(root, text="Send 1", command=toggle_transmission, width=20, height=2)
button.pack(pady=20)

root.mainloop()