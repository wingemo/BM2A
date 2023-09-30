import xml.etree.ElementTree as ET

# Läs in BPMN XML-filen
bpmn_tree = ET.parse('din_bpmn_modell.xml')
bpmn_root = bpmn_tree.getroot()

# Skapa en datastruktur för UML
uml_data_structure = {}

# Loopa igenom BPMN-element och extrahera information om Data Storage Reference
for element in bpmn_root.iter():
    if element.tag.endswith('dataStoreReference'):
        data_store_id = element.attrib['id']
        data_store_name = element.attrib.get('name', 'Unnamed Data Store')
        # Skapa en UML-klass eller objekt för varje Data Storage Reference och lagra det i datastrukturen
        uml_data_structure[data_store_id] = {'name': data_store_name, 'type': 'DataStoreReference'}

# Skapa rotelementet för UML-data modellen
uml_model = ET.Element('UMLModel')

# Loopa igenom datastrukturen och skapa UML-element för varje Data Storage Reference
for data_store_id, data_store_info in uml_data_structure.items():
    # Skapa ett UML-element för Data Storage Reference
    uml_element = ET.SubElement(uml_model, 'UMLDataStoreReference')
    
    # Lägg till attribut för ID och namn
    uml_element.set('id', data_store_id)
    uml_element.set('name', data_store_info['name'])
    
    # Lägg till attribut för typen (DataStoreReference)
    uml_element.set('type', data_store_info['type'])

# Skapa ett ElementTree-objekt från rotelementet
uml_tree = ET.ElementTree(uml_model)

# Spara UML-data modellen som en XML-fil
uml_tree.write('uml_data_model.xml')

print("UML-data modellen har sparats som uml_data_model.xml")
