name = input('welcome to my awsome quiz game where your skills are put to the test. \n Enter your name for the record: ')
caps_name = name.title()
ip_number_high = 4294967296
ip_number_low = 1111111111
correct_one = 'Assur'
score = 0
print(str(caps_name) )
input_one = input('... thats an interesting name \n question #1 \n ---------------- \n what is the capital of assyria?')
if (input_one).capitalize() == (correct_one):
    score += 1
    print('thats Correct!')
else: 
    print('Incorrect.')
    score -= 1
input_two = input('question #2 \n ---------------- \n what is your ip address? (no spaces or commas between the numbers)')
if int(input_two) >= ip_number_low and int(input_two) <= ip_number_high:
    print('correct!')
    score += 1
else: 
    print('thats Incorrect.')
    score -= 1
input_three = input('question #3 \n ---------------- \n what is an example of a red fruit?: ')
if (input_three).capitalize() == 'Strawberry' or 'Cherry' or 'Rhasberry' or 'Apple':
    print('correct!')
    score += 1
else:
    print('incorrect.')
    score -= 1
input_four = input('what is the airspeed velocity of an unladen swallow (in terms of mph)')
if int(input_four) == 24:
    print('correct!')
    score += 1
else:
    print('wrong!')
    score -=1
print('Thanks for taking the quiz! your final score was ' + str(score) + ' out of 4 points!')
