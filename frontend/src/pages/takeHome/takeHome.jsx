import React, { useState, useEffect, useRef } from "react";
import { useParams, useNavigate } from "react-router-dom";
import arrow_goBack from "../../assets/images/arrow-goBack.png";
import littleDogPaw from "../../assets/images/little-dog-paw.png";
import loadingGif from "../../assets/images/Running_dog.gif";
import { fetchPetDetails, getImageLink } from "./API-request";
import "./style-takeHome.css";

const TakeHome = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [pet, setPet] = useState(null);
  const [activeImageIndex, setActiveImageIndex] = useState(0);
  const thumbnailsRef = useRef(null);
  const touchStartX = useRef(0);

  useEffect(() => {
    const fetchPet = async () => {
      try {
        const data = await fetchPetDetails(id);
        setPet(data);
        setActiveImageIndex(0);
      } catch (error) {
        console.error("Error fetching pet data:", error);
      }
    };

    fetchPet();
  }, [id]);

  useEffect(() => {
    if (thumbnailsRef.current && pet && pet.petImage[activeImageIndex]) {
      const activeThumbnail = thumbnailsRef.current.children[activeImageIndex];
      thumbnailsRef.current.scrollTo({
        left:
          activeThumbnail.offsetLeft -
          thumbnailsRef.current.offsetWidth / 2 +
          activeThumbnail.offsetWidth / 2,
        behavior: "smooth",
      });
    }
  }, [activeImageIndex, pet]);

  const handleImageClick = (index) => {
    setActiveImageIndex(index);
  };

  const handleNextImage = () => {
    setActiveImageIndex((prevIndex) =>
      prevIndex === pet.petImage.length - 1 ? 0 : prevIndex + 1
    );
  };

  const handlePrevImage = () => {
    setActiveImageIndex((prevIndex) =>
      prevIndex === 0 ? pet.petImage.length - 1 : prevIndex - 1
    );
  };

  const handleTouchStart = (e) => {
    touchStartX.current = e.touches[0].clientX;
  };

  const handleTouchMove = (e) => {
    const touchEndX = e.touches[0].clientX;
    const diffX = touchStartX.current - touchEndX;

    if (Math.abs(diffX) > 50) {
      if (diffX > 0) {
        handleNextImage();
      } else {
        handlePrevImage();
      }
    }
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

  const calculateAge = (birthDate) => {
    const birthYear = new Date(birthDate).getFullYear();
    const currentYear = new Date().getFullYear();
    return currentYear - birthYear;
  };

  return (
    <div>
      <div className="goBackBtn-and-petName">
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
            src={getImageLink(pet.petImage[activeImageIndex])}
            alt={pet.name}
            onTouchStart={handleTouchStart}
            onTouchMove={handleTouchMove}
          />
          <button className="btn-slider right-btn" onClick={handleNextImage}>
            &gt;
          </button>
          <div className="pet-thumbnails-container">
            <div className="pet-thumbnails" ref={thumbnailsRef}>
              {pet.petImage.map((image, index) => (
                <img
                  className={`pet-thumbnail ${
                    index === activeImageIndex ? "active" : ""
                  }`}
                  key={image.filename}
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
              <span className="font-bold"> Статус:</span> {pet.status.name}
            </p>
            <p>
              <img src={littleDogPaw} alt="dog-paw-img" />
              <span className="font-bold"> Имя:</span> {pet.name}
            </p>
            <p>
              <img src={littleDogPaw} alt="dog-paw-img" />
              <span className="font-bold"> Пол:</span> {pet.gender.name}
            </p>
            <p>
              <img src={littleDogPaw} alt="dog-paw-img" />
              <span className="font-bold"> Возраст:</span>{" "}
              {calculateAge(pet.year_birth)} года
            </p>
          </div>

          <p>
            <span className="font-bold">Описание:</span> {pet.description}
          </p>
          <button
            className="btn take-home-btn"
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
