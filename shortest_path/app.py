from nodemap import NodeMap


if __name__ == "__main__":
    with open("results.txt", "w+") as file:
        for iter in range(100):
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
                    "A": 5,
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
            result = nodemap.start("A")
            print(result)
            stringify = f"Path = {result['path']} , value = {result['value']}\n"
            file.write(stringify)
