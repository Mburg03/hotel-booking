import pandas as pd

hotels_df = pd.read_csv("./hotels.csv")

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


print(hotels_df)
hotel_id = int(input("Enter the id of the hotel you would like to reserve: "))
hotel = Hotel(hotel_id)

if hotel.available():
    customer_name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(customer_name, hotel)
    hotel.book()

    print(reservation_ticket.generate())

else:
    print("Hotel is not available.")
