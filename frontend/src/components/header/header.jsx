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
              <Link to="/#about-us">О нас</Link>
            </li>
            <li className="nav-item">
              <Link to="/#help-us">Как нам помочь</Link>
            </li>
            <li className="nav-item">
              <Link to="#events">Мероприятия</Link>
            </li>
            <li className="nav-item">
              <Link to="/our-pets">Наши любимцы</Link>
            </li>
            <li className="nav-item">
              <Link to="/#help-animals">Помощь вашим животным</Link>
            </li>
            <li className="nav-item">
              <Link to="/#rules">Правила</Link>
            </li>
            <li className="nav-item">
              <Link to="/#contacts">Контакты</Link>
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
              <Link to="/#about-us" className="menu-item">
                О нас
              </Link>
            </li>
            <li>
              <Link to="/#help-us" className="menu-item">
                Как нам помочь
              </Link>
            </li>
            <li>
              <Link to="/#events" className="menu-item">
                Мероприятия
              </Link>
            </li>
            <li>
              <Link to="/#our-pets" className="menu-item">
                Наши любимцы
              </Link>
            </li>
            <li>
              <Link to="/#help-animals" className="menu-item">
                Помощь вашим животным
              </Link>
            </li>
            <li>
              <Link to="/#contacts" className="menu-item">
                Контакты
              </Link>
            </li>
          </ul>
        </div>
      </div>
    </header>
  );
};

export default Header;
