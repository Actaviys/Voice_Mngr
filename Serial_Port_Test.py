import serial.tools.list_ports
import serial
import time

ports = serial.tools.list_ports.comports()

for port in ports:
    print(port.device)
    

port = "COM5"  # Replace with the appropriate COM port name
baudrate = 115200  # Replace with the desired baud rate

ser = serial.Serial(port, baudrate=baudrate)
print("Serial connection established.")
# Perform operations on the COM port

# # # Reading data
# while True:
#     data = ser.read(16)  # Read 10 bytes from the COM port
#     data_str = str(data, "utf-8")
#     print(data.decode())
    
        
a = 10 #Кількість ітерацій
#     # Read data from the Arduino
while True:
    # Read a line of data from the serial port
    line = ser.readline().decode().strip()
    if line:
        print(line)

    command = "0,1"
    # Send the command to the Arduino
    ser.write(command.encode())
    
    
    if a < 0:#Ітератор
        break
    a -= 1

# # Close the serial connection
# ser.close()
