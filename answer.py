def isIncreasing(nums):
    if (sorted(nums) == nums):
        return True
    else:
        return False


def numconvert(nums):
  x = nums[0]
  y = nums[1]
  z = nums[2]
  a = []
  for c in nums:
    a = [x,y,z]

  result = ''
  for x in a:
    result = result + str(x) 
  return result


def binconvert(bin_1):
  result=0
  val=1
  for i in bin_1[::-1]:
    if i == "1":
      result += val
    val = val * 2
  
  return result

def tests():
  print("Question 1: will have a list of numbers and tell you if the numbers are continuously increasing or decreasing.")
  print(isIncreasing([1,2,3,4]))
  print(isIncreasing([1,2,5,3,4]))
  print(isIncreasing([1,2,3,4,0]))
  print("Question 2:Will take a list of multiple numbers and create it into one integer")
  print(numconvert([3,5,1]))
  print(numconvert([8,9,1]))
  print("Question 3: The code will convert a binary value into a integer")
  print(binconvert("100"))
  print(binconvert("1011"))

if __name__ == "__main__":
  tests()