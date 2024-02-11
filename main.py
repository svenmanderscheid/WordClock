# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import datetime

def get_time():
    now = datetime.now()

    hours = now.strftime("%H")
    minutes = now.strftime("%M")

    print(f'Et ass {hours} an {minutes}')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_time()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
