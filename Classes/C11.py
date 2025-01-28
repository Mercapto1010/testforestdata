# nums = [4,5,8,56,58]
# it = iter(nums)
# print(it.__next__())
# print(it.__next__())
# print(next(it))

class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self
    
    def __next__(self):

        if self.num <= 10:
            vals = self.num
            self.num += 1
            return vals
        else:
            raise StopIteration
        
values = TopTen()
print(next(values))
for i in values:
    print(i)