class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        current_max = 0
        
        element_array = self.__elements
        for i in range(len(element_array)):
            for j in range(len(element_array)):
                # print("i: ", i, "j: ", j)
                diff = abs(element_array[j] - element_array[i])
                if diff > current_max:
                    current_max = diff
        self.maximumDifference = current_max
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)