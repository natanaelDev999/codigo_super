comida = ('banana',1.99,'maçã',3.99,'abacate',0.99,'morango',5.99,'bala',2.99,'salgadinho',25.99,'suco',6.99,'refrigerante',14.99,'sabonete',4.99,'dertegente',19.99)
for c in range(0, len(comida)):
    if  c % 2 == 0:
        print(f'{comida[c]:.<30}',end= '')
    else:
        print(f'R${comida[c]:>6.2f}')