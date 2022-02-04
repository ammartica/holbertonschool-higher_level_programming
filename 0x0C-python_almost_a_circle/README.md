Project: 0x0C. Python - Almost a circle

This repository contains tasks that explore serialization, deserialization, JSON files,
\*args and \*kwargs in Python.

  * All your files, classes and methods must be unit tested and be PEP 8 validated.
  * Write the first class Base
  * Write the class Rectangle that inherits from Base
  * Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded)
  * Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance
  * Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character #
  * Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
  * Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y
  * Update the class Rectangle by adding the public method def update(self, \*args): that assigns an argument to each attribute
  * Update the class Rectangle by updating the public method def update(self, \*args): by changing the prototype to update(self, \*args, \*\*kwargs) that assigns a key/value argument to attributes
  * Write the class Square that inherits from Rectangle
  * Update the class Square by adding the public getter and setter size
  * Update the class Square by adding the public method def update(self, \*args, \*\*kwargs) that assigns attributes
  * Update the class Rectangle by adding the public method def to\_dictionary(self): that returns the dictionary representation of a Rectangle
  * Update the class Square by adding the public method def to\_dictionary(self): that returns the dictionary representation of a Square
  * Update the class Base by adding the static method def to\_json\_string(list\_dictionaries): that returns the JSON string representation of list\_dictionaries
