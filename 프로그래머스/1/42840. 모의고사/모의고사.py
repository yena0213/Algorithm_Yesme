def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0] #각 수포자들의 점수
    answer = []
    
    for i in range(0, len(answers)):
        if(answers[i] == one[i%len(one)]):
            score[0] +=1
        if(answers[i] == two[i%len(two)]):
            score[1] +=1
        if(answers[i] == three[i%len(three)]):
            score[2] +=1

    no1 = max(score)
    
    for i in range(len(score)):
        if no1 == score[i]:
            answer.append(i+1)
    
    return answer