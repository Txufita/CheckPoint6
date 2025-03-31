
Las clases sirven para organizar el código y hacerlo más modular. Con las clases, podemos encapsular la lógica de nuestro programa en unidades lógicas y reutilizables. Además, las clases nos permiten heredar propiedades y métodos de otras clases, lo que nos permite crear jerarquías de objetos y reducir la cantidad de código que necesitamos escribir.

SINTAXIS

Para definir una clase en Python, utiliza la palabra clave «class», seguida del nombre de la clase y dos puntos. Por ejemplo:


class Perro:

Los atributos son variables que pertenecen a la clase. Para definir un atributo, utiliza la sintaxis «self.nombre_atributo = valor». Por ejemplo:


    Class Perro:
    def __init__(self, nombre, edad, raza):
    self.nombre = nombre
    self.edad = edad
    self.raza = raza 

Los métodos son funciones que pertenecen a la clase. Para definir un método, utiliza la sintaxis «def nombre_metodo(self, argumentos)». Por ejemplo:


    class Perro:
    def __init__(self, nombre, edad, raza):
    self.nombre = nombre
    self.edad = edad
    self.raza = raza

    def ladrar(self):
    print(«¡Guau!») 

 

En resumen, las clases son una herramienta fundamental en la programación orientada a objetos y en Python en particular. Utilizando las clases, podemos crear objetos que encapsulan la lógica de nuestro programa y nos permiten crear aplicaciones escalables y modulares.

 

 

# Que Método Se Ejecuta automáticamente Cuando Se Crea Una Instancia de una clase?

 

Cuando se crea una ueva instancia de la clase__init__ se ejecuta automáticamente

 

    class Persona:

    Def__init__(self, apellido, edad):

    Self.apellido = apellido

    Seld.edad = edad

 

    Def saludar(self):

    Print(f”Buen día, soy: {self.apellido} y mi edad es: {self.edad}años.”) ''

 

En este ejemplo, __init__ inicializa los atributos nombre y edad cuando se crea un nuevo objeto Persona. El método saludar permite que el objeto imprima un saludo.

 

 

# Cuales son los tres verbos de API?

 

*POST, GET, PUT*

 

Estos verbos, son el formato de comunicación entre el cliente y servidor web.

## GET

Realiza una petición a un recurso específico. No permite el envío de datos a excepción si dichos datos se envían como parámetro en la Url que realiza la petición. Esta petición retorna tanto la cabecera como el contenido. Este método GET puede retornar una respuesta en formato HTML, JSON, XML, Imágenes o JavaScript. Semánticamente se utiliza para consultar información como una SELECT a la base de datos, se puede filtrar datos empleando los datos enviados por la Url.

Formato de URL sin datos

[www.unsitioweb/index.html]

Formato de URL con datos

[www.unsitioweb/index.html?nombre=txufi&apellido=lamejor]

En este caso se envía los datos de nombre y apellido donde los claves son nombre y apellido y, valores txufi y lamejor respectivamente.

Formato envió datos por Formulario

También se usa el método GET en un formulario como se muestra a continuación:

    <form action="[www.unsitioweb/index.html]" method="get">

    Nombre: <input type="text" name="nombre"><br>

    Apellido: <input type="text" name="apellido"><br>

    <input type="submit" value="Enviar">

    </form> 

 

Respuesta HTTP

 

200 ok

400 bad request

404 no found

 

Características

Petición de cuerpo: no

Respuesta valida con cuerpo: si

Seguro: si

Idempotente: si

Chacheable: si

Permitido en HTML forms: si

 

 

## POST

Puede enviar datos al servidor por medio del cuerpo (body) y nada por la Url como se emplea en el método GET. El tipo de cuerpo de solicitud se define en la cabecera Content-Type. Semánticamente se utiliza para registrar información, similar al INSERT de datos a nivel de base de datos.  El POST usa enviando los datos por formularios, formato JSON entre otros. Si se compara con las sentencias SQL es similar a un INSERT.

 

Formato envió datos por Formulario

Por otro lado, se puede enviar usar el método POST en un formulario de la siguiente manera:

    <form action="[www.unsitioweb/index.html]" method="post">

    Nombre: <input type="text" name="nombre"><br>

    Apellido: <input type="text" name="apellido"><br>

    <input type="submit" value="Enviar">

    </form>

 

Formato JSON

Url:[www.unsitioweb/index.html]

Cuerpo:

    [{

    "nombre": "txufi",

     "apellido": "lamejor"

     }] 

 

