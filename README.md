# Ontology Model for Systems Engineering

This repository contains the ontology model for systems engineering based on the work referenced in the following document: [Systems Engineering Ontology for the Department of Defense](https://apps.dtic.mil/sti/citations/trecms/AD1213647).

## Overview

This ontology model has been developed to provide a structured and formalized representation of key concepts and relationships in systems engineering. The ontology is designed to facilitate data sharing, integration, and interoperability across various systems and tools used in the Department of Defense and other engineering domains.

### Key Features
- **Entity Classes and Subclasses**: The ontology includes a comprehensive set of entity classes and their respective subclasses, capturing essential concepts in systems engineering.
- **Data Properties**: Each subclass is enriched with data properties that define key attributes and characteristics, making the ontology a powerful tool for detailed analysis and decision-making.
- **Annotations**: All entity classes, subclasses, and data properties are annotated with definitions and sources, providing clear and concise descriptions based on authoritative references.

## Repository Structure

- **ontology_structure.py**: This file contains the `ontology_structure` dictionary, which defines the entity classes, subclasses, data properties, definitions, and sources.
- **build.py**: A Python script that generates the OWL file from the `ontology_structure`. The output OWL file is saved in the `model` directory.
- **model/ontology_model.owl**: The OWL file generated from the `ontology_structure.py`, ready for use in Protégé or other ontology tools.
- **README.md**: This file provides an overview and instructions for the repository.

## How to Use

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   ```
   
2. Navigate to the repository directory:
   ```bash
   cd your-repo-name
   ```
   
3. Run the `build.py` script to generate the OWL file:
   ```bash
   python build.py
   ```
   
4. The OWL file will be created in the `model` directory as `ontology_model.owl`.

5. Import the OWL file into Protégé or any other ontology management tool for further exploration and use.

## References

This ontology is based on the work documented in the following report:

- **Systems Engineering Ontology for the Department of Defense**. [Access the document](https://apps.dtic.mil/sti/citations/trecms/AD1213647)

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions to this ontology model are welcome. Please submit pull requests or open issues to discuss potential changes.

## Contact

For questions or further information, please contact [John DeHart](mailto:enginetix@gmail.com).
