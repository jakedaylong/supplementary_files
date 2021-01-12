# functional programming
def remove_last_item(mylist):
    """Removes the last item from a list."""
    mylist.pop(-1)  # This modifies mylist


# vs.


def butlast(mylist):
    return mylist[:-1]  # This returns a copy of mylist


# ------


def doit(file):
    print(file)


files = ["a.csv", "b.csv"]

map(doit, files)
