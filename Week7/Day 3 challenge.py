#1. Ask user for input of text of their choosing

text = input("Enter a text: ")


#2 Ask user for 3 random letters from that text

letter_1 = input("One letter from the text: ")
letter_2 = input("One letter from the text: ")
letter_3 = input("One letter from the text: ")



#3 make the letters lowercase
 
letter_1.lower()
letter_2.lower()
letter_3.lower()

#4 count how many times each letter in the list appears. #display the numbers

text_tuple = tuple(text)
print(text_tuple)

letter_1_counted = text_tuple.count(letter_1)
letter_2_counted = text_tuple.count(letter_2)
letter_3_counted = text_tuple.count(letter_3)

print(f"The total number of {letter_1} characters: {letter_1_counted}")

print(f"The total number of {letter_2} characters: {letter_2_counted}")

print(f"The total number of {letter_3} characters: {letter_3_counted}")

#5 make text into a list



text_list = list(text)
print(text_list)

#6 count how many items in list

print(len(text_list))



#7 index first letter of the text

  
print(text[0])


# 8 index last letter of the text
print(text[-1])
# 9 invert list
print(text[::-1])
# 10 boolean command for python if its in the text

print("python" in text)


