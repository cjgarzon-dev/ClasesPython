-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS academia;

-- Usar la base de datos creada
USE academia;

-- Tabla: Estudiantes
CREATE TABLE Estudiantes (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    correo_electronico VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(20)
);

-- Tabla: Profesores
CREATE TABLE Profesores (
    id_profesor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    correo_electronico VARCHAR(100) UNIQUE NOT NULL,
    especialidad VARCHAR(100)
);

-- Tabla: Cursos
CREATE TABLE Cursos (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nombre_curso VARCHAR(100) NOT NULL,
    descripcion TEXT,
    duracion_horas INT,
    fecha_fin DATE,
    profesor_id INT,
    FOREIGN KEY (profesor_id) REFERENCES Profesores(id_profesor)
        ON DELETE SET NULL ON UPDATE CASCADE
);

-- Tabla Matriculas (Relacion muchos a muchos (N:N) entre Estudiantes y Cursos)
CREATE TABLE Matriculas (
    id_matricula INT AUTO_INCREMENT PRIMARY KEY,
    estudiante_id INT,
    curso_id INT,
    fecha_matricula DATE NOT NULL,
    FOREIGN KEY (estudiante_id) REFERENCES Estudiantes(id_estudiante)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (curso_id) REFERENCES Cursos(id_curso)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- Tabla Horarios (Relacion uno a muchos (1:N) entre Cursos y Horarios)
CREATE TABLE Horarios (
    id_horario INT AUTO_INCREMENT PRIMARY KEY,
    curso_id INT,
    dia_semana VARCHAR(20) NOT NULL,
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL,
    FOREIGN KEY (curso_id) REFERENCES Cursos(id_curso)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- ============================================
-- INSERCIÓN DE DATOS DE EJEMPLO
-- ============================================

-- Insertar 10 Profesores
INSERT INTO Profesores (nombre, apellido, correo_electronico, especialidad) VALUES
('Juan', 'Pérez', 'juan.perez@academia.com', 'Programación'),
('María', 'García', 'maria.garcia@academia.com', 'Bases de Datos'),
('Carlos', 'López', 'carlos.lopez@academia.com', 'Desarrollo Web'),
('Ana', 'Martínez', 'ana.martinez@academia.com', 'Diseño Gráfico'),
('Pedro', 'Rodríguez', 'pedro.rodriguez@academia.com', 'Redes'),
('Laura', 'Fernández', 'laura.fernandez@academia.com', 'Ciberseguridad'),
('David', 'Sánchez', 'david.sanchez@academia.com', 'Cloud Computing'),
('Elena', 'González', 'elena.gonzalez@academia.com', 'DevOps'),
('Roberto', 'Torres', 'roberto.torres@academia.com', 'Data Science'),
('Sandra', 'Díaz', 'sandra.diaz@academia.com', 'Mobile Development');

-- Insertar 10 Estudiantes
INSERT INTO Estudiantes (nombre, apellido, correo_electronico, telefono) VALUES
('Miguel', 'Ruiz', 'miguel.ruiz@email.com', '601234567'),
('Sofia', 'Cabrera', 'sofia.cabrera@email.com', '602345678'),
('Diego', 'Vargas', 'diego.vargas@email.com', '603456789'),
('Valentina', 'Rojas', 'valentina.rojas@email.com', '604567890'),
('Andrés', 'Moreno', 'andres.moreno@email.com', '605678901'),
('Camila', 'Medina', 'camila.medina@email.com', '606789012'),
('Lucas', 'Reyes', 'lucas.reyes@email.com', '607890123'),
('Isabella', 'Silva', 'isabella.silva@email.com', '608901234'),
('Fernando', 'Cortés', 'fernando.cortes@email.com', '609012345'),
('Gabriela', 'Navarro', 'gabriela.navarro@email.com', '610123456');

-- Insertar 10 Cursos
INSERT INTO Cursos (nombre_curso, descripcion, duracion_horas, fecha_fin, profesor_id) VALUES
('Python Avanzado', 'Aprende programación avanzada en Python', 40, '2025-03-31', 1),
('Bases de Datos SQL', 'Diseño y manejo de bases de datos relacionales', 35, '2025-04-15', 2),
('Desarrollo Web con Django', 'Framework Django para aplicaciones web', 50, '2025-05-10', 3),
('Diseño UX/UI', 'Principios de diseño de interfaces', 30, '2025-02-28', 4),
('Administración de Redes', 'Configuración y gestión de redes empresariales', 45, '2025-04-30', 5),
('Seguridad Ofensiva', 'Pruebas de penetración y hacking ético', 60, '2025-06-15', 6),
('AWS para Developers', 'Despliegue en Amazon Web Services', 40, '2025-05-20', 7),
('DevOps con Docker y Kubernetes', 'Containerización y orquestación', 55, '2025-06-30', 8),
('Machine Learning Básico', 'Introducción a ML con Python', 50, '2025-07-15', 9),
('Flutter Mobile Development', 'Desarrollo de apps móviles multiplataforma', 45, '2025-05-31', 10);

-- Insertar 10 Matrículas (relación estudiante-curso)
INSERT INTO Matriculas (estudiante_id, curso_id, fecha_matricula) VALUES
(1, 1, '2025-01-15'),
(2, 2, '2025-01-16'),
(3, 3, '2025-01-17'),
(4, 4, '2025-01-18'),
(5, 5, '2025-01-19'),
(6, 6, '2025-01-20'),
(7, 7, '2025-01-21'),
(8, 8, '2025-01-22'),
(9, 9, '2025-01-23'),
(10, 10, '2025-01-24');

-- Insertar 10 Horarios
INSERT INTO Horarios (curso_id, dia_semana, hora_inicio, hora_fin) VALUES
(1, 'Lunes', '09:00:00', '11:00:00'),
(1, 'Miércoles', '09:00:00', '11:00:00'),
(2, 'Martes', '14:00:00', '16:00:00'),
(2, 'Jueves', '14:00:00', '16:00:00'),
(3, 'Lunes', '16:00:00', '18:00:00'),
(4, 'Martes', '10:00:00', '12:00:00'),
(5, 'Miércoles', '15:00:00', '17:00:00'),
(6, 'Jueves', '17:00:00', '19:00:00'),
(7, 'Viernes', '09:00:00', '11:00:00'),
(8, 'Sábado', '10:00:00', '13:00:00');

