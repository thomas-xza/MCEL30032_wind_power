#!/usr/bin/env python3

from itertools import combinations
import math

def main():

    S = (0.55, 0.42, 0.25, 0.24, 0.18, 0.17, 0.14, 0.12, 0.11, 0.11, 0.06)

    S = (0.1, 0.2, 0.3)

    n = 2

    all_combs = ()

    for i in range(1, len(S)):

        all_combs = all_combs + tuple(combinations(S, i))

    product = 0

    all_events = ()

    ##  To calculate the probability of A n B in a probability space
    ##  {A, B, C}, take the product of {A, B, ~C}.

    for comb in all_combs:

        print(comb)

        comb_inv = negate_probabilities(
            tuple(set(S) - set(comb))
            )

        event = comb + comb_inv

        all_events = all_events + (event,)

        print(event)

        print("\n\n")        

        product += math.prod(event)

    if len(all_events) == len(all_combs):

        p = sum(
            tuple(
                map(
                    lambda e: math.prod(e), all_events
                    )
            ))

        print(p)

    else:

        print("Event calculation error")

    print(f"Final probability: {p}")


def negate_probabilities(s: tuple[int]):

    s_inv = ()

    for i in s:

        s_inv = s_inv + (1 - i,)

    return s_inv
    

main()
