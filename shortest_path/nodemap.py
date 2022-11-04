import random
from node import Node


class NodeMap():
    def __init__(self, nodes: dict, start_node: str, max_retries: int) -> None:
        self.nodes = nodes
        self.node = start_node
        self.path = start_node
        self.value = 0
        self.requirements = nodes.keys()
        self.max_retries = max_retries

    def cycle(self, node):
        pass

    def follow_path(self, node=None, is_random=True):
        if not node:
            node = self.start
        siblings = self.nodes[node]
        amount_siblings = len(siblings)
        if is_random:
            goto = random.randint(0, amount_siblings - 1)
            index = 0
            for sib_node, value in siblings.items():
                if index == goto:
                    self.path += sib_node
                    self.value += value
                    self.node = sib_node
                index += 1

    def is_resolved(self):
        for node in self.requirements:
            if node not in self.path:
                return False
        return True

    def start(self, node):
        if not self.is_resolved():
            self.follow_path(node)
            self.start(self.node)
            return {"path": self.path, "value": self.value}
        else:
            print("out")
