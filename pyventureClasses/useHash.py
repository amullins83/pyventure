from collections import defaultdict


class UseHash(defaultdict):
    def __init__(self):
        self.setdefault(dict)
