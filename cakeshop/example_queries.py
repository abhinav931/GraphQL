'''
{
    allCakes{
        id
        name
        price
        flavor{
            id
            name
        }
    }
}
'''
'''
{
  allCakes{
    name
    flavor{
      name
    }
  }
}'''

'''
{
  flavorByName(name:""){
    id
    name
  }
}
'''

'''
cake by flavor name
{
  flavorByName(name:"Vanilla"){
    id
    name
    cakeSet{
      name
    }
  }
}

{
  flavorByName(name:"Chocolate"){
    id
    name
    cakeSet{
      id
      name
    }
  }
}

{
  flavorByName(name: "Chocolate") {
    id
    name
    cakeSet {
      id
      name
      price
    }
  }
}

'''
