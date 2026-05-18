CREATE TABLE eleitores (
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
cpf VARCHAR(255) NOT NULL UNIQUE,
titulo CHAR(13) NOT NULL UNIQUE,
mesario BOOLEAN NOT NULL DEFAULT FALSE,
chave_acesso VARCHAR(255) NOT NULL,
status_voto BOOLEAN DEFAULT FALSE
);

CREATE TABLE candidatos (
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
numero INT NOT NULL UNIQUE,
partido VARCHAR(50) NOT NULL
);

CREATE TABLE votos (
id INT AUTO_INCREMENT PRIMARY KEY,
id_eleitor INT NOT NULL,
id_candidato INT NULL,
data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
protocolo VARCHAR(255) NOT NULL UNIQUE,
UNIQUE (id_eleitor),
FOREIGN KEY (id_eleitor) REFERENCES eleitores(id) ON DELETE CASCADE,
FOREIGN KEY (id_candidato) REFERENCES candidatos(id) ON DELETE SET NULL
);

CREATE TABLE logs (
id INT AUTO_INCREMENT PRIMARY KEY,
data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
tipo VARCHAR(50) NOT NULL,
descricao TEXT NOT NULL
);

CREATE TABLE configuracao_votacao (
    id INT PRIMARY KEY,
    votacao_aberta BOOLEAN NOT NULL
);


INSERTS:
INSERT INTO configuracao_votacao VALUES (1, FALSE);

INSERT INTO eleitores (nome, cpf, titulo, mesario, chave_acesso, status_voto) VALUES 
('Ana Souza', '52998224725', '123456780124', TRUE, 'CHAVE001', TRUE),
('Bruno Lima', '11144477735', '234567890231', FALSE, 'CHAVE002', TRUE),
('Carlos Mendes', '93541134780', '345678900348', FALSE, 'CHAVE003', FALSE),
('Daniela Rocha', '28625587887', '456789010455', TRUE, 'CHAVE004', TRUE),
('Eduardo Alves', '39053344705', '567890120562', FALSE, 'CHAVE005', TRUE),
('Fernanda Costa', '16899535009', '678901230679', FALSE, 'CHAVE006', FALSE),
('Gabriel Pinto', '74682489070', '789012340786', FALSE, 'CHAVE007', TRUE),
('Helena Martins', '35795145682', '890123450893', FALSE, 'CHAVE008', FALSE),
('Igor Ribeiro', '95175385200', '901234560900', TRUE, 'CHAVE009', TRUE),
('Juliana Freitas', '25874136980', '112345670117', FALSE, 'CHAVE010', TRUE),

('Lucas Gomes', '74185296300', '223456780224', FALSE, 'CHAVE011', FALSE),
('Mariana Dias', '45678912366', '334567890331', FALSE, 'CHAVE012', TRUE),
('Nicolas Barros', '32165498706', '445678900448', TRUE, 'CHAVE013', TRUE),
('Olivia Teixeira', '65498732161', '556789010555', FALSE, 'CHAVE014', FALSE),
('Paulo Henrique', '78912345606', '667890120662', FALSE, 'CHAVE015', TRUE),
('Queila Santos', '14725836993', '778901230779', FALSE, 'CHAVE016', FALSE),
('Rafael Nunes', '36925814770', '889012340886', FALSE, 'CHAVE017', TRUE),
('Sabrina Melo', '74196385249', '990123450993', TRUE, 'CHAVE018', TRUE),
('Tiago Cardoso', '85274196353', '101234561100', FALSE, 'CHAVE019', FALSE),
('Vanessa Duarte', '15935748646', '212345671217', FALSE, 'CHAVE020', TRUE),

('Alberto Silva', '95135785206', '323456781324', FALSE, 'CHAVE021', TRUE),
('Bianca Costa', '75315948650', '434567891431', FALSE, 'CHAVE022', TRUE),
('Caio Mendes', '25896314710', '545678901548', FALSE, 'CHAVE023', TRUE),
('Debora Lima', '35715948608', '656789011655', FALSE, 'CHAVE024', TRUE),
('Enzo Rocha', '95148635700', '767890121762', FALSE, 'CHAVE025', TRUE),
('Fabiana Alves', '75348615904', '878901231879', FALSE, 'CHAVE026', TRUE),
('Guilherme Souza', '25814736920', '989012341986', FALSE, 'CHAVE027', TRUE),
('Heloisa Martins', '65412398700', '190123452093', FALSE, 'CHAVE028', TRUE),
('Isabela Freitas', '32178965400', '201234562200', FALSE, 'CHAVE029', TRUE),
('Jonas Ribeiro', '74125896308', '312345672317', FALSE, 'CHAVE030', TRUE),

