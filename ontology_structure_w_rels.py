ontology_structure = {
    "Platform": {
        "definition": "A system that is able to host other systems, including vehicles and weapons.",
        "source": "Vaneman et al. (2022)",
        "subclasses": {
            "AirVehicle": {
                "definition": "A powered flying vehicle with fixed wings and a weight greater than that of the air it displaces.",
                "source": "DOD (2020)",
                "data_types": {
                    "weight": "The empty weight of the aircraft.",
                    "speed": "The maximum speed capability of the aircraft.",
                    "range": "The operational range of the aircraft.",
                    "cargoCapacity": "The payload capacity of the aircraft."
                },
                "relationships": {
                    "designedBy": "Vendor",
                    "hasConfiguration": "Loadout",
                    "locatedAt": "Location",
                    "incurs": "Cost",
                    "enables": "Decision",
                    "resultsIn": "Decision"
                }
            },
            "WeaponSystem": {
                "definition": "A system designed to detect, engage, and destroy enemy forces or targets.",
                "source": "DOD (2020)",
                "subclasses": {
                    "Weapon": {
                        "definition": "An instrument or device used to inflict damage or harm to adversaries.",
                        "source": "DOD (2020)",
                        "data_types": {
                            "type": "Type of weapon, e.g., missile, gun.",
                            "range": "The maximum effective range of the weapon.",
                            "payload": "Type of explosive or functional payload."
                        },
                        "relationships": {
                            "locatedAt": "Location",
                            "incurs": "Cost",
                            "connectedBy": "Connection",
                            "specifiedBy": "Characteristic",
                            "consumedBy": "Action",
                            "enabledBy": "Decision"
                        }
                    }
                }
            }
        }
    },
    "Vendor": {
        "definition": "An organization that designs and produces air vehicles, weapons, and other systems.",
        "source": "Vaneman et al. (2022)",
        "data_types": {
            "name": "The name of the vendor, e.g., Lockheed, Boeing."
        },
        "relationships": {
            "designs": "AirVehicle",
            "incurs": "Cost",
            "enabledBy": "Decision"
        }
    },
    "Loadout": {
        "definition": "A specific configuration of weapons and systems on an air vehicle.",
        "source": "Vaneman et al. (2022)",
        "data_types": {
            "name": "The name of the loadout configuration.",
            "description": "A description of the loadout, e.g., 4 AIM-120 missiles and a gun."
        },
        "relationships": {
            "hasWeapon": "Weapon",
            "specifiedBy": "Characteristic",
            "locatedAt": "Location",
            "resultsIn": "Decision"
        }
    },
    "Characteristic": {
        "definition": "A quality or feature that distinguishes a particular entity, such as an air vehicle or weapon.",
        "source": "Vaneman et al. (2022)",
        "data_types": {
            "type": "The type of characteristic, e.g., performance, cost.",
            "value": "The value of the characteristic, e.g., speed in mph, range in miles."
        },
        "relationships": {
            "specifies": ["AirVehicle", "Weapon", "Loadout"],
            "incurs": "Cost",
            "enabledBy": "Decision",
            "locatedAt": "Location"
        }
    },
    "Connection": {
        "definition": "A logical or physical conduit linking two or more entities.",
        "source": "Vaneman et al. (2022)",
        "subclasses": {
            "Conduit": {
                "definition": "A means of connecting entities within a system.",
                "source": "Vaneman et al. (2022)",
                "data_types": {
                    "protocol": "The communication protocol or method of connection.",
                    "bandwidth": "The capacity of the connection, e.g., in Mbps."
                },
                "relationships": {
                    "connectedBy": ["AirVehicle", "Weapon", "Loadout"],
                    "specifiedBy": "Characteristic",
                    "locatedAt": "Location",
                    "incurs": "Cost",
                    "enabledBy": "Decision"
                }
            }
        }
    },
    "Location": {
        "definition": "A specific geographical or logical location for an entity.",
        "source": "Vaneman et al. (2022)",
        "subclasses": {
            "PhysicalLocation": {
                "definition": "A physical geographic location where an entity is located.",
                "source": "Vaneman et al. (2022)",
                "data_types": {
                    "coordinates": "The GPS coordinates of the location.",
                    "description": "A description of the physical location."
                },
                "relationships": {
                    "locatedAt": ["AirVehicle", "Weapon", "Loadout", "Connection"],
                    "incurs": "Cost",
                    "enabledBy": "Decision",
                    "causedBy": "Risk"
                }
            },
            "VirtualLocation": {
                "definition": "A logical location within a digital or networked environment.",
                "source": "Vaneman et al. (2022)",
                "data_types": {
                    "ipAddress": "The IP address of the virtual location.",
                    "description": "A description of the virtual location."
                },
                "relationships": {
                    "locatedAt": ["AirVehicle", "Weapon", "Loadout", "Connection"],
                    "incurs": "Cost",
                    "enabledBy": "Decision",
                    "causedBy": "Risk"
                }
            }
        }
    },
    "Cost": {
        "definition": "An amount that must be paid or spent to acquire or maintain an entity.",
        "source": "Vaneman et al. (2022)",
        "data_types": {
            "amount": "The cost value, e.g., in dollars.",
            "currency": "The currency of the cost."
        },
        "relationships": {
            "incurredBy": ["AirVehicle", "Weapon", "Loadout", "Connection", "Vendor"],
            "enabledBy": "Decision",
            "causedBy": "Risk",
            "resultsIn": "Decision"
        }
    },
    "Decision": {
        "definition": "A conclusion or resolution reached after consideration, often affecting entities in the system.",
        "source": "Vaneman et al. (2022)",
        "data_types": {
            "outcome": "The result of the decision, e.g., proceed, halt, modify.",
            "justification": "The reason or rationale behind the decision."
        },
        "relationships": {
            "enabledBy": ["Action", "Artifact", "Asset (Resource)", "Characteristic", "Connection", "Cost", "Input/Output", "Location", "Risk", "Statement", "Time"],
            "resultsIn": ["Action", "Artifact", "Asset (Resource)", "Characteristic", "Connection", "Cost", "Input/Output", "Location", "Risk", "Statement", "Time"]
        }
    },
    "Risk": {
        "definition": "The potential of an adverse event occurring, impacting the system.",
        "source": "Vaneman et al. (2022)",
        "data_types": {
            "probability": "The likelihood of the risk occurring.",
            "impact": "The potential consequence of the risk."
        },
        "relationships": {
            "causedBy": ["AirVehicle", "Weapon", "Loadout", "Connection", "Cost", "Decision"],
            "mitigatedBy": "Action",
            "resolvedBy": "Action",
            "resultsIn": "Decision"
        }
    },
    "Statement (Requirement)": {
        "definition": "A formal expression of a condition or capability required by an entity in the system.",
        "source": "Vaneman et al. (2022)",
        "data_types": {
            "requirementID": "A unique identifier for the requirement.",
            "text": "The textual description of the requirement."
        },
        "relationships": {
            "satisfiedBy": ["Action", "Artifact", "Asset (Resource)", "Characteristic", "Connection", "Cost", "Decision", "Input/Output", "Location", "Risk", "Time"],
            "tracedFrom": "Requirement",
            "verifiedBy": "Requirement"
        }
    },
    "Time": {
        "definition": "A temporal reference for events, actions, or states within the system.",
        "source": "Vaneman et al. (2022)",
        "data_types": {
            "timestamp": "The specific time of occurrence.",
            "duration": "The length of time an event or state lasts."
        },
        "relationships": {
            "occurs": ["Action", "Artifact", "Asset (Resource)", "Characteristic", "Connection", "Cost", "Decision", "Input/Output", "Location", "Risk", "Statement (Requirement)"]
        }
    }
}
