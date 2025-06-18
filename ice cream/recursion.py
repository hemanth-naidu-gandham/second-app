def hii():
    print("welcome")
    def add_welcome(f):
        def new_function():
            print("welcome to the class ")
            f()
        return new_function
say_hi= add_welcome(hii)
say_hi()