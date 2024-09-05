import React, { useState, useEffect, useRef } from "react";
import { useNavigate } from "react-router-dom";
import arrow_left from "../../assets/images/arrow-left.png";
import arrow_right from "../../assets/images/arrow-right.png";
import { fetchPetsList } from "./API-request";
import ImageWithPlaceholder from "../../components/ImageWithPlaceholder/ImageWithPlaceholder";
import placeholderImage from "../../assets/images/placeholder-image.jpg";
import "./style-ourPets.css";

const calculateAge = (birthDate) => {
  const birthYear = new Date(birthDate);
  const ageDiff = new Date().getFullYear() - birthYear.getFullYear();
  return ageDiff;
};

const OurPets = () => {
  const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;
  const [posts, setPosts] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [visiblePostsCount, setVisiblePostsCount] = useState(3);
  const touchStartX = useRef(0);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await fetchPetsList();
        setPosts(data);
      } catch (error) {
        console.error("Error fetching posts:", error);
      }
    };

    fetchData();
  }, []);

  const handlePrevClick = () => {
    setCurrentIndex((prevIndex) => (prevIndex === 0 ? 0 : prevIndex - 1));
  };

  const handleNextClick = () => {
    setCurrentIndex((prevIndex) =>
      prevIndex + visiblePostsCount >= posts.length ? prevIndex : prevIndex + 1
    );
  };

  useEffect(() => {
    const handleResize = () => {
      const containerWidth =
        document.querySelector(".cards-container").offsetWidth;
      const postWidth = 300;
      const visibleCount = Math.floor(containerWidth / postWidth);
      setVisiblePostsCount(visibleCount);
    };

    window.addEventListener("resize", handleResize);

    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  const navigate = useNavigate();

  const handleButtonClick = (id) => {
    navigate(`/take-home/${id}`);
  };

  const handleButtonClickToHelp = () => {
    navigate(`/contacts`);
  };

  const handleTouchStart = (e) => {
    touchStartX.current = e.touches[0].clientX;
  };

  const handleTouchMove = (e) => {
    const touchEndX = e.touches[0].clientX;
    const diffX = touchStartX.current - touchEndX;

    if (Math.abs(diffX) > 50) {
      if (diffX > 0) {
        handleNextClick();
      } else {
        handlePrevClick();
      }
    }
  };

  return (
    <section className="helpingAnimalsPage">
      <div className="events-title-container">
        <h1>Наши любимцы</h1>
        <div className="arrows">
          <button className="btn-arrow" onClick={handlePrevClick}>
            <img src={arrow_left} alt="left-arrow" />
          </button>
          <button className="btn-arrow" onClick={handleNextClick}>
            <img src={arrow_right} alt="right-arrow" />
          </button>
        </div>
      </div>
      <div
        className="cards-container"
        onTouchStart={handleTouchStart}
        onTouchMove={handleTouchMove}
      >
        {posts
          .slice(currentIndex, currentIndex + visiblePostsCount)
          .map((post) => {
            const imageUrl =
              post.petImage.length > 0
                ? `${API_BASE_URL}${post.petImage[0].filename}`
                : placeholderImage;
            const age = calculateAge(post.year_birth);

            return (
              <div key={post.id} className="block-for-animalHelp">
                <ImageWithPlaceholder
                  className="image-of-animal"
                  src={imageUrl}
                  placeholder={placeholderImage}
                  alt={post.name}
                />
                <p className="event-title">
                  {post.name}, {age} {age === 1 ? "год" : "лет"}
                </p>
                <p className="event-title">{post.description}</p>
                <div className="btns-container">
                  <button
                    className="btn our-pets-btn"
                    onClick={handleButtonClickToHelp}
                  >
                    Помочь
                  </button>
                  <button
                    className="btn transparent our-pets-btn"
                    onClick={() => handleButtonClick(post.id)}
                  >
                    Забрать
                  </button>
                </div>
              </div>
            );
          })}
      </div>
    </section>
  );
};

export default OurPets;
