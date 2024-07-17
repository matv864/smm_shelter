import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import arrow_goBack from "../assets/images/arrow-goBack.png";
import "./style-takeHome.css";

const TakeHome = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [pet, setPet] = useState(null);

  useEffect(() => {
    const fetchPet = async () => {
      try {
        const response = await fetch(`http://zooprim125.online/api/pets/${id}`);
        const data = await response.json();
        setPet(data);
      } catch (error) {
        console.error("Error fetching pet data:", error);
      }
    };

    fetchPet();
  }, [id]);

  if (!pet) {
    return <div>Loading...</div>;
  }

  const getImageLink = (imageSchema) => {
    let filename = imageSchema.filename.split(".");
    let extension = filename[filename.length - 1];
    let databaseFilename = `${imageSchema.id}.${extension}`;
    let fullDatabaseFilename = `http://zooprim125.online/storage/pets_images/${databaseFilename}`;
    return fullDatabaseFilename;
  };

  return (
    <div>
      <div className="flex">
        <button className="btn-arrow" onClick={() => navigate(-1)}>
          <img src={arrow_goBack} alt="arrow-go-back" />
        </button>
        <p>Забрать</p>
      </div>
      <div className="pet-details">
        <div className="pet-images">
          {pet.images &&
            pet.images.map((image) => (
              <img
                className="pet-photo"
                key={image.id}
                src={getImageLink(image)}
                alt={pet.name}
              />
            ))}
        </div>
        <div className="pet-info">
          <p>Статус: {pet.status}</p>
          <div className="flex">
            <p>Имя:</p>
            <p>{pet.name}</p>
          </div>
          <div className="flex">
            <p>Пол:</p>
            <p>{pet.gender === "F" ? "Женский" : "Мужской"}</p>
          </div>
          <div className="flex">
            <p>Возраст:</p>
            <p>{pet.age} года</p>
          </div>
          <div className="flex">
            <p>Порода:</p>
            <p>{pet.breed}</p>
          </div>
          <div className="flex">
            <p>Характер:</p>
            <p>{pet.personality}</p>
          </div>
          <div className="flex">
            <p>Описание внешности:</p>
            <p>{pet.appearance}</p>
          </div>
          <div className="flex">
            <p>Здоровье:</p>
            <p>{pet.health}</p>
          </div>
          <div className="flex">
            <p>Описание:</p>
            <p>{pet.description}</p>
          </div>
          <button className="btn want-help-btn">Забрать</button>
        </div>
      </div>
    </div>
  );
};

export default TakeHome;
