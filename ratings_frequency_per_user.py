from itertools import groupby, chain
import collections

import matplotlib.pyplot as plt
import numpy as np

import plotly.plotly as py
# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api


def flatten(listOfLists):
    return list(chain.from_iterable(listOfLists))


def calculate_time_diffs(user, ratings):
    result = []
    current = 0
    last = len(ratings) - 1
    while current < last:
        diff = ratings[current + 1] - ratings[current]
        result.append(diff)
        current += 1
    return result


with open("resources/ratings.csv") as source_file:
# with open("resources/ratings_middle.csv") as source_file:
    lines = source_file.readlines()
    split_lines = map(lambda line: line.replace("\n", "").split(","), lines)
    user_time_pairs = map(lambda split_line: (split_line[0], split_line[3]), split_lines)
    grouped_by_user = {}
    for user_id, items in groupby(user_time_pairs, lambda x: x[0]):
        sorted_timestamps = list(sorted(map(lambda x: long(x[1]), list(items))))

        grouped_by_user[user_id] = sorted_timestamps
    # counter = collections.Counter(split_lines)

    time_diffs = flatten(map(lambda x: calculate_time_diffs(x[0],x[1]), grouped_by_user.iteritems()))
    print("calculate counter")
    counter = collections.Counter(time_diffs)
    a = sorted([('abc', 121),('abc', 231),('abc', 148), ('abc',221)], key=lambda x: x[1])
    with open("results/ratings_frequency_stats.csv", mode="w") as result_file:
        result_file.write("time_diff,count\n")

        for x, y in sorted(counter.items(), key=lambda x: x[0]):
            result_file.write(str(x) + "," + str(y) + "\n")
    print("finished")

