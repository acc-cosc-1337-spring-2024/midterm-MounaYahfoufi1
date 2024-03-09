#write functions here, don't add input('') statements here!
def get_sum_of_evens(num):
    sum_evens = sum(number for number in range(2, num+1, 2))
    return sum_evens
