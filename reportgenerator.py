import pydicom
from structured_reporting_parse.StructuredReportingParse import StructuredReportingParse
from statistics import median
from decimal import *

structured_reporting_dataset = pydicom.dcmread('data/sr.dcm')
parsed_sr_instance = StructuredReportingParse(structured_reporting_dataset)


new_value = 0
#Função de calculo de média
def average(dict):
    num=[]
    for key,value in dict.items():
        num.append(value['value'])
    
    m_value = median(num)
    return m_value

#Função para coletar o maior valor de uma lista
def maximus(dict):
    hc=[]
    for key,value in dict.items():
        hc.append(value['value'])

    new_value = max(hc)
    return new_value

    
        

#Coletando as medidas
fetal_biometry=['Gestational Age','Head Circumference','Abdominal Circumference',
'Amniotic Fluid Index','Biparietal Diameter','Estimated Weight','Femur Length',
'Fetal Heart Rate','Number of Fetuses','Occipital-Frontal Diameter']
tags=[]
for item in fetal_biometry:
    tags.append(parsed_sr_instance.searchMeasureName(measure_name=item))
    for elem in tags:
        for key, value in elem.items():
            if value['measure_name'] == 'Gestational Age':
                average(elem)
            elif value['measure_name'] == 'Head Circumference':
                maximus(elem)







#Construção de um dicionário com as tags de interesse
data={}
for item in tags:
    def dataCollector(item):
        for key, value in item.items():
            name = value['measure_name']
            result = value['value']
            data.update({name:result})
        return data
    dataCollector(item)