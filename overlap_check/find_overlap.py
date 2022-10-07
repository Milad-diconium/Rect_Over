class Point:
    """
    Defines the x and y coordinates of a given point
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y


def do_overlap(points_list):
    """
    verifies whether is there any overlap in a given set of 2D rectangles or not.
    Args:
        points_list (list): List of tuples including x and y coordinates of
        lower left and upper right of a given rectangle.
    Returns:
        bool: either any of given rectangles overlap with each other or not.
    """
    check = 0  # index to check number of none-overlapping rectangles
    length = len(points_list)

    for i in range(length-1):
        for j in range(i+1, length):
            # If one rectangle is on left side of other then they overlap
            if points_list[i][0].x > points_list[j][1].x or points_list[j][0].x > points_list[i][1].x:
                # Then rectangles i and j are alongside each other and do not overlap
                check = check+1
                # Since i and j dont overlap we do not check the 2nd condition and continue with next rectangle
                continue

            # If one rectangle is above another then they overlap
            if points_list[i][1].y < points_list[j][0].y or points_list[j][1].y < points_list[i][0].y:
                # Then rectangles i and j are above each other and do not overlap
                check = check+1

    # the number of all comparisons are 2 choose n which is n*(n-1)/2
    # if none of them overlap then check variable must be n*(n-1)/2
    if check == (length*(length-1))/2:
        # None of the rectangles overlap
        return False
    else:
        # Overlapping occurs
        return True
