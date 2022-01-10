import numpy as np
from numpy.lib.function_base import select

sentense1 = ['work', 'rise', 'arrive', 'live', 'go', 'come', 'speak', 'reside', 'arise', 'travel', 'happen', 'occur', 'emgerge', 'take place', 'commute', 'function', 'exist', 'disappear', 'appear', 'convene', 'expire',
             'fall', 'differ', 'conclude', 'vary', 'proceed']   # S + V

sentense2 = ['be', 'become', 'remain', 'seem', 'look', 'feel', 'appear', 'stay'] # S + V + C(명사(to / ing) / 형용사)

sentense4 = ['give', 'offer', 'lend', 'show', 'send', 'award', 'grant', 'win', 'assign', 'issue'] # 발행하다.

sentense5adj = ['make', 'find', 'keep', 'consider', 'deem', 'think','leave']

sentense5to = ['request', 'persuade', 'require', 'allow', 'urge', 'expect', 'ask', 'invite', 'enable', 'encourage', 'permit', 'expect', 'advise']


total = set(sentense1 + sentense2 + sentense4 + sentense5adj + sentense5to)
to = [sentense1, sentense2, sentense4, sentense5adj, sentense5to]

total_len = len(total)
total = list(total)
#영단어 출력

expect = {'appear':"1형식 또는 2형식"}
complict = []   #이전 3개의 값

input1 = "1형식"
input2 = "2형식"
input4 = "4형식"
input5 = "5형식 부정사 or 5형식 형용사"
print("*" * 30)
print("|" + input1.center(28, ' ') + "|")
print("|" + input2.center(28, ' ') + "|")
print("|" + input4.center(28, ' ') + "|")
print("|" + input5.center(28, ' ') + "|")
print("*" * 30)

while 1:
    num = np.random.randint(0, total_len)
    if len(complict) == 20:
        del complict[0]
        
    try:
        answer = ['1형식', '2형식', '4형식', '5형식 형용사', '5형식 부정사']
        choice = total[num]
        print(complict)
        if choice in complict:
            continue
        else:
            complict.append(choice)
            
        #문제 제출
        if (choice in expect):
            print(choice + " 동사는 뜻에 따라 다릅니다. 어떻게 다를까요?")
            answer = expect[choice].replace(" ", '')
            
        else:
            for idx, sen in enumerate(to):
                if choice in sen:
                    answer = answer[idx]
            print(choice + "의 영단어는 몇 형식인가요?")
        
        #정답 확인
        data = input()
        data = data.strip()
        data = ''.join(data.split(' '))
        
        if data == answer.replace(" ", ""):
            print("정답입니다.")
        else:
            print("틀렸습니다, 정답은 " + answer + " 입니다.")
        
    except EOFError:
        print("End")
        break
