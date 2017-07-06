def expanded_form(num):
    # num = float(num)
    str = "{}".format(num % 10)
    num = num / 10
    cnt = 10
    while num / 10 > 0:
        str = "{} + {}".format(num % 10 * cnt, str)
        num = num / 10
        cnt = cnt * 10
    str = "{} + {}".format(num % 10 * cnt, str)
    return str

print expanded_form(56849848694165161561561651651657695)
