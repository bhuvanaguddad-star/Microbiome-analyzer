# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 11:19:35 2026

@author: Bhuvana
"""

import analysis as an

t = an.load_data("sample_microbiome_data.csv")
print(an.most_abundant(t))
print(an.diversity_table(t))