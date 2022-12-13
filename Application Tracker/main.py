import time
import datetime
import win32gui
import bitdotio

# b = bitdotio.bitdotio('api_key')
#
# query_string = """
# SELECT *
# FROM INFORMATION_SCHEMA.TABLES
# WHERE table_type = 'BASE TABLE'
# """
#
# with b.get_connection('nathanpaulbustamante123/DBNPUB') as conn:
#   cur = conn.cursor()
#   cur.execute(query_string)




# Dictionary to keep track of the time spent on each app
app_times = {}
def get_active_app_name():
    # Get the handle of the active window
    active_window = win32gui.GetForegroundWindow()
    # Get the window's title
    title = win32gui.GetWindowText(active_window)
    return title

while True:
    # Get the name of the currently active window
    active_app = get_active_app_name()
    # Check if the app is already in the dictionary
    if active_app in app_times:
        # If it is, increment the time spent on the app by 1 second
        app_times[active_app] += 1
    else:
        # If it's not, add it to the dictionary with a time of 1 second
        app_times[active_app] = 1
    # Sleep for 1 second before checking the active app again
    time.sleep(1)
    print(app_times)


