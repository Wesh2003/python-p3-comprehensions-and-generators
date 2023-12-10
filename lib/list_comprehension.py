#!/usr/bin/env python3

def return_evens(num_list):
    evens_ls = [n for n in num_list if n%2 == 0]
    return evens_ls

def make_exclamation(sentence_list):
    exclam_ls = [x + "!" for x in sentence_list]
    return exclam_ls
    