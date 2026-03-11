import math
co = float(input(f'cateto oposto: '));
ca = float(input(f'cateto adjacente: '));
hip = (math.pow(co,2) + math.pow(ca,2));
hip = math.sqrt(hip);
ang = float(input('Angulo: '));
print(f'\nHipotenuse: {hip}\nSen: {math.sin(math.radians(ang)):.2f}\nCos: {math.cos(math.radians(ang)):.2}\nTang {math.tan(math.radians(ang)):.2}');