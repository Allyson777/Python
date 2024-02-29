x =float(input())
op =input()
y =float(input())
if op == "+":
    print(f"{x} + {y} = {x +y }")		
elif op == "-": 
    print(f"{x} - {y} = {x - y}")
elif op == "*":
    print(f"{x} * {y} = {x * y}")	
elif y == 0 and op == "//":
    print("Divisao por 0!")
elif op == "//":
    print(f"{x} // {y} = {x // y}")
elif op == "**":
    print(f"{x} ** {y} = {x ** y}")
elif y == 0 and op == "%": 
    print("Divisao por 0!")
elif op == "%":
    print(f"{x} % {y} = {x % y}") 
else:
    print("Operacao nao reconhecida!")


  	
 	


	
	
	
