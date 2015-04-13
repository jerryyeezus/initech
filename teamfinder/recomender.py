import itertools
import math
import numpy

__author__ = 'yee'


# Given map of member->answer-vector and my answer-vector, compute covariance score
def cf_map(team_answers_map, my_answer_vec):
    result = [0] * len(team_answers_map.values()[0])
    for vector in team_answers_map.values():
        for i, val in enumerate(vector):
            if val is not None:
                result[i] += list(val)[0].value

    for i, val in enumerate(result):
        result[i] = round(float(val) / len(team_answers_map.values()), 2)
    my_answer_vec = [0 if x is None else x.value for x in my_answer_vec]
    best = [5] * len(my_answer_vec);
    worst = [0] * len(my_answer_vec);
    baseline = math.sqrt(sum((best[k] - worst[k]) ** 2 for k in range(len(my_answer_vec))))
    return 100 * round(
        1 - math.sqrt(sum((my_answer_vec[k] - result[k]) ** 2 for k in range(len(my_answer_vec)))) / baseline, 3)

    # return numpy.cov(result, my_answer_vec)[0, 1] # higher iz better


# Return average pearson covariance between team members given a team
def cf(teams):
    sum = 0
    for i in list(itertools.combinations(range(len(teams)), 2)):
        sum += -numpy.cov([1 + x for x in teams[i[0]]],
                          [1 + x for x in teams[i[1]]])[0, 1]
    return sum / len(teams)


def dist(cf):
    return 3 + round(2 * cf)
