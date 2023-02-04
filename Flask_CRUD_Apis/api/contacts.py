from flask_restful import Resource
from flask import request
from .utils import gen_id
import json

class Items(Resource):
    def get(self):
        data_dict={}
        count=1
        with open('contacts.json', 'r') as file:
            file_data = file.readlines()
            if not file_data:
                return {"message" : "No records found ! Add some new records"}
            for i in file_data:
                data_dict[count] = json.loads(i)
                count += 1
        return data_dict

    def post(self):
        data = request.json
        data['contact_id'] = gen_id()
        with open('contacts.json', 'a') as file:
            file.write(f'{json.dumps(data)}\n')
        return {"status":200,"message":f"Contact with name '{data['name']}' created with id = '{data['contact_id']}'"},200
    
    def delete(self):
        data = request.json
        with open('contacts.json', 'r+') as file:
            file_data = file.readlines()

            if file_data:
                for i in file_data:
                    if len(i)>1:
                        var = json.loads(i)
                        if var['contact_id'] == str(data['contact_id']):
                            file_data.pop(file_data.index(i))
                            file.seek(0)
                            file.writelines(file_data)
                            file.truncate()
                            return {"message" : f"Contact '{var['name']}' deleted !!"}
                    else:
                        continue

                return {"message" : f"Contact '{var['name']}' Not Found !!"}
            else:
                return {"message" : "All Contacts deleted !!"}

    def put(self):
        data = request.json

        dict_info = data['update']

        with open('contacts.json', 'r+') as file:
            file_data = file.readlines()

            if file_data:
                for i in file_data:
                    if len(i)>1:
                        var = json.loads(i)
                        if var['contact_id'] == str(data['contact_id']):
                            
                            var['name'] = dict_info.get('name', var['name'])
                            var['mobile_number'] = dict_info.get('mobile_number', var['mobile_number'])
                            var['email'] = dict_info.get('email', var['email'])
                            var['note'] = dict_info.get('note', var['note'])
                            file_data.pop(file_data.index(i))
                            file_data.append(json.dumps(var)+"\n")
                            file.seek(0)
                            file.writelines(file_data)
                            file.truncate()


                            return {"message" : f"Updated Contact '{var['contact_id']}' successfully !!"}
                    else:
                        continue

                return {"message" : f"Contact '{var['name']}' Not Found !!"}
            else:
                return {"message" : "No contacts found !!"}



class Item(Resource):
    def get(self, pk):
        with open('contacts.json', 'r') as file:
            file_data = file.readlines()
            for i in file_data:
                var = json.loads(i)
                if var['contact_id'] == str(pk):
                    return var
            return {"message" : "No record found for given ID !"}, 404

    


    
