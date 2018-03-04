# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 22:12:48 2016

@author: dsm
"""

from pymining import itemmining, assocrules, seqmining
import time


class freq_mining(object):
    """docstring for ClassName"""
    def __init__(self, transactions, min_sup, min_conf):

        self.transactions = transactions  # database
        self.min_sup = min_sup  # minimum support
        self.min_conf = min_conf  # minimum support

    def freq_items(self):

        relim_input = itemmining.get_relim_input(self.transactions)
        item_sets = itemmining.relim(relim_input, self.min_sup)
        return item_sets

    def association_rules(self):

        item_sets = self.freq_items()
        rules = assocrules.mine_assoc_rules(item_sets, self.min_sup, self.min_conf)
        return rules

    def seqs_mining(self):

        freq_seqs = seqmining.freq_seq_enum(self.transactions, self.min_sup)

        return sorted(freq_seqs)

def main(transactions, min_sup, min_conf):

    item_mining = freq_mining(transactions, min_sup, min_conf)
    #freq_items = item_mining.freq_items()
    #rules = item_mining.association_rules()
    freq_seqs = item_mining.seqs_mining()

    #print freq_items
    print freq_seqs
    #print rules

if __name__ == "__main__":


    transactions = ('caabc', 'abcb', 'cabc', 'abbca')

    min_sup = 2
    min_conf = 0.5

    main(transactions, min_sup, min_conf)






