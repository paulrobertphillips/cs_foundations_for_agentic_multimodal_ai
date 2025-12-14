reasoning_tree = (
    "root",
    [
        ("idea1", []),
        ("idea2", [
            ("idea2a", [])
        ])
    ]
)

def walk(tree):
    value, children = tree
    print("Visiting:",value)
    for child in children:
        walk(child)


walk(reasoning_tree)