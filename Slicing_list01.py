def main(numbers):
    """
    A list called numbers is given. Return the items in the even index.
    Args:
        numbers(list): parameter
    Returns:
        list: return answer.
    """
    return  numbers[::2] #list(map(lambda x :x if numbers.index(x)%2==0 else ,numbers))
print(main([1,2,3,4,5,6,7]))