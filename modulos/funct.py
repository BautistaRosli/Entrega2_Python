#EL MÓDULO __INIT__.PY UNICAMENTE EXISTE PARA INDICAR QUE EL DIRECTORIO "MODULOS" ES UN PAQUETE PYTHON
#NO UTILIZO IF __NAME__ == __MAIN__ PORQUE ESTE MODULO UNICAMENTE CONTIENE DEF

#Inciso 1
def generar_estructura(names, goals,goals_avoided, assists):
    """Recibe 3 parámetros : un string de nombres, y 3 listas de goles, goles evitados y asistencias.
        Luego genera y retorna un diccionario por cada nombre del string que contiene un diccionario por cada parámetro de goles
        La función asume que los nombres no van a repetirse, ya que van a utilizarse como clave primaria del diccionario para asignar el resto de valores"""
    team = {}
    for name, goal,goal_avoided, assist in zip(names.split(", "),goals,goals_avoided,assists):
        #Se utiliza la funcion zip() para generar una tupla con todos los datos 
        team[name] = {"Goles": goal, "Goles evitados": goal_avoided, "Asistencias": assist}
        #Recorro la tupla generada a la vez que genero el diccionario en la variable team
    return team

#Inciso 2
def goleador(team):
    """Recibe como parámetro la estructura generada con generar_estructura y retorna el nombre y la cantidad de goles hechos por el jugador 
        con mayores goles realizados"""
    name = max(team, key = lambda x : team[x]["Goles"])
    #Se utiliza la función max() para buscar el nombre del jugador que mayores goles realizó. Esto se hace pasando 2 parámetros a max().
    #Primeramente se le pasa como parámetro la estructura en la cual se quiere buscar un valor máximo.
    #Como segundo parámetro se pasa como key una funcion lambda la cual especifica cuál es el criterio por el que se busque un valor máximo iterando entre cada nombre y qué quiero que me devuelva.
    #Es decir, se usa el parámetro x de lambda que aclara que se deben iterar los nombres (primera clave del diccionario) y tiene que retornar el nombre (colocado como clave en la estructura) del jugador que tiene el valor más alto dentro de su clave "Goles".
    goal = team[name]["Goles"]
    #luego se consigue la cantidad de goles utilizando el acceso directo por clave de los diccionarios accediendo al nombre con la variable resultado de la funcion max() de la línea anterior
    return name,goal

#Inciso 3
def jugador_mas_influeyente(team):
    """Recibe como parámetro la estructura generada con generar_estructura y retorna el nombre del jugador más influyente según la fórmula : 
        Goles * 1.5 + Goles evitados * 1.25 + Asistencias * 1 aplicando la función max a la estructura pasada como parámetro y una función lambda como key especificando 
        qué debe retornar según el criterio de key
        """
    return max(team, key = lambda x: team[x]["Goles"]*1.5 + team[x]["Goles evitados"]*1.25 + team[x]["Asistencias"])
    #la implementación es similar al de la función goleador()

#Inciso 4
def promedio_goles_team(team):
    """Recibe como parámetro la estructura generada con generar_estructura y retorna el promedio de goles realizados por todo el equipo en 25 partidos jugados"""
    return sum(team[name]["Goles"] for name in team) / 25
    #se utiliza la función sum para sumar cada uno de los valores dentro de la calve "Goles" de cada uno de los nombres del diccionario recorriendo los mismos con un for y se divide el resultado entre 25

#Inciso 5
def promedio_goles_player(team):
    """Recibe como parámetro la estructura generada con generar_estructura y retorna el promedio de goles del jugador que más goles realizó en 25 partidos"""
    return goleador(team)[1]/25
    #Se utiliza un llamado a la función goleador() y se toma el segundo elemento de la tupla (la cantidad de goles) y se divide entre 25 (cantidad de partidos jugados)