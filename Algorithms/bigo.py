#Big O notation (time/space complexity)
#how we measure and compare efficiency of algorithms
#Common Big-O values:
#O(1) - constant space/time
#O(n) - linear space/time
#O(log n) - logarithmic space/time (merge and conquer) 
#O(n^2) - quadratic space/time (nested loops)

#Example: O(n) time 
# where n is the number of items in list 
list = [1, 5, 6, 7, 8, 10, 11]
#this runs in O(n) time - proportional to the input (n)
for num in list:
    print(num)

#Example: O(n^2) time
nested_list = [[1,2,3], [3,5,7], [1,4,7]]

#this runs in O(n^2) time because for each input
#there is a nested operation
for list in nested_list:
    for num in list:
        print(num)




