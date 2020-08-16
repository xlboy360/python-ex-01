import psycopg2 as db

class Conexion:
    #Elementos de la Conexion
    __DATABASE = 'own_tests'
    __USERNAME = 'postgres'
    __PASSWORD = 'admin'
    __DB_PORT = '5432'
    __HOST = '123.0.0.1'
    __conexion = None
    __cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls.__conexion is None:
            try:
                cls.__conexion = db.connect(host=cls.__HOTS,
                                            user=cls.__USERNAME,
                                            password=cls.__PASSWORD,
                                            port=cls.__DB_PORT,
                                            database=cls.__DATABASE)
            except Exception as e:
                print(f'Error al conectar a la base de datos. {e}')
        else:
            return cls.__conexion

    @classmethod
    def obtenerCursor(cls):
        if(cls.__cursor is None):
            try:
                cls.__cursor = cls.obtenerConexion().cursor()
                return cls.__cursor
            except Exception as e:
                print(f'No se ha podido establecer el cursor: {e}')
        else:
            return cls.__cursor

    @classmethod
    def cerrarConexionCursor(cls):
        if cls.__cursor is not None:
            try:
                cls.__cursor.close()
            except Exception as e:
                print(f'No se ha podido cerrar el cursor: {e}')
        if cls.__conexion is not None:
            try:
                cls.__conexion.close()
            except Exception as e:
                print(f'No se ha podido cerrar la conexión: {e}')
        print('Se han cerrado con éxito!')
