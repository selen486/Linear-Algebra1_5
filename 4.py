import numpy as np

#삼각형의 세 꼭짓점
a = np.array([-1, 2, 0])
b = np.array([2, 1, 3])
c = np.array([1, 1, -1])

#같은 점(A)에서 출발하는 두 변의 벡터
u = b - a
v = c - a

#외적 계산
cross_product = np.cross(u, v)

#외적의 길이(평행사변형 넓이)
parallelogram_area = np.linalg.norm(cross_product)

#삼각형 넓이
triangle_area = parallelogram_area / 2

print(f"u = {u}")
print(f"v = {v}")
print(f"u x v = {cross_product}")
print(f"평행사변형의 넓이 = {parallelogram_area:.6f}")
print(f"삼각형의 넓이 = {triangle_area:.6f}")