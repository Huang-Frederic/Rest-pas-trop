from repository.reservation import ReservationRepo
from model.reservation import Reservation

class ReservationService:
    def __init__(self) -> None:
        self.reservation_repo = ReservationRepo()

    def create(self, reservation: Reservation) -> None:
        self.reservation_repo.insert(reservation)    

    def get(self, id_reservation: int) -> Reservation:
        return self.reservation_repo.view(id_reservation)
    
    def get_all(self) -> list[Reservation]:
        return self.reservation_repo.view_all()

    def get_by_username(self, username: str) -> list[Reservation]:
        reservations = self.reservation_repo.view_by_username(username)
        if reservations:
            return [reservation.reservation_to_json() for reservation in reservations]
        return None

    def update(self, reservation: Reservation):
        self.reservation_repo.update(reservation)

    def delete(self, reservation: Reservation) -> None:
        self.reservation_repo.delete(reservation)

    def delete_all(self) -> None:
        self.reservation_repo.delete_all()