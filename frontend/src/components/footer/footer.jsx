import React from "react";
import logo from "../../assets/images/logo.svg";
import tgLogo from "../../assets/images/TG-logo.png";
import waLogo from "../../assets/images/WA-logo.png";
import "./style-footer.css";

const Footer = () => {
  return (
    <footer className="footer">
      <div id="contacts" className="footer-container">
        <div className="footer-block-item">
          <img src={logo} alt="logo" />
          <p>Фонд для животных</p>
          <p>Политика конфиденциальности</p>
        </div>
        <div className="address">
          <p>
            Адрес приюта: <br />
            Приморский край
          </p>
          <p>
            Почта: <br />
            zooprim125@mail.ru
          </p>
          <p>Социальные сети:</p>
          <div className="footer-logos">
            <img src={tgLogo} alt="telegram" />
            <img src={waLogo} alt="whatsapp" />
          </div>
        </div>
        <div>
          <h1 className="phone-number">+7 (966) 287-51-91</h1>
          <p>Круглосуточно</p>
        </div>
        <div>
          <p>Дизайн</p>
          <p>Разработчик</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
