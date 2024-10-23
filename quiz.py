name = input('welcome to my awsome quiz game where your skills are put to the test. \n Enter your name for the record: ')
caps_name = name.title()
correct_one = 'Assur'
print(str(caps_name) )
game_mode = input('... thats an interesting name \n do you want easy or hard mode? ')
caps_game_mode = game_mode.title()
if caps_game_mode == 'Easy':
 answer_one = input('Easy it is then \n question #1 \n ---------------- \n what is the capital of assyria? ') 

if answer_one != correct_one.capitalize():
  print('correct great job!')
else: print('wrong')
answer_two = input('question #2 \n ---------------- \n what is your age? ') 
if answer_two >= 1 and answer_two <= 116:
    print('good job!')
else: print('incorrect')   
    
    
    
elif caps_game_mode == 'hard':
answer_one_hard_ = input('hard it is then \n question #1 \n ---------------- ')
else: (print('that is wrong in every way'))
