import csv
class Item:
 def __init__ (self,number:int, name:str):
   self.number = number
   self.name = name

filename = '.csv'
with open(filename,encoding = 'utf8',newline='')as f:
 csvr = csv.reader(f)
 _ = next(csvr)
 for i in map (Item.create_from_sequence,csvr)
 print(i)