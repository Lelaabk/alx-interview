#!/usr/bin/python3
"Lock Boxes"


def canUnlockAll(boxes):
    """ Determines if all boxes can be opened. """
    if not boxes:
        return False

    nb = len(boxes)
    seen = set()
    queue = [0]

    while queue:
        had_box = queue.pop(0)
        seen.add(had_box)

        for key in boxes[had_box]:
            if key < nb and key not in seen:
                queue.append(key)

    return len(seen) == nb