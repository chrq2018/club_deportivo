# Sistema de Gestión Administrativa para un Club de Deportes

## Grupo 5:

- **Dante Maestrelli**: Documentación
- **Christian Quiroga**: Desarrollo
- **Martín Miselli**: Testeo

## Introducción

Este proyecto tiene como objetivo desarrollar un sistema de gestión administrativa para un club de deportes. El sistema permite administrar clientes, registrar pagos, emitir comprobantes y generar informes mensuales.

## Funcionalidades Principales

1. **Acceso Restringido**: El sistema controla el acceso a ciertas funciones según el rol del usuario (Empleado o Administrador).
2. **Gestión de Clientes**: Alta, baja, modificación, búsqueda y listado de clientes.
3. **Registro de Pagos**: Registro de pagos de cuotas sociales y deportivas.
4. **Emisión de Comprobantes**: Generación de comprobantes de pago por pantalla.
5. **Informes Mensuales**: Generación de informes de recaudación mensual.

## Estructura del Proyecto

El proyecto consta de dos archivos principales: `main.py` y `funciones.py`.

### main.py

Este archivo contiene el flujo principal del programa. Aquí se inicia el menú de inicio de sesión y, dependiendo del rol del usuario (Empleado o Administrador), se navega por las diferentes opciones del sistema.

- **Inicio de Sesión**: Solicita las credenciales del usuario y valida el acceso.
- **Menú Principal**: Dependiendo del rol, muestra opciones específicas para empleados o administradores.

### funciones.py

Este archivo contiene todas las funciones necesarias para la operación del sistema.

#### Funciones Principales

1. **Conexión a la Base de Datos**: Establece una conexión con el servidor SQL Server para realizar operaciones de consulta y manipulación de datos.

2. **Menús de Navegación**:

   - **menu_login**: Muestra el menú de inicio de sesión.
   - **menu_principal**: Muestra el menú principal adaptado según el rol del usuario.

3. **Gestión de Clientes**:

   - **alta**: Permite dar de alta a nuevos clientes en el sistema.
   - **baja**: Marca a los clientes como inactivos en el sistema.
   - **modificar**: Permite modificar los datos de los clientes.
   - **lista**: Muestra un listado de todos los clientes.
   - **ver_cliente**: Permite buscar clientes por nombre o apellido.

4. **Gestión de Pagos**:

   - **registrar_pago**: Registra pagos de cuotas mensuales para los clientes.
   - **mostrar_comprobante_pago**: Genera y muestra un comprobante de pago.
   - **mostrar_pagos**: Muestra un listado de todos los pagos registrados.

5. **Validación y Inicio de Sesión**:

   - **validar_inicio_sesion**: Valida las credenciales de inicio de sesión del usuario.
   - **iniciar_sesion**: Verifica las credenciales contra la base de datos.

6. **Generación de Informes**:
   - **mostrar_informe**: Genera un informe de la recaudación mensual basado en los pagos registrados.

## Roles y Responsabilidades

- **Dante Maestrelli**: Responsable de la documentación del proyecto, incluyendo la creación de este documento.
- **Christian Quiroga**: Responsable principal del desarrollo del sistema, implementando las funcionalidades y asegurando su correcto funcionamiento.
- **Martín Miselli**: Responsable del testeo del sistema, verificando que todas las funciones operen correctamente y realizando pruebas exhaustivas para asegurar la calidad del producto final.

## Conclusión

El sistema desarrollado permite una gestión eficiente de un club de deportes, facilitando la administración de clientes y pagos, y proporcionando herramientas para la generación de informes y comprobantes. La colaboración del equipo fue fundamental para alcanzar los objetivos propuestos, con cada miembro aportando en todas las etapas del desarrollo del proyecto.
