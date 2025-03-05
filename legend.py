zoning_district = {
    'M1-1': {
        'FAR': 1,
        'Accessory Parking PRC-B': '1 per 300 SF',
        'Signage': '6 X Street Frontage',
    },
    'M1-2': {
        'FAR': 2,
        'Accessory Parking PRC-B': '1 per 300 SF',
        'Signage': '6 X Street Frontage',
    },
    'M1-3': {
        'FAR': 5,
        'Accessory Parking PRC-B': '1 per 300 SF',
        'Signage': '6 X Street Frontage',
    },
    'M1-4': {
        'FAR': 2,
        'Accessory Parking PRC-B': 'None',
        'Signage': '6 X Street Frontage',
    },
    'M1-5': {
        'FAR': 5,
        'Accessory Parking PRC-B': 'None',
        'Signage': '6 X Street Frontage',
    },
    'M1-6': {
        'FAR': 10,
        'Accessory Parking PRC-B': 'None',
        'Signage': '6 X Street Frontage',
    },
}

occupancy_desc = {
    'Theater': 'A-1',
    'Concert Hall': 'A-1',
    'TV & Radio Studio': {
        'With spectator seating': 'A-1',
        'Without audience': 'B',
    },
    'Banquet Hall': 'A-2',
    'Cabaret': 'A-2',
    'Casino': 'A-2',
    'Nightclub': 'A-2',
    'Restaurant': 'A-2',
    'Cafeteria': {
        'Childen up to and including 12th grade': 'A-3',
        'Other': 'A-2',
    },
    'Tavern': 'A-2',
    'Bar': 'A-2',
    'Amusement Arcade': 'A-3',
    'Art Gallery': 'A-3',
    'Bowling Alley': 'A-3',
    'Classroom': {
        '75 or more people': 'A-3',
        'Students above 12th grade': 'B',
        'Other': 'E',
    },
    'Community Hall': 'A-3',
    'Courtrooms': 'A-3',
    'Custodial Care Facility': {
        '75 or more people': 'A-3',
        'less than 75 people': 'B',
        'Up to 30 children under the age of 2': 'E', # Day Care Facility
        'More than 2 children under the age of 2': 'I-4',
        'More than 4 people over the age of 2 not capable of responding to emergency situations without physical assistance': 'I-4',
    },
    'Dance Studio': 'A-3',
    'Exhibition Hall': 'A-3',
    'Funeral Parlor': 'A-3',
    'Gym Without Spectator Seating': 'A-3',
    'Swimming Pool': {
        'Indoor without spectator seating': 'A-3',
        'Other': 'A-4',
    },
    'Tennis Court': {
        'Indoor without spectator seating': 'A-3',
        'Other': 'A-4',
    },
    'Lecture Hall': 'A-3',
    'Museum': 'A-3',
    'House Of Worship': 'A-3',
    'Pool & Billiard Parlor': 'A-3',
    'School Auditorium': 'A-3',
    'Waiting Areas In Transportation Terminal': 'A-3',
    'Arena': 'A-4',
    'Skating Rink': 'A-4',
    'Amusement Park': 'A-5',
    'Bleacher': 'A-5',
    'Grandstand': 'A-5',
    'Stadium': 'A-5',
    'Airport Traffic Control Tower': 'B',
    'Ambulatory Care Facility': 'B',
    'Animal Hospital': 'B',
    'Veterinary Clinic': 'B',
    'Pet Shop': 'B',
    'Bank': 'B',
    'Barber Shop': 'B',
    'Beauty Shop': 'B',
    'Civic Administration Office': 'B',
    'Medical Center': 'B',
    'Dry Cleaning': {
        'Without solvents': 'B',
        'Using or storing solvents having a flash point between 100°F (38°C) and 138.2°F (59°C)': 'F-1',
        'Using or storing solvents having a flash point above 138.2°F (59°C)': 'F-2',
    },
    'Laundromat': 'B',
    'Pick-Up & Delivery Station': 'B',
    'Electronic Data Processing': 'B',
    'Laboratory': {
        'Moderate-Hazard Production': 'F-1',
        'Low-hazard Production': 'F-2',
        'Other': 'B',
    },
    'Research Center': 'B',
    'Library': {
        'Accessory to Group E occupancies': 'E',
        'Other': 'B',
    },
    'Motor Vehicle Showroom': 'B',
    'Office': 'B',
    'Post Office': 'B',
    'Printing Shop': 'B',
    'Professional Services': 'B',
    'Telephone Exchange': 'B',
    'Tutoring Center': 'B',
    'Martial Arts Studio': 'B',
    'Academy': 'E',
    'Schools': 'E',
    'Aircraft': {
        'Product': 'F-1',
        'Hangar (storage and repair)': 'S-1',
    },
    'automobile / Motor Vehicle': 'F-1',
    'Bakery': 'F-1',
    'Beverage': {
        'Non-alcoholic': 'F-2',
        'Up to and including 16-percent alcohol content': 'F-2',
        'Over 16-percent alcohol content': 'F-1',
        'Up to and including 16-percent alcohol in metal, glass or ceramic containers': 'S-2',
    },
    'Boat': 'F-1',
    'Broom / Brushe': 'F-1',
    'Canvas': 'F-1',
    'Carpet & Rug': {
        'Products': 'F-1',
        'Cleaning using or storing solvents with a flash point between 100°F (38°C) and 138.2°F (59°C)': 'F-1',
        'Cleaning using or storing solvents with a flash point above 138.2°F (59°C)': 'F-2',
    },
    'Clothing': {
        'Product': 'F-1',
        'Storage, woolen wearing apparel': 'S-1',
    },
    'Disinfectant': 'F-1',
    'Electric Generation Plant': 'F-1',
    'Electrical Substation': 'F-1',
    'Engine': 'F-1',
    'Food Processing': {
        'Establishments and commercial kitchens not adjoining a restaurant, cafeteria or similar dining facilities': 'F-1',
        'Meat slaughtering or preparation of fish for packing': 'F-2',
    },
    'Furniture': {
        'Product': 'F-1',
        'Storage': 'S-1',
    },
    'Hemp Product': 'F-1',
    'Jute Product': 'F-1',
    'Leather': {
        'Product': 'F-1',
        'Storage': 'S-1',
    },
    'Metal': {
        'Finishing, plating, grinding, sharpening, polishing, cleaning, rustproofing, heat treatment or similar processes': 'F-1',
        'Products (fabrication and assembly)': 'F-2',
        'Metal cabinet': 'S-2',
        'Metal desk with plastic tops and trim': 'S-2',
        'Metal part': 'S-2',
        'Products': 'S-2',
    },
    'Millwork': 'F-1',
    'Motion Pictures Filming': 'F-1',
    'Musical Instrument': 'F-1',
    'Optical Goods': 'F-1',
    'Paper Mill': 'F-1',
    'Paper Product': 'F-1',
    'Photographic Film': 'F-1',
    'Plastic': {
        'Nonflammable product': 'F-2',
        'Product': 'F-1',
    },
    'Printing': {
        'Incidental to primary use, area not exceeding 2,000 square feet (185.8 m2)': 'F-2',
        'Service': 'F-1',
    },
    'Publishing': 'F-1',
    'Recreational Vehicle': 'F-1',
    'Refuse Incineration': 'F-1',
    'Shoe': 'F-1',
    'Soap & Detergent': {
        'Product': 'F-1',
        'Storage': 'S-1',
    },
    'Textile': 'F-1',
    'Tobacco': {
        'Product': 'F-1',
        'Storage of Tobacco, cigars, cigarettes and snuff': 'S-1',
    },
    'Trailer': 'F-1',
    'Upholstering': 'F-1',
    'Wood': 'F-1',
    'Woodworking': 'F-1',
    'Appliance': 'F-2',
    'Athletic Equipment': 'F-2',
    'Automobile Laundry': 'F-2',
    'Automobile Wrecking': 'F-2',
    'Bicycles': 'F-2',
    'Brick & Masonry': 'F-2',
    'Business Machine': 'F-2',
    'Camera & Photo Equipment': 'F-2',
    'Ceramic Product': 'F-2',
    'Commercial kitchens adjoining restaurants, cafeterias (including those classified in Group A-3), or similar dining facilities': 'F-2',
    'Construction & Agricultural Machinery': 'F-2',
    'Electronics': 'F-2',
    'Foundries': 'F-2',
    'Glass': {
        'Product': 'F-2',
        'Storage of Glass': 'S-2',
        'Storage of Glass bottles, empty or filled with noncombustible liquids': 'S-2',
    },
    'Gypsum': {
        'Product': 'F-2',
        'Storage of Gypsum board': 'S-2',
    },
    'Ice': 'F-2',
    'Laundry': 'F-2',
    'Machinery': 'F-2',
    'Mechanical and/or electrical equipment room': 'F-2',
    'Television Filming (without spectators)': 'F-2',
    'Adult Home': {
        'Occupants are capable of self-preservation': 'I-1',
        'Occupants are not capable of self-preservation': 'I-2',
        '16 or fewer occupants requiring supervised care within the same building on a 24-hour basis, provided that the number of occupants per dwelling unit does not exceed the definition of a family': 'R-2',
        '16 or fewer occupants requiring supervised care within the same building on a 24-hour basis': 'R-1',
    },
    'Alcohol & Drug Abuse Rehabilitation Center'
    'Assisted living facilities'
    'Community Residence / Intermediate-Care Facility': {
        'Occupants are capable of self-preservation': 'I-1',
        'Occupants are not capable of self-preservation': 'I-2',
    },
    'Congregate Care Facility': 'I-1',
    'Convalescent Facility': 'I-1',
    'Enriched Housing': {
        'Occupants are capable of self-preservation': 'I-1',
        'Occupants are not capable of self-preservation': 'I-2',
    },
    'Halfway House': 'I-1',
    'Overnight Facility': 'I-1',
    'Residential Care Facility': 'I-1',
    'Social Rehabilitation Facility': 'I-1',
    'Child Care Facility': 'I-2',
    'Detoxification Facility': 'I-2',
    'Hospital': 'I-2',
    'Nursing Home': 'I-2',
    'Psychiatric Center': {
        'Patients are not under restraint': 'I-2',
        'Patients are under restraint': 'I-3',
    },
    'Correctional Center': 'I-3',
    'Detention center': 'I-3',
    'Jail': 'I-3',
    'Prerelease Center': 'I-3',
    'Prison': 'I-3',
    'Reformatory': 'I-3',
    'Department Store': 'M',
    'Drug Store': 'M',
    'Market': 'M',
    'Motor Fuel-dispensing Facility': 'M',
    'Retail / Wholesale Store': 'M',
    'Sales Room': 'M',
    'Class B Multiple Dwelling': 'R-1',
    'Club House': 'R-1',
    'Hotel': 'R-1',
    'Motel': 'R-1',
    'Rooming House': 'R-1',
    'Settlement House': 'R-1',
    'Vacation Timeshare': 'R-1',
    'Dormitory': 'R-1',
    'Fraternity & Sorority House': 'R-1',
    'Homeless Shelter': 'R-1',
    'Apartment House': 'R-2',
    'Apartment hotel': 'R-2',
    'Class A Multiple Dwelling': 'R-2',
    'Convent & Monastery': {
        'More than 20 occupants': 'R-2',
        '20 or fewer occupants': 'R-3',
    },
    'Student Apartment': 'R-2',
    'Group Home': 'R-3',
    'One- and two-family dwelling': 'R-2',
    'Storage of Aerosols': 'S-1',
    'Storage of Bags; cloth, burlap and paper': 'S-1',
    'Storage of Bamboo & Rattan': 'S-1',
    'Storage of Basket': 'S-1',
    'Storage of Belting; canvas and leather': 'S-1',
    'Storage of Books and paper in rolls or packs': 'S-1',
    'Storage of Boots and shoes': 'S-1',
    'Storage of Buttons, including cloth covered, pearl or bone': 'S-1',
    'Storage of Cardboard and cardboard boxes': 'S-1',
    'Storage of Cordage': 'S-1',
    'Storage of Dry boat storage (indoor, not accessory to Group R)': 'S-1',
    'Storage of Fur': 'S-1',
    'Storage of Glues, mucilage, pastes and size': 'S-1',
    'Storage of Grain': 'S-1',
    'Storage of Horns and combs, other than celluloid': 'S-1',
    'Storage of Linoleum': 'S-1',
    'Storage of Lumber': 'S-1',
    'Storage of Photo engravings': 'S-1',
    'Storage of Resilient flooring': 'S-1',
    'Storage of Silk': 'S-1',
    'Storage of Sugar': 'S-1',
    'Storage of Tire': 'S-1',
    'Storage of Upholstery and mattresses': 'S-1',
    'Storage of Wax Candles': 'S-1',
    'Storage of Asbestos': 'S-2',
    'Storage of Cement in bags': 'S-2',
    'Storage of Chalk and crayons': 'S-2',
    'Storage of Dairy products in nonwaxed coated paper containers': 'S-2',
    'Storage of Dry cell batteries': 'S-2',
    'Storage of Electrical coils': 'S-2',
    'Storage of Electrical motors': 'S-2',
    'Storage of Empty cans': 'S-2',
    'Storage of Food products': 'S-2',
    'Storage of Foods in noncombustible containers': 'S-2',
    'Storage of Fresh fruits and vegetables in nonplastic trays or containers': 'S-2',
    'Storage of Frozen foods': 'S-2',
    'Storage of Inert pigment': 'S-2',
    'Storage of Ivory': 'S-2',
    'Storage of Meats': 'S-2',
    'Storage of Metal cabinets': 'S-2',
    'Storage of Metal desks with plastic tops and trim': 'S-2',
    'Storage of Metal parts': 'S-2',
    'Storage of Metals': 'S-2',
    'Storage of Mirrors': 'S-2',
    'Storage of Oil-filled and other types of distribution transformers': 'S-2',
    'Storage of Parking garages, open or enclosed': 'S-2',
    'Storage of Porcelain and pottery': 'S-2',
    'Storage of Stoves': 'S-2',
    'Storage of Talc and soapstones': 'S-2',
    'Storage of Washers and dryers': 'S-2',
    'Carport': 'U',
    'Fences more than 6 feet (1829 mm) in height': 'U',
    'Private Garages': 'U',
    'Retaining wall': 'U',
    'Tank': 'U',
    'Tower': 'U',
}

