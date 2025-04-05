import os, time, requests, json
import pandas as pd

from legend import *

def geoservice (address = '', street = '', borough = '', zipcode = '', unit = '', block = '', lot = '', bin = ''):
    url = 'https://geoservice.planning.nyc.gov/geoservice/geoservice.svc'
    with open('config.json', 'r') as config_file:
        key = json.load(config_file)['geoserviceKey']

    if address and street and borough and zipcode:
        if unit: call = f'/Function_1B?AddressNo={address}&StreetName={street}&Unit={unit}&Borough={borough}&ZipCode={zipcode}&Key={key}'
        else: call = f'/Function_1B?AddressNo={address}&StreetName={street}&Borough={borough}&ZipCode={zipcode}&Key={key}'
    elif borough and block and lot:
        call = f'/Function_BBL?Borough={borough}&Block={block}&Lot={lot}&Key={key}'
    elif bin:
        call = f'/Function_BIN?BIN={bin}&Key={key}'
    else: raise ValueError("Failed to retrieve data")

    response = requests.get(url + call)
    if response.status_code == 200:
        data = response.json()
        if data['root'] == None: data = data['display']
    else: raise ValueError(f"Failed to retrieve data: {response.status_code}")
    return data

def getData (address = '', street = '', borough = '', zipcode = '', unit = '', block = '', lot = '', bin = '', numStories = 1):
    data = geoservice(address = address, street = street, borough = borough, zipcode = zipcode, unit = unit, block = block, lot = lot, bin = bin)

    with open('{}.json'.format('zoningData'), 'w') as file:
        json.dump(data, file, indent = 4)

    bbl = int(data['out_bbl'])
    bldgClass = data['out_rpad_bldg_class']
    commDistrict = data['out_cdta_2020']
    zone = data['out_dcp_zoning_map']

    zoningDB = pd.read_csv('data/Zoning/Zoning Tax Lot Database (20250131).csv', low_memory = False)
    zoningDistrict = zoningDB[zoningDB.BBL == bbl]['Zoning District 1'].reset_index(drop = True)[0]
    print('Zoning District:', zoningDistrict)

    # user should be able to change this
    use = building_class[bldgClass]['Occupancy Use']
    print('Occupancy Use:', ', '.join(use))
    if use[0][0] == 'R' and (zoningDistrict[:2] != 'M1' or zoningDistrict[-1] != 'D'):
        raise ValueError(f'Residential use not permitted in the zoning district {zoningDistrict}')

    # user should be able to change this
    sprinkler = building_class[bldgClass]['Sprinkler']
    print('Sprinkler Type:', sprinkler)

    # user should be able to change this
    constructionType = building_class[bldgClass]['Construction Type']
    print('Construction Type:', constructionType)

    FAR = zoning_district[zoningDistrict[:4]]['FAR']
    print('Maximum FAR:', FAR)
    buildingHeight = building_height[use[0]][sprinkler][constructionType[:-2]][constructionType[-1]]
    print('Maximum Building Height:', buildingHeight, 'feet')
    maxStories = num_stories[use[0]][sprinkler][constructionType[:-2]][constructionType[-1]]
    print('Maximum Stories Permitted:', maxStories)
    AAF = allowable_area_factor[use[0]][sprinkler][constructionType[:-2]][constructionType[-1]]
    if len(use) == 1 and numStories > 1:
        areaIncreaseFactor = 0
        NSFactor = allowable_area_factor[use[0]]['NS'][constructionType[:-2]][constructionType[-1]]
        allowableArea = AAF + (NSFactor * areaIncreaseFactor)
    print('Allowable Area:', allowableArea, 'SF')

    # links
    siteModel = f'https://www.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyc-3d-model/nyc_3dmodel_{commDistrict}.zip'
    digitalTaxMap = f'https://propertyinformationportal.nyc.gov/parcels/parcel/{bbl}'
    zoningDistrictInfo = f'https://www.nyc.gov/site/planning/zoning/districts-tools/{zoningDistrict[:2]}.page'
    zoningMap = f'https://s-media.nyc.gov/agencies/dcp/assets/files/pdf/zoning/zoning-maps/map{zone}.pdf'
    historicalZoningMaps = f'https://s-media.nyc.gov/agencies/dcp/assets/files/pdf/zoning/zoning-maps/maps{zone}.pdf'

if __name__ == '__main__':
    # start = time.time()

    data = getData(164, '35 Street', 'Brooklyn', 11232, numStories = 4)
    # data = getData(borough = 'Brooklyn', block = 692, lot = 32, numStories = 4)
    # data = getData(bin = 3010256, numStories = 4)

    # end = time.time()
    # print("Runtime: {}".format(end - start))