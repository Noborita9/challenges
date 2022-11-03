import random


class Node():
    def __init__(self, name: str, siblings: list) -> None:
        self.name = name
        self.siblings = siblings


class NodeMap():
    def __init__(self, nodes: dict, start_node: str) -> None:
        self.nodes = nodes
        self.start_node = start_node
        self.path = ""
        self.value = 0
        self.requirements = nodes.keys()

    def follow_path(self, node=None, is_random=True):
        if not node:
            node = self.start
        siblings = self.nodes[node]
        amount_siblings = len(siblings)
        print("is random")
        if is_random:
            goto = random.randint(0, amount_siblings - 1)
            index = 0
            for sib_node, value in siblings.items():
                print(f"index {index}\nsib_node {sib_node}\nvalue {value}")
                if index == goto:
                    self.path += sib_node
                    self.value += value
                index += 1

    def is_resolved(self):
        for node in self.requirements:
            if node not in self.path:
                return False

        return True

    def start(self):
        counter = 0
        while not self.is_resolved() or counter == 100:
            self.follow_path(self.start_node)
            counter += 1


if __name__ == "__main__":
    nodemap = NodeMap({
        "A": {
            "B": 11,
            "D": 5,
        },
        "B": {
            "A": 11,
            "D": 3,
            "C": 6,
            "E": 2,
        },
        "C": {
            "B": 6,
            "E": 4,
            "F": 7,
        },
        "D": {
            "B": 3,
            "D": 5,
            "E": 12,
            "H": 4,
            "G": 8,
        },
        "E": {
            "B": 2,
            "D": 12,
            "C": 4,
            "F": 5,
            "H": 9,
        },
        "F": {
            "C": 7,
            "E": 5,
            "H": 11,
            "I": 3,
        },
        "G": {
            "H": 9,
            "D": 8,
        },
        "H": {
            "G": 9,
            "E": 9,
            "D": 4,
            "F": 11,
            "I": 10,
        },
        "I": {
            "H": 10,
            "F": 3,
        }
    }, "A")

    nodemap.start()
