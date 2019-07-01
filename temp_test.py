from collections import Counter, OrderedDict

keyword_list = ['this', 'that', 'this', 'twice', 'again',
                'something', 'this', 'that', 'once', 'twice',
                ]

y = dict(Counter(x[0] for x in keyword_list if x))
print(keyword_list[0])