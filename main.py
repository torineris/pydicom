import pydicom

def recurse(dataset):
    for block in dataset:
        if block.tag == (0x0040, 0xa730):
            for item in block:
                code_meaning = item['ConceptNameCodeSequence'][0]['CodeMeaning'].value

                try:
                    numeric_value = item['MeasuredValueSequence'][0]['NumericValue'].value
                except:
                    numeric_value = 'Indefinido'

                generating_string = str(code_meaning) + ': ' + str(numeric_value) + '\n'

                file = open('structured_report.txt', 'a')
                file.write(generating_string)
                file.close()

                [recurse(item) for item in block.value]

sr = pydicom.dcmread('sr.dcm')

recurse(sr)