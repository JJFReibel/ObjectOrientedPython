# MIT License

# Copyright (c) 2020 Jean-Jacques François Reibel

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

class Car:
  def __init__(self, wheels, doors, cylinders):
    self.wheels, self.doors, self.cylinders = (wheels, doors, cylinders)
  def addWheels(self, wheels):
    self.wheels += wheels
  def addDoors(self, doors):
    self.doors += doors
  def addCylinders(self, cylinders):
    self.cylinders += cylinders
  def deleteWheels(self, wheels):
    self.wheels -= wheels
  def deleteDoors(self, doors):
    self.doors -= doors
  def deleteCylinders(self, cylinders):
    self.cylinders -= cylinders

print("Creating car.")
subaru = Car(4, 4, 4)
print("Adding wheel directly to car object.")
subaru.wheels = 5
print("Wheels check: " + str(subaru.wheels))
print("Doors check: " + str(subaru.doors))
print("Cylinders check: " + str(subaru.cylinders))
print("")
print("Removing wheel using class method.")
subaru.deleteWheels(1)
print("Wheels check: " + str(subaru.wheels))
print("Doors check: " + str(subaru.doors))
print("Cylinders check: " + str(subaru.cylinders))
print("")