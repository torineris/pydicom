import pydicom
from reportlab.pdfgen import canvas
from structured_reporting_parse.StructuredReportingParse import StructuredReportingParse

structured_reporting_dataset = pydicom.dcmread('data/sr.dcm')
parsed_sr_instance = StructuredReportingParse(structured_reporting_dataset)

#Coletando as medidas
fetal_biometry=['Number of Fetuses','Amniotic Fluid Index','Biparietal Diameter',
'Head Circumference','Femur Length','Fetal Heart Rate','Occipital-Frontal Diameter',
'Abdominal Circumference','Gestational Age','Estimated Weight']
tags=[]
for item in fetal_biometry:
    tags.append(parsed_sr_instance.searchMeasureName(measure_name=item))

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