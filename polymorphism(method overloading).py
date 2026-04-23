#POLYMORPHISM
#method overloading
def add(datatype,*args):
    if(datatype=='int'):
        answer=0
    if(datatype=='str'):
        answer=''
    for x in args:
        answer=answer+x
    print(answer)
add('int',5,15,56)
add('str','computer','science')

#method overloading
#using class
class methover: 
     def add(self,datatype,*args):
         if(datatype=='int'):
             answer=0
         if(datatype=='str'):
             answer=''
         for x in args:
            answer=answer+x
         print(answer)
a=methover()
a.add('int',5,15,29)
a.add('str','computer ','science ','engineering')


