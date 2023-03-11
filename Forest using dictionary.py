#creating forest using dictionary
#dictionary (forest of 3 trees)
Families={
    'charley':
        {'Sam':{'boxy','Rosy'} ,
         'Nila':{'Pepsi'}},
    'Devi':
        { 'tomy':{'Tony'},
          'Timmy':{'Hamster'},
          'Pana':{'Hamster'} },
    'Carlos':
        {'Diego':'Cat','Ferret':'Fox'}
        }
for Parent,Children in Families.items():
    print(f"{Parent} has {len(Children)} kid(s):")
    print(f"{', and ' .join([str(child) for child in [*Children]])}")
