import pydicom

def recurse(dataset):
    parsed_structured_report = {}

    for block in dataset:
        if block.tag == (0x0040, 0xa730):
            for item in block:
                code_meaning = item['ConceptNameCodeSequence'][0]['CodeMeaning'].value

                try:
                    numeric_value = item['MeasuredValueSequence'][0]['NumericValue'].value
                except:
                    numeric_value = 'Indefinido'

                parsed_structured_report[code_meaning] = numeric_value

                [recurse(item) for item in block.value]
    
    file = open('structured_report.txt', 'a')
    file.write(str(parsed_structured_report))
    file.close()

    return parsed_structured_report

sr = pydicom.dcmread('sr.dcm')

recurse(sr)