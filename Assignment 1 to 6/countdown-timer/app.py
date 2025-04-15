
# import time

# # Function to run countdown timer
# def countdown_timer(seconds):
#     while seconds > 0:
#         mins, secs = divmod(seconds, 60)  # Minutes aur seconds calculate karna
#         time_format = '{:02d}:{:02d}'.format(mins, secs)  # MM:SS format
#         print(time_format, end='\r')  # Timer display
#         time.sleep(1)  # 1 second ka delay
#         seconds -= 1

#     print("00:00 \nTime's Up!")

# # User input
# try:
#     total_seconds = int(input("Enter time in seconds for countdown: "))
#     countdown_timer(total_seconds)
# except ValueError:
#     print("Please enter a valid number.")







# Project 5 : Count Down Timer
import time
import os
import sys

def clear_console():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown_timer(seconds):
    clear_console()
    print("⏳ Countdown Timer Started!\n")
    
    try:
        while seconds >= 0:
            mins, secs = divmod(seconds, 60)
            time_format = f"{mins:02d}:{secs:02d}"
            print(f"\r⏱️  Time Remaining: {time_format}", end="")
            time.sleep(1)
            seconds -= 1
        print("\n\n✅ Time's Up!")
    except KeyboardInterrupt:
        print("\n\n⛔ Timer Interrupted.")

def main():
    while True:
        clear_console()
        print("=== 🕒 Python Countdown Timer ===\n")
        user_input = input("Enter time in seconds (or type 'exit' to quit): ")

        if user_input.lower() in ['exit', 'quit', 'q']:
            print("\n👋 Exiting... Have a productive day!")
            break

        if not user_input.isdigit():
            print("\n⚠️  Please enter a valid number.")
            time.sleep(2)
            continue

        seconds = int(user_input)
        countdown_timer(seconds)
        input("\n🔁 Press Enter to set a new timer...")

if __name__ == "__main__":
    main()

