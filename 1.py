import numpy as np

#입력 벡터
u = np.array([4, 1, 1])
v = np.array([2, 1, 0])

u1, u2, u3 = u
v1, v2, v3 = v

#행렬식 전개(+, -, +)
c1 = u2 * v3 - u3 * v2
c2 = -(u1 * v3 - u3 * v1)
c3 = u1 * v2 - u2 * v1

result = np.array([c1, c2, c3])

print(f"i 성분: {c1}")
print(f"j 성분: {c2}")
print(f"k 성분: {c3}")
print(f"u x v: {result}")

#numpy 검산
reference = np.cross(u, v)
print(f"numpy 결과: {reference}")
print(f"결과 일치: {np.allclose(result, reference)}")

#두 벡터와 수직인지 확인
print(f"u(u x v): {np.dot(u, result)}")
print(f"v(u x v): {np.dot(v, result)}")