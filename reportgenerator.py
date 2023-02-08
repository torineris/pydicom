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


'''#Cálculo da média da idade gestacional
agelist=[]
for key, value in gestational_age.items():
    agelist.append(value['value'])

def medval(list):
    media = sum(list)/len(list)
    return media'''


#Função de criação do PDF
def GeneratePDF(data):
    try:
        nome_pdf = 'Teste'
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))
        x = 720
        for key,value in data.items():
            x -= 20
            pdf.drawString(247,x, '{} : {}'.format(key,value))
        pdf.setTitle(nome_pdf)
        pdf.setFont("Helvetica-Oblique", 14)
        pdf.drawString(245,750, 'Lista de tags')
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(245,724, 'Nome da medida e valor')
        pdf.save()
        print('{}.pdf criado com sucesso!'.format(nome_pdf))
    except:
        print('Erro ao gerar {}.pdf'.format(nome_pdf))


GeneratePDF(data)