#!/usr/bin/env python3


def calc_cost(failure_cost: dict[str, int],
              failure_rate_lookup: dict [int, float],
              category_cost_ratio: dict[int, list[float]]):

    cost = 0

    for cat, fr in failure_rate_lookup.items():

        for i, r in enumerate(category_cost_ratio[cat]):

            cost += fr * r * failure_cost[i]

    return cost
            

failure_cost = {
    0: 500,
    1: 5000,
    2: 15000
}

failure_rate_lookup = {
    1: 1.080,
    2: 1.010,
    3: 1.000,
    4: 0.640,
    5: 0.520,
    6: 0.470,
    7: 0.440,
    8: 0.430,
    9: 0.430,
    10: 0.400,
    11: 0.350,
    12: 0.350,
    13: 0.240,
    14: 0.220,
    15: 0.190,
    16: 0.185,
    17: 0.180,
    18: 0.130,
    19: 0.070
}

category_cost_ratio = {
    1: [0.001, 0.179, 0.824],
    2: [0.001, 0.042, 0.812],
    3: [0.095, 0.321, 0.485],
    4: [0.154, 0.038, 0.395],
    5: [0.001, 0.010, 0.456],
    6: [0.000, 0.006, 0.407],
    7: [0.002, 0.016, 0.358],
    8: [0.002, 0.054, 0.326],
    9: [0.001, 0.054, 0.355],
    10: [0.000, 0.004, 0.373],
    11: [0.000, 0.070, 0.247],
    12: [0.000, 0.043, 0.278],
    13: [0.001, 0.038, 0.182],
    14: [0.000, 0.007, 0.190],
    15: [0.001, 0.006, 0.162],
    16: [0.000, 0.089, 0.092],
    17: [0.005, 0.081, 0.076],
    18: [0.000, 0.001, 0.108],
    19: [0.001, 0.003, 0.052]
}

print(
    calc_cost(failure_cost, failure_rate_lookup, category_cost_ratio)
    )
