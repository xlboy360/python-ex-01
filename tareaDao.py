from conexion import Conexion
from tarea import Tarea
import psycopg2 as db

class TareaDAO:
    
    __SELECT = "SELECT * FROM Tarea WHere Id_tarea = %s"
    __INSERT = "INSERT INTO Tarea(materia, titulo, descripcion, fecha) VALUES(%S,%S,%S,%S)"
    __UPDATE = "UPDATE Tarea SET  materia=%s, titulo=%s, descripcion =%s, fecha=%s WHERE id_tarea = %s"
    __DELETE = "DELETE FROM Tarea WHERE id_tarea = %s"
    
    @classmethod
    def seleccionar(cls):
        cursor=Conexion.obtenerCursor()
        cursor.execute(cls.__SELECT)
        registros = cursor.fetchall()
        tareas = []
        for registro in registros:
            tarea = Tarea(registro[0], registro[1], registro[2], registro[3], registro[4])
            tareas.append(tarea)
        Conexion.close()
        return tareas

    @classmethod
    def insertar(cls, tarea):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            valores = (tarea.get_materia(), tarea.get_titulo(), tarea.get_descripcion(), tarea.get_fecha())
            cursor.execute(cls.__INSERT, valores)
            conexion.commit()
            print('Se ha añadido la tarea...')
        except Exception as e:
            conexion.rollback()
            print(f'No se ha añadido el registro {e}')
        finally:
            conexion.cerrarConexionCursor()
            
    @classmethod
    def actualizar(cls, tarea):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            valores = (tarea.get_materia(), tarea.get_titulo(), tarea.get_descripcion(), tarea.get_fecha(), tarea.get_id_tarea())
            cursor.execute(cls.__UPDATE, valores)
            conexion.commit()
            print('Se ha actualizado la tarea...')
        except Exception as e:
            conexion.rollback()
            print(f'No se actualizo el registro {e}')
        finally:
            conexion.cerrarConexionCursor()
    
    @classmethod
    def eliminar(cls, tarea):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            valores = (tarea.get_id_tarea)
            cursor.execute(cls.__DELETE, valores)
            conexion.commit()
        except Exception as e:
            conexion.rollback()
            print(f'No se eliminó la tarea {e}')
        finally:
            conexion.cerrarConexionCursor()
