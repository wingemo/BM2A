import xml.etree.ElementTree as ET

# Specify the path to your BPMN XML file here
xml_file_path = 'your_bpmn_file.bpmn'

# Parse the BPMN XML file
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Define the BPMN namespace
namespace = {'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL'}

# Mapping of BPMN verbs to operations
verb_to_operation = {
    'GET': 'RETRIEVE',
    'POST': 'CREATE',
    'PUT': 'UPDATE',
    'DELETE': 'DELETE'
}

# List to store extracted data storage references and their operations
data_storage_references = []

data_objects = {}

# Loop through BPMN activities and extract data storage references
for data_object_reference in root.findall('.//bpmn:dataObjectReference', namespace):
    name = data_object_reference.get('name')
    if name:
        data = data_object_reference.find('.//bpmn:dataObject', namespace)
        if data is not None and data.text:
            data_storage_reference = data.text.strip()
            data_storage_references.append(data_storage_reference)

# Loop through data storage references and extract operations
for reference in data_storage_references:
    # Check if the reference contains one of the mapped operations
    for verb, operation in verb_to_operation.items():
        if f'{{{verb}' in reference:
            data = reference.split('[', 1)[1].split(']', 1)[0]  # Extract data variables
            if data not in data_objects:
               data_objects[data] = dict()
               data_objects[data][operation] = true
            
            print(f"Data Storage Reference: {reference}")
            print(f"Operation: {operation}")
            print(f"Data: {data}")
            print("\n")
