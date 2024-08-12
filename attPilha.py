class Stack:

    def __init__(self):
        self.items = []
     
    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[len(self.items)-1]
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def isEmpty (self):
        return self.items == []
    


pilhaPratos = Stack()


#Existem 3 pratos que precisam ser limpos.

pilhaPratos.push('Prato 1')
pilhaPratos.push('Prato 2')
pilhaPratos.push('Prato 3')
print(pilhaPratos.items)

#O primeiro prato foi limpo:

print(pilhaPratos.peek())

pilhaPratos.pop()
print(pilhaPratos.items)

#Agora o segundo prato foi limpo:

print(pilhaPratos.peek())

pilhaPratos.pop()
print(pilhaPratos.items)

#Por fim, o último prato foi limpo:

print(pilhaPratos.peek())

pilhaPratos.pop()
print(pilhaPratos.items)

try:
    pilhaPratos.pop()
except IndexError:
    print('A pilha de pratos está vazia')

