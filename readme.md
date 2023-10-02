# Proyecto Desarrollo Web - Caso Ember Technologies, Inc.

**Desarrollador:** Franco Felix Yance Gutierrez  
**Código:** U202013614  
**Correo:** u202013614@upc.edu.pe

<img src="https://media.discordapp.net/attachments/1148057148522233868/1156237601515257936/WIN_20230926_09_34_37_Pro.jpg?ex=651c26ae&is=651ad52e&hm=a57bd88b5a6bda2cc12164f8271e629cd590c678c2fa841fe5f12f7f0bb4d4a7&=&width=720&height=405" alt="Franco Felix Yance Gutierrez">

## Resumen

Este proyecto se centra en el desarrollo de una aplicación web para Ember Technologies, Inc., una empresa fundada por Clay Alexander, un inventor y empresario con más de 200 patentes en todo el mundo. Ember Technologies se destaca por su tecnología patentada de control de temperatura y su objetivo es mejorar la experiencia de consumir bebidas calientes.

El proyecto se divide en dos partes principales: la creación de una plataforma de backend para mostrar información sobre los productos de Ember Technologies y el desarrollo del sitio web para su catálogo de productos.

### Fake API

Para simular un backend, se proporcionan dos archivos: `db.json` y `routes.json`. Puedes usar json-server para iniciar el Fake API con los siguientes comandos:

cd server
json-server --watch db.json --routes routes.json

La información de los productos en general y los bundles se encuentra en los siguientes endpoints:

- Productos: [http://localhost:3000/api/v1/products](http://localhost:3000/api/v1/products)
- Bundles: [http://localhost:3000/api/v1/bundles](http://localhost:3000/api/v1/bundles)
- Productos pertenecientes a un bundle específico: [http://localhost:3000/api/v1/bundles/:bundleId/products](http://localhost:3000/api/v1/bundles/:bundleId/products)

### Desarrollo Frontend

Para el desarrollo web frontend, se ha elegido TypeScript como lenguaje de programación y Angular como Frontend Framework. La aplicación web debe cumplir con los siguientes requisitos:

- Toolbar con branding Ember y opciones "Home" y "Bundles".
- Vista "Home" con una imagen de héroe, título y párrafo.
- Vista "Bundles" que muestra información de los bundles en forma de tarjetas, incluyendo foto, título, calificación, precio y ahorro calculado.
- Vista "Page Not Found" para rutas no admitidas.
- Navegación a las vistas "Home" y "Bundles" desde las rutas /home y /store/bundles respectivamente.
- Redirección desde la vista raíz (/) a la vista /home.

El objetivo final de Ember Technologies es utilizar el control de temperatura para transformar la forma en que el mundo come, bebe y vive.
