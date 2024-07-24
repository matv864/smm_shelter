import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import arrow_left from "../assets/images/arrow-left.png";
import arrow_right from "../assets/images/arrow-right.png";
import imgForHelpAnimals from "../assets/images/img-for-help-animals.png";
import "./style-ourPets.css";

const getImageLink = (imageSchema) => {
  let filename = imageSchema.filename.split(".");
  let extension = filename[filename.length - 1];
  let databaseFilename = `${imageSchema.id}.${extension}`;
  let fullDatabaseFilename = `http://zooprim125.online/storage/pets_images/${databaseFilename}`;

  return fullDatabaseFilename;
};

const OurPets = () => {
  const [posts, setPosts] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [visiblePostsCount, setVisiblePostsCount] = useState(3);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://zooprim125.online/api/pets/list");
        const data = await response.json();

        if (!Array.isArray(data)) {
          throw new Error("Fetched data is not an array");
        }

        const processedData = await Promise.all(
          data.map(async (post) => {
            if (post.images && post.images.length > 0) {
              const firstImageLink = getImageLink(post.images[0]);
              return { ...post, firstImageLink };
            }
            return { ...post, firstImageLink: imgForHelpAnimals };
          })
        );

        setPosts(processedData);
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
        document.querySelector(".blocks-container").offsetWidth;
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
      <div className="blocks-container">
        {posts
          .slice(currentIndex, currentIndex + visiblePostsCount)
          .map((post) => (
            <div key={post.id} className="block-for-animalHelp">
              <img
                className="image-of-animal"
                src={post.firstImageLink}
                alt={post.name}
              />
              <p className="event-title">
                {post.name}, {post.age} года
              </p>
              <p className="event-title">{post.appearance}</p>
              <div className="btns-container">
                <button
                  className="btn want-help-btn"
                  onClick={handleButtonClickToHelp}
                >
                  Помочь
                </button>
                <button
                  className="btn transparent want-help-btn"
                  onClick={() => handleButtonClick(post.id)}
                >
                  Забрать
                </button>
              </div>
            </div>
          ))}
      </div>
    </section>
  );
};

export default OurPets;
