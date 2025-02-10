product ={
    "name": 'relame 7 pro',
    "price": 2700,
    "battery": '4500mAh',
    "release": '7th Oct 2018',
    "is_available": False
}

print(product)
print(product.items())
pop_product = product.popitem()

new_product = product.pop('name')
print(new_product, product)
product['name'] = 'realme 7 pro'
product.update({'name': 'poco x4'})

for key, value in product.items():
    print(f'{key} : {value}')