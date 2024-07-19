import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import arrow_goBack from "../assets/images/arrow-goBack.png";
import loadingGif from "../assets/images/Running_dog.gif";
import "./style-takeHome.css";

const TakeHome = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [pet, setPet] = useState(null);
  const [activeImageIndex, setActiveImageIndex] = useState(0); // Состояние для отслеживания активного индекса изображения

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

  const handleImageClick = (index) => {
    setActiveImageIndex(index); // Обработчик клика по меньшему изображению
  };

  const handleNextImage = () => {
    setActiveImageIndex((prevIndex) =>
      prevIndex === pet.images.length - 1 ? 0 : prevIndex + 1
    );
  };

  const handlePrevImage = () => {
    setActiveImageIndex((prevIndex) =>
      prevIndex === 0 ? pet.images.length - 1 : prevIndex - 1
    );
  };

  const getImageLink = (imageSchema) => {
    let filename = imageSchema.filename.split(".");
    let extension = filename[filename.length - 1];
    let databaseFilename = `${imageSchema.id}.${extension}`;
    let fullDatabaseFilename = `http://zooprim125.online/storage/pets_images/${databaseFilename}`;
    return fullDatabaseFilename;
  };

  if (!pet) {
    return (
      <div className="loading-container">
        <img src={loadingGif} alt="Loading..." />
      </div>
    );
  }

  return (
    <div>
      <div className="flex">
        <button className="btn-arrow" onClick={() => navigate(-1)}>
          <img src={arrow_goBack} alt="arrow-go-back" />
        </button>
        <p>Забрать {pet.genitiveName}</p>
      </div>
      <div className="pet-details">
        <div className="pet-images">
          <button className="btn-slider" onClick={handlePrevImage}>
            &lt;
          </button>
          <img
            className="pet-photo-main"
            key={pet.images[activeImageIndex].id}
            src={getImageLink(pet.images[activeImageIndex])}
            alt={pet.name}
          />
          <button className="btn-slider" onClick={handleNextImage}>
            &gt;
          </button>
          <div className="pet-thumbnails">
            {pet.images.map((image, index) => (
              <img
                className={`pet-thumbnail ${
                  index === activeImageIndex ? "active" : ""
                }`}
                key={image.id}
                src={getImageLink(image)}
                alt={pet.name}
                onClick={() => handleImageClick(index)}
              />
            ))}
          </div>
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
