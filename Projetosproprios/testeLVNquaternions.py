import LibraryVectorNatan as lvn

q1 = [0,0.1,0.2,0.2]
q2 = [0,0.1,0.2,0.2]
q3 = [0.1,0.2,0.2,0.2]
q4 = [0.0,2,2,0.0]

print('soma:',lvn.soma_quaternions(q1,q2))
print('multiplica por um escalar: ',lvn.multiplica_escalar_quaternion(3,q1))
print('conjuga o quaternion: ', lvn.conjuga_quaternion(q3))
print('norma do quaternion: ',lvn.norma_quaternion(q4))
print('multiplica q1, q2: ',lvn.multiplica_quaternions(q1,q2))
print('multiplica q2, q1: ',lvn.multiplica_quaternions(q2,q1))