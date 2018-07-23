from lib.database.Users import User
from lib.database.Reviews import Review
from lib.database.Status import Status
from lib.database.Follows import Follows
from lib.models.Utils import Utils


class UserModel():
    user_db = User()
    revies_db = Review()
    status_db = Status()
    follow_db = Follows()

    def login(self, name, password):
        hashed_password = Utils.hash_password(password)
        user_dict = self.user_db.get_user_by_name(user_name=name)
        # ユーザの存在確認
        if len(user_dict) == 0:
            return False
        #パスワードの照合
        for user in user_dict:
            if user['password'] == hashed_password:
                return user
        return False

    def register_user(self, name, email, password, image_path=None):
        hashed_password = Utils.hash_password(password)
        if len(self.user_db.get_user_by_name(name)) == 0:
            self.user_db.insert_user(name, email, hashed_password, image_path)
            return True
        else:
            return 'ユーザ名が重複しています'

    def get_user_activity(self, user_id):
        user_info =self.user_db.get_user_by_id(user_id)
        review_data = self.revies_db.get_review_by_user_id(user_id)
        status_data = self.status_db.get_all_status(user_id)
        watch_later = []
        watched = []
        favorite = []
        print(status_data)
        for state in status_data:
            if state['state'] == "0":
                #きになる
                watch_later.append(state)
            elif state['state'] == "1":
                #見たことがある
                watched.append(state)
            elif state['state'] == "2":
                #よかった
                favorite.append(state)
        return {
            'user_info': user_info,
            'watch_later': watch_later,
            'watched': watched,
            'favorite': favorite,
            'review': review_data
        }
    def follow(self, from_id , to_id):
        self.follow_db.insert_follows(from_id, to_id)

    def unfollow(self, from_id, to_id):
        self.follow_db.delete_followers(from_id, to_id)

    def is_followed(self, from_id, to_id):
        if len(self.follow_db.get_follow_by_id(from_id, to_id)):
            return True
        else:
            return False

    def get_user_info(self, id):
        return self.user_db.get_user_by_id(id)

    def update_user_info(self, name, password, email, id):
        hashed_password = Utils.hash_password(password)
        exist_user = self.user_db.get_user_by_name(name)
        print(exist_user)
        print(type(exist_user))
        if len(exist_user) == 0 or exist_user[0].name == name:
            self.user_db.update_user(name, email, hashed_password, id)
            return True
        else:
            return 'ユーザ名が重複しています'








    
