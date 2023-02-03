import pydicom

sr = pydicom.dcmread('data/sr.dcm')
index = 0

def recurse(dataset):
    for block in dataset:
        if block.tag == (0x0040, 0xa730):
            global index
            for item in block:
                code_meaning = item['ConceptNameCodeSequence'][0]['CodeMeaning'].value

                try:
                    numeric_value = item['MeasuredValueSequence'][0]['NumericValue'].value
                except:
                    numeric_value = 'Indefinido'

                parsed_structured_reporting.update({
                    index: {
                        'measure_name': code_meaning,
                        'value': numeric_value
                    }
                })

                index += 1

                [recurse(item) for item in block.value]
    
    return parsed_structured_reporting

def searchMeasureName(parsed_structured_reporting, measure_name):
    found_results = {}
    index = 0

    for item in parsed_structured_reporting:
        if parsed_structured_reporting[item]['measure_name'] == measure_name:
            found_results[index] = parsed_structured_reporting[item]
            index += 1

    return found_results

parsed_structured_reporting = {}
reporting_parsed = recurse(sr)

file = open('structured_reporting.txt', 'a')
file.write(str(reporting_parsed))
file.close()

found_results = searchMeasureName(reporting_parsed, 'Femur Length')

file = open('search_found_results.txt', 'a')
file.write(str(found_results))
file.close()