building_class = {
    'C3': {
        'Occupancy Use': ['R-3'],
        'Sprinkler': 'S-13R',
        'Construction Type': 'Type IIIA'
    }
}

building_height = {
    "A-1": {
        "NS": {
            "Type I": {
                "A": "Unlimited",
                "B": 160,
            },
            "Type II": {
                "A": 65,
                "B": 55
            },
            "Type III": {
                "A": 65,
                "B": 55, # not permitted in fire district without sprinkler
            },
            "Type IV": {
                "HT": 65,
            },
            "Type V": { # not permitted in fire district
                "A": 50,
                "B": 40,
            },
        },
        "S": {
            "Type I": {
                "A": "Unlimited",
                "B": 420,
            },
            "Type II": {
                "A": 85,
                "B": 75
            },
            "Type III": {
                "A": 85,
                "B": 75,
            },
            "Type IV": {
                "HT": 85,
            },
            "Type V": { # not permitted in fire district
                "A": 70,
                "B": 60,
            },
        },
    },
    "A-2": {
        "NS": {
            "Type I": {
                "A": "Unlimited",
                "B": 160,
            },
            "Type II": {
                "A": 65,
                "B": 55
            },
            "Type III": {
                "A": 65,
                "B": 55, # not permitted in fire district without sprinkler
            },
            "Type IV": {
                "HT": 65,
            },
            "Type V": { # not permitted in fire district
                "A": 50,
                "B": 40,
            },
        },
        "S": {
            "Type I": {
                "A": "Unlimited",
                "B": 420,
            },
            "Type II": {
                "A": 85,
                "B": 75
            },
            "Type III": {
                "A": 85,
                "B": 75,
            },
            "Type IV": {
                "HT": 85,
            },
            "Type V": { # not permitted in fire district
                "A": 70,
                "B": 60,
            },
        },
    },
    "A-3": {
        "NS": {
            "Type I": {
                "A": "Unlimited",
                "B": 160,
            },
            "Type II": {
                "A": 65,
                "B": 55
            },
            "Type III": {
                "A": 65,
                "B": 55, # not permitted in fire district without sprinkler
            },
            "Type IV": {
                "HT": 65,
            },
            "Type V": { # not permitted in fire district
                "A": 50,
                "B": 40,
            },
        },
        "S": {
            "Type I": {
                "A": "Unlimited",
                "B": 420,
            },
            "Type II": {
                "A": 85,
                "B": 75
            },
            "Type III": {
                "A": 85,
                "B": 75,
            },
            "Type IV": {
                "HT": 85,
            },
            "Type V": { # not permitted in fire district
                "A": 70,
                "B": 60,
            },
        },
    },
    "A-4": {
        "NS": {
            "Type I": {
                "A": "Unlimited",
                "B": 160,
            },
            "Type II": {
                "A": 65,
                "B": 55
            },
            "Type III": {
                "A": 65,
                "B": 55, # not permitted in fire district without sprinkler
            },
            "Type IV": {
                "HT": 65,
            },
            "Type V": { # not permitted in fire district
                "A": 50,
                "B": 40,
            },
        },
        "S": {
            "Type I": {
                "A": "Unlimited",
                "B": 420,
            },
            "Type II": {
                "A": 85,
                "B": 75
            },
            "Type III": {
                "A": 85,
                "B": 75,
            },
            "Type IV": {
                "HT": 85,
            },
            "Type V": { # not permitted in fire district
                "A": 70,
                "B": 60,
            },
        },
    },
    "A-5": {
        "NS": {
            "Type I": {
                "A": "Unlimited",
                "B": 160,
            },
            "Type II": {
                "A": 65,
                "B": 55
            },
            "Type III": {
                "A": 65,
                "B": 55,
            },
            "Type IV": {
                "HT": 65,
            },
            "Type V": { # not permitted in fire district
                "A": 50,
                "B": 40,
            },
        },
        "S": {
            "Type I": {
                "A": "Unlimited",
                "B": 420,
            },
            "Type II": {
                "A": 85,
                "B": 75
            },
            "Type III": {
                "A": 85,
                "B": 75,
            },
            "Type IV": {
                "HT": 85,
            },
            "Type V": { # not permitted in fire district
                "A": 70,
                "B": 60,
            },
        },
    },
    "B": {
        "NS": {
            "Type I": {
                "A": "Unlimited",
                "B": 160,
            },
            "Type II": {
                "A": 65,
                "B": 55
            },
            "Type III": {
                "A": 65,
                "B": 55, # not permitted in fire district without sprinkler
            },
            "Type IV": {
                "HT": 65,
            },
            "Type V": { # not permitted in fire district
                "A": 50,
                "B": 40,
            },
        },
        "S": {
            "Type I": {
                "A": "Unlimited",
                "B": 420,
            },
            "Type II": {
                "A": 85,
                "B": 75
            },
            "Type III": {
                "A": 85,
                "B": 75,
            },
            "Type IV": {
                "HT": 85,
            },
            "Type V": { # not permitted in fire district
                "A": 70,
                "B": 60,
            },
        },
    },
    "E": {
        "NS": {
            "Type I": {
                "A": "Unlimited",
                "B": 160,
            },
            "Type II": {
                "A": 65,
                "B": 55
            },
            "Type III": {
                "A": 65,
                "B": 55, # not permitted in fire district without sprinkler
            },
            "Type IV": {
                "HT": 65,
            },
            "Type V": { # not permitted in fire district
                "A": 50,
                "B": 40,
            },
        },
        "S": {
            "Type I": {
                "A": "Unlimited",
                "B": 420,
            },
            "Type II": {
                "A": 85,
                "B": 75
            },
            "Type III": {
                "A": 85,
                "B": 75,
            },
            "Type IV": {
                "HT": 85,
            },
            "Type V": { # not permitted in fire district
                "A": 70,
                "B": 60,
            },
        },
    },
    "F-1": {
        "NS": {
            "Type I": {
                "A": "Unlimited",
                "B": 160,
            },
            "Type II": {
                "A": 65,
                "B": 55, # not permitted in fire district without sprinkler
            },
            "Type III": {
                "A": 65,
                "B": 55 # not permitted in fire district
            },
            "Type IV": {
                "HT": 65,
            },
            "Type V": { # not permitted in fire district
                "A": 50,
                "B": 40,
            },
        },
        "S": {
            "Type I": {
                "A": "Unlimited",
                "B": 420,
            },
            "Type II": {
                "A": 85,
                "B": 75
            },
            "Type III": {
                "A": 85,
                "B": 75, # not permitted in fire district
            },
            "Type IV": {
                "HT": 85,
            },
            "Type V": { # not permitted in fire district
                "A": 70,
                "B": 60,
            },
        },
    },
    "F-2": {
        "NS": {
            "Type I": {
                "A": "Unlimited",
                "B": 160,
            },
            "Type II": {
                "A": 65,
                "B": 55
            },
            "Type III": {
                "A": 65,
                "B": 55, # not permitted in fire district without sprinkler
            },
            "Type IV": {
                "HT": 65,
            },
            "Type V": { # not permitted in fire district
                "A": 50,
                "B": 40,
            },
        },
        "S": {
            "Type I": {
                "A": "Unlimited",
                "B": 420,
            },
            "Type II": {
                "A": 85,
                "B": 75
            },
            "Type III": {
                "A": 85,
                "B": 75,
            },
            "Type IV": {
                "HT": 85,
            },
            "Type V": { # not permitted in fire district
                "A": 70,
                "B": 60,
            },
        },
    },
    "H-1": {
        "S": { # not permitted in fire district
            "Type I": {
                "A": "Unlimited",
                "B": 160,
            },
            "Type II": {
                "A": 65,
                "B": 55,
            },
            "Type III": {
                "A": 65,
                "B": 55,
            },
            "Type IV": {
                "HT": 65,
            },
            "Type V": {
                "A": 50,
                "B": 'Not Permitted',
            },
        },
    },
    "H-2": {
        "S": {
            "Type I": {
                "A": "Unlimited",
                "B": 160,
            },
            "Type II": {
                "A": 65,
                "B": 55
            },
            "Type III": {
                "A": 65,
                "B": 55,
            },
            "Type IV": {
                "HT": 65,
            },
            "Type V": { # not permitted in fire district
                "A": 50,
                "B": 'Not Permitted',
            },
        },  
    },
    "H-3": {
        "S": {
            "Type I": {
                "A": "Unlimited",
                "B": 160,
            },
            "Type II": {
                "A": 65,
                "B": 55
            },
            "Type III": {
                "A": 65,
                "B": 55,
            },
            "Type IV": {
                "HT": 65,
            },
            "Type V": { # not permitted in fire district
                "A": 50,
                "B": 'Not Permitted',
            },
        },  
    },
    "H-4": {
        "S": {
            "Type I": {
                "A": "Unlimited",
                "B": 180,
            },
            "Type II": {
                "A": 85,
                "B": 75
            },
            "Type III": {
                "A": 85,
                "B": 75,
            },
            "Type IV": {
                "HT": 85,
            },
            "Type V": { # not permitted in fire district
                "A": 70,
                "B": 60,
            },
        },  
    },
    "H-5": {
        "S": {
            "Type I": {
                "A": "Unlimited",
                "B": 160,
            },
            "Type II": {
                "A": 65,
                "B": 55
            },
            "Type III": {
                "A": 65,
                "B": 55,
            },
            "Type IV": {
                "HT": 65,
            },
            "Type V": { # not permitted in fire district
                "A": 50,
                "B": 'Not Permitted',
            },
        },  
    },
    "I-1": {
        "S-13D": {
            "Type I": {
                "A": 60,
                "B": 60,
            },
            "Type II": {
                "A": 60,
                "B": 'Not Permitted'
            },
            "Type III": {
                "A": 60,
                "B": 55, # not permitted in fire district
            },
            "Type IV": {
                "HT": 60,
            },
            "Type V": {
                "A": 'Not Permitted',
                "B": 'Not Permitted',
            },
        },
        "S-13R": {
            "Type I": {
                "A": 60,
                "B": 60,
            },
            "Type II": {
                "A": 60,
                "B": 'Not Permitted'
            },
            "Type III": {
                "A": 60,
                "B": 55, # not permitted in fire district
            },
            "Type IV": {
                "HT": 60,
            },
            "Type V": {
                "A": 'Not Permitted',
                "B": 'Not Permitted',
            },
        },
        "S": {
            "Type I": {
                "A": "Unlimited",
                "B": 420,
            },
            "Type II": {
                "A": 85,
                "B": 'Not Permitted',
            },
            "Type III": {
                "A": 85,
                "B": 75, # not permitted in fire district
            },
            "Type IV": {
                "HT": 85,
            },
            "Type V": {
                "A": 'Not Permitted',
                "B": 'Not Permitted',
            },
        },
    },
    "I-2": {
        "S": {
            "Type I": {
                "A": "Unlimited",
                "B": 180,
            },
            "Type II": {
                "A": 85,
                "B": 55,
            },
            "Type III": {
                "A": 65,
                "B": 55, # not permitted in fire district
            },
            "Type IV": {
                "HT": 65,
            },
            "Type V": {
                "A": 50, # not permitted in fire district
                "B": 'Not Permitted',
            },
        },
    },
    "I-3": {
        "S": {
            "Type I": {
                "A": "Unlimited",
                "B": 180,
            },
            "Type II": {
                "A": 85,
                "B": 75,
            },
            "Type III": {
                "A": 85,
                "B": 75,
            },
            "Type IV": {
                "HT": 85,
            },
            "Type V": {
                "A": 70, # not permitted in fire district
                "B": 'Not Permitted',
            },
        },
    },
    "I-4": {
        "NS": {
            "Type I": {
                "A": "Unlimited",
                "B": 160,
            },
            "Type II": {
                "A": 65,
                "B": 55
            },
            "Type III": {
                "A": 65,
                "B": 55,
            },
            "Type IV": {
                "HT": 65,
            },
            "Type V": { # not permitted in fire district
                "A": 50,
                "B": 40,
            },
        },
        "S": {
            "Type I": {
                "A": "Unlimited",
                "B": 420,
            },
            "Type II": {
                "A": 85,
                "B": 75
            },
            "Type III": {
                "A": 85,
                "B": 75,
            },
            "Type IV": {
                "HT": 85,
            },
            "Type V": { # not permitted in fire district
                "A": 70,
                "B": 60,
            },
        },
    },
    "M": {
        "NS": {
            "Type I": {
                "A": "Unlimited",
                "B": 160,
            },
            "Type II": {
                "A": 65,
                "B": 55
            },
            "Type III": {
                "A": 65,
                "B": 55, # not permitted in fire district without sprinkler
            },
            "Type IV": {
                "HT": 65,
            },
            "Type V": { # not permitted in fire district
                "A": 50,
                "B": 40,
            },
        },
        "S": {
            "Type I": {
                "A": "Unlimited",
                "B": 420,
            },
            "Type II": {
                "A": 85,
                "B": 75
            },
            "Type III": {
                "A": 85,
                "B": 75,
            },
            "Type IV": {
                "HT": 85,
            },
            "Type V": { # not permitted in fire district
                "A": 70,
                "B": 60,
            },
        },
    },
    "R-1": {
        "S-13R": {
            "Type I": {
                "A": 60,
                "B": 60,
            },
            "Type II": {
                "A": 60,
                "B": 'Not Permitted'
            },
            "Type III": {
                "A": 60,
                "B": 'Not Permitted'
            },
            "Type IV": {
                "HT": 60,
            },
            "Type V": {
                "A": 'Not Permitted',
                "B": 'Not Permitted',
            },
        },
        "S": {
            "Type I": {
                "A": "Unlimited",
                "B": 420,
            },
            "Type II": {
                "A": 85,
                "B": 'Not Permitted',
            },
            "Type III": {
                "A": 85,
                "B": 'Not Permitted',
            },
            "Type IV": {
                "HT": 85,
            },
            "Type V": {
                "A": 'Not Permitted',
                "B": 'Not Permitted',
            },
        },
    },
    "R-2": {
        "S-13R": {
            "Type I": {
                "A": 60,
                "B": 60,
            },
            "Type II": {
                "A": 60,
                "B": 'Not Permitted'
            },
            "Type III": {
                "A": 60,
                "B": 60,
            },
            "Type IV": {
                "HT": 60,
            },
            "Type V": {
                "A": 'Not Permitted',
                "B": 'Not Permitted',
            },
        },
        "S": {
            "Type I": {
                "A": "Unlimited",
                "B": 420,
            },
            "Type II": {
                "A": 85,
                "B": 'Not Permitted',
            },
            "Type III": {
                "A": 85,
                "B": 75,
            },
            "Type IV": {
                "HT": 85,
            },
            "Type V": {
                "A": 'Not Permitted',
                "B": 'Not Permitted',
            },
        },
    },
    "R-3": {
        "NS": {
            "Type I": {
                "A": "Unlimited",
                "B": 160,
            },
            "Type II": {
                "A": 65,
                "B": 55
            },
            "Type III": {
                "A": 65,
                "B": 55, # not permitted in fire district without sprinkler
            },
            "Type IV": {
                "HT": 65,
            },
            "Type V": { # not permitted in fire district
                "A": 50,
                "B": 40,
            },
        },
        "S-13D": {
            "Type I": {
                "A": 60,
                "B": 60,
            },
            "Type II": {
                "A": 60,
                "B": 60,
            },
            "Type III": {
                "A": 60,
                "B": 55,
            },
            "Type IV": {
                "HT": 60,
            },
            "Type V": { # not permitted in fire district
                "A": 50,
                "B": 40,
            },
        },
        "S-13R": {
            "Type I": {
                "A": 60,
                "B": 60,
            },
            "Type II": {
                "A": 60,
                "B": 60,
            },
            "Type III": {
                "A": 60,
                "B": 60,
            },
            "Type IV": {
                "HT": 60,
            },
            "Type V": { # not permitted in fire district
                "A": 60,
                "B": 60,
            },
        },
        "S": {
            "Type I": {
                "A": "Unlimited",
                "B": 420,
            },
            "Type II": {
                "A": 85,
                "B": 75,
            },
            "Type III": {
                "A": 85,
                "B": 75,
            },
            "Type IV": {
                "HT": 85,
            },
            "Type V": { # not permitted in fire district
                "A": 70,
                "B": 60,
            },
        },
    },
    "S-1": {
        "NS": {
            "Type I": {
                "A": "Unlimited",
                "B": 160,
            },
            "Type II": {
                "A": 65,
                "B": 55, # not permitted in fire district without sprinkler
            },
            "Type III": {
                "A": 65,
                "B": 55 # not permitted in fire district
            },
            "Type IV": {
                "HT": 65,
            },
            "Type V": { # not permitted in fire district
                "A": 50,
                "B": 40,
            },
        },
        "S": {
            "Type I": {
                "A": "Unlimited",
                "B": 180,
            },
            "Type II": {
                "A": 85,
                "B": 75
            },
            "Type III": {
                "A": 85,
                "B": 75, # not permitted in fire district
            },
            "Type IV": {
                "HT": 85,
            },
            "Type V": { # not permitted in fire district
                "A": 70,
                "B": 60,
            },
        },
    },
    "S-2": {
        "NS": {
            "Type I": {
                "A": "Unlimited",
                "B": 160,
            },
            "Type II": {
                "A": 65,
                "B": 55
            },
            "Type III": {
                "A": 65,
                "B": 55, # not permitted in fire district without sprinkler
            },
            "Type IV": {
                "HT": 65,
            },
            "Type V": { # not permitted in fire district
                "A": 50,
                "B": 40,
            },
        },
        "S": {
            "Type I": {
                "A": "Unlimited",
                "B": 420,
            },
            "Type II": {
                "A": 85,
                "B": 75,
            },
            "Type III": {
                "A": 85,
                "B": 75,
            },
            "Type IV": {
                "HT": 85,
            },
            "Type V": { # not permitted in fire district
                "A": 70,
                "B": 60,
            },
        },
    },
    "U": {
        "NS": {
            "Type I": {
                "A": "Unlimited",
                "B": 160,
            },
            "Type II": {
                "A": 65,
                "B": 55,
            },
            "Type III": {
                "A": 65,
                "B": 55,
            },
            "Type IV": {
                "HT": 65,
            },
            "Type V": { # not permitted in fire district
                "A": 50,
                "B": 40,
            },
        },
        "S": {
            "Type I": {
                "A": "Unlimited",
                "B": 180,
            },
            "Type II": {
                "A": 85,
                "B": 75
            },
            "Type III": {
                "A": 85,
                "B": 75,
            },
            "Type IV": {
                "HT": 85,
            },
            "Type V": { # not permitted in fire district
                "A": 70,
                "B": 60,
            },
        },
    },
}

