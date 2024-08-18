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



--
-- Data for Name: image; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: pet; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: petType; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: status; Type: TABLE DATA; Schema: public; Owner: postgres
--



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

