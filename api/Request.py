import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def get_posts():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("GET Response:", response.json())
    else:
        print("GET Request failed:", response.status_code)


def create_post():
    new_post = {
        "title": "Foo",
        "body": "Bar",
        "userId": 1
    }
    response = requests.post(BASE_URL, json=new_post)
    if response.status_code == 201:
        print("POST Response:", response.json())
    else:
        print("POST Request failed:", response.status_code)


def update_post(post_id):
    updated_post = {
        "id": post_id,
        "title": "Updated Title",
        "body": "Updated Body",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/{post_id}", json=updated_post)
    if response.status_code == 200:
        print("PUT Response:", response.json())
    else:
        print("PUT Request failed:", response.status_code)


def delete_post(post_id):
    response = requests.delete(f"{BASE_URL}/{post_id}")
    if response.status_code == 200:
        print(f"DELETE Response: Post {post_id} deleted successfully")
    else:
        print("DELETE Request failed:", response.status_code)


########################
# GET Request
print("\n\n# GET Request")
get_posts()

########################
# POST Request
print("\n\n# POST Request")
create_post()

########################
# PUT Request
print("\n\n# PUT Request")
update_post(1)

########################
# DELETE Request
print("\n\n# DELETE Request")
delete_post(1)
