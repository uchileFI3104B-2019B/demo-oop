#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Este script muestra los elementos basicos de la programacion orientada al
objeto implementada en Python.
'''


class Person(object):
    '''
    Este es el docstring the la clase Person.
    En gral. las clases tienen nombres que parten con mayuscula.
    El argumento en el parentesis es opcional en python 2, obligatorio en python
    3 y corresponde a la clase de la cual se derivan los objetos. Si no saben
    bien lo que hacen, al principio es seguro usar 'object', lo que quiere decir
    es que la nueva clase 'Persona', hereda de la clase abstracta 'object'.
    '''

    nombre = 'no tengo nombre'
    apellido = 'no tengo apellido'

    def saluda(self):
        '''
        Imprime mensaje de saludo de parte de la persona.
        '''
        print 'Hola, my nombre es {} {}'.format(self.nombre, self.apellido)


# Demostrando el uso de la clase

una_persona = Person()
una_persona.nombre = 'Juanito'
una_persona.apellido = 'Perez'
una_persona.saluda()
