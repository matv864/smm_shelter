--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3 (Debian 16.3-1.pgdg120+1)
-- Dumped by pg_dump version 16.3 (Debian 16.3-1.pgdg120+1)

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
-- Name: image; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.image (
    id uuid NOT NULL,
    path character varying NOT NULL,
    parent_id uuid NOT NULL
);


ALTER TABLE public.image OWNER TO postgres;

--
-- Name: pets; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pets (
    id uuid NOT NULL,
    status character varying NOT NULL,
    type_id uuid NOT NULL,
    date_birth timestamp without time zone,
    litter_box boolean,
    vaccinated boolean,
    castrated boolean,
    description character varying
);


ALTER TABLE public.pets OWNER TO postgres;

--
-- Name: pets_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pets_type (
    id uuid NOT NULL,
    name character varying NOT NULL,
    description character varying
);


ALTER TABLE public.pets_type OWNER TO postgres;

--
-- Data for Name: image; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.image (id, path, parent_id) VALUES ('8d883f63-d47d-47c7-b265-6d04be668765', 'собакен в полный рост', '29d176b7-a94f-4a92-ac52-cfe6c302c82e');
INSERT INTO public.image (id, path, parent_id) VALUES ('1c6086f3-957b-478f-926a-e3c96607d3e9', 'собакен лежит', '29d176b7-a94f-4a92-ac52-cfe6c302c82e');


--
-- Data for Name: pets; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.pets (id, status, type_id, date_birth, litter_box, vaccinated, castrated, description) VALUES ('29d176b7-a94f-4a92-ac52-cfe6c302c82e', 'в приюте', '08118767-fe63-48bb-9548-74da14eab996', '1000-01-01 00:00:00', true, true, true, 'собакен');


--
-- Data for Name: pets_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.pets_type (id, name, description) VALUES ('08118767-fe63-48bb-9548-74da14eab996', 'собака', '-----');


--
-- Name: image image_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.image
    ADD CONSTRAINT image_pkey PRIMARY KEY (id);


--
-- Name: pets pets_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pets
    ADD CONSTRAINT pets_pkey PRIMARY KEY (id);


--
-- Name: pets_type pets_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pets_type
    ADD CONSTRAINT pets_type_pkey PRIMARY KEY (id);


--
-- Name: image image_parent_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.image
    ADD CONSTRAINT image_parent_id_fkey FOREIGN KEY (parent_id) REFERENCES public.pets(id);


--
-- Name: pets pets_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pets
    ADD CONSTRAINT pets_type_id_fkey FOREIGN KEY (type_id) REFERENCES public.pets_type(id);


--
-- PostgreSQL database dump complete
--