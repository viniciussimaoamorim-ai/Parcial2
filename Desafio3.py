# Lista de Objetos
def criar_lista_material():
    material_escolar = []
    print("Digite os materiais escolares. Quando terminar, digite 'fim'.")

    while True:
        item = input("Digite um material: ")
        if item.lower() == 'fim':
            break
        material_escolar.append(item)

    return material_escolar

# Criando a lista com os materiais
material_escolar = criar_lista_material()

# Imprimindo a lista de materiais escolares
print("\nLista de materiais escolares:")
for item in material_escolar:
    print(item)
