import pydicom

sr = pydicom.dcmread('sr.dcm')

for elem in sr['ContentSequence']:
    try:
        for elem in elem['ContentSequence']:
            print(elem['ConceptNameCodeSequence'][0]['CodeMeaning'].value)
            try:
                print(elem['MeasuredValueSequence'][0])
            except:
                print('INDEFINIDO;')
    except:
        print('Aguardando o próximo')
        