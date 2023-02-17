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

    def createPDF(self):
        return 'PDF gerado'