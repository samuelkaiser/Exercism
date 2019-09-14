def convert(number):
    factorValues = {'3' : 'Pling', 
                    '5' : 'Plang',
                    '7' : 'Plong'}
    
    raindropString = '';

    if((number % 3) == 0):
        raindropString += factorValues['3']
    
    if((number % 5) == 0):
        raindropString += factorValues['5']
    
    if((number % 7) == 0):
        raindropString += factorValues['7']

    if not raindropString:
        raindropString += str(number)
    
    return raindropString

print (convert(34))
    
