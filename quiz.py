name = input('welcome to my awsome quiz game where your skills are put to the test. \n Enter your name for the record: ')
caps_name = name.title()
ip_number_high = 4294967296
ip_number_low = 1111111111
correct_one = 'Assur'
print(str(caps_name) )
game_mode = input('... thats an interesting name \n do you want easy or hard mode? ')
caps_game_mode = game_mode.title()
if caps_game_mode == 'Easy':
 answer_one = input('Easy it is then \n question #1 \n ---------------- \n what is the capital of assyria? ') 
if answer_one == correct_one:
  print('correct!')
elif caps_game_mode == 'Hard':
  answer_one_hard = input('Hard it is then \n question #1 \n ---------------- \n what is your ip address? (no spaces or commas between the numbers) ')
  if int(answer_one_hard) <= (ip_number_high) and int(answer_one_hard) >= (ip_number_low):
    print('correct!')
  else: print('wrong')
  answer_two_hard = input('question #2 \n ---------------- \n what is an example of a red fruit?: ')
  if (answer_two_hard.title()) == ('strawberry') or ('rhasberry') or ('cherry') or ('apple'):
    print('correct!')
    answer_three_hard = input('question #3 \n ---------------- \n is fortnite a good game? ')
    if answer_three_hard.capitalize == ('yes') or ('no'):
      print('correct!')
      answer_four_hard = input('question #4 \n ---------------- \n what is the name of the first computer? ')
      if answer_four_hard.capitalize == ('Analytical engine'):
        print("correct")



    else: print('so you don\'t want to play then.')
if answer_one != correct_one.capitalize():
  print('correct great job!')
else: print('wrong')
answer_two = input('question #2 \n ---------------- \n what is your age? ') 
if answer_two >= 1 and answer_two <= 116:
    print('good job!')
else: print('incorrect')  
