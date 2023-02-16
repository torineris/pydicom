from structured_reporting_parse.StructuredReportingParse import StructuredReportingParse
from statistics import mean

class TagCollector:
    def __init__(self, dataset: StructuredReportingParse):
        self.dataset = dataset

    def collectingTags(self, tags: list[str]) -> list:
        found_values = []

        for item in tags:
            found_values.append(self.dataset.searchMeasureName(measure_name=item))

        return found_values

    def gestationalTagCollector(self) -> dict:
        # Coletando as medidas
        fetal_biometry = ['Gestational Age', 'Head Circumference', 'Abdominal Circumference', 'Amniotic Fluid Index', 'Biparietal Diameter', 'Estimated Weight', 'Femur Length', 'Fetal Heart Rate', 'Number of Fetuses', 'Occipital-Frontal Diameter']

        found_values = self.collectingTags(fetal_biometry)

        average_value = []
        head_c = []
            
        for elem in found_values:
            for key, value in elem.items():
                if value['measure_name'] == 'Gestational Age':
                        average_value.append(value['value'])
                elif value['measure_name'] == 'Head Circumference':
                    head_c.append(value['value'])

        # Atribuição de valores tratados
        average_age = mean(average_value)
        max_value = max(head_c)

        #Construção de um dicionário com as tags de interesse
        data={}

        for item in found_values:
            for key, value in item.items():
                if value['measure_name'] == 'Gestational Age':
                    data['Gestational Age'] = "{:.2f}".format(average_age)
                elif value['measure_name'] == 'Head Circumference':
                    data['Head Circumference'] = max_value
                else:
                    name = value['measure_name']
                    result = value['value']
                    data.update({name:result})
        
        return data

