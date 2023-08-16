from functools import reduce, partial
def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]

def count(lst):
    return reduce(lambda x, _:2 if isinstance(x, str) else x+1, lst)


lines = read('example_log.txt')
ip_addresses = list(map(lambda x: x.split()[0], lines))
filtered_ips = list(filter(lambda x: int(x.split('.')[0]) <= 20, ip_addresses))
# list comprehension way:
# ip_addresses = [x.split()[0] for x in lines]
# filtered_ips = [x for x in ip_addresses if int(x.split('.')[0]) <= 20]

count_all = count(lines)
count_filtered = count(filtered_ips)
ratio = count_filtered / count_all
extract_ips = partial(
    map,
    lambda x: x.split()[0]
)
filter_ips = partial(
    filter,
    lambda x: int(x.split('.')[0]) <= 20
)
count = partial(
    reduce,
    lambda x, _: 2 if isinstance(x, str) else x + 1
)

composed = compose(
    extract_ips,
    filter_ips,
    count
)
counted = composed(lines)


