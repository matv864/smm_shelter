import React from "react";
import waitingCat from "../assets/images/kotik-na-klaviature.jpg";
import "./style-contacts.css";

const contactsPage = () => {
  return (
    <div className="contacts-container">
      <img className="contacts-main-img" src={waitingCat} alt="cat-img" />
      <h1 className="contacts-main-text">
        Сервис находится в стадии разработки. Если вы хотите забрать этого
        питомца, свяжитесь с владельцем приюта
      </h1>
    </div>
  );
};

export default contactsPage;
