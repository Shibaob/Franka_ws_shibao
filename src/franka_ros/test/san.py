import three
import numpy as np

state_0 = three.StateCubicPolynomial()
state_f = three.StateCubicPolynomial()
state_0.t = 0
state_0.q = 0
state_0.v = 0
state_f.t = 5
state_f.q = 10
state_f.v = 0
step = 0.01
cubicPolynomial = three.CubicPolynomial(state_0,state_f)
cubicPolynomial.PrintCoefficients()
t_list = np.arange(state_0.t,state_f.t + step,step)
print(t_list)
q_list = []
v_list = []
a_list = []
for t in t_list:
        q_t = cubicPolynomial.CalcuCubicPolynomial(cubicPolynomial.coefficients,t,state_0.t)
        q_list.append(q_t.q)
        v_list.append(q_t.v)
        a_list.append(q_t.a)
q = q_list[2]
v = v_list[2]
print(len(t_list))    
print(q)
print(v)       
