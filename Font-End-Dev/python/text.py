# python class

class TagCloud:
  def __init__(self):
    # to make the attributes private by just using '__' or two underscore
    self.__tags = {}

  def add(self, tag):
    self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

  def __getitem__(self, tag):
    return self.__tags.get(tag.lower(), 0)
  
  def __setitem__(self, tag, value):
    self.__tags[tag.lower()] = value

  def __len__(self):
    return len(self.__tags)
  
  def __iter__(self):
    return iter(self.__tags)


cloud = TagCloud()
cloud.add("python")
cloud.add("Python")
cloud.add("python")
cloud["English"] = 4
len(cloud)


# print(cloud["python"])

# To access or get all the attributes of a given class
# cloud.__dict__  : cloud - is the instance of the given class, so this gives us the all attribute
# to access private attributes of the cl                      ass
# print(cloud._TagCloud__tags)

# for key in cloud:
#   print(f"key:{key}, value:{cloud[key]}")



class Product:
  def __init__(self, price):
    self.set_price(price)

  def get_price(self):
    return self.price
   
  def set_price(self, price):
    if price < 0:
      raise ValueError("Price can't be negative")
    self.price = price
  price = property(get_price, set_price)





product = Product(10)
# product.set_item(5)
# product.price = -1
print(product.price)