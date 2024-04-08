# Día 2 de 30 dias de Python

# Nivel 1
# declara una variable
nombre = 'Claudio'
print( nombre )

apellido = 'Aravena'
print( apellido )

nombre_completo = nombre + ' ' + apellido
print( nombre_completo )

edad = 35
print( edad )

ciudad = 'Quillota'
print( ciudad )

is_light_on = True
print( is_light_on )

num_1, num_2, num_3 = 3, 4, 5
print( num_1, num_2, num_3)

#Nivel 2

#comprobar tipos de datos en variables
print( 'Tipo de nombre: ', type( nombre ))
print ( 'Tipo de nombre_completo: ', type( nombre_completo ))
print ( 'Tipo de edad: ', type( edad ))
print( 'Tipo de is_light_on: ', type( is_light_on ))

#utilizar la funcion integrada len()
print( 'Longitud de nombre: ', len( nombre ))
#compara la longitud de tu nombre y apellido 
print( 'Longitud de nombre: ', len( nombre ), ', longitud de apellido: ', len( apellido ))
#calcular el area de un circulo de radio 30m
pi = 3.14
radio = 30
area = pi * radio**2
print( area )
#calcular area de un circulo, radio ingresado por input
input_radio = float(input( 'Ingresa el radio del circulo en metros para calcular su area' ))
area_input = pi * input_radio**2
print( 'El valor del area del circulo de radio ', str(input_radio), ' es: ', str(area_input), ' mm2')