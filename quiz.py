name = input('welcome to my awsome quiz game where your skills are put to the test. \n Enter your name for the record: ')
caps_name = name.title()
correct_one = 'assur' or 'Assur'
print(str(caps_name) )
game_mode = input('... thats an interesting name \n do you want easy or hard mode? ')
caps_game_mode = game_mode.title()
if caps_game_mode == 'Easy':
 answer_one = input('Easy it is then \n question #1 \n ---------------- \n what is the capital of assyria? ') 
elif caps_game_mode == 'hard':
  answer_one_hard_ = input('hard it is then \n question #1 \n ---------------- ')
if answer_one == (correct_one):
   print('correct')
  
else: (print('that is wrong in every way'))


