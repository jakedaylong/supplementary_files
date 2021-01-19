# Testing

## What are mocks? ?

Mock is a category of so-called test doubles – objects that mimic the
behaviour of other objects. They are meant to be used in tests to replace
real implementation that for some reason cannot be used (e.g. because they
are linked up to external services, like transferring funds or lengthy
database operations).

I create mock objects (even mocks of builtin objects) in order to
check what impacts and calls that the function under test makes on the object.
Being able to track calls and provide known repeatable ‘fake data’ is really
important. This includes mocking out individual files, or even mocking out
entire file systems. 

Essentially when testing a function, you pass it mock
objects in order to prove what happens to the object. A good example of using
mocks is where you want to ensure that the file opens and closes a file
correctly (even under error conditions) - you would pass a mocked file and
then confirm that the file object had either close function called or that the
function used __enter__() and __exit__() (context manager).

## What is patching

Patching is used when you know that the function under test uses some
underlying library or code which is complex in it’s behaviour, and you want
to have known repeatable results. For example you might be testing a function
which your know uses the requests library to get data from a web site. You
can use patching to replace the requests.get() function call with a known mock
object, in order to make the requests.get() call to return known data, or
generate an exception etc


## Note!
Most of the time when you patch something as part of a unit test, you will
patch with a mock object anyway, so they work hand in hand.

## Useful links

https://realpython.com/python-mock-library/

https://medium.com/@yeraydiazdiaz/what-the-mock-cheatsheet-mocking-in-python-6a71db997832

https://bhch.github.io/posts/2017/09/python-testing-how-to-mock-requests-during-tests/
