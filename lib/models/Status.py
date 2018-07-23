from lib.database.Status import Status


class StatusModel():
    status_db = Status()

    def check_existence(self, user_id, work_id):
        result = self.status_db.get_status_by_work_id(user_id, work_id)
        if len(result) != 0:
            return True
        else:
            return False

    def change_status(self, user_id, work_id, state):
        if self.check_existence(user_id, work_id):
            self.status_db.update_status(state, user_id, work_id)
            return 'Update status'
        else:
            self.status_db.insert_status(state, user_id, work_id)
            return 'Insert Status'
