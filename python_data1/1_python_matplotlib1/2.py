# -*- coding: utf-8 -*-

# 확률
# 확률은 매우 간단합니다. 주사위로 생각해 봅시다.
# 주사위 1개를 던저 나오는 눈의 수를 생각 할때, 주사위 던지는 조작을 "시행"이라고 합니다.
# 이 시행으로 얻어진 결과 중에서 조건에 맞는 결과 집합을 "사상" 이라고 합니다. 말이 어려우니 저는 "케이스"라고 할게요.
# 만약 홀수가 나오는 케이스라면 시행의 결과가 1, 3, 5 인 눈의 집합이 됩니다.
# 결국 공식을 다음과 같이 정의 할 수 있습니다.
# 확률 P = 문제 삼고 있는 케이스가 일어나는 경우의 수(A) / 일어날 수 있는 모든 경우의 수(U) * 100 (%)
dice = [1, 2, 3, 4, 5, 6]
odd = [1, 3, 5]
oddCase = len(odd) / len(dice)
print('주사위 홀수 나올 확률: ', oddCase * 100, '%')

# 곱사상
# 두 케이스가 있다고 합시다.
# under4 는 4 이하의 눈이 나오는 케이스
# even 은 짝수가 나오는 케이스
# Q. under4 와 even 이 동시에 일어나는 "동시확률" 은 ?
under4 = [1, 2, 3, 4]
even = [2, 4, 6]
under4Case = len(under4) / len(dice)  # under4Case = 4/6
evenCase = len(even) / len(dice)  # evenCase = 3/6
# under4Case * evenCase = 1/3   즉 두개의 케이스가 함께 일어날 확률은 두 케이스를 곱하여 계산합니다.
bothCase = under4Case * evenCase
# A. 결과값 출력
print('under4 와 even 이 동시에 일어날 확률: ', bothCase * 100, '%')

# 조건부 확률
# 어떤 케이스 A 가 일어났다고 하는 조건 아래서 케이스 B 가 일어나는 확률을 "조건부 확률" 이라고 합니다.
# P(B | A) 라고 합니다. (A 가 일어난 후에 B가 일어날 확률)
# Q. 4 이하의 눈이 나왔을 때 그 눈이 짝수 일 확률은? = P(B | A) = 2/4
condition1 = []
for x in under4:  # 4이하의 눈이 나온 모든 경우의 수에서..
    if x in even:  # 짝수만 추려낸 값에 해당할 시..
        condition1.append(x)  # 해당값 추가
condition1Case = len(condition1) / len(under4)
# Q. 짝수의 눈이 나왔을때 그 눈이 4이하일 확률은? = P(A | B) = 2/3
condition2 = []
for x in even:  # 짝수의 눈이 나온 모든 경우의 수에서..
    if x in under4:  # 4이하의 눈만 추려낸 값에 해당할 시..
        condition2.append(x)  # 해당값 추가
condition2Case = len(condition2) / len(even)
# A. 결과값 출력
print('4 이하의 눈이 나왔을 때 그 눈이 짝수 일 확률: ', condition1Case * 100, '%')
print('짝수의 눈이 나왔을때 그 눈이 4이하일 확률: ', condition2Case * 100, '%')

# 베이즈 확률1
# 두개의 상자가 있다고 해보자.
# Q. A 상자에는 빨강색 공 3개와 파랑색 공 7개가 있다. A 상자에서 눈을 감고 하나를 골라내었을 경우 빨강색 공일 경우의 확률은?
A = ['red', 'red', 'red', 'blue', 'blue',
     'blue', 'blue', 'blue', 'blue', 'blue']
red = []
for x in A:
    if 'red' in x:
        red.append('red')
redCase1 = len(red) / len(A)
# A. 결과 : 3/10 = 0.3
print('A 상자에서 눈을 감고 하나를 골라내었을 경우 빨강색 공일 경우의 확률: ', redCase1)
# Q. B 상자가 있다, 빨강색 공 7개와 파랑색 공 3개가 있다. B 상자에서 눈을 감고 하나를 골라내었을 경우 빨강색 공일 경우의 확률은?
B = ['red', 'red', 'red', 'red', 'red',
     'red', 'red', 'blue', 'blue', 'blue']
red = []
for x in B:
    if 'red' in x:
        red.append('red')
