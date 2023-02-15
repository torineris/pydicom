import pydicom
from structured_reporting_parse.StructuredReportingParse import StructuredReportingParse
from tag_collector.TagCollector import TagCollector

structured_reporting_dataset = pydicom.dcmread('data/sr.dcm')
parsed_sr_instance = StructuredReportingParse(structured_reporting_dataset)

tag_collector = TagCollector(parsed_sr_instance)

print(tag_collector.gestationalTagCollector())