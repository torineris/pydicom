import pydicom
from structured_reporting_parse.StructuredReportingParse import StructuredReportingParse
from statistics import median
from decimal import *

structured_reporting_dataset = pydicom.dcmread('data/sr.dcm')
parsed_sr_instance = StructuredReportingParse(structured_reporting_dataset)


#Função de calculo de média
def average(gestational_age):
    return median(gestational_age)


#Função para coletar o maior valor de uma lista
def maximum(hc):
    return max(hc)

        

#Coletando as medidas
fetal_biometry=['Gestational Age','Head Circumference','Abdominal Circumference',
'Amniotic Fluid Index','Biparietal Diameter','Estimated Weight','Femur Length',
'Fetal Heart Rate','Number of Fetuses','Occipital-Frontal Diameter']
tags=[]
gestational_age=[]
hc=[]
for item in fetal_biometry:
    tags.append(parsed_sr_instance.searchMeasureName(measure_name=item))
    for elem in tags:
        for key, value in elem.items():
            if value['measure_name'] == 'Gestational Age':
                gestational_age.append(float(value['value']))
            elif value['measure_name'] == 'Head Circumference':
                hc.append(float(value['value']))

g_age = average(gestational_age)
max_value = maximum(hc)



#Construção de um dicionário com as tags de interesse
data={}
for item in tags:
    def dataCollector(item):
        for key, value in item.items():
            if value['measure_name'] == 'Gestational Age':
                data['Gestational Age']=g_age
            elif value['measure_name'] == 'Head Circumference':
                data['Head Circumference']=max_value
            else:
                name = value['measure_name']
                result = value['value']
                data.update({name:result})
        return data
    dataCollector(item)


print(data)