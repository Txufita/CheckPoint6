# Cree una clase de Python llamada Usuario que use el método init y cree un nombre de usuario y una contraseña. Crea un objeto usando la clase.
class User: 
  def __init__(self, username, password):
    self.username = username
    self.password = password

  def print_user(self):
    print(self.username, self.password)  

user1 = User("txufi", "Txufi123")
user1.print_user()

  


