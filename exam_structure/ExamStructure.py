from reportlab.pdfgen import canvas

class ExamStructure:
    def __init__(self, dataset):
        self.dataset = dataset
    
    def translator(self):

        gestational_translate = (
            ('Abdominal Circumference', 'Circunferência Abdominal'),
            ('Amniotic Fluid Index', 'Índice de Líquido Amniótico'),
            ('Biparietal Diameter', 'Diâmetro Biparietal'),
            ('Estimated Weight', 'Peso Estimado'),
            ('Femur Length', 'Comprimento do Fêmur'),
            ('Fetal Heart Rate', 'Batimentos Cárdio-Fetais Rítmicos'),
            ('Gestational Age', 'Idade Gestacional'),
            ('Head Circumference', 'Circunferência Cefálica'),
            ('Number of Fetuses', 'Número de Fetos'),
            ('Occipital-Frontal Diameter', 'Diâmetro Occipto-Frontal')     
        )

        data_translated={}
        for key, value in self.dataset.items():
            i=0
            for item in gestational_translate:
                if key == gestational_translate[i][0]:
                    data_translated.update({gestational_translate[i][1]:value})
                i+=1
        return data_translated
    
    translated_data = translator()

    def createPDF(self, translated_data):
        try:
            nome_pdf = 'Fetal Biometry'
            pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))
            x = 720
            for key,value in translated_data.items():
                x -= 20
                pdf.drawString(80,x, '{}: {}'.format(key,value))
            pdf.setTitle(nome_pdf)
            pdf.setFont("Helvetica-Bold", 14)
            pdf.drawString(245,750, 'Informações do SR')
            pdf.setFont("Helvetica", 12)
            pdf.drawString(245,724, 'Nome da medida e valor')
            pdf.save()
            print('{}.pdf criado com sucesso!'.format(nome_pdf))
        except:
            print('Erro ao gerar {}.pdf'.format(nome_pdf))