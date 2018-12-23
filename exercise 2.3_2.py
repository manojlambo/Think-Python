"""
Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
$3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
60 copies
"""
price=24.95
discount=(price/100)*40
book_price=price-discount
nos=int(input("Enter the number of books : "))
if nos==1:
    print("the total cost is : $",nos*book_price+3)
else:
    total=(book_price*60)+(nos-1)*0.75+3
    print("the total cost is : $",total)
    
