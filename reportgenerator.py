import pydicom
from structured_reporting_parse.StructuredReportingParse import StructuredReportingParse
from tag_collector.TagCollector import TagCollector
from exam_structure.ExamStructure import ExamStructure

structured_reporting_dataset = pydicom.dcmread('data/sr.dcm')
parsed_sr_instance = StructuredReportingParse(structured_reporting_dataset)

tag_collector = TagCollector(parsed_sr_instance)

'''Uma instância que chama o método coletor de tags. Neste caso, do exame gestacional.'''
gestational_tags = tag_collector.gestationalTagCollector()
#print(gestational_tags)

gestational_exam = ExamStructure(gestational_tags)
'''Uma instâcia com o método de tradução das medidas do exame gestacional'''
gestational_translated = gestational_exam.translator()
#print(gestational_translated)

'''Chamando o método gerador de PDF'''
exam_doc = gestational_exam.createPDF(gestational_translated)