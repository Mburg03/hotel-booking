import pandas as pd

hotels_df = pd.read_csv("./hotels.csv")
cards_df = pd.read_csv("./cards.csv", dtype=str).to_dict(orient="records")
cards_security_df = pd.read_csv("./card_security.csv", dtype=str)


class Hotel: 
    def __init__(self, hotel_id) -> None:
        self.hotel_id = hotel_id
        self.name = hotels_df.loc[hotels_df["id"] == self.hotel_id, 
                                  "name"].squeeze()
        
    def book(self):
        """Books a hotel by changing its availability to no"""
        hotels_df.loc[hotels_df["id"] == self.hotel_id, "available"] = "no"
        hotels_df.to_csv("hotels.csv", index=False)

    def available(self):
        """Checks if the hotel is available"""
        availability = hotels_df.loc[hotels_df["id"] == self.hotel_id, 
                                     "available"].squeeze()
                
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object) -> None:
        self.customer_name = customer_name
        self.hotel = hotel_object
    
    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        """
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration, "holder": holder, "cvc": cvc}
        
        if card_data in cards_df:
            return True
        else:
            return False
        

class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = cards_security_df.loc[cards_security_df["number"] == self.number, "password"].squeeze()
        
        if given_password == password:
          return True
        else:
          return False



print(hotels_df)
hotel_id = int(input("Enter the id of the hotel you would like to reserve: "))
hotel = Hotel(hotel_id) # Hotel instance

if hotel.available():
    credit_card = SecureCreditCard(number="1234567890123456") # CreditCard instance
    if credit_card.validate(expiration="12/26", holder ="JOHN SMITH", cvc="123"): 
        psw = input("Type in your password: ")
        if credit_card.authenticate(psw):
            customer_name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(customer_name, hotel) # ReservationTicket instance
            hotel.book()
            print(reservation_ticket.generate())
        else:
            print("Credit card authentication failed.")
    else:
        print("There was a problem with your payment. Card not validated.")

else:
    print("Hotel is not available.")
