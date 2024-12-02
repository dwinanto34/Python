# Class and method
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("USER001", "Budi")
user2 = User("USER002", "Bambang")

user1.follow(user2)
user2.follow(user1)

print(
    f"{user1.following} "
    f"{user1.followers} "
    f"{user2.following} "
    f"{user2.followers} "
)

# Inheritance
class VipUser(User):
    def __init__(self, user_id, username):
        super().__init__(user_id, username)

    def vip_feature(self):
        print("You can access vip features")


vip_user = VipUser("VIP_USER001", "John")
vip_user.vip_feature()
