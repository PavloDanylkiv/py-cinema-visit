from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    names = []
    for customer in customers:
        cus = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(
            product=cus.food,
            customer=cus,
        )
        names.append(cus)
    CinemaHall.movie_session(
        CinemaHall(hall_number),
        movie,
        names,
        Cleaner(cleaner)
    )
