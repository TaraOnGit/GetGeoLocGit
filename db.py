import json
class Database:
    def insert(self, name,email,password):

        with open('users.json' , 'r') as rf:
            users_data = json.load(rf)

            if email in users_data :
                return 1
            else :
                users_data[email] = [name, password]
                with open('users.json', 'w') as wf:
                    json.dump(users_data,wf,indent=4)
                    return 0

    def search(self,email,password):
        with open('users.json', 'r') as rf:
            users_data = json.load(rf)

            if email in users_data:
                if users_data[email][1] == password :
                    return 1
                else :
                    return 0
            else :
                return 0
