class StructuredReportingParse:
    def __init__(self, dataset):
        self.dataset = dataset
        self.index = 0
        self.parsed_structured_reporting = {}
        self.recurse(dataset)

    def recurse(self, dataset):
        for block in dataset:
            if block.tag == (0x0040, 0xa730):
                for item in block:
                    code_meaning = item['ConceptNameCodeSequence'][0]['CodeMeaning'].value

                    try:
                        numeric_value = item['MeasuredValueSequence'][0]['NumericValue'].value
                    except:
                        numeric_value = 'Indefinido'

                    self.parsed_structured_reporting.update({
                        self.index: {
                            'measure_name': code_meaning,
                            'value': numeric_value
                        }
                    })

                    self.index += 1

                    [self.recurse(item) for item in block.value]
        
        return self.parsed_structured_reporting

    def searchMeasureName(self, measure_name):
        found_results = {}
        self.index = 0

        for item in self.parsed_structured_reporting:
            if self.parsed_structured_reporting[item]['measure_name'] == measure_name:
                found_results[self.index] = self.parsed_structured_reporting[item]
                self.index += 1

        return found_results