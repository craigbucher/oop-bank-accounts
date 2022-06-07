#
class Owner:
    def __init__(self, first_name, last_name, address, telephone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.telephone = telephone
        self.email = email

    # def __str__(self):
    #     return(f"""
    #     Name: {self.first_name} {self.last_name}
    #     Address: {self.address}
    #     Telephone: {self.telephone}
    #     Email address: {self.email}
    #     """)

# craig = Owner('Craig', 'Bucher', 'Chicago somewhere', '739-8994', 'craig@mail.com')
# print(craig)
