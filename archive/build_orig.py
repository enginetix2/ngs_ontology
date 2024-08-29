import os
from rdflib import Graph, Namespace, Literal, RDF, RDFS, OWL, XSD
from ontology_structure import ontology_structure

# Create 'model' directory if it doesn't exist
output_dir = "model"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Initialize graph
g = Graph()

# Define namespaces
EX = Namespace("http://example.org/ontology#")
g.bind("ex", EX)

# Create classes, subclasses, and annotations for definitions, sources, and data types
for entity_class, subclasses in ontology_structure.items():
    class_uri = EX[entity_class]
    g.add((class_uri, RDF.type, OWL.Class))
    for subclass, details in subclasses.items():
        subclass_uri = EX[subclass]
        g.add((subclass_uri, RDF.type, OWL.Class))
        g.add((subclass_uri, RDFS.subClassOf, class_uri))
        
        # Add annotations for definition and source
        g.add((subclass_uri, RDFS.comment, Literal(details["definition"])))
        g.add((subclass_uri, EX.source, Literal(details["source"])))
        
        # Add data types as data properties
        for data_type, data_definition in details["data_types"].items():
            data_prop_uri = EX[data_type]
            g.add((data_prop_uri, RDF.type, OWL.DatatypeProperty))
            g.add((data_prop_uri, RDFS.domain, subclass_uri))
            g.add((data_prop_uri, RDFS.range, XSD.string))
            g.add((data_prop_uri, RDFS.comment, Literal(data_definition)))

# Serialize the graph to an OWL file
output_path = os.path.join(output_dir, "ontology_model.owl")
g.serialize(destination=output_path, format="xml")

print(f"Ontology model saved to: {output_path}")
