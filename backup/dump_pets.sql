--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3 (Debian 16.3-1.pgdg120+1)
-- Dumped by pg_dump version 16.3

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
-- Name: gender; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gender (
    id uuid NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.gender OWNER TO postgres;

--
-- Name: image; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.image (
    id uuid NOT NULL,
    filename character varying NOT NULL,
    pet_id uuid
);


ALTER TABLE public.image OWNER TO postgres;

--
-- Name: pet; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pet (
    id uuid NOT NULL,
    status_id uuid NOT NULL,
    name character varying NOT NULL,
    gender_id uuid NOT NULL,
    type_id uuid NOT NULL,
    date_birth date,
    breed character varying,
    personality character varying,
    appearance character varying,
    health character varying,
    description character varying
);


ALTER TABLE public.pet OWNER TO postgres;

--
-- Name: petType; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."petType" (
    id uuid NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public."petType" OWNER TO postgres;

--
-- Name: status; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.status (
    id uuid NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.status OWNER TO postgres;

--
-- Data for Name: gender; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.gender (id, name) VALUES ('ef6f09c6-3dfc-4e07-918b-6686fe16c35d', 'мальчик');
INSERT INTO public.gender (id, name) VALUES ('e9d62c72-e667-45c3-adc9-4ccaa7c6f1da', 'девочка');


--
-- Data for Name: image; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: pet; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.pet (id, status_id, name, gender_id, type_id, date_birth, breed, personality, appearance, health, description) VALUES ('bb6400c0-6825-486d-907d-57a8cb2c6b7f', 'b2079a7c-3eca-458a-82e6-926254804e15', '1', 'e9d62c72-e667-45c3-adc9-4ccaa7c6f1da', 'efb89c62-f0b6-4c45-9af2-1fd0977b8564', NULL, NULL, NULL, NULL, NULL, NULL);


--
-- Data for Name: petType; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."petType" (id, name) VALUES ('97a0612f-df2e-47a8-80b6-7cab6b4bf3bf', 'кошка');
INSERT INTO public."petType" (id, name) VALUES ('efb89c62-f0b6-4c45-9af2-1fd0977b8564', 'собака');


--
-- Data for Name: status; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.status (id, name) VALUES ('b2079a7c-3eca-458a-82e6-926254804e15', 'в приюте');
INSERT INTO public.status (id, name) VALUES ('a2f9542e-7573-43e9-a00f-dcaab2a1c4ca', 'забралти');
INSERT INTO public.status (id, name) VALUES ('0bf86c16-e1cb-4b8b-90af-21ba07287b58', 'на лечении');


--
-- Name: gender gender_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gender
    ADD CONSTRAINT gender_pkey PRIMARY KEY (id);


--
-- Name: image image_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.image
    ADD CONSTRAINT image_pkey PRIMARY KEY (id);


--
-- Name: petType petType_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."petType"
    ADD CONSTRAINT "petType_pkey" PRIMARY KEY (id);


--
-- Name: pet pet_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pet
    ADD CONSTRAINT pet_pkey PRIMARY KEY (id);


--
-- Name: status status_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.status
    ADD CONSTRAINT status_pkey PRIMARY KEY (id);


--
-- Name: image image_pet_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.image
    ADD CONSTRAINT image_pet_id_fkey FOREIGN KEY (pet_id) REFERENCES public.pet(id);


--
-- Name: pet pet_gender_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pet
    ADD CONSTRAINT pet_gender_id_fkey FOREIGN KEY (gender_id) REFERENCES public.gender(id);


--
-- Name: pet pet_status_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pet
    ADD CONSTRAINT pet_status_id_fkey FOREIGN KEY (status_id) REFERENCES public.status(id);


--
-- Name: pet pet_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pet
    ADD CONSTRAINT pet_type_id_fkey FOREIGN KEY (type_id) REFERENCES public."petType"(id);


--
-- PostgreSQL database dump complete
--

