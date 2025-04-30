class P:
    def display(self):
        print("Inside P")

class Q(P):
    def display(self):
        print("Inside Q")

class R(P):
    pass

class S(Q, R):
    pass

s = S()
s.display()  # This will call the display method from class Q due to method resolution order (MRO)
