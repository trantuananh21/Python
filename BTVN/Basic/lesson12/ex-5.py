print('Give the correct answers to get points.')
score = 0

with open('/Users/macbook/Documents/Python/Python/BTVN/Basic/lesson12/question-bank.txt', 'r') as test:
    lines = test.readlines()
    
    for i in lines:
        result = i.split(',')
        ques = result[0]

        # Lấy đáp án
        test_ans = result[1]
        # Output: 3\n
        l_ans = test_ans.split('\n')
        # Output: ['3', '\n']
        final_ans = l_ans[0]
        # Output: 3

        user_input = input(ques)
        if user_input == final_ans:
            score += 1


print(f'== You get {score}/{len(lines)} points ==')