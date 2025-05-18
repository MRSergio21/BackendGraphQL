# BackendGraphQL

Para ejecutar primero en la consola CDM dentro del proyecto coloca la siguiente sentencia:

## WINDOWS 🛠️

```
venv\Scripts\activate
```
## MAC && LINUX 🛠️

```
source venv/bin/activate
```

✅ Cuando está listo tiene que salir en la consola de siguiente manera

```
(venv) C:\Users\sergi\Documents\BackendGraphQL>
```

Luego en la consola coloca la siguiente instrucción

```
python main.py

```

## Preguntas

### 1. ¿Qué ventajas ofrece GraphQL sobre REST en este contexto?
GraphQL te da más flexibilidad y control sobre los datos. A diferencia de REST, donde estás limitado a endpoints fijos como /usuarios o /productos, con GraphQL tú decides exactamente qué datos quieres y cómo los quieres. Por ejemplo, puedes pedir un usuario junto con todos sus pedidos en una sola consulta, en vez de hacer varias llamadas.

También es genial cuando el frontend cambia seguido o cuando tienes múltiples versiones de app, porque GraphQL permite evolucionar la API sin romper nada, algo que en REST puede volverse un caos.

### 2. ¿Cómo se definen los tipos y resolvers en una API con GraphQL?
En GraphQL, primero defines los tipos de datos, que son como modelos. Luego creas los resolvers, que son funciones que dicen cómo obtener esos datos o cómo modificarlos.

### 3. ¿Por qué es importante que el backend también actualice disponible y no depender solo del frontend?
Porque el backend es el que manda cuando se trata de mantener los datos reales. Si el frontend decide si un producto está disponible, pero alguien hace otra compra al mismo tiempo, puedes terminar mostrando algo que ya no existe. Eso genera errores, quejas y mala experiencia para el usuario.

Además, el backend puede aplicar reglas que el frontend no siempre conoce, como “no marcar disponible si el stock está en negativo” o “bloquear productos caducados”. En resumen: el backend asegura que todo sea coherente y confiable.

### 4. ¿Cómo garantizas que la lógica de actualización de stock y disponibilidad sea coherente?
Lo clave es centralizar la lógica de negocio en el backend. No dejes que el frontend o la base de datos tomen decisiones por su cuenta.

Por ejemplo, cuando alguien compra un producto, una función del backend debería:

- Verificar si hay suficiente stock.

- Restarlo.

- Cambiar disponible a False si el stock llegó a cero.

- Guardar el nuevo estado.