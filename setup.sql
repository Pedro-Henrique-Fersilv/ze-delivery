CREATE DATABASE IF DONT EXISTS delivery;
USE delivery;

CREATE TABLE parceiros (
    id INT PRIMARY key AUTO_INCREMENT,
    tradingName VARCHAR(100),
    ownerName VARCHAR(100),
    document CHAR(14),
    coverage_radius_km FLOAT,
    latitude DOUBLE,
    longitude DOUBLE
);

INSERT INTO parceiros (
    tradingName, ownerName, document, coverage_radius_km, latitude, longitude
) VALUES
-- São Paulo
('Parceiro SP', 'Carlos Silva', '12345678000195', 10.0, -23.550520, -46.633308),

-- Rio de Janeiro
('Parceiro RJ', 'Mariana Rocha', '98765432000188', 8.5, -22.906847, -43.172896),

-- Belo Horizonte
('Parceiro BH', 'João Costa', '45678912000133', 6.0, -19.916681, -43.934493),

-- Brasília
('Parceiro DF', 'Ana Lima', '78912345000177', 15.0, -15.793889, -47.882778),

-- Curitiba
('Parceiro PR', 'Lucas Martins', '32165498000111', 5.0, -25.428954, -49.267137),

-- Porto Alegre
('Parceiro RS', 'Juliana Souza', '11223344000122', 12.0, -30.034647, -51.217658),

-- Salvador
('Parceiro BA', 'Fernando Dias', '99887766000144', 20.0, -12.971111, -38.510833),

-- Recife
('Parceiro PE', 'Beatriz Castro', '44332211000166', 7.0, -8.047562, -34.877003),

-- Manaus
('Parceiro AM', 'Rafael Gomes', '55667788000155', 30.0, -3.119028, -60.021731),

-- Fortaleza
('Parceiro CE', 'Camila Fernandes', '66778899000177', 9.0, -3.717220, -38.543306);