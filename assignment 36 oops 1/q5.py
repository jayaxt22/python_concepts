class shoppingbill:
    def __init__(self,
                  Product_name,
                  Product_price,
                  Quantity,
                  Discount_percentage,
                  GST_percentage):
          
          self.Product_name=Product_name
          self.Product_price=Product_price
          self.Quantity=Quantity
          self.Discount_percentage=Discount_percentage
          self.GST_percentage=GST_percentage
          self.subtotal=0
          self.discount=0
          self.gst=0
          self.finalbill=0
          self.discount_amt=0

    def calculate_subtotal(self) :

          self.subtotal=self.Product_price*self.Quantity
          return self.subtotal
    
         

    def calculate_discount(self) :
         self.discount=self.subtotal*self.Discount_percentage/100
         return self.discount
 
    def calculate_gst(self) :
         self.discount_amt=self.subtotal-self.discount
         self.gst=self.discount_amt*self.GST_percentage/100
         return self.gst

    def calculate_final_bill(self):
         self.finalbill=self.discount_amt+self.gst
         return self.finalbill
         
         
    def display_bill(self) :
         print("============== bill ==============")
         print("product name     :",self.Product_name)
         print("product price    :",self.Product_price)
         print("quantity         :",self.Quantity)
         print("discount rate    :",self.Discount_percentage,"%")
         print("gst percent      :",self.GST_percentage,"%")
         print("subtotal         :",self.subtotal)
         print("gst amount       :",self.gst)
         print("discount amt     :",self.discount_amt)
         print()
         print("final bill       :",self.finalbill)
         print()
         print("===================================")


s1 = shoppingbill("robot",150000,5,10,28)

s1.calculate_subtotal()
s1.calculate_discount()    
s1.calculate_gst()
s1.calculate_final_bill()
s1.display_bill()  