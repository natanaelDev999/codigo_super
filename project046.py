times = ('flamengo','são paulo','botafogo','corinthians','palmeiras','vasco','goias','coritiba',
         'athletico paranaense','cuiaba','vitoria','sport','crb','avai',
         'vila nova','chapecoense','crimiuma','crs','vitoria','cuiaba')
print(times)
print('=-='*30)
print(f'os 5 primeiros são: {times[:5]}')
print('=-='*30)
print(f'os 4 ultimos são: {times[-4:]}')
print('=-='*30)
print(f'os times em ordem alfabetica: {sorted(times)}')
print('=-='*30)
print(f'a posição do chapecoense: {times.index("chapecoense")+1}°')