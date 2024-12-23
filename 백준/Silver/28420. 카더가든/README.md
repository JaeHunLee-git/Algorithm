# [Silver I] 카더가든 - 28420 

[문제 링크](https://www.acmicpc.net/problem/28420) 

### 성능 요약

메모리: 36664 KB, 시간: 1948 ms

### 분류

브루트포스 알고리즘, 구현, 누적 합

### 제출 일자

2024년 1월 31일 19:03:46

### 문제 설명

<p>화전역 옆에는 땅이 매우 많다. 이 땅에 우리는 캠핑카가 달린 차를 세우려고 한다. 이때 캠핑카를 차 옆에 <strong>정확히 아래 그림의 3개의 모양으로만</strong> 배치할 수 있고, 캠핑카와 차는 회전하거나 뒤집힐 수 없다.</p>

<p style="text-align: center;"><img alt="" src="" style="height: 80%; width: 80%;"></p>

<p>차와 캠핑카는 너비는 $a$로 같지만 차의 길이 $b$와 캠핑카의 길이 $c$는 다를 수 있다. 이때 너비는 차량의 좌우로 측정된 가로 폭 치수를, 길이는 차체의 앞부분에서 뒷부분까지의 치수를 의미한다. 땅은 1X1의 단위 구역마다 흐림 정도가 주어진다. <strong>차와 캠핑카가 차지하는 단위 구역의 흐림 정도 합</strong>이 낮을수록 맑다. 단, 차와 캠핑카가 차지하는 단위 구역이 땅을 벗어나서는 안 된다. 어떻게 하면 가장 맑은 곳에서 캠핑할 수 있도록 차를 세울 수 있을까?</p>

<p>아래 예시를 참고하자. 차와 캠핑카의 너비는 1, 차의 길이는 2, 캠핑카의 길이는 3일 때, 아래 땅에 가장 맑은 위치에 차와 캠핑카를 배치하고 싶다. 예제 입력 1의 땅은 아래와 같다. 해당 땅에 3가지 방법로 차를 놓을 수 있다고 했을 때, 차의 배치도는 3가지 방법 그대로이어야 하나, 차의 앞부분의 위치는 달라질 수 있다. 단, 차체가 땅을 벗어나는 일은 없다. 아래와 같이 배치했을 때 가장 맑은 곳에서 캠핑할 수 있다. 이때의 흐림 정도는 12이다.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 50%; height: 50%;"></p>

### 입력 

 <p>첫째 줄에 땅의 세로와 가로의 길이 $N$, $M$이 공백으로 구분되어 주어진다. $(2 \le N,M \le 300)$</p>

<p>둘째 줄에는 차와 캠핑카의 너비 $a$, 차의 길이 $b$, 캠핑카의 길이 $c$가 공백으로 구분되어 주어진다. 차와 캠핑카의 너비는 $a$로 동일하다. $(1 \le a,b,c \le min(\frac{N}{2}, \frac{M}{2}))$</p>

<p>셋째 줄부터 $N$ 개의 줄에 걸쳐 각 단위 구역의 흐림 정도 $A_{i,j}$가 공백으로 구분되어 주어진다. $(1 \le A_{i,j} \le 20;$ $1 \leq i \leq N;$ $1 \leq j \leq M)$</p>

<p>입력으로 주어지는 모든 수는 정수이다.</p>

### 출력 

 <p>가장 맑은 곳에서 캠핑할 때의 흐림 정도를 구하여라.</p>

