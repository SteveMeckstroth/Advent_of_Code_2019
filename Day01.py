import math

inputs = """98435
61869
123694
51157
70664
107632
60289
140493
135101
89758
142578
63389
126315
133069
139989
121089
148127
117475
65718
129198
98612
67678
79752
97930
141835
80575
125798
114298
139861
75550
64724
76315
71871
132949
117877
57157
93756
113889
60388
145810
86668
94498
50502
106789
119505
65341
60103
75963
104149
134483
92833
102273
56988
74202
69016
110217
132242
87186
95704
88433
56225
60206
70508
62692
143847
70088
129908
133319
104284
108627
106977
107696
59576
76422
115945
137414
83299
138678
108034
140276
74857
143726
116028
101970
84298
133544
116069
77564
91964
57954
121404
54416
83370
74842
91677
65323
82036
138725
95805
112490"""

modules = [int(i) for i in inputs.splitlines()]


def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return int(math.floor(n * multiplier) / multiplier)


def calc_module_fuel(mass):

    fuel = round_down((mass / 3) - 2)
    return fuel


fuel_counter_upper = 0

for i in modules:
    total_fuel = calc_module_fuel(i)
    remaining_fuel_required = total_fuel

    finished = False
    while not finished:
        added_fuel = calc_module_fuel(remaining_fuel_required)
        if added_fuel > 0:
            total_fuel = total_fuel + added_fuel
            remaining_fuel_required = added_fuel
        else:
            finished = True

        print("{0} : {1} : {2}".format(i, added_fuel, total_fuel))
    fuel_counter_upper = fuel_counter_upper + total_fuel

print(fuel_counter_upper)
