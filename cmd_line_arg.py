# Command-line argument: input parameters passed to the script when executing them.

import sys

# try:
#     print("Hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")

# if len(sys.argv) < 2:
#     sys.exit("Too few args")
# elif len(sys.argv) > 2:
#     sys.exit("Too many args")

# print("Hello, my name is", sys.argv[1])

if len(sys.argv) < 2:
    sys.exit("Too few args")

for name in sys.argv[
        1:]:  # slices: take a subset of data. start a element at 1 and go to end
    #  and also we can slices from last index by [1:-1]
    print("hello, my name is", name)
