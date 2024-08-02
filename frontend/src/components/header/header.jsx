import React from "react";
import { Link } from "react-router-dom";
import logo from "../../assets/images/logo.svg";
import "./style-header.css";

const Header = () => {
  return (
    <header className="header">
      <Link to="/">
        <img className="logo" src={logo} alt="logo" />
      </Link>
      <div className="header-container">
        <div>
          <ul className="navbar">
            <li className="nav-item">
              <a href="#about-us">О нас</a>
            </li>
            <li className="nav-item">
              <a href="#help-us">Как нам помочь</a>
            </li>
            <li className="nav-item">
              <a href="#events">Мероприятия</a>
            </li>
            <li className="nav-item">
              <a href="#our-pets">Наши любимцы</a>
            </li>
            <li className="nav-item">
              <a href="#help-animals">Помощь вашим животным</a>
            </li>
            <li className="nav-item">
              <a href="#rules">Правила</a>
            </li>
            <li className="nav-item">
              <a href="#contacts">Контакты</a>
            </li>
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
              <a href="#about-us" className="menu-item">
                О нас
              </a>
            </li>
            <li>
              <a href="#help-us" className="menu-item">
                Как нам помочь
              </a>
            </li>
            <li>
              <a href="#events" className="menu-item">
                Мероприятия
              </a>
            </li>
            <li>
              <a href="#our-pets" className="menu-item">
                Наши любимцы
              </a>
            </li>
            <li>
              <a href="#help-animals" className="menu-item">
                Помощь вашим животным
              </a>
            </li>
            <li>
              <a href="#contacts" className="menu-item">
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
