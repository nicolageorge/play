# we have an array of inputs which defines heights of walls. Find the container with the largest area within all
def largest_container(inputs):
    left, right = 0, len(inputs)-1
    max_left, max_right, max_area = None, None, 0

    while left < right:
        area = min( inputs[left], inputs[right] ) * (right-left)
        if max_area < area:
            max_area = area
            max_left = left
            max_right = right

        if inputs[left] < inputs[right]:
            left += 1
        else:
            right -= 1

    print max_area, max_left, max_right

inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
largest_container(inputs)
