import React, { useState, useEffect } from "react";
import arrows from "../assets/images/arrows.png";
import imgForHelpAnimals from "../assets/images/img-for-help-animals.png";
import "./style-ourPets.css";

// Provided function to get image link
const getImageLink = async (imageSchema) => {
  let filename = imageSchema.filename.split(".");
  let extension = filename[filename.length - 1];
  let databaseFilename = `${imageSchema.id}.${extension}`;
  let fullDatabaseFilename = `/storage/pets_images/${databaseFilename}`;
  return fullDatabaseFilename;
};

const OurPets = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://zooprim125.online/api/pets/list");
        const data = await response.json();

        console.log("Fetched data:", data); // Log fetched data

        // Ensure data is an array
        if (!Array.isArray(data)) {
          throw new Error("Fetched data is not an array");
        }

        // Process images for each post
        const processedData = await Promise.all(
          data.map(async (post) => {
            if (post.images && post.images.length > 0) {
              const firstImageLink = await getImageLink(post.images[0]);
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

  return (
    <section className="marginSection helpingAnimals">
      <div className="events-title-container">
        <h1>Помощь вашим животным</h1>
        <div className="arrows">
          <img src={arrows} alt="arrows" />
        </div>
      </div>
      <div className="blocks-container">
        {posts.map((post) => (
          <div key={post.id} className="block-for-animalHelp">
            <img src={post.firstImageLink} alt={post.name} />
            <p className="event-title">
              {post.name}, {post.age} года
            </p>
            <p className="event-title">{post.appearance}</p>
            <button className="btn want-help-btn">Помочь</button>
          </div>
        ))}
      </div>
    </section>
  );
};

export default OurPets;
