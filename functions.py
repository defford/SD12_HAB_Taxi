import math
import datetime
import time
import sys

def sumPrevClaims(prevClaims):
    sum = 0
    
    for claim in prevClaims:
        sum += claim
    
    return sum


def PPrint(screenWidth, *args):
    """
    Stands for 'Positional Print'
    Positions multiple text elements along a line.

    *args allows functions to take arguments as they're given: 
        Earch arg is a tuple of variable length. Each tuple contains:
            - content (str): The string to print.
            - position (int or str): The position along the line if an int, or one of 'left', 'right', 'center'.
            - align (str, optional): If position is an int, align can be 'left' or 'right'. Defaults to 'left'.

    Returns the elements along a line specifically positioned.
    """

    line = [' '] * screenWidth  # Creates a list of spaces to build the line

    for content, position, *optional in args:
        if content: 
            align = optional[0] if optional else 'left'
            if isinstance(position, int): 
                start = position if align == 'left' else position - len(content)
            elif position == 'left':
                start = 0
            elif position == 'right':
                start = screenWidth - len(content)
            elif position == 'center':
                start = (screenWidth - len(content)) // 2

            # Insert the content into the line list
            for i, char in enumerate(content):
                if 0 <= start + i < screenWidth:
                    line[start + i] = char
        else:
            print() 


    # Convert list back to string and print
    print(''.join(line))



def FirstNextMonth(date):
    day = 1
    month = date.month
    year = date.year

    # Calculate the new month and year
    if month < 12:
        month += 1

    elif month >= 12:
        month += 1
        month -= 12
        year += 1

    newDate = datetime.datetime(year, month, day)
    
    return newDate

def WaitSave(wait):
    time.sleep(wait)
    print("SAVING...")


# Saving is tied to the progress bar so that both are done at the same time
def ProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█', printEnd="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd, flush=True)
    if iteration == total:
        print()

def SaveToFileBar(message, items, filePath, filePathAlias):
    total_items = len(items)
    suffix = 'Complete'
    length = 50

    with open(filePath, "a") as filePathAlias:
        for i, item in enumerate(items, start=1):
            if i == total_items:
                filePathAlias.write(f"{item}\n")
            else:
                filePathAlias.write(f"{item}, ")
            ProgressBar(i, total_items, prefix=message, suffix=suffix, length=length)
            time.sleep(0.1)

def WaitingMessage(content, space):

    ogContent = content

    seconds = 10
    for dot in range(1, seconds + 1):
        sys.stdout.write('\r' + (" " * space) + content)
        sys.stdout.flush()

        time.sleep(0.2)
        content += "."

        if len(content) > len(ogContent) + 3:
            content = ogContent