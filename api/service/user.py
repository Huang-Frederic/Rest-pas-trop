from repository.user import UserRepo
from service.reservation import ReservationService
from service.apartment import ApartmentService
from model.user import User

class UserService:
    def __init__(self) -> None:
        self.user_repo = UserRepo()
        self.reservation_service = ReservationService()
        self.apartment_service = ApartmentService()

    def create(self, user: User) -> None:
        self.user_repo.insert(user)    

    def get(self, username: str) -> dict:
        user = self.user_repo.view(username)
        user_json = user.user_to_json()
        user_json['apartment'] = self.apartment_service.get_by_username(username)
        user_json['reservation'] = self.reservation_service.get_by_username(username)
        return user_json
    
    def get_all(self) -> list[dict]:
        users = self.user_repo.view_all()
        users_json = [user.user_to_json() for user in users]
        for user_json in users_json:
            user_json['apartment'] = self.apartment_service.get_by_username(user_json['username'])
            user_json['reservation'] = self.apartment_service.get_by_username(user_json['username'])
        return users_json

    def get_id(self, username: str):
        return self.user_repo.get_id(username)

    def update(self, user: User, username: str) -> None:
        user.id = self.get_id(username)
        print(user.id)
        self.user_repo.update(user)

    def delete(self, username: str) -> None:
        self.user_repo.delete(username)

    def delete_all(self) -> None:
        self.user_repo.delete_all()

    def check_user(self, username: str) -> bool:
        if self.user_repo.get_id(username):
            return True
        return False

    def check_values(self, user: User) -> bool:
        if (len(user.username) > 60):
            return False
        if (len(user.first_name) > 30):
            return False
        if (len(user.last_name) > 30):
            return False
        return True    
