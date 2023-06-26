#!/usr/bin/python3


class DerivedClassName(BaseClassName):
    def __init__(self):
        super().__init__()  # calls the constructor of the base class
        # additional initialization code for the derived class

    def some_method(self):
        super().some_method()  # calls the method of the base class
        # additional code for the derived class
