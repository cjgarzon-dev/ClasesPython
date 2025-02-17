class Booking:
    def __init__(self, client, date):
        self.client = client
        self.date = date
        
bookings = [
    Booking('Juan', None),
    Booking('Maria', '2025-02-27')
]

for booking in bookings:
    if not booking.date:
        print(f'Error: Fecha no asignada para el cliente: {booking.client}')