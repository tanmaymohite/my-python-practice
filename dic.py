cars  ={
    'car1':{
    'brand':'tesla',
    'model':'s',
    'year':'2020'
    },
    'car2':{
  'brand':'tata',
   'model':'Evision',
   'year':'2022'
},
    'car3':{
        'brand':'suzuki',
        'model':'alto K10',
        'year':'2014'
    },
    'car4':{
        'brand':'Kia',
        'model':'selton',
        'year':2019

    }
}

cars.update({'colour':'white'})
cars.update({'colour':'black'})
for x ,y in cars.items():
    print(x,y)






