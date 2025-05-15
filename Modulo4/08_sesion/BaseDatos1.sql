# Creacion de Base de datos>
CREATE DATABASE AcademiaDevSenior;

# Uso de la Base de datos>
USE AcademiaDevSenior;

# Creacion de una tabla>
CREATE TABLE Estudiantes(
id INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100),
edad INT,
curso VARCHAR(100)
);

# Insertar datos en la tabla
INSERT INTO estudiantes(nombre, edad, curso) VALUES
('Juan', 25, 'Programacion'),
('Pepe', 30, 'Analisis');

# Consultar solo algunos campos>
SELECT nombre, curso FROM estudiantes;

# Filtrar datos:
SELECT * FROM estudiantes WHERE edad > 25;

# Actualizar datos
UPDATE estudiantes SET curso = 'Analisis de datos' WHERE id = 2;

# Eliminar datos
DELETE FROM estudiantes WHERE id = 2;

# Crear una tabla Profesores con id, nombre, especialidad y experiencia
CREATE TABLE profesores(
id INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100),
espacialidad VARCHAR(100),
experiencia INT
);

# Modificar una tabla una vez ya creada
ALTER TABLE profesores CHANGE
	COLUMN espacialidad especialidad VARCHAR(100);

# Insertar diez registros de profesores y estudiantes
INSERT INTO profesores(nombre, especialidad, experiencia) VALUES
('Carlos Ospina', 'Matemáticas', 5),
('Laura Gómez', 'Física', 3),
('Andrés Pérez', 'Química', 7),
('María Rodríguez', 'Biología', 4),
('Jorge Martínez', 'Historia', 6),
('Ana Torres', 'Lengua', 2),
('Luis Ramírez', 'Geografía', 8),
('Diana Salazar', 'Inglés', 5),
('Felipe Castro', 'Educación Física', 9),
('Natalia Ríos', 'Arte', 3);

INSERT INTO estudiantes(nombre, edad, curso) VALUES
('Diego Chacón', 22, 'Programación de Software'),
('Laura Méndez', 20, 'Diseño Gráfico'),
('Carlos Ruiz', 23, 'Ingeniería de Sistemas'),
('Ana Beltrán', 21, 'Administración de Empresas'),
('Julián Torres', 22, 'Contaduría Pública'),
('Mariana López', 19, 'Psicología'),
('Santiago Vargas', 24, 'Derecho'),
('Valentina Ríos', 20, 'Medicina'),
('Camilo Herrera', 22, 'Ingeniería Electrónica'),
('Isabela Gómez', 21, 'Arquitectura');


# Consultar todos los profesores con mas de 5 años de experiencia
SELECT * FROM profesores WHERE experiencia > 5;

# Actualizar la especialidad de un profesor
UPDATE profesores SET especialidad = 'Programacion' WHERE id = 5;

# Eliminar un registro
DELETE FROM profesores WHERE id = 3;

# Agregar una columna a tabla existente y una foreign key
ALTER TABLE estudiantes 
	ADD COLUMN curso_id INT,
	ADD FOREIGN KEY (curso_id) REFERENCES cursos(id_cursos);

# Consulta personalizada
SELECT estudiantes.nombre, cursos.nombre AS curso
FROM estudiantes
JOIN cursos ON estudiantes.curso_id = cursos.id_cursos