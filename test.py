import json
import requests

# create user
user = {
  "id": 635421,
  "username": "NataSu",
  "firstName": "Natalia",
  "lastName": "Sukortseva",
  "email": "natasu@sumail.ru",
  "password": "963852741",
  "phone": "89114512651",
  "userStatus": 0
}
res_add_user = requests.post('https://petstore.swagger.io/v2/user', data=json.dumps(user, ensure_ascii=False), headers={'accept': 'application/json', 'Content-Type': 'application/json'})
print(f'Статус кода POST: {res_add_user}')
print(res_add_user.json())


# search by user's name
get_user_name = 'NataSu'
res_get_user_name = requests.get(f'https://petstore.swagger.io/v2/user/{get_user_name}', headers={'accept': 'application/json'})
print(f'Статус кода GET: {res_get_user_name}')
print(res_get_user_name.json())

# change of user's name
user_name = 'NataSu'
put_user = {
  "id": 635421,
  "username": "NataSun",
  "firstName": "Nata",
  "lastName": "Su",
  "email": "natasu@sumail.ru",
  "password": "963852741",
  "phone": "89114512651",
  "userStatus": 0
}
res_put_user = requests.put(f'https://petstore.swagger.io/v2/user/{user_name}', data=json.dumps(put_user, ensure_ascii=False),
                            headers={'accept': 'application/json', 'Content-Type': 'application/json'})
print(f'Статус кода PUT: {res_put_user}')
print(res_put_user.json())

# deleting the user
delete_user = 'NataSun'
res_delete_user = requests.delete(f'https://petstore.swagger.io/v2/user/{delete_user}',
                            headers={'accept': 'application/json'})
print(f'Статус кода DELETE: {res_delete_user}')
print(res_delete_user.json())





# finding all pets
status = {'status': ['available', 'pending', 'sold']}
res_get_pets = requests.get('https://petstore.swagger.io/v2/pet/findByStatus', params=status, headers={'accept': 'application/json'})
print(f'Статус кода GET: {res_get_pets}')
print(res_get_pets.json())

# change name and status by id
id_pet = '9223372036854774872'
new_info = {'name': 'Snake', 'status': 'pending'}
res_post_pet = requests.post(f'https://petstore.swagger.io/v2/pet/{id_pet}', data=new_info, headers={'accept': 'application/json'})
print(f'Статус кода POST: {res_post_pet}')
print(res_post_pet.json())

# search pet by "id"
id_pet = '9223372036854774872'
res_get_pet_id = requests.get(f'https://petstore.swagger.io/v2/pet/{id_pet}', headers={'accept': 'application/json'})
print(f'Статус кода GET: {res_get_pet_id}')
print(res_get_pet_id.json())

# adding  a photo of the pet
files = {'file': open('snake.jpg.', 'rb')}
id_pet = '9223372036854774872'
res_post_pet_file = requests.post(f'https://petstore.swagger.io/v2/pet/{id_pet}/uploadImage', files=files, headers={'accept': 'application/json'})
print(f'Статус кода POST: {res_post_pet_file}')
print(res_post_pet_file.json())

# deleting the user
api_key = '123456789'
id_pet = '9223372036854774872'
res_delete_pet = requests.delete(f'https://petstore.swagger.io/v2/pet/{id_pet}', headers={'accept': 'application/json'})
print(f'Статус кода DELETE: {res_delete_pet}')
print(res_delete_pet.json())
