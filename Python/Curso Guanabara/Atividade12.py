pdt = float(input(': '))
if pdt <= 200:
    des = float(input(': '))
    print(f'Seu produto possui {des}% de desconto\n Com desconto é de: {(des*pdt)/100:.2f}\n seu produto custa {pdt-((des*pdt)/100)}')
else:
    print("não há desconto para esse produto")
