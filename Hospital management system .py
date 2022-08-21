#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Ptaient:   
   def __init__(self) :
     self.name = "" 
     self.state = 0 
   def set_data(self) : 
     print("Enter the patient name : ")
     self.name = input() 
     print("Enter the State (0 Normal / 1 Urgent / 2 Super Urgent): ") 
     self.state=int(input()) 
     
     
 
class  Specialization :   
      
  def __init__(self) : 
    self.l_sp = [[] for _ in range(0 , 21)] 
    self.curr_urg  = 0  
    self.cuur_spr =  -1   
    self.dec={'0':"Regular" , '1':"Urgent" ,'2':"Super Urgent"} 
 
   
  def  can_enter(self , no) :  
    if(len(self.l_sp[no]) == 10 ) : 
      print("Sorry we can't help at the moment ") 
      return False 
    return True    
 
  def  add_pt(self , p , no )  : 
     
       if(p.state == 0 ):
            self.l_sp[no].append("0" + p.name) 
            print("added")
       elif(p.state == 1 ):
            self.l_sp[no].insert(self.curr_urg + 1, "1" + p.name)
            self.curr_urg += 1
       elif(p.state == 2 ):
          self.l_sp[no].insert(self.cuur_spr  + 1, "2" + p.name)
          self.cuur_spr += 1 
      
  def print_list(self ) : 
       for i in range(0, 20):
         if (not self.l_sp[i]):
             continue
         print("Specialization  ", i , ": ", "has ", len( self.l_sp[i]), " patients")
         for j in range(len( self.l_sp[i])):
             print("patient :",  self.l_sp[i][j][1:], "is a ", self.dec[self.l_sp[i][j][0]])
        
  def call_next(self , no) :  
       if(self.l_sp[no]) :
         next_p = self.l_sp[no][0]
         print(self.l_sp[no][0][1:] ,"  Please go with the Dr")
         self.l_sp[no].remove(self.l_sp[no][0])
        
       else :
              print("there is no patient here ")
            
  def  getout_p(self , no ,p) :
      leaving_p = str(p.state)+p.name
          
      if (leaving_p in self.l_sp[no]) :
             self.l_sp[no].remove(leaving_p) 
             print("patient left :)")
      else :
              print("No such patient")

if __name__=='__main__' :
 
 
 program_list = """  
the program menue : 
1) Add new patient 
2) Print all patients 
3) Get the next patient 
4) Remove an atient  
5)End the program  
enter a number from (0 to 5)
"""  
 spobj = Specialization()    
 pobj = Ptaient()  
 
 
 
while("entering") : 
   print(program_list)
   ch = input()  
   
   if(ch == "1") :#enter
      print("Enter the Specialization : ") 
      sp=int(input())   
      if(not spobj.can_enter(sp) ) :
       continue 
      pobj.set_data() 
      spobj.add_pt(pobj , sp)
     
   elif(ch == '2') : #printing
    spobj.print_list()
 
        
 
          
   elif(ch=='3') : #next patient  
     sp=int(input()) 
     spobj.call_next(sp)
      
     
 
 
   elif(ch== '4') : #leaving patient   
     print("Enter Specialization : ")
     sp=int(input() )   
     
     pobj.set_data()
     spobj.getout_p(sp , pobj)  
 
      
   elif(ch=='5') : 
      print("thanks for your use =>")  
      break
      


# In[ ]:




