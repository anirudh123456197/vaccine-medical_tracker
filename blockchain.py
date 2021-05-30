import hashlib

class Neutral:
    def __init__(self, pre_blo_hash,trans_list):
      self.pre_blo_hash=pre_blo_hash
      self.trans_list= trans_list
      self.block_data="-".join(trans_list)+"-"+pre_blo_hash
      self.block_hash=hashlib.sha256(self.block_data.encode()).hexdigest()

flag=0
data_statement= []
data_hashes= []
if flag==0:
      st = input("Enter initial produced ")
      initial_block= Neutral("initial string",[st])
      data_statement.append(initial_block.block_data)
      data_hashes.append(initial_block.block_hash)
      flag=1



for i in range (1,20):
      x = int(input('Enter 1 to input data adn 2 to view the data  3 to break '))
      if x==1:
        st = input("Enter AMOUNT RECIEVED ")
        block= Neutral("initial string",[st])
        print(block.block_hash)
        print("keep your code safely")
        data_statement.append(block.block_data)
        data_hashes.append(block.block_hash)
      if x==2:
        print(data_statement)
        print(data_hashes)
      if x==3:
         break      




        


      





print(initial_block.block_data)
print(initial_block.block_hash)


