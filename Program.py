import sys

//lowest_num function
//parameters: array of numbers (negative is accepted)
//returns: integer of lowest postive number that is not included in the array
def lowest_num(array):
        greatest_num = sys.maxsize
        for num in array:
                if abs(num) < greatest_num and is_in_array(array, abs(num)+1) == False:
                        greatest_num = abs(num)+1
        return greatest_num

//is_in_array function
//parameters: array of numbers and integer
//returns: true if number is in array, false if otherwise
def is_in_array(nums, num):
        for n in nums:
                if n == num:
                        return True
        return False

def main():
        //this can be any number
        nums = [0,2,1]
        print lowest_num(nums)


if __name__ == "__main__":
        main()
