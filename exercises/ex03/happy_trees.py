"""Drawing forests in a loop."""

__author__ = "730318770"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
if depth > 0:
    print((TREE * depth))
    depth = depth - 1
