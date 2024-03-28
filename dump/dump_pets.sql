--
-- PostgreSQL database dump
-- pg_dump --column-inserts
--

-- Dumped from database version 16.2 (Debian 16.2-1.pgdg120+2)
-- Dumped by pg_dump version 16.2 (Debian 16.2-1.pgdg120+2)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: article; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.article (
    id integer NOT NULL,
    title character varying NOT NULL,
    body text,
    date_publish date NOT NULL,
    card_id integer NOT NULL
);


ALTER TABLE public.article OWNER TO postgres;

--
-- Name: article_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.article_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.article_id_seq OWNER TO postgres;

--
-- Name: article_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.article_id_seq OWNED BY public.article.id;


--
-- Name: card; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.card (
    id integer NOT NULL,
    pet_name character varying NOT NULL,
    pet_type_id integer NOT NULL,
    date_birth date,
    castrated boolean,
    vaccinated boolean,
    cat_litter_box boolean,
    description text,
    counter_views integer DEFAULT 0,
    donated_amount integer DEFAULT 0,
    main_image character varying
);


ALTER TABLE public.card OWNER TO postgres;

--
-- Name: card_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.card_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.card_id_seq OWNER TO postgres;

--
-- Name: card_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.card_id_seq OWNED BY public.card.id;


--
-- Name: image; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.image (
    id integer NOT NULL,
    filename character varying NOT NULL,
    article_id integer NOT NULL
);


ALTER TABLE public.image OWNER TO postgres;

--
-- Name: image_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.image_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.image_id_seq OWNER TO postgres;

--
-- Name: image_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.image_id_seq OWNED BY public.image.id;


--
-- Name: pet_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pet_type (
    id integer NOT NULL,
    title character varying NOT NULL,
    description text
);


ALTER TABLE public.pet_type OWNER TO postgres;

--
-- Name: pet_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pet_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.pet_type_id_seq OWNER TO postgres;

--
-- Name: pet_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pet_type_id_seq OWNED BY public.pet_type.id;


--
-- Name: article id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.article ALTER COLUMN id SET DEFAULT nextval('public.article_id_seq'::regclass);


--
-- Name: card id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.card ALTER COLUMN id SET DEFAULT nextval('public.card_id_seq'::regclass);


--
-- Name: image id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.image ALTER COLUMN id SET DEFAULT nextval('public.image_id_seq'::regclass);


--
-- Name: pet_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pet_type ALTER COLUMN id SET DEFAULT nextval('public.pet_type_id_seq'::regclass);


--
-- Data for Name: article; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.article (id, title, body, date_publish, card_id) VALUES (4, 'его приезд', 'В выходные к нам приехал тяжеленький маленький котенок - малыш Поребрик. Он жил во дворе, болел и умирал на глазах у людей. Нос был забит соплями, по всему тельцу толпами катались блохи. Когда малыша доставили к нам, он уже был без сил, с осипшим голосом, истощенный и анемичный. От усталости он даже не мог есть сам. На свой страх и риск мы обработали его каплями от блох, потому что начинать лечение нужно было именно с избавления от лишних пассажиров. Первые сутки были очень тяжелыми - Поребрик постоянно спал на грелочке, а мы его кормили со шприца. На вторые сутки он начал самостоятельно кушать, но все еще ему не хватало сил, чтобы самому доесть пауч. Сейчас прошло уже несколько дней, и мы рады, что ребенок идет на поправку, кушает, ходит в лоточек и радует нас своими красивыми оформленными какашками. Сейчас для него нам необходимо как можно больше влажного и сухого корма для котят. Мы уверены, что многим из вас откликнется история спасения нашего Поребрика. Будем признательны за любую вашу помощь. тел. 8-914-790-08-33 (Елена); 8-904-629-94-23 (Ксения) или 8-914-705-75-22 (Екатерина)
 ', '2024-03-05', 1);
INSERT INTO public.article (id, title, body, date_publish, card_id) VALUES (1, 'string', 'string', '2024-03-28', 1);
INSERT INTO public.article (id, title, body, date_publish, card_id) VALUES (2, '===', '===', '2024-03-28', 1);


--
-- Data for Name: card; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.card (id, pet_name, pet_type_id, date_birth, castrated, vaccinated, cat_litter_box, description, counter_views, donated_amount, main_image) VALUES (1, 'Малыш Поребрик ', 1, '2024-03-23', false, false, true, 'не знаю что писать', 8, 0, NULL);
INSERT INTO public.card (id, pet_name, pet_type_id, date_birth, castrated, vaccinated, cat_litter_box, description, counter_views, donated_amount, main_image) VALUES (2, 'собака', 2, NULL, NULL, NULL, NULL, NULL, 8, 0, NULL);
INSERT INTO public.card (id, pet_name, pet_type_id, date_birth, castrated, vaccinated, cat_litter_box, description, counter_views, donated_amount, main_image) VALUES (3, 'string', 7, '2024-03-27', true, true, true, 'string', 8, 0, 'string');


--
-- Data for Name: image; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.image (id, filename, article_id) VALUES (2, 'rrr', 4);


--
-- Data for Name: pet_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.pet_type (id, title, description) VALUES (1, 'котята и котики до года', 'описание');
INSERT INTO public.pet_type (id, title, description) VALUES (2, 'собаки', NULL);


--
-- Name: article_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.article_id_seq', 2, true);


--
-- Name: card_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.card_id_seq', 3, true);


--
-- Name: image_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.image_id_seq', 1, false);


--
-- Name: pet_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.pet_type_id_seq', 1, false);


--
-- Name: article article_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.article
    ADD CONSTRAINT article_pk PRIMARY KEY (id);


--
-- Name: card card_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.card
    ADD CONSTRAINT card_pk PRIMARY KEY (id);


--
-- Name: image image_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.image
    ADD CONSTRAINT image_pk PRIMARY KEY (id);


--
-- Name: pet_type pet_type_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pet_type
    ADD CONSTRAINT pet_type_pk PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--