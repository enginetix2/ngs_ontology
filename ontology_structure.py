ontology_structure = {
    "Artifact": {
        "Guidance": {
            "definition": "An authoritative document intended to lead or steer the execution of actions.",
            "source": "DOD (2010)",
            "data_types": {
                "StrategicObjectivesAndPolicies": "A long-term plan to achieve preset goals.",
                "Directives": "An authoritative statement intended to impel actions and the achievement of goals.",
                "DefensePlanningGuidance": "The product of the planning programming budgeting and execution process’ planning phase.",
                "Plans": "A set of activities that result in a goal, desired effect, outcome, or objective."
            }
        },
        "Governance": {
            "definition": "The set of rules, policies, and decision-making criteria that will guide the SoS to achieving its goals and objectives.",
            "source": "Vaneman et al. (2022)",
            "data_types": {
                "Regulations": "An agency statement of general applicability and future effect.",
                "Policy": "A course of action, guiding principle, or procedure considered expedient, prudent, or advantageous."
            }
        },
        "Agreement": {
            "definition": "A consent among parties regarding the terms and conditions of activities that said parties participate in.",
            "source": "DOD (2010)",
            "data_types": {
                "MemorandumOfUnderstanding": "De facto agreement generally recognized by all partners as binding.",
                "MemorandumOfAgreement": "An agreement in principle as to how a program will be administered."
            }
        },
        "Standard": {
            "definition": "A formal agreement documenting generally accepted specifications or criteria for products, processes, procedures, policies, systems, and/or personnel.",
            "source": "DOD (2010)",
            "data_types": {
                "JointCapabilitiesAreasDocument": "High-level capabilities specified at the joint level.",
                "MissionEssentialTaskList": "A list of mission-essential tasks selected by a commander.",
                "TechnicalStandard": "Technical standards document specific technical methodologies and practices."
            }
        }
    },
    "Action": {
        "Activity": {
            "definition": "Work not specific to a single organization, weapon system, or individual that transforms inputs (Resources) into outputs (Resources) or changes their state.",
            "source": "DOD (2010)",
            "data_types": {
                "OperationalActivity": "An action performed in conducting the business of an enterprise.",
                "Training": "To make proficient by instruction and practice in particular knowledge or skills.",
                "Maintenance": "Actions taken to retain materiel in a serviceable condition or to restore it to serviceability."
            }
        },
        "Capabilities": {
            "definition": "The ability to achieve a desired effect under specified (performance) standards and conditions through combinations of ways and means (activities and resources) to perform a set of activities.",
            "source": "DOD (2010)",
            "data_types": {
                "Capabilities": "The ability to achieve a desired effect under specified conditions."
            }
        },
        "Function": {
            "definition": "Constitutes a specific or discrete action required to achieve a desired objective.",
            "source": "Blanchard and Fabrycky (2011)",
            "data_types": {
                "Function": "A specific or discrete action required to achieve a desired objective.",
                "SystemFunction": "A function that is performed by a system.",
                "ServiceFunction": "White box implementation of the activities of the service.",
                "SOAFunction": "A distinct part of the functionality provided by a technical system.",
                "TestProcess": "The process of evaluating and verifying data under fully controlled and traceable conditions."
            }
        }
    },
    "Program": {
        "Program": {
            "definition": "The process for controlling the cost, schedule, and performance of a project or group of projects to achieve a stated goal.",
            "source": "AcqNotes (2023)",
            "data_types": {
                "ProgramActivity": "A directed funded effort that provides a new, improved, or continuing materiel weapon or information system or service capability in response to an approved need."
            }
        }
    },
    "Asset": {
        "Platform": {
            "definition": "A system that is able to host other systems.",
            "source": "Vaneman et al. (2022)",
            "data_types": {
                "System": "A functionally, physically, and/or behaviorally related group of regularly interacting or interdependent elements.",
                "SubSystem": "A functional grouping of components that combine to perform a major function within an element.",
                "Assembly": "A portion of a system or subsystem that can be provisioned and replaced as an entity.",
                "SubAssembly": "Two or more parts joined to form a unit that is capable of being disassembled.",
                "Component": "A part or combination of parts having a specific function."
            }
        },
        "Service": {
            "definition": "A mechanism to enable access to a set of one or more capabilities where the access is provided using a prescribed interface and is exercised consistent with constraints and policies as specified by the service description.",
            "source": "DOD (2010)",
            "data_types": {
                "Service": "A mechanism to enable access to a set of one or more capabilities."
            }
        }
    },
    "Resource": {
        "Organization": {
            "definition": "A specific real-world assemblage of people and other resources organized for an ongoing purpose.",
            "source": "DOD (2010)",
            "data_types": {
                "Organization": "A specific real-world assemblage of people and other resources organized for an ongoing purpose."
            }
        },
        "Performer": {
            "definition": "Any entity – human, automated, or any aggregation of human and/or automated – that performs an activity and provides a capability.",
            "source": "DOD (2010)",
            "data_types": {
                "UserPerson": "Any entity -- human, automated, or any aggregation of human and/or automated -- that performs an activity and provides a capability."
            }
        },
        "Installation": {
            "definition": "A military or industrial establishment.",
            "source": "Vaneman et al. (2022)",
            "data_types": {
                "Facility": "A real property entity consisting of underlying land and one or more of the following: a building, a structure, a utility system, or pavement.",
                "Site": "Physical (geographic) location that is or was owned by, leased to, or otherwise possessed."
            }
        }
    },
    "Characteristic": {
        "Condition": {
            "definition": "The state of an environment or situation in which a Performer performs.",
            "source": "DOD (2010)",
            "data_types": {
                "EnvironmentalState": "The state of an environment or situation in which a Performer performs or is disposed to perform.",
                "OperationalCondition": "A statement of the values or states needed for the execution of actions within the processes and transactions of an enterprise."
            }
        },
        "Skill": {
            "definition": "The ability coming from one’s knowledge, practice, aptitude, etc. to do something well.",
            "source": "DOD (2010)",
            "data_types": {
                "Skill": "The ability coming from one’s knowledge, practice, aptitude, etc. to do something well."
            }
        }
    },
    "Measure": {
        "MOE": {
            "definition": "The 'operational' measures of success that are closely related to the achievement of the mission or operation being evaluated in the intended operational environment under a specified set of conditions.",
            "source": "Roedler and Jones (2005)",
            "data_types": {
                "MOE": "Measures of success that are closely related to the achievement of the mission or operation."
            }
        },
        "KPP": {
            "definition": "Key Performance Parameters are a special case of Measures of Effectiveness that are so critical that failure to achieve the KPP may result in program cancellation or significant program restructuring.",
            "source": "Roedler and Jones (2005)",
            "data_types": {
                "KPP": "Key Performance Parameters that are critical to mission success."
            }
        },
        "MOP": {
            "definition": "The measures that characterize physical or functional attributes relating to the system operation measured or estimated under specific testing and/or operational environment conditions.",
            "source": "Roedler and Jones (2005)",
            "data_types": {
                "MOP": "Measures that characterize physical or functional attributes of the system."
            }
        },
        "TPM": {
            "definition": "Metrics which measure the attributes of a system element to determine how well a system or system element is satisfying or expected to satisfy a technical requirement or goal.",
            "source": "Roedler and Jones (2005)",
            "data_types": {
                "TPM": "Metrics to determine how well a system satisfies technical requirements."
            }
        }
    },
    "Cost": {
        "Cost": {
            "definition": "An amount that has to be paid or spent to buy or obtain something.",
            "source": "Vaneman et al. (2022)",
            "data_types": {
                "Cost": "An amount that has to be paid or spent to buy or obtain something."
            }
        }
    },
    "Location": {
        "Orbital": {
            "definition": "An Orbital entity specifies a location along an orbit around a celestial body.",
            "source": "LML v1.4 (2022)",
            "data_types": {
                "Orbital": "A location along an orbit around a celestial body."
            }
        },
        "Physical": {
            "definition": "A Physical entity specifies a location on, above, or below the surface.",
            "source": "LML v1.4 (2022)",
            "data_types": {
                "AddressGeolocation": "A location on, above, or below the surface."
            }
        },
        "Virtual": {
            "definition": "A Virtual entity specifies a location within a digital network.",
            "source": "LML v1.4 (2022)",
            "data_types": {
                "IPAddress": "A location within a digital network."
            }
        }
    },
    "Statement": {
        "Guidance": {
            "definition": "An authoritative statement intended to lead or steer the execution of actions.",
            "source": "DOD (2010)",
            "data_types": {
                "Mission": "The task together with the purpose that clearly indicates the action to be taken and the reason.",
                "Doctrine": "The body of principles by which an enterprise seeks to guide its activities."
            }
        },
        "Standard": {
            "definition": "The set of rules governing the arrangement, interaction, and interdependence of parts or elements of the system or model of the system.",
            "source": "Vaneman et al. (2022)",
            "data_types": {
                "JointCapabilities": "The ability to execute a specified course of action at the Joint Level.",
                "Task": "An action, activity, or undertaking enabling missions, activities, or functions to be performed or accomplished."
            }
        }
    },
    "Requirement": {
        "Originating": {
            "definition": "Requirements that are the cornerstone upon which the systems engineering process is based.",
            "source": "Buede (2009)",
            "data_types": {
                "PerformanceRequirement": "Define quantitatively the extent or how well and under what conditions a function or task is to be performed."
            }
        },
        "Derived": {
            "definition": "Requirements that result from the analysis and allocation of technical requirements to logical functional architectures.",
            "source": "AcqNotes (2023)",
            "data_types": {
                "FunctionalRequirements": "Describe qualitatively the system functions or tasks to be performed in operation."
            }
        }
    },
    "Risk": {
        "Risks": {
            "definition": "The potential that something will go wrong as a result of one or a series of events.",
            "source": "Vaneman et al. (2022)",
            "data_types": {
                "Risks": "The combined effect of the probability of occurrence and the assessed consequence given the occurrence."
            }
        }
    }
}
