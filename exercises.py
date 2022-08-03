# EXERCISES
# EXERCISE 1:
# Reverse the list below in-place using an in-place algorithm.
# For extra credit: Reverse the strings at the same time.

words = ['this' , 'is', 'a', 'sentence', '.']
words2 = (lambda w: [w[4], w[3], w[2], w[1], w[0]])(words)
print(words2)



# EXERCISE 2:
# Create a function that counts how many distinct words are in the string below, 
# then outputs a dictionary with the words as the key and the value as the amount
#  of times that word appears in the string.
# Example Output: {'in': 1, 'computing': 1, 'a': 5, ...}
a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

cache = {}
def distinct_words(str):
    expanded = str.lower().split()
    for w in expanded:
        if w not in cache:
            cache[w] = expanded.count(w)
    return cache

print(distinct_words(a_text))


# EXERCISE 3:
# Write a function implementing a Linear Search Algorithm.
# A linear search is a method for finding an element within a list. 
# It sequentially checks each element of the list until a match is found or the whole list has been searched. 
# If you do not find a match, return -1

nums_list = [10,23,45,70,11,15]
target = 70
def linear_search(lst,target):
    for i, num in enumerate(lst):
        if num == target:
            return f"The index for {target} is {i}."
    else:
        return -1

print(linear_search(nums_list, target))

# If number is not present return -1
