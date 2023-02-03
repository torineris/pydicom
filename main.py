import pydicom
from structured_reporting_parse.StructuredReportingParse import StructuredReportingParse

# Ler SR e gerar dataset
structured_reporting_dataset = pydicom.dcmread('data/sr.dcm')

# Criar instância do parser
parsed_sr_instance = StructuredReportingParse(structured_reporting_dataset)

# Propriedade que retorna o objeto inteiro
print(parsed_sr_instance.parsed_structured_reporting)

# Método de pesquisa por nome de medida
print(parsed_sr_instance.searchMeasureName('Gestational Age'))