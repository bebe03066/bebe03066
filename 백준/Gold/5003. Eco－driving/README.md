# [Gold III] Eco-driving - 5003 

[문제 링크](https://www.acmicpc.net/problem/5003) 

### 성능 요약

메모리: 47344 KB, 시간: 2612 ms

### 분류

데이크스트라, 그래프 이론, 최단 경로

### 제출 일자

2026년 2월 23일 20:49:45

### 문제 설명

<p>My colleague Elisabeth is lazy, both at work and when going to work. She never wants to do more than necessary, which also applies to her journey to work. Her goal is to use a minimum amount of energy, which she achieves by braking and accelerating as little as possible. This method applies to all wheel-based transport means she owns.</p>

<p>Elisabeth has earlier optimized her route by trial and error, but now wants your help to find the optimal path. She has provided a map with N junctions and R straight one-way roads between the junctions. If a road is dual way, it is represented as two one way roads.</p>

<p>Fortunately, Elisabeth often works night shifts, so braking and acceleration are only needed when turning in a junction, as there is no other traffic on the roads. Her goal is to find a route where the maximum turning angle in the junctions is minimized, as this means maximized speed. However, the route can not be too long.</p>

### 입력 

 <p>The first line of input contains three space separated integers J, R, D (2 ≤ J ≤ 200, 1 ≤ R ≤ 39 800, 1 ≤ D ≤ 1 000 000). J is the number of junctions, R is the number of one way roads which are connecting two junctions, and D is the maximum distance, in meters, that Elisabeth wants to travel. The road network is such that there is no path, that Elisabeth may want to use, which has the length L such that D < L < D ∗ (1 + 1e − 6).</p>

<p>Then follow J lines with two integers X and Y , (−100 000 ≤ X, Y ≤ 100 000), the distinct coordinates in meters on a flat ground. Elisabeth lives at junction 1 and her work is at junction J.</p>

<p>After that, R lines follow with two integers A and B. This should be interpreted as the one way road between the one-indexed source and destination junctions A and B (1 ≤ A, B ≤ J).</p>

### 출력 

 <p>Output one line with the maximum turning angle of the route that thas the maximum turning angle as low as possible. The turning angle must be output in degrees and have an absolute or relative error at most 10<sup>-6</sup>. If there</p>

<p>is no such route that is short enough, output “Impossible” on a single line.</p>

