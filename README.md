# InnosoftDiplomas
Herramienta de generación de diplomas para las jornadas de Innosoft de la Universidad de Sevilla.
La herramienta utiliza archivos generados mediante la plataforma [Evidentia](https://github.com/drorganvidez/evidentia)

Herramienta realizada por:
* Alé Palacios, Francisco (fraalepal@alum.us.es)
* Biedma Fresno, Pedro (pedbiefre@alum.us.es)
* Gata Fernández, José Manuel (josgatfer@alum.us.es)
* Losada Ostos, Guillermo (guilosost@alum.us.es)
* Merino Verde, Enrique (enrmerver@alum.us.es)
* Yanes Ariza, Miguel (migyanari@alum.us.es)

# Requisitos de uso

### Preparación para el uso
Para el correcto funcionamiento de la aplicación, es necesario descargar la carpeta **InnosoftDiploma** al completo y el archivo .exe del siguiente enlace: https://mega.nz/file/spxmCYQZ#BW-5sxYzJjbD5UWdk8Lyo_Gq_LciNodiibAjYA_7-c8, el cual se deberá meter en la carpeta y **NO** deberá moverse de esta ruta.

### Archivos necesarios para la generación de diplomas
Para exportar en Evidentia el archivo .xlsx requerido para generar automáticamente los diplomas de asistencia, habrá que estar conectado con la cuenta de **Profesor**, acceder a **Exportaciones** y dejar seleccionadas **todas las opciones**

![Menú navegable de Evidentia](https://cdn.discordapp.com/attachments/768136234287366175/778612940278333480/unknown.png)
![Imagen de cómo generar .xlsx en Evidentia](https://cdn.discordapp.com/attachments/768136234287366175/778610418896863282/unknown.png)

### Generación de diplomas
Para poder generar los distintos tipos de diplomas, deberemos haber completado los dos pasos anteriores. Ejecutaremos el archivo .exe y nos encontraremos la siguiente interfaz. En la que vemos cinco opciones diferentes (con submenús anidados) en la parte superior: Generación automática, Diplomas especiales, Opciones, Envío automático y Salir.

![Interfaz InnosoftDiplomas](https://cdn.discordapp.com/attachments/646777871016263713/800330702238253066/Screenshot_1.png)

Para generar los diplomas de asistencia a las jornadas de Innosoft automáticamente, nos dirigiremos a la primera opción y nos saldrá un desplegable con dos opciones: Generar diplomas de Asistencia y Generar diplomas de Organizadores.

![Botón Generación automáticas](https://cdn.discordapp.com/attachments/646777871016263713/800330992409378826/Screenshot_2.png)

Si elegimos la primera opción (Generar diplomas de asistencia) nos aparecerá la siguiente ventana con distintas opciones y parámetros.

![Diplomas asistencia](https://cdn.discordapp.com/attachments/646777871016263713/800330994132975626/Screenshot_3.png)

Tenemos dos opciones distintas para elegir el tipo de diploma que queremos generar: la primera sería un diploma básico en la que los parámetros se rellenarían dándole como fuente de información el archivo .xlsx que hemos generado con Evidentia.

![Archivo diploma básico](https://cdn.discordapp.com/attachments/646777871016263713/800330995635191870/Screenshot_4.png)

La otra opción, sería generar un diploma personalizado con los parámetros que introduzcamos en cada uno de los campos, simplemente tendríamos que rellenarlos para crearlo.

Si continuamos con la siguiente opción del menú superior, tenemos un menú desplegable con tres opciones: Diplomas extraordinarios, Diplomas ponente y Diplomas organizadores.

![Tipos de diplomas](https://cdn.discordapp.com/attachments/646777871016263713/800331000302272522/Screenshot_8.png)

El primer tipo es diplomas extraordinarios, y al pulsar en él nos muestra la siguiente interfaz:

![Diplomas extraordinarios](https://cdn.discordapp.com/attachments/646777871016263713/800330997756723210/Screenshot_5.png)

Los otros dos tipos (ponentes y organizadores) nos ofrecen una ventana con la misma interfaz obteniendo como resultados diplomas diferentes:

![Diplomas ponentes/organizadores](https://cdn.discordapp.com/attachments/646777871016263713/800330997982822411/Screenshot_6.png)

En el menú Opciones, podemos cambiar la fuente de letras con la que se generarán los diplomas.

![Opciones](https://cdn.discordapp.com/attachments/646777871016263713/800333863943012372/Screenshot_9.png)

Por defecto, viene seleccionada la fuente Philosopher, pero tenemos dos fuentes más para elegir.

![Fuentes de letra](https://cdn.discordapp.com/attachments/646777871016263713/800333868590825472/Screenshot_10.png)

La penúltima opción, sirve para enviar correos a cada asistente con su diploma adjunto.

![Emails](https://cdn.discordapp.com/attachments/646777871016263713/800334931829194772/Screenshot_11.png)

Para hacer uso de esta funcionalidad, habrá que realizar una configuración previa en nuestra cuenta de Gmail. Dado que Google, por defecto, bloquea el acceso de aplicaciones externas para realizar este tipo de envíos 'masivos'.

Tendremos que dirigirnos a la siguiente página web: https://myaccount.google.com/lesssecureapps e iniciar sesión con nuestra cuenta de Google. Nos encontraremos con la siguiente interfaz, y deberemos permitir el acceso a aplicaciones menos seguras.

![Configuración Gmail](https://cdn.discordapp.com/attachments/646777871016263713/800330985320349726/Screenshot_15.png)

Una vez hecho esto, podemos iniciar sesión en nuestra cuenta y enviar los correos. En la aplicación, veremos lo siguiente:

![Login](https://cdn.discordapp.com/attachments/646777871016263713/800331032443355166/Screenshot_12.png)

Cuando iniciemos sesión, tendremos que indicar a la aplicación, de nuevo, qué archivo debe utilizar como fuente de información para las direcciones de correo a las que enviar los diplomas previamente, generados. Deberemos elegir el archivo generado por Evidentia:

![Archivo email](https://cdn.discordapp.com/attachments/646777871016263713/800331038467424276/Screenshot_13.png)

La aplicación tardará un poco en enviar todos los emails, pero cuando lo haga obtendremos el siguiente mensaje:

![Envío correos](https://cdn.discordapp.com/attachments/646777871016263713/800330981503926312/Screenshot_14.png)


