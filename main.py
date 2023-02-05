# This is a sample Python script.
from nsepy import get_history
from datetime import date

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import util
import common_fun
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    util.get_histoy_Details()
    # data=get_history(symbol="INFY",start=date(2022,11,2),end=date(2023,2,1))
    # print(data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
