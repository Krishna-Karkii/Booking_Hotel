import pandas

df = pandas.read_csv("hotels.csv", dtype={'id': str})
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient='records')


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()

    def book(self):
        df.loc[df['id'] == self.hotel_id, 'available'] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        if availability.lower() == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object

    def generate(self):
        content = f"""
                Your Reservation Has Been Successful!
                
                your booking name : {self.customer_name}
                hotel booked : {self.hotel_object.name}
                
                Thanks For Booking With Us."""
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expire_date, holder_name, cvc):
        card_info = {'number': self.number, 'expiration': expire_date, 'cvc': cvc, 'holder': holder_name}
        if card_info in df_cards:
            return True


print(df)
print(df_cards)
hotel_id = input("Enter hotel id: ")
hotel = Hotel(hotel_id)

if hotel.available():

    card_number = input("Enter your card number : ").strip()
    expiration = input("Enter your card expiration date: ").strip()
    holder_name = input("Enter the card holder name: ").strip().upper()
    cvc_number = input("Enter your cvc number: ").strip()

    credit_card = CreditCard(number=card_number)
    if credit_card.validate(expire_date=expiration, holder_name=holder_name, cvc=cvc_number):
        hotel.book()
        name = input("Enter your name : ")
        reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
        print(reservation_ticket.generate())

    else:
        print("There is no such card info!")

else:
    print("Hotel is not available!!")

