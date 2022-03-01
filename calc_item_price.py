import price;

print_list = '''
sgr --> sugar
cks --> cookies
bread --> bread
sdn --> sardines
milo --> milo
drk_c --> drink-cocacola
swt_cg --> sweet-chewinggum
bsct --> bsct
lptn --> lipton 
'''

print(print_list);

item = input("Enter the item you want to buy  ");
qty = int(input("Enter the quantity you want to buy  "));

if(item == 'sgr'): 
    print("You just choose to buy sugar ");
    print("The total is ", price.sugar * qty);

if(item == 'cks'):
    print("You just choose to buy cookies");
    print("The total is ", price.cookies * qty);


if(item == 'bread'): 
    print("You just choose to buy bread");
    print("The total is ", price.bread * qty);


if(item == 'sdn'): 
    print("You just choose to buy sardines");
    print("The total is ", price.sardine * qty);


if(item == 'milo'): 
    print("You just choose to buy milo");
    print("The total is ", price.milo * qty);


if(item == 'drk_c'): 
    print("You just choose to buy cocacola drink");
    print("The total is ", price.drink_cocacola * qty);


if(item == 'swt-cg'): 
    print("You just choose to buy sweet chewinggum");
    print("The total is ", price.sweet_chewinggum * qty);


if(item == 'bsct'): 
    print("You just choose to buy biscuit");
    print("The total is ", price.biscuit * qty);


if(item == 'lptn'): 
    print("You just choose to buy lipton");
    print("The total is ", price.lipton * qty);





