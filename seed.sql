USE `desafio`;

INSERT INTO desafio.categories (name) VALUES
    ("brinquedo"),
    ("item mágico"),
    ("item raro");

INSERT INTO desafio.products (name, category_id, price, serie) VALUES
	  ('Martelo de Thor', 3, 155.25, 2022),
	  ('O um anel', 3, 9999.99, 2022),
	  ('Varinha das varinhas',  2, 200.99, 2022),
	  ('Miniatura do Luffy', 1, 17.55, 2022);