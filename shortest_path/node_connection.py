class NodeConnection():
    def __init__(self, base_node: str, end_node: str, value: int) -> None:
        self.base_node = base_node
        self.end_node = end_node
        self.value = value

    def alter_node(self, node):
        if node == self.base_node:
            return self.end_node
        else:
            return self.base_node

    def follow_path(self, actual_node):
        return {
            "new_node": self.alter_node(actual_node),
            "value": self.value
        }
