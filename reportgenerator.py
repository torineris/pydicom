import pydicom
from reportlab.pdfgen import canvas
from structured_reporting_parse.StructuredReportingParse import StructuredReportingParse

structured_reporting_dataset = pydicom.dcmread('data/sr.dcm')

parsed_sr_instance = StructuredReportingParse(structured_reporting_dataset)


gestational = parsed_sr_instance.searchMeasureName('Gestational Age')
agelist=[]
for key, value in gestational.items():
    agelist.append(value['value'])

def medval(list):
    media = sum(list)/len(list)
    return media

print(medval(agelist))

'''
Função de criação do PDF
def GeneratePDF(lista):
    try:
        nome_pdf = input('Informe o nome do PDF: ')
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))
        x = 720
        for nome,idade in lista.items():
            x -= 20
            pdf.drawString(247,x, '{} : {}'.format(nome,idade))
        pdf.setTitle(nome_pdf)
        pdf.setFont("Helvetica-Oblique", 14)
        pdf.drawString(245,750, 'Lista de Convidados')
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(245,724, 'Nome e idade')
        pdf.save()
        print('{}.pdf criado com sucesso!'.format(nome_pdf))
    except:
        print('Erro ao gerar {}.pdf'.format(nome_pdf))


lista = {'Rafaela': '19', 'Jose': '15', 'Maria': '22','Eduardo':'24'}
GeneratePDF(lista)
'''