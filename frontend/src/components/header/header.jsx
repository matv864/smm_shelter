import React from "react";
import logo from "../../assets/images/logo.svg";
import "./style-header.css";

const Header = () => {
  return (
    <header className="header">
      <div>
        <img src={logo} alt="logo" />
      </div>
      <div className="header-container">
        <div>
          <ul className="navbar">
            <li className="nav-item">О нас</li>
            <li className="nav-item">Как нам помочь</li>
            <li className="nav-item">Мероприятия</li>
            <li className="nav-item">Наши любимцы</li>
            <li className="nav-item">Помощь вашим животным</li>
            <li className="nav-item">Правила</li>
            <li className="nav-item">Контакты</li>
          </ul>
        </div>

        <div className="menu">
          <input
            type="checkbox"
            id="burger-checkbox"
            className="burger-checkbox"
          />
          <label htmlFor="burger-checkbox" className="burger"></label>
          <ul className="menu-list">
            <li>
              <a href="#" className="menu-item">
                О нас
              </a>
            </li>
            <li>
              <a href="#" className="menu-item">
                Как нам помочь
              </a>
            </li>
            <li>
              <a href="#" className="menu-item">
                Мероприятия
              </a>
            </li>
            <li>
              <a href="#" className="menu-item">
                Наши любимцы
              </a>
            </li>
            <li>
              <a href="#" className="menu-item">
                Что делать, если я нашел животное
              </a>
            </li>
            <li>
              <a href="#" className="menu-item">
                Контакты
              </a>
            </li>
          </ul>
        </div>
      </div>
    </header>
  );
};

export default Header;
