def convert(number):
    factorValues = {'3' : 'Pling', 
                    '5' : 'Plang',
                    '7' : 'Plong'}
    
    raindropString = '';
    
    for key, value in factorValues.items():
        if((number % int(key)) == 0):
            raindropString += value

    if not raindropString:
        raindropString += str(number)
    
    return raindropString

print (convert(34))
    
