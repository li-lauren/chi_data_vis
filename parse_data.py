import json

id = 1

notice_data = {
        "type": "FeatureCollection",

        "features": []
    }

for csv_file in ['data/chicago_public_urination.csv', 'data/chicago_public_urination_2.csv']:
    with open(csv_file, 'r') as f:
        lines = f.readlines()[1:]

        for line in lines:
            line_s = line.split(",")
            if 'UNKNOWN' not in line_s[2]:
                notice_data['features'].append({
                    "type": "Feature", 
                    "id": id,
                    "properties": {
                        "NOV_DATE": line_s[0],
                        "NOV_NUM": line_s[1],
                        "STR_ADDRESS": line_s[2],
                        "DESC": line_s[5],
                        "LATITUDE": line_s[6],
                        "LONGITUDE": line_s[7]
                    },
                    "geometry": {
                        "type": "Point",
                        "coordinates": [line_s[7], line_s[6]]
                    }
                })
                id += 1

with open('data/chicago_public_urination.json', 'w') as outfile:
    json.dump(notice_data, outfile, indent=4)