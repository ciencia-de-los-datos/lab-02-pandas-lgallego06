"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01(dataframe):
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    num_rows=dataframe.shape[0]
    return num_rows
#cantidad_fila=pregunta_01(tbl0)
#print(cantidad_fila)


def pregunta_02(dataframe):
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    num_columns=dataframe.shape[1]
    return num_columns
#cantidad_columns=pregunta_02(tbl0)
#print(cantidad_columns)


def pregunta_03(dataframe):
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna _c1 del archivo
    `tbl0.tsv`?

    Rta/
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: _c1, dtype: int64

    """
    registros_tabla=dataframe['_c1'].value_counts().sort_index()
    return registros_tabla
#registro=pregunta_03(tbl0)
#print(registro)


def pregunta_04(dataframe):
    """
    Calcule el promedio de _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: _c2, dtype: float64
    """
    promedio=dataframe.groupby('_c1')['_c2'].mean()
    return promedio
#promedio=pregunta_04(tbl0)
#print(promedio)


def pregunta_05(dataframe):
    """
    Calcule el valor máximo de _c2 por cada letra en la columna _c1 del archivo
    `tbl0.tsv`.

    Rta/
    _c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: _c2, dtype: int64
    """
    maximo=dataframe.groupby('_c1')['_c2'].max()
    return maximo
#maximo=pregunta_05(tbl0)
#print(maximo)


def pregunta_06(dataframe):
    """
    Retorne una lista con los valores unicos de la columna _c4 de del archivo `tbl1.csv`
    en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    value_unique=sorted(dataframe['_c4'].str.upper().unique())
    return value_unique
#valor_unico=pregunta_06(tbl1)
#print(valor_unico)


def pregunta_07(dataframe):
    """
    Calcule la suma de la _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    _c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: _c2, dtype: int64
    """
    suma_por_letra=dataframe.groupby('_c1')['_c2'].sum()
    return suma_por_letra
#suma_por_letra=pregunta_07(tbl0)
#print(suma_por_letra)


def pregunta_08(dataframe):
    """
    Agregue una columna llamada `suma` con la suma de _c0 y _c2 al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  suma
    0     0   E    1  1999-02-28     1
    1     1   A    2  1999-10-28     3
    2     2   B    5  1998-05-02     7
    ...
    37   37   C    9  1997-07-22    46
    38   38   E    1  1999-09-28    39
    39   39   E    5  1998-01-26    44

    """
    dataframe['suma']=dataframe['_c0']+dataframe['_c2']
    return dataframe
#suma=pregunta_08(tbl0)
#print(suma)


def pregunta_09(dataframe):
    """
    Agregue el año como una columna al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  year
    0     0   E    1  1999-02-28  1999
    1     1   A    2  1999-10-28  1999
    2     2   B    5  1998-05-02  1998
    ...
    37   37   C    9  1997-07-22  1997
    38   38   E    1  1999-09-28  1999
    39   39   E    5  1998-01-26  1998

    """
    dataframe['year']=dataframe['_c3'].str[:4].astype(int)
    return dataframe
#year=pregunta_09(tbl0)
#print(year)


def pregunta_10(dataframe):
    """
    Construya una tabla que contenga _c1 y una lista separada por ':' de los valores de
    la columna _c2 para el archivo `tbl0.tsv`.

    Rta/
                                   _c1
      _c0
    0   A              1:1:2:3:6:7:8:9
    1   B                1:3:4:5:6:8:9
    2   C                    0:5:6:7:9
    3   D                  1:2:3:5:5:7
    4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """
    tabla=dataframe.groupby('_c1')['_c2'].apply(lambda x:':'.join(map(str,sorted(x)))).reset_index()
    return tabla
#tabla_num=pregunta_10(tbl0)
#print(tabla_num)


def pregunta_11(dataframe):
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c4 del archivo `tbl1.tsv`.

    Rta/
        _c0      _c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    tabla_letra=dataframe.groupby('_c0')['_c4'].apply(lambda x:','.join(map(str,sorted(x)))).reset_index()
    return tabla_letra
#tabla_letra=pregunta_11(tbl1)
#print(tabla_letra)



def pregunta_12(dataframe):
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.

    Rta/
        _c0                                  _c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    dataframe['_c5']=dataframe['_c5a'].astype(str)+':'+dataframe['_c5b'].astype(str)
    tabla=dataframe.groupby('_c0')['_c5'].apply(lambda x:','.join(map(str,sorted(x)))).reset_index()
    return tabla
#tabla_c5=pregunta_12(tbl2)
#print(tabla_c5)


def pregunta_13(dataframe):
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, compute la
    suma de tbl2._c5b por cada valor en tbl0._c1.

    Rta/
    _c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: _c5b, dtype: int64
    """
    merged=pd.merge(dataframe,tbl2, on='_c0')
    suma_por_c1=merged.groupby('_c1')['_c5b'].sum()
    return suma_por_c1
merged=pregunta_13(tbl0)
print(merged)