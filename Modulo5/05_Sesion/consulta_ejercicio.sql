-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS academia;

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