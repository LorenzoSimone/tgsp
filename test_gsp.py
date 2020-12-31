from gsp import *

dataset =  [
    [["a"], ["a", "b", "c"], ["a", "c"], ["c"]],
    [["a"], ["c"], ["b", "c"]],
    [["a", "b"], ["d"], ["c"], ["b"], ["c"]],
    [["a"], ["c"], ["b", "c"]]
]
timestamps = [
              [1, 3, 4, 5],
              [1, 7, 20],
              [1, 3, 6, 7,9],
              [1, 3, 4],
]

print('----Dataset----')
for c in dataset:
    print(c)

print('----Timestamps----')
for c in timestamps:
    print(c)

result_set, rules, freq = apriori(dataset,timestamps, minSupport = 2, minGap = 1, maxGap = 3, minInterval = 10, verbose=False)
