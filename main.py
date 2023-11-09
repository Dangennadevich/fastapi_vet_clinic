from enum import Enum
from fastapi import FastAPI, Query
from pydantic import BaseModel
from datetime import datetime
from fastapi.responses import JSONResponse
from typing import List

app = FastAPI()


class DogType(str, Enum):
    terrier = "terrier"
    bulldog = "bulldog"
    dalmatian = "dalmatian"


class Dog(BaseModel):
    name: str
    pk: int
    kind: DogType


class Timestamp(BaseModel):
    id: int
    timestamp: int


dogs_db = {
    0: Dog(name='Bob', pk=0, kind='terrier'),
    1: Dog(name='Marli', pk=1, kind="bulldog"),
    2: Dog(name='Snoopy', pk=2, kind='dalmatian'),
    3: Dog(name='Rex', pk=3, kind='dalmatian'),
    4: Dog(name='Pongo', pk=4, kind='dalmatian'),
    5: Dog(name='Tillman', pk=5, kind='bulldog'),
    6: Dog(name='Uga', pk=6, kind='bulldog')
}

post_db = [
    Timestamp(id=0, timestamp=12),
    Timestamp(id=1, timestamp=10)
]


class Dogs(BaseModel):
    name: str
    pk: int
    kind: str

class G_post(BaseModel):
    id: int
    timestamp: int




@app.get('/'
    , operation_id="root__get"
    , summary="Root"
    , responses={200: {"description": "Successful Response"}})
def root():
    '''
    :return: json with default info
    '''

    h = datetime.now().hour
    m = datetime.now().minute

    content = {
        'message': "Veterinary clinic",
        "Current time": f'{h}:{m}'
    }

    return JSONResponse(content=content)






@app.post("/post"
    , operation_id="get_post_post_post"
    , summary="Get Post"
    , response_model=List[G_post]
    , responses={200: {"description": "Successful Response"}})
def post(data: dict):
    '''
    id -> integer,
    Timestamp: integer

    :return: json of added data
    '''
    data['id']: int
    data['Timestamp']: int

    id = data['id']
    tstamp = data['Timestamp']

    post_db.append(Timestamp(id=id, timestamp=tstamp))

    data["status"] = "insertet in DB"
    content = data
    return JSONResponse(content=content)  # post_db



@app.get("/dog"
    , operation_id="get_dogs_dog_get"
    , summary="Get Dogs"
    , response_model=List[Dogs]
    , responses={
        200: {"description": "Successful Response"},
        422: {"description": "Validation Error"}
    })
def get_dog(data: dict): #QueryParams
    '''
        Available values : terrier, bulldog, dalmatian

        kind -> string

        Example
        {"kind": "dalmatian"}
    '''
    list_dogs = list()

    value = data['kind']

    if value == 'bulldog':
        dog_class = DogType.bulldog
    elif value == 'terrier':
        dog_class = DogType.terrier
    elif value == 'dalmatian':
        dog_class = DogType.bulldog
    else:
        return 'not avaliable dog type'

    filtered_dogs = {key: dog for key, dog in dogs_db.items() if dog.kind == dog_class}

    for key in filtered_dogs.keys():
        json_dog = {
            "name": filtered_dogs[key].name,
            "pk": filtered_dogs[key].pk,
            "kind": value
        }
        list_dogs.append(json_dog)

    return JSONResponse(content=list_dogs)




@app.post("/dog"
    , operation_id="create_dog_dog_post"
    , response_model=List[Dogs]
    , summary="Create Dog"
    , responses={200: {"description": "Successful Response"}, 422: {"description": "Validation Error"}}
          )
def post(data: dict):
    '''
    return added dog to db
    '''

    new_dog = Dog(name=data['name'], pk=data['pk'], kind=data['kind'])  # Новая строчка класса Dog
    new_key = max(dogs_db.keys()) + 1  # Ключ для добавления в dogs_db

    # Add dog to db
    dogs_db[new_key] = new_dog

    contetnt = data

    return JSONResponse(content=contetnt)




@app.get("/dog/{pk}"
    , operation_id="get_dog_by_pk_dog__pk__get"
    , response_model=List[Dogs] #
    , responses={
        200: {"description": "Successful Response"},
        422: {"description": "Validation Error"}
    })
def get_dog_pk(pk: int):
    '''
    Get Dog By Pk

    :return: JSON with onfo about dog
    '''

    find_dogs = [[dog.name, dog.pk, dog.kind] for dog in dogs_db.values() if dog.pk == pk]

    if len(find_dogs) == 1:
        find_dogs = find_dogs[0]

        content = {
            "name": find_dogs[0],
            "pk": find_dogs[1],
            "kind": find_dogs[2]
        }
        return JSONResponse(content=content)

    elif len(find_dogs) == 0:
        content = {"error": "no data"}
        return JSONResponse(content=content)  # , dogs_db

    else:
        find_dogs = find_dogs[0]
        content = {
            "name": find_dogs[0],
            "pk": find_dogs[1],
            "kind": find_dogs[2]
        }

        content = {"error": "not uniq pk"}
        return JSONResponse(content=content)




@app.patch("/dog/{pk}"
    , operation_id="update_dog_dog__pk__patch"
    , response_model = List[Dogs]
    , responses={200: {"description": "Successful Response"}, 422: {"description": "Validation Error"}})
def get_dog_pk(data: dict, pk: int):
    '''
    Update Dog

    name -> str,
    pk -> integer,
    kind: str

    :return: JSON updatet info about dog
    '''

    data['name']: str
    data['pk']: 0
    data['kind']: str


    # найдем ключ и объект
    find_dogs = {key: dog for key, dog in dogs_db.items() if dog.pk == pk}

    # выведем ключ
    key = list(find_dogs.keys())[0]

    # обновим данные по нему- кроме айдишника
    dogs_db[key].name = data['name'][0]
    dogs_db[key].kind = DogType(data['kind'])

    json_dog = {
        "name": dogs_db[key].name,
        "pk": dogs_db[key].pk,
        "kind": dogs_db[key].kind
    }

    return JSONResponse(content=json_dog)