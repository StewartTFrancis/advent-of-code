import json

def part1():
    with open('day12.txt', 'r') as file:
        data = json.load(file)

        total = 0

        for num in iter_all_nums(data):
            total += num
        
        print (total)

def iter_all_nums(data):
    if isinstance(data, dict):
        for _, val in data.items():
            for item in iter_all_nums(val):
                yield item
    elif isinstance(data, list):
        for val in data:
            for item in iter_all_nums(val):
                yield item
    elif isinstance(data, int):
        yield data
        
def iter_all_nums2(data):
    if isinstance(data, dict):
        if 'red' in [v for k, v in data.items()]:
            return 0
        for _, val in data.items():
            for item in iter_all_nums2(val):
                yield item
    elif isinstance(data, list):
        for val in data:
            for item in iter_all_nums2(val):
                yield item
    elif isinstance(data, int):
        yield data

def part2():
    with open('day12.txt', 'r') as file:
        data = json.load(file)

        total = 0

        for num in iter_all_nums2(data):
            total += num
        
        print (total)
        

part1()
part2()