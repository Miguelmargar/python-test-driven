# # def count_upper_case(message):
# # 	count = 0
# # 	for c in message:
# # 		if c.isupper():
# # 			count += 1
# # 	return count
	
	
# # assert count_upper_case("") == 0, "Empty string, should return 0"
# # assert count_upper_case("A") == 1, "A, uppercase so should return 1"
# # assert count_upper_case("AA") == 2, "AA, uppercase should return 2"
# # assert count_upper_case("a") == 0, "a, lower case so should return 0"
# # assert count_upper_case("#") == 0, "# is not a letter, should return 0"
# # assert count_upper_case("Hello") == 1, "String with one uppercase letter, should return 1"
# # assert count_upper_case("Hello World") == 2, "String containing 2 uppercase letters, should return 2"
# # assert count_upper_case("   ") == 0, "String with spaces, should return 0"
	
# # print("All tests pass")


# # the below function is the same as the one on top but in a different way so as to show that tests work with different ways to write the function
# # def count_upper_case(message):
# #     return sum([1 for c in message if c.isupper()])
    
# # assert count_upper_case("") == 0, "Empty string, should return 0"
# # assert count_upper_case("A") == 1, "A, uppercase so should return 1"
# # assert count_upper_case("AA") == 2, "AA, uppercase should return 2"
# # assert count_upper_case("a") == 0, "a, lower case so should return 0"
# # assert count_upper_case("#") == 0, "# is not a letter, should return 0"
# # assert count_upper_case("Hello") == 1, "String with one uppercase letter, should return 1"
# # assert count_upper_case("Hello World") == 2, "String containing 2 uppercase letters, should return 2"
# # assert count_upper_case("   ") == 0, "String with spaces, should return 0"
	
	
# # print("All tests pass")

# # Write a function that accepts a list of numbers and returns True if the list contains an even number of even numbers.
# # This is a relatively simple statement, most program specifications are for more complex. However even a program as simple as this as room for some ambiguity.



# def even_evens(l):
#     count = 0
#     for i in l:
#         if i %2 == 0:
#             count += 1 
            
#     if count == 0:
#         return False
        
#     if count %2 == 0:
#         return True
#     else:
#         return False

# assert even_evens([3]) == False, "Just one number, decided that 0 index is not even so returns False"
# assert even_evens([]) == False, "Empty list should return False"
# assert even_evens([3, 5, 7]) == False, "No even numbers should return False"
# assert even_evens([3, 4, 6]) == True, "Two even numbers in list should return True"
# assert even_evens([2, 4, 6]) == False, "Three even numbers, should return True"
# assert even_evens([2]) == False, "just one even number, should return False, we need an even number of even numbers"

# print("All tests pass")

