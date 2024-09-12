import React from "react";
import logo from "../../assets/images/logo.svg";
import tgLogo from "../../assets/images/logo-TG.svg";
import waLogo from "../../assets/images/logo-WA.svg";
import VKLogo from "../../assets/images/logo-VK.svg";
import IGLogo from "../../assets/images/logo-IG.svg";
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
            <a href="https://t.me/zooprim125" target={"_blank"}>
              <img src={tgLogo} alt="telegram" />
            </a>
            <a href="https://wa.me/79662875191" target={"_blank"}>
              <img src={waLogo} alt="whatsapp" />
            </a>
            <a href="https://vk.com/zooprim125" target={"_blank"}>
              <img src={VKLogo} alt="VKontakte" />
            </a>
            <a href="https://www.instagram.com/zooprim125/" target={"_blank"}>
              <img src={IGLogo} alt="Instagram" />
            </a>
          </div>
        </div>
        <div>
          <h1 className="phone-number">+7 (966) 287-51-91</h1>
          <p>Круглосуточно</p>
        </div>
        <div className="dev-links">
          <a href="https://www.behance.net/baa225bf">Дизайнер</a>
          <a href="https://t.me/matv864">
            Разработчики: <br /> Backend
          </a>
          <a href="https://t.me/arturdr45">Frontend</a>
          <a href="https://www.figma.com/design/CaX0hdy3qJFHSeqpXsGCpn/landing?node-id=0-1&t=q8Ul7Icp0iOqcUw0-1">
            Макет сайта
          </a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
