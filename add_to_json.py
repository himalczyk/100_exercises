import json

with open ('company2.json', 'r+') as jsonfile:
    json_file_formatted = json.load(jsonfile)
    json_file_formatted['employees'].append({'firstName':'Albert', 'lastName':'Bert'})
    jsonfile.seek(0)
    json.dump(json_file_formatted, jsonfile, indent=4)
    
    

