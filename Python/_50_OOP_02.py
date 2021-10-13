# Class and instance attributes
class MyClass:
    class_attribute = "Class Atribute"

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute


objectA = MyClass("Attribute A")
objectB = MyClass("Attribute B")

print('MyClass.class_attribute =', MyClass.class_attribute)
print('objectA.class_attribute =', objectA.class_attribute)
print('objectB.class_attribute =', objectB.class_attribute)

print('objectA.instance_attribute =', objectA.instance_attribute)
print('objectB.instance_attribute =', objectB.instance_attribute)
