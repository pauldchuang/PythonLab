import redis

client = redis.Redis(host='localhost', port=6379, db=0)

client.set("he", "yo")

value = client.get("he")
print(value.decode())

value = client.get("hello")
print(value.decode())