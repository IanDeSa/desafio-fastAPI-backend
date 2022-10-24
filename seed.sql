USE `desafio`;

INSERT INTO desafio.categories (name) VALUES
		("item ofensivo"),
		("item defensivo"),
    ("item consumível"),
		("bota");

INSERT INTO desafio.products (name, category_id, price, serie) VALUES
	  ('Lâmina Cálida', 1, 350, 11),
		('Lâmina Álgida', 1, 350, 21),
	  ('Anel do Doran', 1, 400, 31),
	  ('Lacre Sombrio',  3, 400, 43),
		('Lágrima da Deusa', 1, 400, 51),
	  ('Guma do Ladrão Arcano', 1, 400, 61),
	  ('Guarda-Ombros de Aço',  1, 400, 71),
		('Escudo Relicário', 2, 400, 82),
	  ('Foice Espectral', 1, 400, 91),
	  ('Escudo de Doran',  2, 450, 102),
	  ('Lâmina de Doran', 1, 450, 111),
		('Abatedora',  1, 450, 121),
		('Botas Simples',  4, 300, 134),
		('Botas da Rapidez',  4, 900, 144),
		('Botas da Mobilidade',  4, 1000, 154),
		('Poção de Vida',  3, 50, 163),
		('Poção com Refil',  3, 150, 173),
		('Poção Corrupta',  3, 500, 183),
		('Elixir de Ferro',  3, 500, 193),
		('Elixir da Ira',  3, 500, 203);