num_stories = {
    "R-3": {
        "S-13R": {
            "Type I": {
                "A": 6,
                "B": 6,
            },
            "Type II": {
                "A": 6,
                "B": 4,
            },
            "Type III": {
                "A": 6,
                "B": 4,
            },
            "Type IV": {
                "HT": 6,
            },
            "Type V": { # not permitted in fire district
                "A": 4,
                "B": 4,
            },
        },
   },
}

allowable_area_factor = {
    "R-3": {
        "NS": {
            "Type I": {
                "A": 'Unlimited',
                "B": 'Unlimited',
            },
            "Type II": {
                "A": 17500,
                "B": 10500,
            },
            "Type III": {
                "A": 14700,
                "B": 5600, # not permitted in fire district without sprinklers
            },
            "Type IV": {
                "HT": 30000,
            },
            "Type V": { # not permitted in fire district
                "A": 8400,
                "B": 5500,
            },
        },
        "S-13R": {
            "Type I": {
                "A": 'Unlimited',
                "B": 'Unlimited',
            },
            "Type II": {
                "A": 17500,
                "B": 10500,
            },
            "Type III": {
                "A": 14700,
                "B": 5600,
            },
            "Type IV": {
                "HT": 30000,
            },
            "Type V": { # not permitted in fire district
                "A": 8400,
                "B": 5500,
            },
        },
   },
}