from structured_reporting_parse.StructuredReportingParse import StructuredReportingParse
from statistics import mean

class TagCollector:
    """Responsável por receber uma instância do StructuredReportingParse e selecionar valores baseado no tipo de exame escolhido."""
    def __init__(self, dataset: StructuredReportingParse):
        self.dataset = dataset

    def collectingTags(self, tags: list[str]) -> list:
        """Método para coleta de tags específicas. Executado internamente."""
        found_values = []

        for item in tags:
            found_values.append(self.dataset.searchMeasureName(measure_name=item))

        return found_values

    def gestationalTagCollector(self) -> dict:
        """Coleta medidas relacionadas à um exame gestacional no dataset da instância."""

        # Tags das medidas
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
                    data['Gestational Age'] = str("{:.2f}".format(average_age))+" "+ value['measure_unit']
                elif value['measure_name'] == 'Head Circumference':
                    data['Head Circumference'] = str(max_value) +" "+ value['measure_unit']
                elif value['measure_name'] == 'Number of Fetuses':
                    data['Number of Fetuses'] = value['value']
                else:
                    name = value['measure_name']
                    result = str(value['value']) +" "+ value['measure_unit']
                    data.update({name:result})
        
        return data

