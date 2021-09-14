#
# Dutch National Flag
# in-place
def dutch_flag_sort(balls):
    r = -1  # red pointer
    g = -1  # green pointer
    i = 0  # current pointer

    while (i < len(balls)):

        if balls[i] == 'G':
            g += 1
            balls[i], balls[g] = balls[g], balls[i]

        elif (balls[i] == "R"):
            g += 1
            balls[i], balls[g] = balls[g], balls[i]

            r += 1
            balls[g], balls[r] = balls[r], balls[g]
        i += 1 