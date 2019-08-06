def cuboid_diff(a, b):
    if len(a) > 3 or len(b) > 3:
        return('The length of one or both of the lists are more than 3')
    else:
        vol_a = int(a[0] * a[1] * a[2])
        vol_b = int(b[0] * b[1] * b[2])
        if vol_a > vol_b:
            return('The difference in volumes is {}'.format(vol_a - vol_b))
        elif vol_b > vol_a:
            return('The difference in volumes is {}'.format(vol_b - vol_a))
        else:
            return('The volumes are the same and the differece is 0')


a = [2, 7, 4]
b = [2, 3, 5]
print(cuboid_diff(a, b))
