def show_args(*args):
    print(args)
show_args(1, 2, 3)


def sum_args(*args):
    print(sum(args))
sum_args(4, 5)


def last_arg(*args):
    print(args[-1])
last_arg(10, 20, 30)


def multiply_args(*args):
    result = 1
    for x in args:
        result *= x
    print(result)
multiply_args(2, 3, 4)


def args_to_list(*args):
    print(list(args))
args_to_list(7, 8, 9)


def get_value(**kwargs):
    print(kwargs.get("name"))
get_value(name="Sara", age=25)


def count_kwargs(**kwargs):
    print(len(kwargs))
count_kwargs(a=1, b=2, c=3)


def kwargs_keys_list(**kwargs):
    print(list(kwargs.keys()))
kwargs_keys_list(p=1, q=2)


def only_numbers(*args):
    for x in args:
        print(x)
only_numbers(5, 6, 7)


def sum_and_count(*args):
    print(sum(args), len(args))
sum_and_count(2, 4, 6)
