import os
from rdflib import Graph, Namespace, Literal, RDF, RDFS, OWL, XSD
from ontology_structure_w_rels import ontology_structure

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
        
        # Check if details is a dictionary before accessing keys
        if isinstance(details, dict):
            # Add annotations for definition and source if they exist
            if "definition" in details:
                g.add((subclass_uri, RDFS.comment, Literal(details["definition"])))
            if "source" in details:
                g.add((subclass_uri, EX.source, Literal(details["source"])))
            
            # Add data types as data properties if they exist
            if "data_types" in details:
                for data_type, data_definition in details["data_types"].items():
                    data_prop_uri = EX[data_type]
                    g.add((data_prop_uri, RDF.type, OWL.DatatypeProperty))
                    g.add((data_prop_uri, RDFS.domain, subclass_uri))
                    g.add((data_prop_uri, RDFS.range, XSD.string))
                    g.add((data_prop_uri, RDFS.comment, Literal(data_definition)))
            
            # Add relationships as object properties if they exist
            if "relationships" in details:
                for relation, target in details["relationships"].items():
                    rel_uri = EX[relation]
                    target_uri = EX[target] if isinstance(target, str) else [EX[t] for t in target]
                    if isinstance(target_uri, list):
                        for t_uri in target_uri:
                            g.add((subclass_uri, rel_uri, t_uri))
                    else:
                        g.add((subclass_uri, rel_uri, target_uri))
        else:
            # Handle cases where details might be a simple string
            g.add((subclass_uri, RDFS.comment, Literal(details)))

# Serialize the graph to an OWL file
output_path = os.path.join(output_dir, "ontology_model_w_rels.owl")
g.serialize(destination=output_path, format="xml")

print(f"Ontology model saved to: {output_path}")
