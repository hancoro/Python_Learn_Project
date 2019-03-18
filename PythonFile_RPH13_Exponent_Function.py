
# this is a function that accepts 2 parameters


def raise_to_the_power_of(base_num, pow_num):
    result = 1
    for num in range(pow_num):
        result = result * base_num
        # print(num)
    return result


print(raise_to_the_power_of(3, 3))
