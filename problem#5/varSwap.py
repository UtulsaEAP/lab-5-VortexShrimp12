
def swap_values(user_val1, user_val2, user_val3, user_val4):   
   #write your code here
   one = user_val1
   three = user_val3
   user_val1 = user_val2
   user_val2 = one
   user_val3 = user_val4
   user_val4 = three
   return user_val1, user_val2, user_val3, user_val4

if __name__ == '__main__':   
   user_input1 = int(input())
   user_input2 = int(input())
   user_input3 = int(input())
   user_input4 = int(input())
   #store output for every input here
   #print those output

   print(swap_values(user_input1, user_input2, user_input3, user_input4))

 