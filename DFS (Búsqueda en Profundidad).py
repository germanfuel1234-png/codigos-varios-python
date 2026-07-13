# Definición de la función de Búsqueda en Profundidad (DFS)
def dfs(grafo, nodo, visitados=None):
    """
    grafo: Diccionario con las conexiones (Listas de adyacencia)
    nodo: El punto donde estamos parados actualmente
    visitados: Un conjunto (set) para recordar por dónde ya pasamos
    """
    
    # 1. Si es la primera llamada, inicializamos el conjunto de visitados
    if visitados is None:
        visitados = set()
    
    # 2. Verificamos si este nodo es "nuevo" para nosotros
    if nodo not in visitados:
        # Imprimimos el nodo para ver el orden de exploración
        print(f"Visitando nodo: {nodo}")
        
        # 3. Lo marcamos como visitado para no volver a entrar aquí (evita bucles infinitos)
        visitados.add(nodo)
        
        # 4. Revisamos a cada uno de los vecinos (hijos) del nodo actual
        for vecino in grafo[nodo]:
            # 5. RECURSIVIDAD: Nos lanzamos de cabeza al vecino antes de seguir con el siguiente
            # Esto es lo que hace que sea "en profundidad"
            dfs(grafo, vecino, visitados)

# --- CONFIGURACIÓN DEL ESCENARIO ---

# Representación del grafo: cada letra es un nodo y su lista son sus conexiones
red_de_nodos = {
    'A': ['B', 'C'],    # A está conectado con B y C
    'B': ['D', 'E'],    # B nos lleva a D y E
    'C': ['F'],         # C nos lleva a F
    'D': [],            # D es un camino sin salida
    'E': ['F'],         # E nos lleva a F
    'F': []             # F es un camino sin salida
}

# --- EJECUCIÓN ---
print("Iniciando exploración DFS desde el nodo A:")
dfs(red_de_nodos, 'A')