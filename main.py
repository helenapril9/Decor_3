from decor_logger import path_log
import os
import sys

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]
@path_log(sys.argv[0])
def flat_generator(nl):
    for l in nl:
        for i in l:
            yield i

for item in  flat_generator(nested_list):
	print(item)



