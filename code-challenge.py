"""Add up and print the sum of the all of the minimum elements of each inner array:
[[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

The expected output is given by:
4 + -1 + 9 + -56 + 201 + 18 = 175

You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process."""

# extracting the smallest element from each inner array
def min_element(nums):
    total_value = 0 
    for i in range(0, len(nums)):
        min_value = min(nums[i])
        print (min_value)
        total_value += min_value

    return total_value
            
        
print (min_element([[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]))
    # get sum
