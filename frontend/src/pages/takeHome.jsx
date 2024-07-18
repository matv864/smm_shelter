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
          <p>
            <span className="font-bold">Статус:</span> {pet.status}
          </p>
          <p>
            <span className="font-bold">Имя:</span> {pet.name}
          </p>
          <p>
            <span className="font-bold">Пол:</span>{" "}
            {pet.gender === "F" ? "Женский" : "Мужской"}
          </p>
          <p>
            <span className="font-bold">Возраст:</span> {pet.age} года
          </p>
          <p>
            <span className="font-bold">Порода:</span> {pet.breed}
          </p>
          <p>
            <span className="font-bold">Характер:</span> {pet.personality}
          </p>
          <p>
            <span className="font-bold">Описание внешности:</span>{" "}
            {pet.appearance}
          </p>
          <p>
            <span className="font-bold">Здоровье:</span> {pet.health}
          </p>
          <p>
            <span className="font-bold">Описание:</span> {pet.description}
          </p>
          <button className="btn want-help-btn">Забрать</button>
        </div>
      </div>
    </div>
  );
};

export default TakeHome;
