print('Welcome to Maths for Kids')
print('Level 1')

# list of questions and answers
questions = [('What is 1 + 1?', '2'),
             ('What is 2 + 2?', '4'),
             ('What is 2 + 1?', '3'),
             ('What is 3 + 3?', '6'),
             ('What is 3 + 2?', '5'),
             ('What is 4 + 4?', '8'),
             ('What is 4 + 3?', '7'),
             ('What is 5 + 5?', '10'),
             ('What is 5 + 4?', '9'),
             ('What is 6 + 6?', '12'),
             ('What is 7 + 7?', '14'),
             ('What is 6 + 4?', '10'),
             ('What is 8 + 7?', '15'),
             ('What is 8 + 8?', '16'),
             ('What is 9 + 9?', '18'),
             ('What is 10 + 10?', '20'),
             ('What is 7 + 6?', '13'),
             ('What is 9 + 7?', '16')]

num_errors = 0  # error counter

# loop for all the questions in the level
for i, (question, answer) in enumerate(questions):
    
    # loop for one question
    while True:
        user_input = input(question)
        if user_input == answer:
            print('Correct! Well done!')
            break
        else:
            num_errors += 1
            if num_errors == 2:
                print('Game over. You have used all your attempts.')
                if i != 4:
                    print('Press b to restart the level ')
                    choice = input().lower()
                    if choice == 'b':
                        print('Starting level again...')
                        num_errors = 0
                        break
                    else:
                        print('Press d to quit')
                        choice=input().lower()
                        if choice=='d':
                            quit()
                
                   
            else:
                print(f'Sorry, that is incorrect. You have {2-num_errors} attempt(s) left.')

print('Congratulations! You have completed Level 1.')









