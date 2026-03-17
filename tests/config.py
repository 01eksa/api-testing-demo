BASE_URL = 'https://jsonplaceholder.typicode.com/'

METHODS = ['get', 'post', 'put', 'patch', 'delete']

DATA = {
    'albums': {
        'get': [
            {
                "userId": 1,
                "id": 1,
                "title": "quidem molestiae enim"
            },
            {
                "userId": 1,
                "id": 2,
                "title": "sunt qui excepturi placeat culpa"
            },
            {
                "userId": 1,
                "id": 3,
                "title": "omnis laborum odio"
            },
        ],
        'post': [
            {
                "userId": 1,
                "title": "test title 1"
            },
            {
                "userId": 5,
                "title": "looooooooooooooooooooooooooooooooooong test title 2"
            },
            {
                "userId": 10,
                "title": "3"
            },
        ],
        'put': [
            {
                "userId": 2,
                "id": 1,
                "title": "new title 1"
            },
            {
                "userId": 4,
                "id": 2,
                "title": "looooooooooooooooooooooooooooooooooooooooong new title 2"
            },
            {
                "userId": 8,
                "id": 3,
                "title": "3"
            },
        ],
        'patch': [
            {
                "userId": 3,
                "id": 10,
            },
            {
                "id": 20,
                "title": "looooooooooooooooooooooooooooooooooooooooooooooong new title"
            },
            {
                "userId": 8,
                "id": 30,
                "title": "n"
            },
        ],
        'delete': [1, 2, 3, ]
    },
    'comments': {
        'get': [
            {
                "postId": 1,
                "id": 1,
                "name": "id labore ex et quam laborum",
                "email": "Eliseo@gardner.biz",
            },
            {
                "postId": 1,
                "id": 2,
                "name": "quo vero reiciendis velit similique earum",
                "email": "Jayne_Kuhic@sydney.com",
            },
            {
                "postId": 1,
                "id": 3,
                "name": "odio adipisci rerum aut animi",
                "email": "Nikita@garfield.biz",
            },
        ],
        'post': [
            {
                "postId": 1,
                "name": "test name 1",
                "email": "test1@mail.com",
            },
            {
                "postId": 2,
                "name": "looooooooooooooooooooooooooooooooooooooooooooooooooooong test name",
                "email": "test1@mail.com",
            },
            {
                "postId": 3,
                "name": "3",
                "email": "test2@mail.org",
            },
        ],
        'put': [
            {
                "postId": 2,
                "id": 1,
                "name": "new name 1",
                "email": "test1@mail.com",
            },
            {
                "postId": 3,
                "id": 2,
                "name": "loooooooooooooooooooooooooooooooooooooooooooooooooooooooooong new name 2",
                "email": "test2@mail.org",
            },
            {
                "postId": 4,
                "id": 3,
                "name": "3",
                "email": "test2@mail.biz",
            },
        ],
        'patch': [
            {
                "id": 1,
                "name": "new name",
                "email": "new@mail.com",
            },
            {
                "postId": 5,
                "id": 2,
                "email": "new@@mail.org",
            },
            {
                "postId": 6,
                "id": 3,
                "name": "loooooooooooooooooooooooooooooooooooooooong new name",
            },
        ],
        'delete': [1, 2, 3, ]
    },
    'posts': {
        'get': [
            {
                "userId": 1,
                "id": 1,
                "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            },
            {
                "userId": 1,
                "id": 2,
                "title": "qui est esse",
            },
            {
                "userId": 1,
                "id": 3,
                "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
            },
        ],
        'post': [
            {
                "userId": 1,
                "title": "test title 1",
            },
            {
                "userId": 2,
                "title": "looooooooooooooooooooooooooong test title!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
            },
            {
                "userId": 3,
                "title": "t",
            },
        ],
        'put': [
            {
                "userId": 2,
                "id": 1,
                "title": "new title",
            },
            {
                "userId": 3,
                "id": 2,
                "title": "loooooooooooooooooooooooooooooooooooooooooooooong new title",
            },
            {
                "userId": 4,
                "id": 3,
                "title": "3",
            },
        ],
        'patch': [
            {
                "userId": 3,
                "id": 1,
            },
            {
                "userId": 7,
                "id": 2,
                "title": "loooooooooooooooooooooooooooooooooooooooooooooong new title",
            },
            {
                "id": 3,
                "title": "3",
            },
        ],
        'delete': [1, 2, 3, ]
    },
    'photos': {
        'get': [
            {
                "albumId": 1,
                "id": 1,
                "title": "accusamus beatae ad facilis cum similique qui sunt",
                "url": "https://via.placeholder.com/600/92c952",
                "thumbnailUrl": "https://via.placeholder.com/150/92c952"
            },
            {
                "albumId": 1,
                "id": 2,
                "title": "reprehenderit est deserunt velit ipsam",
                "url": "https://via.placeholder.com/600/771796",
                "thumbnailUrl": "https://via.placeholder.com/150/771796"
            },
            {
                "albumId": 1,
                "id": 3,
                "title": "officia porro iure quia iusto qui ipsa ut modi",
                "url": "https://via.placeholder.com/600/24f355",
                "thumbnailUrl": "https://via.placeholder.com/150/24f355"
            },
        ],
        'post': [
            {
                "albumId": 1,
                "title": "test title",
                "url": "https://via.placeholder.com/600/92c952",
                "thumbnailUrl": "https://via.placeholder.com/150/92c952"
            },
            {
                "albumId": 2,
                "title": "looooooooooooooooooooooooooooooooooooooooooong test title!",
                "url": "https://via.placeholder.com/600/771796",
                "thumbnailUrl": "https://via.placeholder.com/150/771796"
            },
            {
                "albumId": 3,
                "title": "3",
                "url": "https://via.placeholder.com/600/24f355",
                "thumbnailUrl": "https://via.placeholder.com/150/24f355"
            },
        ],
        'put': [
            {
                "albumId": 2,
                "id": 1,
                "title": "new title",
                "url": "https://via.placeholder.com/600/1000",
                "thumbnailUrl": "https://via.placeholder.com/150/1000"
            },
            {
                "albumId": 3,
                "id": 2,
                "title": "looooooooooooooooooooooooooooooooooooooooong new title",
                "url": "https://via.placeholder.com/600/1001",
                "thumbnailUrl": "https://via.placeholder.com/150/1001"
            },
            {
                "albumId": 4,
                "id": 3,
                "title": "3",
                "url": "https://via.placeholder.com/600/1002",
                "thumbnailUrl": "https://via.placeholder.com/150/1002"
            },
        ],
        'patch': [
            {
                "albumId": 3,
                "id": 1,
            },
            {
                "id": 2,
                "title": "looooooooooooooooooooooooooooooooooooooooong new title",
            },
            {
                "id": 3,
                "url": "https://via.placeholder.com/600/1006",
                "thumbnailUrl": "https://via.placeholder.com/150/1006"
            },
        ],
        'delete': [1, 2, 3, ]
    },
    'todos': {
        'get': [
            {
                "userId": 1,
                "id": 1,
                "title": "delectus aut autem",
                "completed": False
            },
            {
                "userId": 1,
                "id": 2,
                "title": "quis ut nam facilis et officia qui",
                "completed": False
            },
            {
                "userId": 1,
                "id": 3,
                "title": "fugiat veniam minus",
                "completed": False
            },
        ],
        'post': [
            {
                "userId": 1,
                "title": "new todo 1",
                "completed": False
            },
            {
                "userId": 2,
                "title": "looooooooooooooooooooooooooooooooooooooooooooooooooooooooooong title",
                "completed": True
            },
            {
                "userId": 3,
                "title": "3",
                "completed": False
            },
        ],
        'put': [
            {
                "userId": 1,
                "id": 1,
                "title": "new title",
                "completed": False
            },
            {
                "userId": 2,
                "id": 2,
                "title": "quis ut nam facilis et officia qui",
                "completed": True
            },
            {
                "userId": 1,
                "id": 3,
                "title": "looooooooooooooooooooooooooooooooooooooooooooooooooooong title",
                "completed": True
            },
        ],
        'patch': [
            {
                "id": 1,
                "completed": True
            },
            {
                "userId": 3,
                "id": 2,
            },
            {
                "id": 3,
                "title": "looooooooooooooooooooooooooooooooooooooooooooooooooooong title2",
            },
        ],
        'delete': [1, 2, 3]
    },
    'users': {
        'get': [
            {
                "id": 1,
                "name": "Leanne Graham",
                "username": "Bret",
                "email": "Sincere@april.biz",
                "address": {
                    "street": "Kulas Light",
                    "suite": "Apt. 556",
                    "city": "Gwenborough",
                    "zipcode": "92998-3874",
                    "geo": {
                        "lat": "-37.3159",
                        "lng": "81.1496"
                    }
                },
                "phone": "1-770-736-8031 x56442",
                "website": "hildegard.org",
                "company": {
                    "name": "Romaguera-Crona",
                    "catchPhrase": "Multi-layered client-server neural-net",
                    "bs": "harness real-time e-markets"
                }
            },
            {
                "id": 2,
                "name": "Ervin Howell",
                "username": "Antonette",
                "email": "Shanna@melissa.tv",
                "address": {
                    "street": "Victor Plains",
                    "suite": "Suite 879",
                    "city": "Wisokyburgh",
                    "zipcode": "90566-7771",
                    "geo": {
                        "lat": "-43.9509",
                        "lng": "-34.4618"
                    }
                },
                "phone": "010-692-6593 x09125",
                "website": "anastasia.net",
                "company": {
                    "name": "Deckow-Crist",
                    "catchPhrase": "Proactive didactic contingency",
                    "bs": "synergize scalable supply-chains"
                }
            },
            {
                "id": 3,
                "name": "Clementine Bauch",
                "username": "Samantha",
                "email": "Nathan@yesenia.net",
                "address": {
                    "street": "Douglas Extension",
                    "suite": "Suite 847",
                    "city": "McKenziehaven",
                    "zipcode": "59590-4157",
                    "geo": {
                        "lat": "-68.6102",
                        "lng": "-47.0653"
                    }
                },
                "phone": "1-463-123-4447",
                "website": "ramiro.info",
                "company": {
                    "name": "Romaguera-Jacobson",
                    "catchPhrase": "Face to face bifurcated interface",
                    "bs": "e-enable strategic applications"
                }
            },
        ],
        'post': [
            {
                "name": "Test User",
                "username": "testuser",
                "email": "test@mail.com",
                "phone": "123-456-7890",
                "website": "test.com",
                "address": {
                    "street": "Test Street",
                    "suite": "Apt. 101",
                    "city": "Test City",
                    "zipcode": "12345",
                    "geo": {
                        "lat": "10.1234",
                        "lng": "-10.1234"
                    }
                },
                "company": {
                    "name": "Test Corp",
                    "catchPhrase": "Testing the limits",
                    "bs": "innovate testing solutions"
                }
            },
            {
                "name": "Looooooooooooooooooooooooooooooooong Name",
                "username": "longname",
                "email": "long@mail.org",
                "phone": "000-000-0000",
                "website": "long.org",
                "address": {
                    "street": "Looooooooooooooooooooooooooooooooong Street",
                    "suite": "Suite 000",
                    "city": "Long City",
                    "zipcode": "00000",
                    "geo": {
                        "lat": "89.9999",
                        "lng": "179.9999"
                    }
                },
                "company": {
                    "name": "Long Corp",
                    "catchPhrase": "Looooooooooooooooooooooooooooooooong catchphrase",
                    "bs": "scale long enterprises"
                }
            },
            {
                "name": "A",
                "username": "a",
                "email": "a@a.com",
                "phone": "1",
                "website": "a.com",
                "address": {
                    "street": "B",
                    "suite": "C",
                    "city": "D",
                    "zipcode": "1",
                    "geo": {
                        "lat": "1.1",
                        "lng": "1.1"
                    }
                },
                "company": {
                    "name": "E",
                    "catchPhrase": "F",
                    "bs": "G"
                }
            },
        ],
        'put': [
            {
                "id": 1,
                "name": "New Name 1",
                "username": "newuser1",
                "email": "new1@mail.com",
                "phone": "111-111-1111",
                "website": "new1.com",
                "address": {
                    "street": "New Street 1",
                    "suite": "Suite 111",
                    "city": "New City 1",
                    "zipcode": "11111",
                    "geo": {
                        "lat": "11.1111",
                        "lng": "-11.1111"
                    }
                },
                "company": {
                    "name": "New Corp 1",
                    "catchPhrase": "New proactive didactic contingency",
                    "bs": "new synergize scalable supply-chains"
                }
            },
            {
                "id": 2,
                "name": "Looooooooooooooooooooooooooooooooong New Name",
                "username": "newuser2",
                "email": "new2@mail.org",
                "phone": "222-222-2222",
                "website": "new2.org",
                "address": {
                    "street": "Looooooooooooooooooooooooooooooooong New Street",
                    "suite": "Apt. 222",
                    "city": "New City 2",
                    "zipcode": "22222",
                    "geo": {
                        "lat": "22.2222",
                        "lng": "-22.2222"
                    }
                },
                "company": {
                    "name": "New Corp 2",
                    "catchPhrase": "Another long catchphrase right here",
                    "bs": "synergize long supply-chains"
                }
            },
            {
                "id": 3,
                "name": "3",
                "username": "newuser3",
                "email": "new3@mail.biz",
                "phone": "333-333-3333",
                "website": "new3.biz",
                "address": {
                    "street": "3",
                    "suite": "3",
                    "city": "3",
                    "zipcode": "3",
                    "geo": {
                        "lat": "3.3",
                        "lng": "-3.3"
                    }
                },
                "company": {
                    "name": "3",
                    "catchPhrase": "3",
                    "bs": "3"
                }
            },
        ],
        'patch': [
            {
                "id": 1,
                "email": "patched1@mail.com",
                "address": {
                    "city": "Patched City",
                    "geo": {
                        "lat": "99.9999"
                    }
                }
            },
            {
                "id": 2,
                "name": "Patched Name",
                "phone": "999-999-9999",
                "company": {
                    "name": "Patched Corp",
                    "bs": "patched scale testing"
                }
            },
            {
                "id": 3,
                "name": "Looooooooooooooooooooooooooooooooong Patched Name",
                "username": "patcheduser3",
                "email": "patched3@mail.biz",
                "address": {
                    "street": "Patched Street",
                    "city": "Patched City 3",
                    "zipcode": "99999"
                },
                "company": {
                    "name": "Patched Corp 3"
                }
            },
        ],
        'delete': [1, 2, 3]
    },
}
