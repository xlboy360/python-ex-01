#Clase para probar nuestra bd
from tarea import Tarea
from tareaDao import TareaDAO
opc = 0

while(opc!=0):
    print('MENU TAREAS-BASE DE DATOS')
    print('1.Añadir Tarea \n2.Enlistar Tareas \n3.Actualizar Tarea \n4.Eliminar tarea \n5.Salir')
    opc = int(input('Ingrese su opcion [1-5]:' ))
    switch(opc):
        case 1:
            print('INGRESAR NUEVA TAREA')
            materia = input('Ingrese la materia: ')
            titulo = input('Ingrese el titulo: ')
            descripcion = input('Ingrese la descripcion de la tarea: ')
            fecha = input('Ingrese fecha de entrega: [dd-mm-YYYY]: ')
            tareaI = Tarea(materia, titulo, descripcion, fecha)
            TareaDAO.insertar(tareaI)
            break;
        case 2:
            print(TareaDAO.seleccionar())
            break;
        case 3:
            print('INGRESAR ACTUALIZACION DE TAREA')
            idA = input('Ingrese el id de la tarea a actualizar')
            materia = input('Ingrese la materia para actualizar: ')
            titulo = input('Ingrese el titulo actualizado: ')
            descripcion = input('Ingrese la descripcion de la tarea: ')
            fecha = input('Ingrese fecha de entrega: [dd-mm-YYYY]: ')
            tareaA = Tarea(materia, titulo, descripcion, fecha, idA)
            TareaDAO.actualizar(tareaA)
            break;
        case 4:
            print('ELIMINAR TAREA')
            idE = input('Ingrese el id de la tarea a eliminar')
            TareaDAO.eliminar(idE)
            break;
