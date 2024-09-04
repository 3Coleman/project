import serial
import logging
import time

# Configuration settings
SERIAL_PORT = 'COM100'  # Replace with your serial port (e.g., 'COM3' for Windows or '/dev/ttyUSB0' for Linux)
BAUD_RATE = 115200              # Baud rate (should match the device's baud rate)
TIMEOUT = 1                   # Timeout in seconds for read operations
LOG_FILE = 'serial_log.txt'  # Log file name
LOG_DURATION = 20           # Duration to collect logs in seconds

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    start_time = time.time()  # Record the start time

    try:
        # Open the serial port
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=TIMEOUT) as ser:
            print("Serial port opened successfully.")
            logging.info("Serial port opened successfully.")

            while True:
                current_time = time.time()
                elapsed_time = current_time - start_time

                if elapsed_time >= LOG_DURATION:
                    print("Log collection stopped after 20 seconds.")
                    logging.info("Log collection stopped after 20 seconds.")
                    break

                if ser.in_waiting > 0:
                    # Read data from the serial port
                    received_data = ser.readline().decode('utf-8').strip()
                    # Log the received data
                    logging.info(f"Data received: {received_data}")
                    print(f"Data received: {received_data}")

                # Small delay to prevent high CPU usage
                time.sleep(1)

    except serial.SerialException as e:
        logging.error(f"Error opening serial port: {e}")
        print(f"Error opening serial port: {e}")
    except KeyboardInterrupt:
        logging.info("Program terminated by user.")
        print("Program terminated by user.")

if __name__ == "__main__":
    main()
