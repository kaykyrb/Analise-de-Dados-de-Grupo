cont_years = 0;
cont_woman = 0;
cont_man = 0;

print('-=' *15);
print('CADASTRO DE PESSOAS')
print('-=' *15);

while True:
  years = int(input('Fale sua idade: '));
  gender = ' ';

  while gender not in 'MF':
    gender = input('Informe seu sexo [M/F]: ').upper().strip()[0];
  
  if years >= 18:
    cont_years += 1;
  if gender == 'M':
    cont_man += 1;
  if gender == 'F' and years < 20:
    cont_woman += 1;

  proceed = ' ';

  print('-' *30);
  while proceed not in 'SN':
    proceed = input('Deseja continuar? [S/N] ').upper().strip()[0];
  print('-=' *15);

  if proceed == 'N':
    break;
  

print(f'Total de pessoas com mais de 18 anos: {cont_years}');
print(f'No total tem {cont_man} homens cadatrados.');
print(f'E temos {cont_woman} mulheres com menos de 20 anos.');
print('-=' *15);