redCase2 = len(red) / len(B)
# A. 결과 : 7/10 = 0.7
print('B 상자에서 눈을 감고 하나를 골라내었을 경우 빨강색 공일 경우의 확률: ', redCase2)
# 이 두 경우는 너무 쉽다.
# 하지만 반대로 되면 어떨까?
# 빨강공을 당신에게 주고서, 이 빨간공이 A,B상자 중에서 A상자에서 나왔을 확률을 계산하라고 하면?
# 말문이 막힐거 같다. 그러나 이런 경우에는 베이즈 확률을 사용하여 구할 수 있다.
# P(B|A)를 P(D|H) 로 바꿔서 표현해보면, 원인, 가정인 H(Hypothesis)가 일어날 때 어떤 데이터 D(Data)가 얻어질 확률이 된다.
# P(D|H) = 가능도 : 원인 H가 일어났을때 데이터 D가 얻어질 확률
# P(H|D) = 사후확률 : 데이터 D가 얻어졌을때 그 원인이 H일 확률
# P(H) = 사전확률 : (결과 데이터 D를 얻기 전에)  원인인 H가 성립될 확률
# 여기서는 공식이 중요한게 아니라, 「베이즈 확률이 필요한 경우에 대해 이해」하는게 중요하다.

# 통계를 논할 때 사회조사, 역학조사, 생물통계학 등에 주로 쓰이는 "빈도론"과 계량경제학, 머신러닝 분야에 주로 쓰이는 "베이즈론자"들은
# 확률을 둘러싸고 이론적 대립을 하고 있다.
# 데이터마이닝 머신러닝 분야에서는 "베이즈론"쪽으로 치우치는 경향이 있으므로, 개념 정도는 알아두어야 한다.
# 베이즈 확률로 얻을 수 있는 확률치는 "가능도"와 "사후확률"이다.

# 예1 ) 가능도
# 실생활적으로 생각해보면 음성인식에서 어떤 데이터의 값들이 얻어졌을때 그 원인이 "아" 라고 발음해서인 확률인 것이다.
# 예2 ) 사후확률
# 어느 지역의 기상통계에서 4월 1일 흐릴 확율은 0.6이고, 다음 날인 2일 비가 올 확률은 0.4 였다.
# 또한 1일 날 흐릴 때 다음날 2일에 비가 올 확률은 0.5 이다.
# 이 지역에서 2일에 비가 왔을 때 전날인 1일 날 흐릴 확률은?
# 이런 식으로 "「특정 조건 이후」비 올 확률"을 계산한다.
# 예3 ) 일명 「몬티홀」 문제
# 무한도전에서 박명수는 시민들에게 무작위로 선물을 주기 위해 선물트럭을 몰고 시내로 나갔습니다.
# 트럭에는 3개의 칸막이가 있고, 지나가던 시민은 그 중 하나를 선택하면 그 칸막이 뒤에 있는 선물을 받게 됩니다.
# 하나의 칸막이에는 벤츠자동차가 있으며, 나머지 칸막이에는 각각 박명수, 유재석의 사인 카드가 있습니다.
# 일단 시민이 칸막이 A를 선택했고, 박명수는 나머지 칸막이 중 자동차가 없는 칸막이 하나(B)를 보여 주며 긴장감을 고조 시킵니다.
# 그리고 시민에게 묻습니다.
# " 혹시 선택을 나머지 C 로 바꾸겠습니까?"
# 처음 선택한 칸막이를 고수 할 것인가?  나머지 하나의 칸막이로 바꿀 것인가?  당신의 선택은?
# 베이즈 확률에 의하면 정답은 「바꾼다」이다.
# 베이즈 확률에 의하면 사전확률은 1/3 이지만 사후확률은 A는 1/3, B는 2/3가 되기 때문이다. * 이유는 「몬티홀」 검색!

# 마무리
# 이런식으로 이어나가면서 통계 -> 확률 -> 표준편차 -> 회귀분석 -> 데이터 분석 알고리즘을 공부하면서
# 진도는 머신러닝에 까지 이르게 되는데요, 이후에 나올 통계 확률의 세계는 공식도 많이 나오고 사실 심오해서 거기까지는 공부할 필요는 굳이 생각합니다.
# 그래서 이 정도까지만 보고 "대략적으로 머신러닝이 우도, 베이즈언 확률, 선형회귀 ... 이러한 통계학적 공식들로 시작되어 연구를 거듭해,
# 컴퓨터가 자동으로 학습할 수 있는 로직을 만들 수 있게 되었다" 정도로만 이해를 하고 갑시다.
# 여기까지 데이터분석 맛보기였습니다.



