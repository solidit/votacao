Votação
=======

Web Service de votação usado no Workshop Amazon AWS ( Python/Django com Redis NoSQL )

curl -l http://192.168.1.101:8000/ws/votar/a/
curl -l http://192.168.1.101:8000/ws/votar/a/
curl -l http://192.168.1.101:8000/ws/votar/a/

curl -l http://192.168.1.101:8000/ws/votar/b/

curl -l http://192.168.1.101:8000/ws/resutado/

{
    "A": 3, 
    "B": 1
}
