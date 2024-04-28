-- DROP SCHEMA public;

CREATE SCHEMA public AUTHORIZATION pg_database_owner;
-- public.sources definition

-- Drop table

-- DROP TABLE public.sources;

CREATE TABLE public.sources (
	id serial4 NOT NULL,
	CONSTRAINT sources_pk PRIMARY KEY (id)
);


-- public.quotes definition

-- Drop table

-- DROP TABLE public.quotes;

CREATE TABLE public.quotes (
	id serial4 NOT NULL,
	"text" text NOT NULL,
	"source" int4 NULL,
	date_added timestamptz NULL,
	tags text NULL,
	CONSTRAINT quotes_pk PRIMARY KEY (id),
	CONSTRAINT quotes_fk FOREIGN KEY ("source") REFERENCES public.sources(id) ON DELETE SET NULL ON UPDATE SET NULL
);


-- public.books definition

-- Drop table

-- DROP TABLE public.books;

CREATE TABLE public.books (
	source_id int4 NOT NULL,
	title text NOT NULL,
	author text NULL,
	publication_year int4 NULL,
	isbn text NULL,
	CONSTRAINT books_pk PRIMARY KEY (source_id),
	CONSTRAINT books_fk FOREIGN KEY (source_id) REFERENCES public.sources(id) ON DELETE CASCADE ON UPDATE CASCADE
);


-- public.people definition

-- Drop table

-- DROP TABLE public.people;

CREATE TABLE public.people (
	source_id int4 NOT NULL,
	"name" text NOT NULL,
	notes text NULL,
	CONSTRAINT people_pk PRIMARY KEY (source_id),
	CONSTRAINT people_fk FOREIGN KEY (source_id) REFERENCES public.sources(id) ON DELETE CASCADE ON UPDATE CASCADE
);
