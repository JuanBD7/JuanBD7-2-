#Tipos de sushi

Pikachu_roll=4500
Otaku_roll =5000
Pulpo_Venenoso_roll =5200
Anguila_Eléctrica_roll=4800
pedido = 'x'
respuesta = False

while pedido=='x':
    
        print('Escoja los sushis:')
        print('1. Pikachu Roll $4500')
        print('2. Otaku Roll $5000')
        print('3. Pulpo Venenoso Roll $5200')
        print('4. Anguila Eléctrica Roll $4800')
        cant_pikachu =int(input('Pikachu: '))
        cant_otaku =int(input('Otaku: '))
        cant_pulpo =int(input('Pulpo: '))
        cant_anguila =int(input('Anguila: '))

        Precio_total_pedido = Pikachu_roll*cant_pikachu + Otaku_roll*cant_otaku + Pulpo_Venenoso_roll*cant_pulpo + Anguila_Eléctrica_roll*cant_anguila
        
        nuevo_pedido=(input('¿Desea algo mas?: x. si / 0.no: '))
        pedido=nuevo_pedido

while respuesta==False:
    pregunta_codigo=(input('¿Posee codigo de descuento?:1 (si) / 2 (no): '))
    if pregunta_codigo=='1':
        codigo=input('Ingrese codigo: ')
        if codigo=='soyotaku':
            Precio_total_pedido=(Precio_total_pedido)*0.1
            respuesta==True
        else:
            print('Codigo no valido.')
            opcion=input('Ingrese codigo (1) o vuelva a menu presionando x')
            if opcion=='1':
                pregunta_codigo=opcion
    else:
        respuesta==True
        break
print(f'Su pedido total es: {Precio_total_pedido}')
        
            
            

    
