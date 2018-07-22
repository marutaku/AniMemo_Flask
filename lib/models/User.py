from lib.database.Users import User
from lib.models.Utils import Utils


class UserModel():
    user_db = User()

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

    def register_user(self, name, email, password, confirm_password, image_path=None):
        hashed_password = Utils.hash_password(password)
        if len(self.user_db.get_user_by_name(name)) == 0:
            self.user_db.insert_user(name, email, hashed_password, image_path)
            return True
        else:
            return 'ユーザ名が重複しています'


    
