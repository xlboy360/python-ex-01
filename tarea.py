class Tarea:
    def __init__ (self, id_tarea = None, materia_tarea = None, titulo_tarea = None, descripcion = None, fecha_entrega = None):
        self.__id_tarea = id_tarea
        self.__materia_tarea = materia_tarea
        self.__titulo_tarea = titulo_tarea
        self.__descripcion = descripcion
        self.__fecha_entrega = fecha_entrega
    
    def __str__(self):
        return (
            f'Id tarea: {self.__id_tarea}, '
            f'Materia: {self.__materia_tarea}, '
            f'Titulo tarea: {self.__titulo_tarea}, '
            f'Descripcion: {self.__descripcion}, '
            f'Fecha entrega: {self.__fecha_entrega}'
        )
        
    def get_materia(self):
        return self.__materia_tarea
    
    def set_materia(self, materia):
        self.__materia_tarea = materia
        
    def get_titulo(self):
        return self.__titulo_tarea
    
    def set_titulo(self, titulo):
        self.__titulo_tarea = titulo
        
    def get_descripcion(self):
        return self.__descripcion
    
    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion
        
    def get_fecha(self):
        return self.__fecha_entrega

    def set_fecha(self, fecha):
        self.__fecha_entrega = fecha
        
    def get_id_tarea(self):
        return self.__id_tarea

    def set_id_tarea(self, id_tarea):
        self.__id_tarea = id_tarea
