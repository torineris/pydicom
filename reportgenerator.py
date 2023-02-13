import pydicom
from structured_reporting_parse.StructuredReportingParse import StructuredReportingParse
from statistics import *

structured_reporting_dataset = pydicom.dcmread('data/sr.dcm')
parsed_sr_instance = StructuredReportingParse(structured_reporting_dataset)      


#Coletando as medidas
fetal_biometry=['Gestational Age','Head Circumference','Abdominal Circumference',
'Amniotic Fluid Index','Biparietal Diameter','Estimated Weight','Femur Length',
'Fetal Heart Rate','Number of Fetuses','Occipital-Frontal Diameter']

#Armazenando dicionários de medidas
tags=[]
average_value=[]
head_c=[]

for item in fetal_biometry:
    tags.append(parsed_sr_instance.searchMeasureName(measure_name=item))
    for elem in tags:
        for key, value in elem.items():
            if value['measure_name'] == 'Gestational Age':
                average_value.append(value['value'])
            elif value['measure_name'] == 'Head Circumference':
                head_c.append(value['value'])

#Atribuição de valores tratados
average_age = mean(average_value)
max_value = max(head_c)



#Construção de um dicionário com as tags de interesse
data={}
for item in tags:
    def dataCollector(item):
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
    dataCollector(item)


print(data)