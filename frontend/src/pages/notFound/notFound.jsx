import React from "react";
import "./style-notFound.css";
import NotFound from "../../assets/images/not-found.png";

const notFound = () => {
  return (
    <div className="notFound-container">
      <h1 className="notFound-text">Упс! Что-то пошло не так</h1>
      <img className="notFound-img" src={NotFound} alt="not-foung-img" />
      <h1 className="notFound-text">Страница не найдена</h1>
    </div>
  );
};

export default notFound;
