# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def fizzbuzz(n):
    for i in range(n):
        if i % 3 == 0:
            print("fizz")
        if i % 5 == 0:
            print("buzz")
        if i == 7:
            print("gozz")
        else:
            print(i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fizzbuzz(20)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
