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
    pets_id uuid NOT NULL
);


ALTER TABLE public.image OWNER TO postgres;

--
-- Name: pets; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pets (
    id uuid NOT NULL,
    status character varying NOT NULL,
    name character varying NOT NULL,
    gender character varying NOT NULL,
    type_id uuid NOT NULL,
    date_birth timestamp without time zone,
    age integer,
    breed character varying,
    personality character varying,
    appearance character varying,
    health character varying,
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

INSERT INTO public.image (id, filename, pets_id) VALUES ('89e01371-f2ff-4457-8611-98a1a55ef751', 'Luna_1.JPG', '948c6d60-8726-4be0-8578-9fcc8a5248bc');
INSERT INTO public.image (id, filename, pets_id) VALUES ('3b55eef1-945a-48a4-888c-7de84188608f', 'Luna_2.JPG', '948c6d60-8726-4be0-8578-9fcc8a5248bc');
INSERT INTO public.image (id, filename, pets_id) VALUES ('60d619e7-2762-4422-beff-cedd7e90657f', 'Luna_3.JPG', '948c6d60-8726-4be0-8578-9fcc8a5248bc');
INSERT INTO public.image (id, filename, pets_id) VALUES ('54461f85-0ef0-49ca-9dea-4ec414ef7bde', 'Luna_4.JPG', '948c6d60-8726-4be0-8578-9fcc8a5248bc');
INSERT INTO public.image (id, filename, pets_id) VALUES ('1c87d377-3ff7-4875-a5e3-e2b26ac0bf34', 'Luna_5.JPG', '948c6d60-8726-4be0-8578-9fcc8a5248bc');
INSERT INTO public.image (id, filename, pets_id) VALUES ('d420fd85-69cf-4129-9249-338b682b2c62', 'Luna_6.JPG', '948c6d60-8726-4be0-8578-9fcc8a5248bc');
INSERT INTO public.image (id, filename, pets_id) VALUES ('a1cf1f90-f32c-45ca-8662-b15986841dd5', 'Luna_7.JPG', '948c6d60-8726-4be0-8578-9fcc8a5248bc');
INSERT INTO public.image (id, filename, pets_id) VALUES ('a9635386-ddf2-45f4-83fd-985de4a78b7d', 'Luna_8.JPG', '948c6d60-8726-4be0-8578-9fcc8a5248bc');
INSERT INTO public.image (id, filename, pets_id) VALUES ('0cee8723-b08b-4b80-8614-d609ad4ad2f2', 'Luna_9.JPG', '948c6d60-8726-4be0-8578-9fcc8a5248bc');
INSERT INTO public.image (id, filename, pets_id) VALUES ('e0a1a9fd-96df-4880-b102-eedf1d71b605', 'Luna_10.JPG', '948c6d60-8726-4be0-8578-9fcc8a5248bc');
INSERT INTO public.image (id, filename, pets_id) VALUES ('65eeecf5-aac7-4b63-a4de-a6526391f660', 'White_1.JPG', '1fb4d052-8780-4246-b3e4-5cbcab4554a3');
INSERT INTO public.image (id, filename, pets_id) VALUES ('a973e9c1-eeb7-47fc-9694-ba35375f15ca', 'White_2.JPG', '1fb4d052-8780-4246-b3e4-5cbcab4554a3');
INSERT INTO public.image (id, filename, pets_id) VALUES ('8e34a2ca-139b-4f7c-9a04-cc7bb68e2826', 'White_3.JPG', '1fb4d052-8780-4246-b3e4-5cbcab4554a3');
INSERT INTO public.image (id, filename, pets_id) VALUES ('e971b71f-14fe-42bc-9e39-d1e6f6cf39c4', 'White_4.JPG', '1fb4d052-8780-4246-b3e4-5cbcab4554a3');
INSERT INTO public.image (id, filename, pets_id) VALUES ('daa768cd-f31d-4e64-9d84-d39ec45c4bb0', 'White_5.JPG', '1fb4d052-8780-4246-b3e4-5cbcab4554a3');
INSERT INTO public.image (id, filename, pets_id) VALUES ('1204d86f-2740-4b5c-a9fa-e52913c808ef', 'White_6.JPG', '1fb4d052-8780-4246-b3e4-5cbcab4554a3');
INSERT INTO public.image (id, filename, pets_id) VALUES ('0ccccad6-9652-4381-a21f-5c749a974122', 'White_7.JPG', '1fb4d052-8780-4246-b3e4-5cbcab4554a3');
INSERT INTO public.image (id, filename, pets_id) VALUES ('ca9c8b97-e12a-48a2-b12a-a5db4dedbe13', 'Vik_1.JPG', '837a64d7-2428-4e30-a900-d714fb845590');
INSERT INTO public.image (id, filename, pets_id) VALUES ('2dc35def-47af-4ab0-9a73-d2ba56e7efe3', 'Vik_2.JPG', '837a64d7-2428-4e30-a900-d714fb845590');
INSERT INTO public.image (id, filename, pets_id) VALUES ('833684e2-933e-49f2-8325-3cb5d9ce3127', 'Vik_3.JPG', '837a64d7-2428-4e30-a900-d714fb845590');
INSERT INTO public.image (id, filename, pets_id) VALUES ('b23c8490-5dcc-4ec0-b1fa-cffebe00e547', 'Vik_4.JPG', '837a64d7-2428-4e30-a900-d714fb845590');
INSERT INTO public.image (id, filename, pets_id) VALUES ('535c8672-c2b0-4aa3-8c5a-86a7298a0051', 'Vik_5.JPG', '837a64d7-2428-4e30-a900-d714fb845590');
INSERT INTO public.image (id, filename, pets_id) VALUES ('32065642-3b8e-496d-9085-1b2500120956', 'Vik_6.JPG', '837a64d7-2428-4e30-a900-d714fb845590');
INSERT INTO public.image (id, filename, pets_id) VALUES ('b93c5a4c-9b78-4b9a-8a5a-3dd0eafa6570', 'Vik_7.JPG', '837a64d7-2428-4e30-a900-d714fb845590');
INSERT INTO public.image (id, filename, pets_id) VALUES ('2642e58a-959d-4b5f-8ec4-c4099aa7dbde', 'Vik_8.JPG', '837a64d7-2428-4e30-a900-d714fb845590');
INSERT INTO public.image (id, filename, pets_id) VALUES ('cb4732a5-06b4-4af3-8d6a-df3a451db447', 'Vik_9.JPG', '837a64d7-2428-4e30-a900-d714fb845590');
INSERT INTO public.image (id, filename, pets_id) VALUES ('55d09bcb-32f9-4850-a449-1fe7142fd3d6', 'Vik_10.JPG', '837a64d7-2428-4e30-a900-d714fb845590');
INSERT INTO public.image (id, filename, pets_id) VALUES ('ee794b92-bbdc-4f7c-a4fb-51be7420ee63', 'Dana_1.JPG', 'a2aa7d05-f1e6-43c5-a810-cc56f2b2c48f');
INSERT INTO public.image (id, filename, pets_id) VALUES ('0b76726c-2ec2-4829-bf13-beacc5ed5863', 'Dana_2.JPG', 'a2aa7d05-f1e6-43c5-a810-cc56f2b2c48f');
INSERT INTO public.image (id, filename, pets_id) VALUES ('56cbdd3b-9d05-43e4-9fa5-4958594d52d1', 'Dana_3.JPG', 'a2aa7d05-f1e6-43c5-a810-cc56f2b2c48f');
INSERT INTO public.image (id, filename, pets_id) VALUES ('d7e57970-69c7-465f-bf2b-c1fccc0f31e3', 'Dana_4.JPG', 'a2aa7d05-f1e6-43c5-a810-cc56f2b2c48f');
INSERT INTO public.image (id, filename, pets_id) VALUES ('8e614ba0-ce1d-4e5c-84ee-2d2bdf57616d', 'Demon_1.JPG', 'a05306b6-9564-4b74-8ac6-46eb00ad3c3f');
INSERT INTO public.image (id, filename, pets_id) VALUES ('d7062dce-7ee3-477f-a4df-4362b7504299', 'Demon_2.JPG', 'a05306b6-9564-4b74-8ac6-46eb00ad3c3f');
INSERT INTO public.image (id, filename, pets_id) VALUES ('f32c7a93-6a50-4408-aaf9-4a6c84ab4fdd', 'Demon_3.JPG', 'a05306b6-9564-4b74-8ac6-46eb00ad3c3f');
INSERT INTO public.image (id, filename, pets_id) VALUES ('332cb4f9-705f-4f4f-8545-d2e130916635', 'Demon_4.JPG', 'a05306b6-9564-4b74-8ac6-46eb00ad3c3f');
INSERT INTO public.image (id, filename, pets_id) VALUES ('fd61dadb-9589-45b9-9714-3d0e5ec9bed8', 'Demon_5.JPG', 'a05306b6-9564-4b74-8ac6-46eb00ad3c3f');
INSERT INTO public.image (id, filename, pets_id) VALUES ('5d5a8144-aa81-4f7e-b86e-7963fdea8c74', 'Demon_6.JPG', 'a05306b6-9564-4b74-8ac6-46eb00ad3c3f');
INSERT INTO public.image (id, filename, pets_id) VALUES ('62b27a72-a112-42e4-b888-df4819c29032', 'Demon_7.JPG', 'a05306b6-9564-4b74-8ac6-46eb00ad3c3f');
INSERT INTO public.image (id, filename, pets_id) VALUES ('bb0b62f8-89a0-4822-8716-6e124d88c99e', 'Demon_8.JPG', 'a05306b6-9564-4b74-8ac6-46eb00ad3c3f');
INSERT INTO public.image (id, filename, pets_id) VALUES ('7bd1742b-52f4-4f11-8a0f-6689f5d56c50', 'Demon_9.JPG', 'a05306b6-9564-4b74-8ac6-46eb00ad3c3f');
INSERT INTO public.image (id, filename, pets_id) VALUES ('1232ac3b-ae16-48b1-92d4-505510b9e0e5', 'Polkan_1.JPG', '41950861-dc47-4137-9c6a-84d19b7eb90d');
INSERT INTO public.image (id, filename, pets_id) VALUES ('7e3e1f5b-6a65-4f78-a436-19da1179f892', 'Polkan_2.JPG', '41950861-dc47-4137-9c6a-84d19b7eb90d');
INSERT INTO public.image (id, filename, pets_id) VALUES ('154e5d28-da78-4119-ac06-e4c73826f8d2', 'Polkan_3.JPG', '41950861-dc47-4137-9c6a-84d19b7eb90d');
INSERT INTO public.image (id, filename, pets_id) VALUES ('15c186c4-0ec9-4018-81a6-54aa8490f4a9', 'Polkan_4.JPG', '41950861-dc47-4137-9c6a-84d19b7eb90d');
INSERT INTO public.image (id, filename, pets_id) VALUES ('afa54df4-2ac4-4fd7-9043-f4f3bbadec07', 'Polkan_5.JPG', '41950861-dc47-4137-9c6a-84d19b7eb90d');
INSERT INTO public.image (id, filename, pets_id) VALUES ('556060a4-1a22-4c38-a6b2-c38ec86ca8c1', 'Tina_1.JPG', '09f1b0d3-fcf2-4b40-92cb-cf24b33a56d7');
INSERT INTO public.image (id, filename, pets_id) VALUES ('1472db75-6372-4435-8c00-8d2934e1956d', 'Tina_2.JPG', '09f1b0d3-fcf2-4b40-92cb-cf24b33a56d7');
INSERT INTO public.image (id, filename, pets_id) VALUES ('5323615a-9fdc-4b00-9ff2-afb3cc8c46e7', 'Tina_3.JPG', '09f1b0d3-fcf2-4b40-92cb-cf24b33a56d7');
INSERT INTO public.image (id, filename, pets_id) VALUES ('0d0d00ee-4a40-4991-aa0d-8f33cfe479c5', 'Tina_4.JPG', '09f1b0d3-fcf2-4b40-92cb-cf24b33a56d7');
INSERT INTO public.image (id, filename, pets_id) VALUES ('98f0fc2e-4c60-4862-a50e-2cf70fd0a86c', 'Tina_5.JPG', '09f1b0d3-fcf2-4b40-92cb-cf24b33a56d7');
INSERT INTO public.image (id, filename, pets_id) VALUES ('677c77aa-0092-4713-a83d-41fd21beaf22', 'Tina_6.JPG', '09f1b0d3-fcf2-4b40-92cb-cf24b33a56d7');
INSERT INTO public.image (id, filename, pets_id) VALUES ('495beebf-8982-45ee-9d95-7ef763b791f0', 'Tina_7.JPG', '09f1b0d3-fcf2-4b40-92cb-cf24b33a56d7');
INSERT INTO public.image (id, filename, pets_id) VALUES ('fcaf2d42-e61a-4f50-a63c-9304c4b4f2da', 'Tina_8.JPG', '09f1b0d3-fcf2-4b40-92cb-cf24b33a56d7');
INSERT INTO public.image (id, filename, pets_id) VALUES ('2a940ca5-8dbf-4d0a-9ab1-b993d540416c', 'Tina_9.JPG', '09f1b0d3-fcf2-4b40-92cb-cf24b33a56d7');
INSERT INTO public.image (id, filename, pets_id) VALUES ('46529a5b-3bc9-49d7-8c23-1909cb89e342', 'Rex_1.JPG', '9d46bd18-156f-438e-9379-00ba451cea31');
INSERT INTO public.image (id, filename, pets_id) VALUES ('c930fd9e-0caa-4e65-978e-2919ec0f3ad0', 'Rex_2.JPG', '9d46bd18-156f-438e-9379-00ba451cea31');
INSERT INTO public.image (id, filename, pets_id) VALUES ('4f743e2d-6cb4-4a42-90c2-889f21f64448', 'Rex_3.JPG', '9d46bd18-156f-438e-9379-00ba451cea31');
INSERT INTO public.image (id, filename, pets_id) VALUES ('f293e4db-a884-48fc-ad8b-0e7e4d00f325', 'Rex_4.JPG', '9d46bd18-156f-438e-9379-00ba451cea31');
INSERT INTO public.image (id, filename, pets_id) VALUES ('861734f2-b449-499c-a5ad-26d8654b4748', 'Rex_5.JPG', '9d46bd18-156f-438e-9379-00ba451cea31');
INSERT INTO public.image (id, filename, pets_id) VALUES ('307b23e8-b988-42d0-ad9b-801bad1afe91', 'Rex_6.JPG', '9d46bd18-156f-438e-9379-00ba451cea31');
INSERT INTO public.image (id, filename, pets_id) VALUES ('b6c2d59c-24b7-41d9-a8c5-f9e6bb8d060a', 'Rex_7.JPG', '9d46bd18-156f-438e-9379-00ba451cea31');
INSERT INTO public.image (id, filename, pets_id) VALUES ('0688c674-6811-4c14-ad59-ab493801e41c', 'Rex_8.JPG', '9d46bd18-156f-438e-9379-00ba451cea31');
INSERT INTO public.image (id, filename, pets_id) VALUES ('41882214-1b7f-48c3-acc5-cb212d26107f', 'Piratik_1.JPG', '46773309-39cd-4aab-a849-e76987333032');
INSERT INTO public.image (id, filename, pets_id) VALUES ('b6d8e4cf-4a05-4f95-b4bd-f323098b6b67', 'Piratik_2.JPG', '46773309-39cd-4aab-a849-e76987333032');
INSERT INTO public.image (id, filename, pets_id) VALUES ('edf2033c-46ef-4ce2-828c-1cf9cfc16a30', 'Piratik_3.JPG', '46773309-39cd-4aab-a849-e76987333032');
INSERT INTO public.image (id, filename, pets_id) VALUES ('18969bb9-8d03-4355-b41b-3b2fb8695b0c', 'Piratik_4.JPG', '46773309-39cd-4aab-a849-e76987333032');
INSERT INTO public.image (id, filename, pets_id) VALUES ('a614a862-d57f-48d9-8495-d08dbb134385', 'Piratik_5.JPG', '46773309-39cd-4aab-a849-e76987333032');
INSERT INTO public.image (id, filename, pets_id) VALUES ('7e08816d-c3bf-430b-a3fe-71ced316caa7', 'Buran_1.JPG', 'a6155c48-0970-4a6a-ac42-5164461e706b');
INSERT INTO public.image (id, filename, pets_id) VALUES ('9686a335-9fec-43db-93ad-db7f0edbc8cd', 'Buran_2.JPG', 'a6155c48-0970-4a6a-ac42-5164461e706b');
INSERT INTO public.image (id, filename, pets_id) VALUES ('709426e1-79e2-4b21-8171-b3eff3c7770c', 'Buran_3.JPG', 'a6155c48-0970-4a6a-ac42-5164461e706b');
INSERT INTO public.image (id, filename, pets_id) VALUES ('961781ca-5c5a-4708-b928-f3bfc9062de6', 'Buran_4.JPG', 'a6155c48-0970-4a6a-ac42-5164461e706b');
INSERT INTO public.image (id, filename, pets_id) VALUES ('ff67c4c0-e0e4-4504-9fc0-184366b46a56', 'Buran_5.JPG', 'a6155c48-0970-4a6a-ac42-5164461e706b');
INSERT INTO public.image (id, filename, pets_id) VALUES ('9445dc24-184b-43f8-a45e-5e00d99b8feb', 'Sobak_1.jpg', 'ae407015-9ae4-4489-9f70-e4ca285af209');
INSERT INTO public.image (id, filename, pets_id) VALUES ('4d4f9bb3-c287-454e-b66c-75aded20f376', 'Sobak_2.jpg', 'ae407015-9ae4-4489-9f70-e4ca285af209');
INSERT INTO public.image (id, filename, pets_id) VALUES ('7920bc47-91f5-4ba6-8ca4-09fcc5ef98ee', 'Sobak_3.jpg', 'ae407015-9ae4-4489-9f70-e4ca285af209');
INSERT INTO public.image (id, filename, pets_id) VALUES ('b6758075-6188-4023-9b14-be45055f5cef', 'Sobak_4.jpg', 'ae407015-9ae4-4489-9f70-e4ca285af209');
INSERT INTO public.image (id, filename, pets_id) VALUES ('d02cf8b0-921e-44d9-9ab3-fdcc99ae00c3', 'Sobak_5.jpg', 'ae407015-9ae4-4489-9f70-e4ca285af209');
INSERT INTO public.image (id, filename, pets_id) VALUES ('b96d874a-1024-45eb-8fa4-9465a3402b79', 'Sobak_6.jpg', 'ae407015-9ae4-4489-9f70-e4ca285af209');
INSERT INTO public.image (id, filename, pets_id) VALUES ('cbd83f3f-5955-42aa-ab89-91e1283b1eef', 'Sobak_7.jpg', 'ae407015-9ae4-4489-9f70-e4ca285af209');
INSERT INTO public.image (id, filename, pets_id) VALUES ('485be4b7-c0ac-400c-8510-7123f35dd998', 'Sobak_8.jpg', 'ae407015-9ae4-4489-9f70-e4ca285af209');
INSERT INTO public.image (id, filename, pets_id) VALUES ('d8b02fd1-fa64-457b-9bd1-b5739896d575', 'Sobak_9.jpg', 'ae407015-9ae4-4489-9f70-e4ca285af209');
INSERT INTO public.image (id, filename, pets_id) VALUES ('f1f8ff89-871c-4502-874e-a7038b02f535', 'Sobak_10.jpg', 'ae407015-9ae4-4489-9f70-e4ca285af209');
INSERT INTO public.image (id, filename, pets_id) VALUES ('6e57924a-c1fe-4acb-ab2b-8fcfa9371852', 'Sobak_12.jpg', 'ae407015-9ae4-4489-9f70-e4ca285af209');
INSERT INTO public.image (id, filename, pets_id) VALUES ('8d0c26f6-5cf1-4d3b-9f4f-8c69300661e8', 'Sobak_13.jpg', 'ae407015-9ae4-4489-9f70-e4ca285af209');
INSERT INTO public.image (id, filename, pets_id) VALUES ('92612ad8-f627-4451-9dc1-75a978f83750', 'Sobak_14.jpg', 'ae407015-9ae4-4489-9f70-e4ca285af209');
INSERT INTO public.image (id, filename, pets_id) VALUES ('4576f098-423b-40dc-9c2c-de65ae09959e', 'Sobak_15.jpg', 'ae407015-9ae4-4489-9f70-e4ca285af209');
INSERT INTO public.image (id, filename, pets_id) VALUES ('d7462863-b2b0-44f2-ba95-f3d967234adf', 'Sobak_16.jpg', 'ae407015-9ae4-4489-9f70-e4ca285af209');
INSERT INTO public.image (id, filename, pets_id) VALUES ('a325feec-3bbf-4970-9c14-c61c0f954d4f', 'Sobak_17.jpg', 'ae407015-9ae4-4489-9f70-e4ca285af209');
INSERT INTO public.image (id, filename, pets_id) VALUES ('501d3f2f-a1ce-48b4-adb7-068d117d8cf9', 'Sobak_18.jpg', 'ae407015-9ae4-4489-9f70-e4ca285af209');
INSERT INTO public.image (id, filename, pets_id) VALUES ('f04365db-7c21-482d-af7b-fbc0734cc9f9', 'Sobak_19.jpg', 'ae407015-9ae4-4489-9f70-e4ca285af209');
INSERT INTO public.image (id, filename, pets_id) VALUES ('abdf2766-3363-46fe-9407-bd5198624f7c', 'Sobak_20.jpg', 'ae407015-9ae4-4489-9f70-e4ca285af209');
INSERT INTO public.image (id, filename, pets_id) VALUES ('1040f33b-5bba-4a19-bac3-233a9cc7193c', 'Sobak_21.jpg', 'ae407015-9ae4-4489-9f70-e4ca285af209');
INSERT INTO public.image (id, filename, pets_id) VALUES ('aef8f3c4-f41a-46b0-816c-743e901e0342', 'Sobak_22.jpg', 'ae407015-9ae4-4489-9f70-e4ca285af209');
INSERT INTO public.image (id, filename, pets_id) VALUES ('83dce2c2-b2ed-456b-a446-eb16d9fb0392', 'Sobak_23.jpg', 'ae407015-9ae4-4489-9f70-e4ca285af209');
INSERT INTO public.image (id, filename, pets_id) VALUES ('b85dcc60-0be1-48e6-9c1c-51c4d18e89c8', 'Sobak_24.jpg', 'ae407015-9ae4-4489-9f70-e4ca285af209');
INSERT INTO public.image (id, filename, pets_id) VALUES ('efbd700e-c5b4-4f15-b034-fb7a8e29df9f', 'Sobak_25.jpg', 'ae407015-9ae4-4489-9f70-e4ca285af209');
INSERT INTO public.image (id, filename, pets_id) VALUES ('df8f530d-94b5-4e9d-a989-446c83db6469', 'Mila_1.jpg', '67b15fe5-c9d1-47ac-8272-398bc4895b33');
INSERT INTO public.image (id, filename, pets_id) VALUES ('8be32bff-d40d-4aab-844c-23690d200d19', 'Mila_2.jpg', '67b15fe5-c9d1-47ac-8272-398bc4895b33');
INSERT INTO public.image (id, filename, pets_id) VALUES ('e957ae7c-8a42-46d8-af54-fba27d466fff', 'Viski_6 (1).jpg', '9890957f-59e9-406c-90cf-602f279f4b15');
INSERT INTO public.image (id, filename, pets_id) VALUES ('235066bc-c723-4095-9bbf-5e4887583234', 'Viski_1.jpg', '9890957f-59e9-406c-90cf-602f279f4b15');
INSERT INTO public.image (id, filename, pets_id) VALUES ('e3915a81-3ad3-4426-9345-597602683c0d', 'Viski_2.jpg', '9890957f-59e9-406c-90cf-602f279f4b15');
INSERT INTO public.image (id, filename, pets_id) VALUES ('de45cffa-ffb3-45a3-87e8-e964291f70ba', 'Viski_3.jpg', '9890957f-59e9-406c-90cf-602f279f4b15');
INSERT INTO public.image (id, filename, pets_id) VALUES ('b1b59dd8-ecc0-4476-827c-1cfe5a7b4be3', 'Viski_4.jpg', '9890957f-59e9-406c-90cf-602f279f4b15');
INSERT INTO public.image (id, filename, pets_id) VALUES ('6f86f995-7aab-4bb4-824a-a91097572e19', 'Viski_5.jpg', '9890957f-59e9-406c-90cf-602f279f4b15');
INSERT INTO public.image (id, filename, pets_id) VALUES ('49b79ea1-6d17-49f5-bb5b-59ae16f22208', 'Kasper_1.jpg', '2d370b50-52a5-4eb9-a9f7-5b5a712cfc8a');
INSERT INTO public.image (id, filename, pets_id) VALUES ('aa30c804-392c-4d45-9085-9486e0d38980', 'Kasper_2.jpg', '2d370b50-52a5-4eb9-a9f7-5b5a712cfc8a');
INSERT INTO public.image (id, filename, pets_id) VALUES ('4328cc3a-d07e-4bb9-ba84-39f9e84c50cc', 'Kasper_3.jpg', '2d370b50-52a5-4eb9-a9f7-5b5a712cfc8a');
INSERT INTO public.image (id, filename, pets_id) VALUES ('a1b3c909-f4bc-4aef-ba9c-d11068286080', 'Kasper_4.jpg', '2d370b50-52a5-4eb9-a9f7-5b5a712cfc8a');


--
-- Data for Name: pets; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.pets (id, status, name, gender, type_id, date_birth, age, breed, personality, appearance, health, description) VALUES ('948c6d60-8726-4be0-8578-9fcc8a5248bc', 'в приюте', 'Луна', 'F', '92469a91-925d-4863-97d0-27517cf1822f', NULL, 3, 'Акита', 'Очень привязана к хозяину и очень ранимая. Если на нее накричать, то может обидеться. С другими собаками агрессивна, но это можно исправить дрессировкой.', 'Очень красивая собака, с хорошим телосложением, густая шерсть трех цветов.', 'Не стерилизована', NULL);
INSERT INTO public.pets (id, status, name, gender, type_id, date_birth, age, breed, personality, appearance, health, description) VALUES ('1fb4d052-8780-4246-b3e4-5cbcab4554a3', 'в приюте', 'Вайт', 'M', '92469a91-925d-4863-97d0-27517cf1822f', NULL, 8, NULL, 'Еще не до конца привык к людям и иногда бывает агрессивным, но с собаками ладит замечательно.', 'Полностью черная шерсть, подранные уши.', 'Нет правой передней лапы, привит, стерилизован.', 'У него очень тяжелая история, его нашли с опухшими лапами перемотанными металлической проволкой и долго не могли поймать. Когда его отвезли к ветеринару, ему ампутировали лапу, но он отлично передвигается на трех ногах.');
INSERT INTO public.pets (id, status, name, gender, type_id, date_birth, age, breed, personality, appearance, health, description) VALUES ('837a64d7-2428-4e30-a900-d714fb845590', 'в приюте', 'Вик', 'M', '92469a91-925d-4863-97d0-27517cf1822f', NULL, 4, NULL, 'На сегодняшний день очень хорошо гуляет на поводке. Да, он тянет, да, он иногда не слушается, уходит в себя и бежит, куда ему уступается. Но это лишь потому, что ему хочется получить все эмоции здесь и сейчас, послушный. Когда рядом с ним машешь руками, он все равно прижимается к земле. Но когда понимает, что никакой опасности от человека нет, что человек только с хорошими намерениями, то он с удовольствием будет сидеть рядом, даст пузико почесать и с удовольствием поест вкусняшки.', 'ходячая любовь грумера, потому что у него не шерсть, а волосы. Очень умные глаза. ', 'привит, кастрирован', 'Он и его сестра Тина были подброшены на СТО в городе Владивостоке и оставлены там. Работники с утра, придя на работу, увидели под контейнерами двух щенков зашуганных. В течение года их не трогали в прямом смысле слова. То есть не приручали, не приучали к поводку, к ошейнику. И они немножко были диковаты, точнее сильно были диковаты. Когда поняли, что переезды в их новый дом не предвидится, занялись их воспитанием.');
INSERT INTO public.pets (id, status, name, gender, type_id, date_birth, age, breed, personality, appearance, health, description) VALUES ('a2aa7d05-f1e6-43c5-a810-cc56f2b2c48f', 'в приюте', 'Дана', 'F', '92469a91-925d-4863-97d0-27517cf1822f', NULL, 2, NULL, 'Родилась среди людей, поэтому очень дружелюбная, к другим собакам тоже относится без агрессии. Очень активная и тактильная, подойдет семьям с детьми или подвижным людям.', 'Светлая шерсть', 'Стерилизована, привита.', 'Бросили на стройке.');
INSERT INTO public.pets (id, status, name, gender, type_id, date_birth, age, breed, personality, appearance, health, description) VALUES ('a05306b6-9564-4b74-8ac6-46eb00ad3c3f', 'в приюте', 'Демон', 'M', '92469a91-925d-4863-97d0-27517cf1822f', NULL, 5, NULL, 'Очень дружелюбный и любвеобильный. Очень хорошо относится к людям и собакам, но агрессивен с котами. Не любит одиночество', 'Черно-белая шерсть, прижатые ушки.', 'Кастрирован, привит', NULL);
INSERT INTO public.pets (id, status, name, gender, type_id, date_birth, age, breed, personality, appearance, health, description) VALUES ('41950861-dc47-4137-9c6a-84d19b7eb90d', 'в приюте', 'Полкан', 'M', '92469a91-925d-4863-97d0-27517cf1822f', NULL, 6, NULL, 'Боится людей, любит одиночество. Недавно, благодаря теплому обращению, стал интересоваться человеком.', 'Черно-желтоватая шерсть, крупные размеры, добрые глаза.', 'Кастрирован, привит', 'Полкан с другой собакой жил в заброшенном доме, чувствовал опасность от человека, потому что до этого его отравили. Люди успели его спасти, но он сбежал обратно в барак, который похоже сгорел. Полкан пошёл в гостинку - на улице было холодно, ему негде было жить. Затем его снова пытались отравить, но он вышел к людям и обратился за помощью. Его спасли только потому, что в его организм попало мало яда. Теперь он боязливый житель фонда, который хочет вернуть доверие к человеку.');
INSERT INTO public.pets (id, status, name, gender, type_id, date_birth, age, breed, personality, appearance, health, description) VALUES ('09f1b0d3-fcf2-4b40-92cb-cf24b33a56d7', 'в приюте', 'Тина', 'F', '92469a91-925d-4863-97d0-27517cf1822f', NULL, 4, NULL, 'Боязлива, ей нужно время, чтобы привыкнуть к человеку. Но пройдя момент притирки становится ласковой, послушной собакой. Она уже осознаёт, что человек может стать её хорошим другом. ', 'Напоминает плюшевого мишку - имеет чёрную мягкую шёрстку.', 'Стерелизована, привита', NULL);
INSERT INTO public.pets (id, status, name, gender, type_id, date_birth, age, breed, personality, appearance, health, description) VALUES ('9d46bd18-156f-438e-9379-00ba451cea31', 'в приюте', 'Рекс', 'M', '92469a91-925d-4863-97d0-27517cf1822f', NULL, 10, NULL, 'Сначала сильно боялся людей. Сейчас это дружелюбный пёс, который любит вкусно покушать. Он свободолюбив и имеет силу воли. ', 'Преимущественно чёрная шерсть, понимающие глаза.', 'Кастрирован, привит', 'У этой собаки совсем она трагична. Поступает звонок. Просьба о помощи - на Баляева найден подстреленный пёс. Кинули клич по соцсетям. Более 10 человек ринулись спасать Рекса. Три пули в спину. Достали только две - одна слишком близко к позвоночнику. Он должен был остаться инвалидом…
Но его стремление к жизни сотворило чудо. Он выкарабкался из этого тяжело но состояния. И теперь бегает, прыгает, лишь иногда подволакивает задние лапы. Рекс любит жизнь, и хочет, чтобы она проходила в тёплом доме с добрым хозяином.');
INSERT INTO public.pets (id, status, name, gender, type_id, date_birth, age, breed, personality, appearance, health, description) VALUES ('46773309-39cd-4aab-a849-e76987333032', 'в приюте', 'Пират', 'M', '92469a91-925d-4863-97d0-27517cf1822f', NULL, 6, NULL, 'Очень долго притирается к человеку. Предположительно, пострадал от воздействия человека, поэтому он боязливый пёс. Трудно уживается с другими собаками.', 'Черно-белая шерсть, прижатые ушки.', 'Нарушение строение позвоночника - опущенный таз, из-за этого не кастрирован, привит.', NULL);
INSERT INTO public.pets (id, status, name, gender, type_id, date_birth, age, breed, personality, appearance, health, description) VALUES ('a6155c48-0970-4a6a-ac42-5164461e706b', 'в приюте', 'Буран', 'M', '92469a91-925d-4863-97d0-27517cf1822f', NULL, 9, NULL, 'Очень неприхотливый, спокойный и понимающий пёс. Все, что ему нужно - добрый человек рядом. Хорошо уживается с любимыми животными, даже с кошками. Может и хочет стать верным, лохматым спутником вашей жизни.', 'Смешанный окрас, вдумчивая морда', 'Кастрирован, привит', 'Он жил со стаей собак на заброшенной стоянке, в районе Второй речки. Не всем людям нравилось их пребывание там, поэтому было решено забрать хотя бы одну собаку оттуда на передержку в фонд.  Когда мы приехали на стоянку, то увидели Бурана, с большой дыркой на лбу - его ударили каким-то  тяжелым предметом по голове. Получилось его спасти, и теперь он ждёт для себя хорошего хозяина.');
INSERT INTO public.pets (id, status, name, gender, type_id, date_birth, age, breed, personality, appearance, health, description) VALUES ('ae407015-9ae4-4489-9f70-e4ca285af209', 'в приюте', 'Малыши-щеночки', 'M', '147112ce-c140-415d-95bb-a09edc4ef699', NULL, 1, NULL, NULL, NULL, NULL, '3 мальчика, 2 девочки.    Попали в фонд совсем недавно. В начале мая. Родились в районе Карьерной на промзоне. Так часто случается - люди заводят собак на охрану, а о кастрации или стерилизации животных не задумываются. Результатом этого становятся такие выброшенные щенки 
Красивые, белоснежные и бесконечно добрые, но, людям не нужные. 
Было принято решение забрать их подальше от опасных больших машин
Готовятся к вакцинации 
Будут выше среднего роста, гладкошёрстные. С возрастом может быть они и перестанут быть такими белыми, но то, что они останутся верными и надёжными друзьями на всю жизнь- это точно.');
INSERT INTO public.pets (id, status, name, gender, type_id, date_birth, age, breed, personality, appearance, health, description) VALUES ('67b15fe5-c9d1-47ac-8272-398bc4895b33', 'в приюте', 'Мила', 'F', 'aae9e32b-4322-4170-b2bc-d0e13c1092ce', NULL, 1, NULL, NULL, 'пушистая, интересный окрас шерсти', 'получает полное медикаментозное лечение, правильное питание, витамины; полностью прооперирована', 'сама пришла за помощью к человеку. Была совсем малышкой с поражением кожи, клещами, обезвоживанием, недобором веса и инфекцией, которая поразила глаз.
Характер: котенок, который любит жизнь. Мила - борец, прошла через множество трудностей, имеет непоколебимый волевой характер. Заслуживает любящей семьи как никто другой.');
INSERT INTO public.pets (id, status, name, gender, type_id, date_birth, age, breed, personality, appearance, health, description) VALUES ('9890957f-59e9-406c-90cf-602f279f4b15', 'в приюте', 'Виски', 'F', 'aae9e32b-4322-4170-b2bc-d0e13c1092ce', NULL, 1, NULL, 'очень активный котенок, быстро адаптируется к незнакомой обстановке. Виски любит бегать, прыгать, играть с людьми. Ласковая, любит помурчать. При первом контакте с незнакомым человеком - осторожничает.', 'зеленоглазая красавица с серой шерстью', 'проглистована, готовится к «детской» вакцинации', ' 6 апреля ее вместе с братом нашли в кустах, скорее всего их мама погибла. Прошла через искусственное вскармливание. приучена к лотку, кушает самостоятельно');
INSERT INTO public.pets (id, status, name, gender, type_id, date_birth, age, breed, personality, appearance, health, description) VALUES ('2d370b50-52a5-4eb9-a9f7-5b5a712cfc8a', 'в приюте', 'Каспер', 'M', 'aae9e32b-4322-4170-b2bc-d0e13c1092ce', NULL, 1, NULL, 'ласковый, любит поиграть. В отличие от своей сестры, увидев опасность предпочтет поспать в сторонке, а не бежать на рожон. Спокойный котенок.', 'зеленоглазый мальчик с коричнево-бежевым окрасом', 'проглистован готовится к «детской» вакцинации', ' 6 апреля ее вместе с братом нашли в кустах, скорее всего их мама погибла. Прошла через искусственное вскармливание. приучена к лотку, кушает самостоятельно');


--
-- Data for Name: pets_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.pets_type (id, name, description) VALUES ('92469a91-925d-4863-97d0-27517cf1822f', 'собака', 'собакен');
INSERT INTO public.pets_type (id, name, description) VALUES ('147112ce-c140-415d-95bb-a09edc4ef699', 'щенок', 'собака поменьше');
INSERT INTO public.pets_type (id, name, description) VALUES ('5362c214-35f4-4db8-90dc-12db513df838', 'кот/кошка', 'кошара');
INSERT INTO public.pets_type (id, name, description) VALUES ('aae9e32b-4322-4170-b2bc-d0e13c1092ce', 'котёнок', 'котик поменьше');


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
-- Name: image image_pets_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.image
    ADD CONSTRAINT image_pets_id_fkey FOREIGN KEY (pets_id) REFERENCES public.pets(id);


--
-- Name: pets pets_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pets
    ADD CONSTRAINT pets_type_id_fkey FOREIGN KEY (type_id) REFERENCES public.pets_type(id);


--
-- PostgreSQL database dump complete
--