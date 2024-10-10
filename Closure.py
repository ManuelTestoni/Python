def create_multiplier(arg1):
    def multiplier(arg1,arg2):
        b = arg1 * arg2
        print(b)

    return multiplier(arg1,6)

create_multiplier(5)

