#!/usr/bin/env python3

from itertools import combinations
import math

def main():

    ##  Probabilities in independent probability spaces.

    R = (0.55, 0.42, 0.25, 0.24, 0.18, 0.17, 0.14, 0.12, 0.11, 0.11, 0.06)

    S = tuple(map(
        lambda r: r / sum(R),
        R
    ))
    
    print(S)

    print(f"New probability space: {sum(S)}")

    # S = (0.1, 0.2, 0.3)
    
    n = 2

    all_combs = gen_all_combs(S)

    all_events = gen_all_events(S, all_combs)

    if len(all_events) == len(all_combs):

        p = sum(
            tuple(
                map(
                    lambda e: math.prod(e), all_events
                    )
            ))

    else:

        print("Event calculation error")

    print(f"Final probability: {p}")

    
def gen_all_combs(S: tuple[float]) -> tuple[tuple[float]]:

    all_combs = ()

    for i in range(1, len(S)):

        all_combs = all_combs + tuple(combinations(S, i))

    return all_combs


def gen_all_events(S: tuple[float], all_combs: tuple[tuple[float]]) -> tuple[tuple[float]]:

    all_events = ()

    ##  To calculate the probability of A n B in a probability space
    ##  {A, B, C}, take the product of {A, B, ~C}.

    for comb in all_combs:

        comb_inv = negate_probabilities(
            tuple(set(S) - set(comb))
            )

        event = comb + comb_inv

        all_events = all_events + (event,)

    return all_events

        

def negate_probabilities(s: tuple[int]):

    s_inv = ()

    for i in s:

        s_inv = s_inv + (1 - i,)

    return s_inv
    

main()
