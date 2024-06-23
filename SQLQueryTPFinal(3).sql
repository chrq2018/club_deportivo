CREATE DATABASE CLUB_DEPORTIVO;
GO

USE CLUB_DEPORTIVO;
GO

CREATE TABLE Clientes (
    id_cliente INT PRIMARY KEY IDENTITY(1,1),
    nombre NVARCHAR(100) NOT NULL,
    apellido NVARCHAR(100) NOT NULL,
    telefono NVARCHAR(20) NOT NULL,
    deporte NVARCHAR(20) NULL CHECK (Deporte IN (NULL, 'Fútbol', 'Tenis', 'Básquet')),
    tipo_de_cliente NVARCHAR(20) NOT NULL CHECK (tipo_de_cliente IN ('Socio', 'No socio', 'Invitado')),
    estado NVARCHAR(20) DEFAULT 'Activo' CHECK (estado IN (NULL, 'Activo', 'Inactivo'))
);


CREATE TABLE Pagos (
    id_pago INT PRIMARY KEY IDENTITY(1,1),
    mes INT NOT NULL,
    anio INT NOT NULL,
    monto DECIMAL(10, 2) NOT NULL,
    tipo_de_cuota NVARCHAR(20) NOT NULL CHECK (tipo_de_cuota IN ('Social', 'Deportiva')),
    id_cliente INT NOT NULL,
    CONSTRAINT FK_Pagos_Clientes FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);




CREATE TABLE Usuarios (
    id_usuario INT PRIMARY KEY IDENTITY(1,1),
    usuario NVARCHAR(50) NOT NULL UNIQUE,
    pass NVARCHAR(50) NOT NULL,
    tipo_de_cuenta NVARCHAR(20) NOT NULL CHECK (tipo_de_cuenta IN ('Administrador', 'Empleado'))
);



INSERT INTO Clientes (Nombre, Apellido, Telefono, Deporte, Tipo_de_cliente)
VALUES 
    ('Juan', 'Pérez', '1145632548', 'Fútbol', 'Socio'),
    ('Ana', 'Martínez', '1145678913', 'Tenis', 'No socio'),
    ('Luis', 'García', '1122333445', 'Básquet', 'Socio'),
    ('María', 'López', '1123456789', NULL, 'Socio'),
    ('Carlos', 'Sánchez', '1135356485', 'Fútbol', 'No socio'),
    ('Laura', 'Fernández', '1134578956', 'Tenis', 'Invitado'),
    ('Miguel', 'Torres', '1166569886', 'Básquet', 'No socio'),
    ('Lucía', 'Ramírez', '1145674562', NULL, 'Socio'),
    ('Pedro', 'Hernández', '1124578695', NULL, 'Invitado'),
    ('Elena', 'Díaz', '1132654875', 'Tenis', 'No socio');




INSERT INTO Pagos (Mes, Anio, Monto, Tipo_de_cuota, Id_cliente)
VALUES 
    (1, 2024, 7500, 'Deportiva', 1),
    (1, 2024, 12500, 'Deportiva', 2),
    (1, 2024, 7500, 'Deportiva', 3),
    (1, 2024, 10000, 'Social', 4),
    (1, 2024, 12500, 'Deportiva', 5),
    (2, 2024, 7500, 'Deportiva', 1),
    (2, 2024, 12500, 'Deportiva', 2),
    (2, 2024, 7500, 'Deportiva', 3),
    (2, 2024, 10000, 'Social', 4),
    (2, 2024, 12500, 'Deportiva', 5),
    (3, 2024, 7500, 'Deportiva', 1),
    (3, 2024, 12500, 'Deportiva', 2),
    (3, 2024, 7500, 'Deportiva', 3),
    (3, 2024, 10000, 'Social', 4),
    (3, 2024, 12500, 'Deportiva', 5),
    (4, 2024, 7500, 'Deportiva', 1),
    (4, 2024, 12500, 'Deportiva', 2),
    (4, 2024, 7500, 'Deportiva', 3),
    (4, 2024, 10000, 'Social', 4),
    (4, 2024, 12500, 'Deportiva', 5),
    (5, 2024, 7500, 'Deportiva', 1),
    (5, 2024, 12500, 'Deportiva', 2),
    (5, 2024, 7500, 'Deportiva', 3),
    (5, 2024, 10000, 'Social', 4),
    (5, 2024, 12500, 'Deportiva', 5),
    (6, 2024, 12500, 'Deportiva', 5),
    (6, 2024, 7500, 'Deportiva', 1),
    (6, 2024, 12500, 'Deportiva', 7),
    (6, 2024, 12500, 'Social', 8),
    (6, 2024, 12500, 'Deportiva', 2),
    (6, 2024, 12500, 'Deportiva', 10);



INSERT INTO Usuarios (Usuario, Pass, Tipo_de_cuenta)
VALUES 
    ('Juan', 'pass1', 'Empleado'),
    ('Maria', 'pass2', 'Administrador'),
    ('Carlos', 'pass3', 'Administrador'),
    ('Elena', 'pass4', 'Empleado');


	SELECT * FROM Clientes 
    SELECT * FROM Usuarios
    SELECT * FROM Pagos