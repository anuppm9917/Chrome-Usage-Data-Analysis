import os
import csv
import time
from datetime import datetime
from win32gui import GetWindowText, GetForegroundWindow


# Function to get the active window title
def get_active_window_title():
    window_title = ""
    window_handle = GetForegroundWindow()
    window_title = GetWindowText(window_handle)
    return window_title

# Function to track Chrome application usage
def track_chrome_usage(duration):
    start_time = time.time()  # Record the start time
    chrome_apps = ["Gmail", "Netflix", "Jovian", "Github", "LinkedIn", "ChatGPT", "Whatsapp", "YouTube"]
    csv_file = "D:\Python\Chrome Usage\chrome_usage.csv"

    # Create CSV file if it doesn't exist
    if not os.path.exists(csv_file):
        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Time", "Application"])

    while True:
        current_window = get_active_window_title()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        current_date = datetime.now().strftime("%Y-%m-%d")

        for app in chrome_apps:
            if app.lower() in current_window.lower():
                with open(csv_file, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([current_date, current_time, app])
                print(f"{current_time}: {app} opened.")
               
    
        # Check if the elapsed time exceeds the specified duration
        if time.time() - start_time >= duration:
            break

        time.sleep(3600)  # Check every 1 hour


if __name__ == "__main__":
    try:
        track_chrome_usage(360)
    except KeyboardInterrupt:
        print("\nTracking stopped.")
