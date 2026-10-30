CREATE TABLE categoria(
    categoriaID int PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nome VARCHAR(20) NOT NULL,
    data DATE
);

CREATE TABLE produto(
    produtoID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nome VARCHAR(20) NOT NULL,
    descricao text NOT NULL,
    preco DECIMAL(8, 2) NOT NULL,
    categoriaID INT NOT NULL,
    data DATE,
    FOREIGN KEY (categoriaID) REFERENCES categoria(categoriaID)
);
    
CREATE TABLE usuarios(
    nome VARCHAR(20) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    email VARCHAR(64) NOT NULL UNIQUE,
	data DATE
);