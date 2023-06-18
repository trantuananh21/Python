names = {
'students': [
{'firstName': 'Nikki', 'lastName': 'Roysden'},
{'firstName': 'Mervin', 'lastName': 'Friedland'},
{'firstName': 'Aron', 'lastName': 'Wilkins'}
],
'teachers': [
{'firstName': 'Amberly', 'lastName': 'Calico'},
{'firstName': 'Regine', 'lastName': 'Agtarap'}
]
}

print('List of students:')
for i in names['students']:
    print(f'- {i["firstName"]} {i["lastName"]}')
    
    
print('List of teachers:')
for i in names['teachers']:
    print(f'- {i["firstName"]} {i["lastName"]}')