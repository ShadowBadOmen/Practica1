CREATE DATABASE IF NOT EXISTS flaskdb;

USE flaskdb;

CREATE TABLE IF NOT EXISTS cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255) NOT NULL
);

INSERT INTO cursos (nombre, descripcion)
VALUES
    ('Python', 'Fundamentos de programación con Python'),
    ('Flask', 'Desarrollo de aplicaciones web con Flask'),
    ('Docker', 'Contenedores y despliegue de aplicaciones'),
    ('MySQL', 'Gestión de bases de datos relacionales');
