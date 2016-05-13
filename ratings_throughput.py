import collections

# with open("../resources/ratings.csv") as f:
with open("resources/ratings.csv") as f:
    lines = f.readlines()
    a = map(lambda line: line.split(",")[3], lines)
    counter = collections.Counter(a)
    print(counter.most_common(3))