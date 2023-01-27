import pydicom

#Leitura
sr = pydicom.dcmread('sr.dcm')
#contentseq = sr['ContentSequence'][0]['ConceptNameCodeSequence'][0]['CodeMeaning']
#contentseq = sr['ContentSequence'][0]

#tags = contentseq.elements()

'''for elem in tags:
    print(elem.tag)
print('----------print------------')'''
print(sr)