#!/usr/bin/env python3

from typing import Any


APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name='Fido', breed='Pug'):
        self._name = None
        self._breed = None
        self.name = name
        self.breed = breed
    
    def get_name(self):
        return self._name
    
    def set_name(self, name ):
          if isinstance(name, str) and 1<= len(name) <= 25:
            print(f"Setting name to {name}.")
            self._name = name
          elif name == "":
            print("Name must be string between 1 and 25 characters.")
          elif not isinstance(name, str):
            print("Name must be string between 1 and 25 characters.")
          elif len(name) > 25:
            print("Name must be a string between 1 and 25 characters.")
          else:
            print("Name must be a string between 1 and 25 characters.")
            

    name = property(get_name, set_name,)

    def get_breed(self):
        return self._breed
    
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed=breed
        else: 
            print("Breed must be in list of approved breeds.")  

    breed= property(get_breed, set_breed)          
    
             