('Karen Dias', '85236974104', '423456782424', FALSE, 'CHAVE031', TRUE),
('Leonardo Pinto', '96374185200', '534567892531', FALSE, 'CHAVE032', TRUE),
('Monica Teixeira', '14736925800', '645678902648', FALSE, 'CHAVE033', TRUE),
('Nathan Gomes', '25836914708', '756789012755', FALSE, 'CHAVE034', TRUE),
('Otavio Barros', '36914725804', '867890122862', FALSE, 'CHAVE035', TRUE),
('Priscila Santos', '74185296349', '978901232979', FALSE, 'CHAVE036', TRUE),
('Ruan Cardoso', '85214796302', '189012343086', FALSE, 'CHAVE037', TRUE),
('Simone Melo', '96325874105', '290123453193', FALSE, 'CHAVE038', TRUE),
('Tatiane Nunes', '15975348692', '301234563300', FALSE, 'CHAVE039', TRUE),
('Ueslei Duarte', '35748615903', '412345673417', FALSE, 'CHAVE040', TRUE);

INSERT INTO candidatos (nome, numero, partido) VALUES
('João Silva', 10, 'ABC'),
('Maria Oliveira', 11, 'DEF'),
('Pedro Santos', 12, 'GHI'),
('Carla Souza', 13, 'JKL'),
('Roberto Lima', 14, 'MNO'),
('Patricia Alves', 15, 'PQR'),
('Fernando Costa', 16, 'STU'),
('Luciana Rocha', 17, 'VWX'),
('Ricardo Mendes', 18, 'YZA'),
('Camila Ribeiro', 19, 'BCD'),
('André Gomes', 20, 'EFG'),
('Julio Martins', 21, 'HIJ'),
('Beatriz Freitas', 22, 'KLM'),
('Eduarda Dias', 23, 'NOP'),
('Vinicius Barros', 24, 'QRS'),
('Larissa Teixeira', 25, 'TUV'),
('Felipe Henrique', 26, 'WXY'),
('Renata Santos', 27, 'ZAB'),
('Gustavo Nunes', 28, 'CDE'),
('Aline Melo', 29, 'FGH');

INSERT INTO votos (id_eleitor, id_candidato, protocolo) VALUES
(1, 1, 'PROTO001'),
(2, 2, 'PROTO002'),
(3, NULL, 'PROTO003'),
(4, 4, 'PROTO004'),
(5, 5, 'PROTO005'),
(6, NULL, 'PROTO006'),
(7, 7, 'PROTO007'),
(8, 8, 'PROTO008'),
(9, 9, 'PROTO009'),
(10, 10, 'PROTO010'),
(11, NULL, 'PROTO011'),
(12, 12, 'PROTO012'),
(13, 13, 'PROTO013'),
(14, NULL, 'PROTO014'),
(15, 15, 'PROTO015'),
(16, 16, 'PROTO016'),
(17, 17, 'PROTO017'),
(18, 18, 'PROTO018'),
(19, NULL, 'PROTO019'),
(20, 20, 'PROTO020'),
(21, 1, 'PROTO021'),
(22, 2, 'PROTO022'),
(23, 3, 'PROTO023'),
(24, 4, 'PROTO024'),
(25, 5, 'PROTO025'),
(26, 6, 'PROTO026'),
(27, 7, 'PROTO027'),
(28, 8, 'PROTO028'),
(29, 9, 'PROTO029'),
(30, 10, 'PROTO030'),
(31, 11, 'PROTO031'),
(32, 12, 'PROTO032'),
(33, 13, 'PROTO033'),
(34, 14, 'PROTO034'),
(35, 15, 'PROTO035'),
(36, 16, 'PROTO036'),
(37, 17, 'PROTO037'),
(38, 18, 'PROTO038'),
(39, 19, 'PROTO039'),
(40, 20, 'PROTO040');

INSERT INTO logs (tipo, descricao) VALUES
('ABERTURA', 'Votação iniciada com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('ALERTA', 'Tentativa de acesso negado'),
('SUCESSO', 'Voto realizado com sucesso'),
('ALERTA', 'Tentativa de voto duplo'),
('SUCESSO', 'Voto realizado com sucesso'),
('ALERTA', 'Tentativa de acesso negado'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('ALERTA', 'Tentativa de voto duplo'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('ALERTA', 'Tentativa de acesso negado'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('ALERTA', 'Tentativa de voto duplo'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('ALERTA', 'Tentativa de acesso negado'),
('ENCERRAMENTO', 'Votação finalizada com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso');
