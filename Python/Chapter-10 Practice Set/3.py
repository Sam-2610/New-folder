""" Add a static method to greet the user with hello.  """

class Greeting:
    @staticmethod
    def greet():
        return "Hello"
    
print(Greeting.greet(),"Sam")