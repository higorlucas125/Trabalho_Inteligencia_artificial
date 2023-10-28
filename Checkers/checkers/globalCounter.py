class GlobalCounter:
    def __init__(self):
        self.node_count = 0

    def increment(self):
        self.node_count += 1

    def get_count(self):
        return self.node_count