Respuesta HTTP

 

200 Ok

201 Creado

400 Bad Request

404 No Found

 

 

 

Características

 

Peticion de cuerpo: Si

Respuesta valida con cuerpo: Si

Seguro: No

Idempotente: No

Chacheable: Sólo si incluye nueva informacion

Permitido en HTML forms: Si

 

 

## PUT

Es similar al método de petición POST, solo que el método PUT  puede ser ejecutado varias veces y tiene el mismo efecto, caso contrario a un POST que cada vez que se ejecuta realiza la agregación de un nuevo objeto, ya que semánticamente es como una inserción de un nuevo registro. Semánticamente el método PUT se utiliza para la actualización de información existente, es semejante a un UPDATE de datos a nivel de base de datos. Los requests de un PUT usualmente se envían los datos por formularios, formato JSON entre otros. Si se compara con las sentencias SQL es similar a un UPDATE.

 

Respuesta HTTP

 

200 Ok

201 Creado

204 No Responde, Si el servidor no devuelve ningún contenido

400 Bad Request

404 Not Found

 

 

 

Características

 

Peticion de cuerpo: Si

Respuesta valida con cuerpo: No

Seguro: No

Idempotente: Si

Chacheable: No

Permitido en HTML forms: No

 

# Es MongoDB una base de datos SQL o NoSQL?

 ![una imagen](https://cdn.prod.website-files.com/649b8ab4a5eb52039dce4a28/658e91c195208ba1f0db5079_what-is-MongoDB-900.webp)

MongoDB es una base de datos de código abierto NoSQL. Proporciona escalabilidad y alto rendimiento. Una base de datos relacional tiene tablas y las tablas tienen filas y columnas. Del mismo modo, MongoDB tiene colecciones y documentos. Un documento es un registro en la colección MongoDB. Una colección es un conjunto de documentos de MongoDB. Normalmente, todos los documentos tienen un propósito similar

La diferencia entre NoSQL y MongoDB es que NoSQL es un mecanismo para almacenar y recuperar datos en la base de datos no relacional y MongoDB es una base de datos orientada a documentos que pertenece a NoSQL.

El programador escribe documentos en formato JSON. MongoDB convierte internamente los objetos JSON se convierten a BSON. BSON es un objeto binario y tiene comillas tanto en clave como en valor. MongoDB es útil para el desarrollo de software basado en agile porque puede cambiar a una gran cantidad de datos. Es fácil cambiar los documentos agregando y eliminando fácilmente los existentes. MongoDB puede almacenar diferentes tipos de tipos de datos tales como cadenas, números, fechas, matrices, booleanos, etc. También tiene un tipo de datos de búfer para almacenar videos, imágenes y audio. El tipo de datos mixtos puede combinar diferentes tipos de datos. MongoDB tiene una sintaxis sencilla, por lo que es fácil escribir consultas. También puede proporcionar programas de reducción de mapas en arquitectura distribuida.

 
![mark](https://kinsta.com/es/wp-content/uploads/sites/8/2022/06/que-es-mongodb.jpeg)
 

Similitudes entre NoSQL y MongoDB:

1.Ambos pueden manejar Big Data.

2.Admite la escalabilidad horizontal sin hardware costoso.

3.Apoya la arquitectura distribuida.

4.Ambos no soportan uniones.

5.Ambos no pueden manejar transacciones complejas.

6.El esquema es dinámico.

7.Flexible y fácil de usar.

 

 

Diferencia entre NoSQL y MongoDB

 

NoSQL se utiliza para almacenar y recuperar datos en una base de datos no relacional

MongoDB es una base de datos escalable, de alto rendimiento, orientada a documentos, que es un sistema de gestión de base de datos no relacional

NoSQL puede ser de diferentes tipos, como base de documentos, almacén de valores clave, base de datos de gráficos, etc..

MongoDB es una base de datos orientada a documentos.

 

# Que es una API?

 

Las API son mecanismos que permiten a dos componentes de software comunicarse entre sí mediante un conjunto de definiciones y protocolos. Por ejemplo, el sistema de software del instituto de meteorología contiene datos meteorológicos diarios. La aplicación meteorológica de su teléfono “habla” con este sistema a través de las API y le muestra las actualizaciones meteorológicas diarias en su teléfono.

API significa “interfaz de programación de aplicaciones”. En el contexto de las API, la palabra aplicación se refiere a cualquier software con una función distinta. La interfaz puede considerarse como un contrato de servicio entre dos aplicaciones. Este contrato define cómo se comunican entre sí mediante solicitudes y respuestas. La documentación de su API contiene información sobre cómo los desarrolladores deben estructurar esas solicitudes y respuestas.

La arquitectura de las API suele explicarse en términos de cliente y servidor. La aplicación que envía la solicitud se llama cliente, y la que envía la respuesta se llama servidor. En el ejemplo del tiempo, la base de datos meteorológicos del instituto es el servidor y la aplicación móvil es el cliente. 

Las API pueden funcionar de cuatro maneras diferentes, según el momento y el motivo de su creación.

API de SOAP 

Estas API utilizan el protocolo simple de acceso a objetos. El cliente y el servidor intercambian mensajes mediante XML. Se trata de una API menos flexible que era más popular en el pasado.

API de RPC

Estas API se denominan llamadas a procedimientos remotos. El cliente completa una función (o procedimiento) en el servidor, y el servidor devuelve el resultado al cliente.

API de WebSocket

La API de WebSocket es otro desarrollo moderno de la API web que utiliza objetos JSON para transmitir datos. La API de WebSocket admite la comunicación bidireccional entre las aplicaciones cliente y el servidor. El servidor puede enviar mensajes de devolución de llamada a los clientes conectados, por lo que es más eficiente que la API de REST.

API de REST

Estas son las API más populares y flexibles que se encuentran en la web. El cliente envía las solicitudes al servidor como datos. El servidor utiliza esta entrada del cliente para iniciar funciones internas y devuelve los datos de salida al cliente.

API de REST

La principal característica de la API de REST es que no tiene estado. La ausencia de estado significa que los servidores no guardan los datos del cliente entre las solicitudes. Las solicitudes de los clientes al servidor son similares a las URL que se escriben en el navegador para visitar un sitio web. La respuesta del servidor son datos simples, sin la típica representación gráfica de una página web.

 

Las API de REST ofrecen cuatro beneficios principales:

 

Integración 

Las API se utilizan para integrar nuevas aplicaciones con los sistemas de software existentes. Esto aumenta la velocidad de desarrollo, ya que no hay que escribir cada funcionalidad desde cero. Puede utilizar las API para aprovechar el código existente.

Innovación 

Sectores enteros pueden cambiar con la llegada de una nueva aplicación. Las empresas deben responder con rapidez y respaldar la rápida implementación de servicios innovadores. Para ello, pueden hacer cambios en la API sin tener que reescribir todo el código.

 

Ampliación

Las API presentan una oportunidad única para que las empresas satisfagan las necesidades de sus clientes en diferentes plataformas. Por ejemplo, la API de mapas permite la integración de información de los mapas en sitios web, Android, iOS, etc. Cualquier empresa puede dar un acceso similar a sus bases de datos internas mediante el uso de API gratuitas o de pago.

 

Facilidad de mantenimiento

La API actúa como una puerta de enlace entre dos sistemas. Cada sistema está obligado a hacer cambios internos para que la API no se vea afectada. De este modo, cualquier cambio futuro que haga una de las partes en el código no afectará a la otra.

 

API web

Una API web o API de servicios web es una interfaz de procesamiento de aplicaciones entre un servidor web y un navegador web. Todos los servicios web son API, pero no todas las API son servicios web. La API de REST es un tipo especial de API web que utiliza el estilo arquitectónico estándar explicado anteriormente.

 

En cuanto al ámbito de uso se clasifican en:

 

API privadas

Estas son internas de una empresa y solo se utilizan para conectar sistemas y datos dentro de la empresa.

API públicas 

Están abiertas al público y pueden cualquier persona puede utilizarlas. Puede haber o no alguna autorización y coste asociado a este tipo de API.

API de socios 

Solo pueden acceder a ellas los desarrolladores externos autorizados para ayudar a las asociaciones entre empresas.

API compuestas 

Estas combinan dos o más API diferentes para abordar requisitos o comportamientos complejos del sistema. 

 

 

# Que es Postman?

![postman](https://desarrolloweb.com/media/181/boton-send.jpg)

Postman en sus inicios nace como una extensión que podía ser utilizada en el navegador Chrome de Google y básicamente nos permite realizar peticiones de una manera simple para testear APIs de tipo REST propias o de terceros.

Postman ha evolucionado y ha pasado de ser de una extensión a una aplicación que dispone de herramientas nativas para diversos sistemas operativos como lo son Windows, Mac y Linux.

Para qué sirve Postman

Postman sirve para múltiples tareas dentro de las cuales destacaré las siguientes:

Testear colecciones o catálogos de APIs tanto para Frontend como para Backend.

Organizar en carpetas, funcionalidades y módulos los servicios web.

Permite gestionar el ciclo de nuestra API.

Generar documentación de nuestras APIs.

Trabajar con entornos (calidad, desarrollo, producción) y de este modo es posible compartir a través de un entorno cloud la información con el resto del equipo involucrado en el desarrollo.

Métodos más utilizados y posibles errores

Postman cuenta con una serie de métodos que nos permiten tomar acción ante nuestras peticiones, a continuación, te dejamos los más utilizados:

GET: Obtener información

POST: Agregar información

PUT: Reemplazar la información

PATCH: Actualizar alguna información

DELETE: Borrar información

En cuanto a los posibles errores que podemos apreciar en la respuesta que nos ofrece la herramienta, lo resumiremos en que si la respuesta dada se encuentra en el rango de “200” quiere decir que toda la petición ha salido sin inconvenientes; mientras que el rango de los códigos de error “400” hacen referencia a errores con el cliente y aquellos errores en la línea de los “500” tienen que ver con fallos en el servidor.

 

Características de Postman

Cuenta con una comunidad grande de usuarios.

Es posible llevar a cabo trabajos de colaboración con el resto de los miembros de un equipo.

Su interface es sencilla e intuitiva.

Cuenta con una extensión para el navegador web Google Chrome.

Es posible agregar scripts (JavaScript) para añadir validaciones, automatizar y/o configurar pruebas.

Es posible integrarla con otras herramientas.

Permite trabajar con colecciones, que vienen siendo nuestra base de datos con las peticiones realizadas.

image.png
 

# Que es el polimorfismo?

 

El polimorfismo es la capacidad de un objeto para asumir diferentes formas. En programación, esto quiere decir que un objeto de una clase puede ser manejado como si fuera de una clase superior (o base), pero puede actuar de manera distinta dependiendo de cómo lo uses.

El polimorfismo es esa característica de los lenguajes de programación que permite que una misma función, método o incluso un operador se comporte de distintas maneras según el tipo de dato o el objeto con el que esté trabajando. Este concepto es fundamental para escribir código que sea más flexible y fácil de reutilizar.

Relación entre polimorfismo y herencia

Lo que permite la herencia es que una clase hija herede las propiedades y los métodos de una clase padre. Entonces, el polimorfismo entra en acción cuando un objeto de una clase hija es tratado como si fuera un objeto de la clase padre.

Por ejemplo, imagina que tienes una clase base Instrumento y varias clases derivadas como Guitarra, Piano y Batería. Lo que puedes hacer con el polimorfismo es crear una lista de Instrumentos y llenar esa lista con instancias de Guitarra, Piano y Batería, tratándolas todas como Instrumentos pero permitiendo que cada una actúe de acuerdo a su propia implementación.

 

Principalmente hay dos tipos de polimorfismo en programación:

 

Polimorfismo de sobrecarga (o polimorfismo estático): Es la capacidad de definir múltiples funciones con el mismo nombre pero con diferentes parámetros. Por ejemplo, podrías tener varias versiones de una función sumar(), una que sume enteros, otra que sume números decimales, y otra que concatene cadenas de texto.

 

Polimorfismo de inclusión (o polimorfismo dinámico): Este tipo ocurre cuando una clase derivada sobrescribe un método de su clase base y la decisión de qué método ejecutar se toma en tiempo de ejecución. Esto es lo que permite que un mismo método se comporte de manera diferente según el objeto que lo invoque.

 

 

Ejemplo:

Imagina que tienes dos clases, Gaviota y Aladelta, ambas con un método volar(). A pesar de no tener una clase base común, lo que hace Python es dejar que ambas clases compartan un método con el mismo nombre y lo llamen de manera polimórfica. Queda algo así:

    class Gaviota:
    def volar(self):
        return "La gaviota está volando

    class Aladelta:
    def volar(self):
        return "El aladelta está volando"

    def hacer_volar(objeto):
    print(objeto.volar())

    gaviota = Gaviota()
    aladelta = Aladelta()

    hacer_volar(gaviota)  

    Salida: La gaviota está volando.
    hacer_volar(aladelta)  

    Salida: El aladelta está volando. 

 

En este ejemplo, la función hacer_volar() es capaz de manejar objetos de diferentes clases Gaviota y Aladelta) siempre que estos implementen el método volar(). Esto es polimorfismo en acción, y demuestra cómo Python puede aplicar este concepto sin necesidad de una jerarquía de clases.

 

 

¿Para qué sirve el polimorfismo?

El polimorfismo sirve para que el código sea mucho más flexible, escalable, limpio y se pueda reutilizar. Entonces, en lugar de que debas escribir múltiples funciones para manejar cada tipo de objeto, simplemente escribes una sola función que maneje un objeto de la clase base y de ahí, solo te resta confiar en el polimorfismo para que el comportamiento se ajuste de manera automática al tipo de objeto específico.

De esta manera logras reducir la duplicación de código y facilitas el mantenimiento y la escalabilidad de los proyectos de software. Además, el código se podrá adaptar a cambios futuros, ya que puedes agregar nuevas clases derivadas sin necesidad de modificar el código existente.

 

# Que es un método dunder?

En Python, los métodos Dunder son aquellos cuyo nombre comienza y termina con dos guiones bajos (__).

Estos métodos no se llaman directamente, sino que son invocados automáticamente por el intérprete de Python en diversas situaciones (como operaciones aritméticas, manipulación de secuencias y gestión del contexto).

También conocidos como métodos mágicos o especiales

Algunos de los métodos dunder más comunes son:

Método

Descripción

__init__

Inicializa una nueva instancia de una clase

__str__

Devuelve una string de un objeto, amigable para el usuario

__repr__

Devuelve una string de un objeto, amigable para el desarrollador

__len__

Devuelve la longitud de un objeto

__getitem__

Permite acceder a elementos mediante índices

__setitem__

Permite asignar valores a elementos mediante índices

__delitem__

Permite eliminar elementos mediante índices

__iter__

Devuelve un iterador para el objeto

__next__

 

Devuelve el siguiente elemento del iterador

SINTAXIS

 

Método __init__

El método __init__ se utiliza para inicializar los atributos de una clase cuando se crea una nueva instancia.

 

class Persona:

     def __init__(self, nombre, edad):

        self.nombre = nombre

        self.edad = edad 

 

 

 

    persona1 = Persona("Txufi", 4)

    print(persona1.nombre) 

     Salida: Txufi

    print(persona1.edad)   

    Salida: 4 

 

 

Métodos __str__ y __repr__

 

Los métodos __str__ y __repr__ devuelven representaciones en cadena de un objeto. La diferencia principal es que __str__ está destinado a una representación amigable para el usuario, mientras que __repr__ está orientado a los desarrolladores y debe ser más detallado.

 

    class Persona:

    def __init__(self, nombre, edad):

        self.nombre = nombre

        self.edad = edad

   

    def __str__(self):

        return f"Persona: {self.nombre}, {self.edad} años"

   

    def __repr__(self):

        return f"Persona('{self.nombre}', {self.edad})

 

    persona1 = Persona("Txufi", 4)

    print(str(persona1)) 

    Salida: Persona: Txufi, 4 años

    print(repr(persona1))

    Salida: Persona('Txufi', 4) ''

 

 

Método __len__

El método __len__ se utiliza para devolver la longitud de un objeto.

 

    class Grupo:

    def __init__(self, miembros):

        self.miembros = miembros

   

    def __len__(self):

        return len(self.miembros)

 

    grupo = Grupo(["Alice", "Bob", "Charlie"])

    print(len(grupo)) 

    Salida: 3

 

 

Métodos __getitem__, __setitem__ y __delitem__

Estos métodos permiten que los objetos de una clase se comporten como contenedores (listas, diccionarios, etc.).

 

    class MiLista:

    def __init__(self):

        self.data = []

   

    def __getitem__(self, index):

        return self.data[index]

   

    def __setitem__(self, index, value):

        self.data[index] = value

   

    def __delitem__(self, index):

        del self.data[index]

 

    mi_lista = MiLista()

    mi_lista.data = [1, 2, 3, 4, 5]

    print(mi_lista[2])  

 

    Salida: 3

    mi_lista[2] = 30

    print(mi_lista[2])  

    Salida: 30

 

    del mi_lista[2]

    print(mi_lista.data)

    Salida: [1, 2, 4, 5]  

 

 

Métodos __iter__ y __next__

Estos métodos permiten que los objetos de una clase sean iterables.

 

    class Contador:

    def __init__(self, max):

        self.max = max

        self.contador = 0

   

    def __iter__(self):

        return self

   

    def __next__(self):

        if self.contador < self.max:

            self.contador += 1

            return self.contador

        else:

            raise StopIteration

 

    contador = Contador(5)

    for numero in contador:

    print(numero) 

 

 

Métodos Dunder para operaciones aritméticas

Además de los métodos mencionados, Python permite sobrecargar operadores aritméticos usando métodos dunder como __add__, __sub__, __mul__, __truediv__, entre otros.

 

    class Vector:

    def __init__(self, x, y):

        self.x = x

        self.y = y

   

    def __add__(self, otro):

        return Vector(self.x + otro.x, self.y + otro.y)

   

    def __repr__(self):

        return f"Vector({self.x}, {self.y})"

 

    v1 = Vector(2, 3)

    v2 = Vector(4, 5)

    v3 = v1 + v2

    print(v3) 

    Salida: Vector(6, 8) ''

 

 

 

# Que es un decorador?

Un decorador en Python es una función que recibe otra función como parámetro, le añade cosas y retorna una función diferente.

Lo siguiente es un decorador.

 

    def make_upper(func):

    def wrapper():

        return func().upper()

   

    return wrapper

 

    def python_greeting():

    return 'hi, i\'m a Python developer!'

 

    python_greeting = make_upper(python_greeting)  #This is what decorates the function

 

    print(python_greeting()) 

 

La función que recibe otra función es make_upper que recibe el argumento func que es una función. Dentro, se modifica a func usando wrapper. Y finalmente devuelve wrapper que es func pero diferente.

La función que se decora es python_greeting y la línea de código que lo hace es:

    python_greeting = make_upper(python_greeting)

Mira que implícitamente nunca modificamos python_greeeting. Solo usamos un decorador para convertir su output en mayúsculas. Salida:

 

HI, I'M A PYTHON DEVELOPER!

Si imprimimos solo la referencia a la función con print(python_greeting) solo se mostraría la clase a la que pertenece y su espacio en memoria.

    <function make_upper.<locals>.wrapper at 0x7f896e8c20e0>

Decoradores pythónicos: 

Ahora utilizamos el operador @ para decorar la función y obtener el mismo retorno.

 

    def make_upper(func):

    def wrapper():

        return func().upper()

   

    return wrapper

 

    @make_upper

    def python_greeting():

    return 'hi, i\'m a Python developer!'

 

    print(python_greeting()) 

 

 

Podemos decorar varias veces una sola función. No obstante, esto ocurre en el orden en que llamas a los decoradores. Un ejemplo en el que, además del decorador anterior, aplicamos uno que invierta el orden de las letras que le pasamos:

 

     def make_upper(func):

    def wrapper():

        return func().upper()

   

    return wrapper

 

    def reverse_str(func):

    def wrapper():

        return func()[::-1]

    

    return wrapper  

 

    @make_upper

    @reverse_str

    def python_greeting():

    return 'hi, i\'m a Python developer!'

 

    print(python_greeting()) 

 

Internamente, primero se aplica @make_upper para convertir todo el string en mayúsculas y luego @reverse_str para invertir el orden de la misma. Por lo tanto, en la terminal veremos.

!REPOLEVED NOHTYP A M'I ,IH

 

Es posible pasarles argumentos a la función decorada de la siguiente manera:

 

    def decorate_sum(func):

    def wrapper(arg1, arg2):

        print(f'Values to sum are: {arg1} and {arg2}.')

        return func(arg1, arg2)

    return wrapper

 

    @decorate_sum

    def sum_nums(num_1, num_2):

    return num_1 + num_2

 

    print(sum_nums(7, 9)) 

 

Como output obtenemos:

    Values to sum are: 7 and 9.

    16

 

 

 

Decoradores con múltiples variables: *args y **kwargs

Los argumentos especiales *args y **kwargs nos permiten pasar múltiples positional arguments y keyword arguments. Esto es una excelente ventaja para escribir código pythónico y escalable.

El decorador anterior ahora modificado para que pueda recibir tantos argumentos como queramos:

 

    def multiply_result(*args_parent):

    def inner_decorator(func):

        def wrapper(*args):

            nums_sum = args

            nums_multiply = sum(args_parent)

            print(f'sum{nums_sum} * {nums_multiply}:')

            return func(*args) * sum(args_parent)

        return wrapper

    return inner_decorator

 

    @multiply_result(3, 4, 5)

    def sum_nums(*args):

    return sum(args)

 

    print(sum_nums(1, 2))  

 

Modificamos el decorador y su función de tal forma que podamos pasar tantos argumentos como queramos. El código anterior hace que sum_nums reciba varios números y los suma. multiply_result hace lo mismo, pero este valor es multiplicado con aquel retornado de sum_nums.
