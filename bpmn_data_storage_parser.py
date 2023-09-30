import xml.etree.ElementTree as ET

# Specify the path to your BPMN XML file here
xml_file_path = 'your_bpmn_file.bpmn'

# Parse the BPMN XML file
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Define the BPMN namespace
namespace = {'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL'}

# List to store extracted data storage references and their operations
data_storage_references = []

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
    # For example, if we are looking for {CREATE [NAME, ID, TIMESTAMP]}
    if '{CREATE' in reference:
        data = reference.split('[', 1)[1].split(']', 1)[0]  # Extract data variables
        operation = 'CREATE'
        print(f"Data Storage Reference: {reference}")
        print(f"Operation: {operation}")
        print(f"Data: {data}")
        print("\n")
