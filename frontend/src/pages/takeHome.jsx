import React, { useState, useEffect, useRef } from "react";
import { useParams, useNavigate } from "react-router-dom";
import arrow_goBack from "../assets/images/arrow-goBack.png";
import littleDogPaw from "../assets/images/little-dog-paw.png";
import loadingGif from "../assets/images/Running_dog.gif";
import "./style-takeHome.css";

const TakeHome = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [pet, setPet] = useState(null);
  const [activeImageIndex, setActiveImageIndex] = useState(0);
  const thumbnailsRef = useRef(null);

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

  useEffect(() => {
    if (thumbnailsRef.current) {
      const activeThumbnail = thumbnailsRef.current.children[activeImageIndex];
      thumbnailsRef.current.scrollTo({
        left:
          activeThumbnail.offsetLeft -
          thumbnailsRef.current.offsetWidth / 2 +
          activeThumbnail.offsetWidth / 2,
        behavior: "smooth",
      });
    }
  }, [activeImageIndex]);

  const handleImageClick = (index) => {
    setActiveImageIndex(index);
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

  const handleButtonClickToHelp = () => {
    navigate(`/contacts`);
  };

  return (
    <div>
      <div className="flex">
        <button className="btn-arrow" onClick={() => navigate(-1)}>
          <img src={arrow_goBack} alt="arrow-go-back" />
        </button>
        <h2>{pet.name}</h2>
      </div>
      <div className="pet-details">
        <div className="pet-images">
          <button className="btn-slider left-btn" onClick={handlePrevImage}>
            &lt;
          </button>
          <img
            className="pet-photo-main"
            key={pet.images[activeImageIndex].id}
            src={getImageLink(pet.images[activeImageIndex])}
            alt={pet.name}
          />
          <button className="btn-slider right-btn" onClick={handleNextImage}>
            &gt;
          </button>
          <div className="pet-thumbnails-container">
            <div className="pet-thumbnails" ref={thumbnailsRef}>
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
        </div>
        <div className="pet-info">
          <div className="main-info-container">
            <p>
              <img src={littleDogPaw} alt="dog-paw-img" />
              <span className="font-bold"> Статус:</span> {pet.status}
            </p>
            <p>
              <img src={littleDogPaw} alt="dog-paw-img" />
              <span className="font-bold"> Имя:</span> {pet.name}
            </p>
            <p>
              <img src={littleDogPaw} alt="dog-paw-img" />
              <span className="font-bold"> Пол:</span>{" "}
              {pet.gender === "F" ? "Женский" : "Мужской"}
            </p>
            <p>
              <img src={littleDogPaw} alt="dog-paw-img" />
              <span className="font-bold"> Возраст:</span> {pet.age} года
            </p>
            <p>
              <img src={littleDogPaw} alt="dog-paw-img" />
              <span className="font-bold"> Порода:</span> {pet.breed}
            </p>
          </div>

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
          <button
            className="btn want-help-btn"
            onClick={handleButtonClickToHelp}
          >
            Забрать
          </button>
        </div>
      </div>
    </div>
  );
};

export default TakeHome;
