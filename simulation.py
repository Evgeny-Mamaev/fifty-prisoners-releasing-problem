import numpy as np
import sys


def main():
    num = int(input("Enter the number of prisoners: "))
    repetitions = int(input("Enter the number of repetitions: "))
    print("Number of prisoners: " + repr(num) + ", number of boxes: " + repr(num * 2))
    counter = 0
    for i in range(repetitions):
        arr = populate(num)
        if approach(arr, num):
            counter += 1
    print("The probability of the relese is:" + repr(counter / repetitions))


def populate(num):
    arr = np.arange(num * 2)
    np.random.shuffle(arr)
    return arr


def approach(arr, num):
    prisoners = np.arange(num)
    np.random.shuffle(prisoners)
    for i in prisoners:
        next_ind = i
        particular = False
        for counter in range(num):
            next_ind = arr[next_ind]
            if next_ind == i:
                particular = True
                break
        if not particular:
            return False
    return True


if __name__ == '__main__':
    sys.exit(main())