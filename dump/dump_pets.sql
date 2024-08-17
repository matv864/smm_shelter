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
    filename character varying NOT NULL,
    pet_id uuid
);


ALTER TABLE public.image OWNER TO postgres;

--
-- Name: pet; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pet (
    id uuid NOT NULL,
    status character varying NOT NULL,
    name character varying NOT NULL,
    gender character varying NOT NULL,
    type_name character varying NOT NULL,
    date_birth timestamp without time zone,
    breed character varying,
    personality character varying,
    appearance character varying,
    health character varying,
    description character varying
);


ALTER TABLE public.pet OWNER TO postgres;

--
-- Data for Name: image; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: pet; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.pet (id, status, name, gender, type_name, date_birth, breed, personality, appearance, health, description) VALUES ('1e2b859d-f95e-4828-a87b-3aa6de57df9f', '11', '11', '111', '1', NULL, NULL, NULL, NULL, NULL, NULL);


--
-- Name: image image_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.image
    ADD CONSTRAINT image_pkey PRIMARY KEY (id);


--
-- Name: pet pet_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pet
    ADD CONSTRAINT pet_pkey PRIMARY KEY (id);


--
-- Name: image image_pet_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.image
    ADD CONSTRAINT image_pet_id_fkey FOREIGN KEY (pet_id) REFERENCES public.pet(id);


--
-- PostgreSQL database dump complete
--