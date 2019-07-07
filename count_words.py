from collections import Counter

keyword_list = ['this', 'that', 'this', 'twice', 'again',
                'something', 'this', 'that', 'once', 'twice',
                ]

y = dict(Counter(x for x in keyword_list if x))
print(y)