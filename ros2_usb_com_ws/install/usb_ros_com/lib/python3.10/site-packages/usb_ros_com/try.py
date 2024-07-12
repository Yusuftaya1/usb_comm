import serial
import time

# UART bağlantısını başlatın
uart_port = '/dev/ttyUSB0'  # Belirlenen doğru portu kullanın
baud_rate = 115200

try:
    ser = serial.Serial(uart_port, baud_rate)
except serial.SerialException as e:
    print(f"Could not open port {uart_port}: {e}")
    exit()

# İlk aşama: [1000, 1000] -> [0, 0]
for i in range(1000, -1, -10):
    data = [i, i]
    data_str = ','.join(map(str, data)) + '\n'
    ser.write(data_str.encode())
    print(f"Sent: {data_str.strip()}")
    time.sleep(0.5)

    data = [i, i]
    data_str = ','.join(map(str, data)) + '\n'
    ser.write(data_str.encode())
    print(f"Sent: {data_str.strip()}")
    time.sleep(0.5)

# UART bağlantısını kapatın
ser.close()

