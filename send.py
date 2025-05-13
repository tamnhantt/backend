import serial
import time
import threading
import tkinter as tk

# Cấu hình UART
port = '/dev/ttyS0'  # Cổng Serial trên Raspberry Pi
baudrate = 115200

# Biến điều khiển
running = False  # Đang gửi dữ liệu hay không
data_value = 1   # Giá trị dữ liệu gửi (1 hoặc 0)
thread = None    # Luồng gửi dữ liệu

# Hàm gửi dữ liệu liên tục
def send_data_to_stm32():
    global running, data_value
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        print(f"Serial port {port} opened successfully.")

        while running:
            ser.write(str(data_value).encode())  # Gửi '1' hoặc '0'
            print(f"Data sent: {data_value}")
            time.sleep(1)  # Gửi mỗi giây
        
        ser.close()
        print("Serial port closed.")
    except serial.SerialException as e:
        print(f"Error: {e}")

# Điều khiển chuyển đổi giữa 1 ↔ 0
def toggle_transmission():
    global running, data_value, thread

    if not running:
        # Nếu đang tắt → Bật gửi
        running = True
        thread = threading.Thread(target=send_data_to_stm32, daemon=True)
        thread.start()
    else:
        # Nếu đang gửi → Chuyển đổi giữa 1 và 0
        data_value = 1 if data_value == 0 else 0

    # Cập nhật nút bấm
    button.config(text=f"Send {1 if data_value == 0 else 0}")

# Giao diện Tkinter
root = tk.Tk()
root.title("Serial Transmission Control")

button = tk.Button(root, text="Send 1", command=toggle_transmission, width=20, height=2)
button.pack(pady=20)

root.mainloop()
