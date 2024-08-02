import React from "react";
import { useNavigate } from "react-router-dom";
import imgDog1 from "../../assets/images/img-dog-1.png";
import singlePawImage from "../../assets/images/paw-image.png";
import arrows from "../../assets/images/arrows.png";
import imgAnimalWaiting from "../../assets/images/img-animal-waiting.png";
import imgForHelpAnimals from "../../assets/images/img-for-help-animals.png";
import "./style-mainPage.css";

const MainPage = () => {
  const navigate = useNavigate();

  const handleButtonClick = () => {
    navigate("/our-pets");
  };

  const handleButtonClickForHelp = () => {
    navigate("/contacts");
  };

  return (
    <div>
      <section className="marginSection start">
        <div className="paw-container">
          <div>
            <img src={singlePawImage} alt="singlePawImage" />
          </div>
          <div className="text-animal-need-home">
            <p className="textAngst animal">Животным</p>
            <p className="textAngst need-home">Нужен дом</p>
          </div>
          <button className="btn want-help" onClick={handleButtonClickForHelp}>
            Хочу помочь
          </button>
        </div>
      </section>
      <section id="about-us" className="marginSection aboutUs">
        <h1 className="title">О нас</h1>
        <div className="aboutUs-container">
          <img className="img-aboutUs" src={imgDog1} alt="img-dog-1" />
          <p className="text-start">
            <span className="text-bold">Фонд для животных</span> — это место,
            где содержат бездомных, потерянных или брошенных собак и кошек.
            Основные функции приюта: оперативная помощь животным, долгосрочная
            забота, поиск нового дома или хозяина. В мире существуют приюты двух
            типов: неограниченного приёма (государственные учреждения) и приюты
            ограниченного приёма, существующие на средства благотворительных
            организаций и частных пожертвований.
          </p>
        </div>
      </section>
      <div className="section-wrapper">
        <section id="help-us" className="marginSection helpUs">
          <h1 className="title">Как нам помочь?</h1>
          <div className="blocks-container">
            <div className="block">Сделать так</div>
            <div className="block">Сделать так</div>
            <div className="block">Сделать так</div>
            <div className="block">Сделать так</div>
          </div>
        </section>
      </div>
      {/* <section id="events" className="marginSection events">
        <div className="events-title-container">
          <h1 className="title">Мероприятия</h1>
          <div className="arrows">
            <img src={arrows} alt="arrows" />
          </div>
        </div>
        <div className="event-blocks-container">
          <div className="event-block">
            <img src={imgEvents} alt="img-events" />
            <p className="event-title">День открытых дверей</p>
            <p className="event-date">12.06.2024</p>
          </div>
          <div className="event-block">
            <img src={imgEvents} alt="img-events" />
            <p className="event-title">День открытых дверей</p>
            <p className="event-date">12.06.2024</p>
          </div>
          <div className="event-block">
            <img src={imgEvents} alt="img-events" />
            <p className="event-title">День открытых дверей</p>
            <p className="event-date">12.06.2024</p>
          </div>
        </div>
      </section> */}
      <section id="our-pets" className="marginSection ourFreinds">
        <div className="left-side-section">
          <h1 className="title font-size-64">
            Все животные <span className="light-color">ждут своих хозяев!</span>
          </h1>
          <p>
            Фонд для животных — это место, где содержат бездомных, потерянных
            или брошенных собак и кошек.
          </p>
          <div className="twoButtons">
            <button className="btn ourPets" onClick={handleButtonClick}>
              Наши любимцы
            </button>
            <button className="transparent btn">Хочу приехать</button>
          </div>
        </div>
        <img
          className="img-animal-waiting"
          src={imgAnimalWaiting}
          alt="img-animal-waiting"
        />
      </section>
      <section
        id="help-animals"
        className="marginSection helpingAnimalsSection"
      >
        <div className="events-title-container">
          <h1 className="title">Помощь вашим животным</h1>
          <div className="arrows">
            <img src={arrows} alt="arrows" />
          </div>
        </div>
        <div className="blocks-container">
          <div className="block-for-animalHelp">
            <img
              className="img-aboutUs"
              src={imgForHelpAnimals}
              alt="img-for-help-animals"
            />
            <p className="event-title">Муня, девочка, 2,5 года</p>
            <p className="event-title">
              Собака — это домашнее животное с продолговатым поджарым телом,
              длинным хвостом и круглой головой. У неё большие глаза
              золотистого, зелёного или орехового цвета.
            </p>
            <button className="btn want-help-btn">Помочь</button>
          </div>
          <div className="block-for-animalHelp">
            <img
              className="img-aboutUs"
              src={imgForHelpAnimals}
              alt="img-for-help-animals"
            />
            <p className="event-title">Муня, девочка, 2,5 года</p>
            <p className="event-title">
              Собака — это домашнее животное с продолговатым поджарым телом,
              длинным хвостом и круглой головой. У неё большие глаза
              золотистого, зелёного или орехового цвета.
            </p>
            <button className="btn want-help-btn">Помочь</button>
          </div>
          <div className="block-for-animalHelp">
            <img
              className="img-aboutUs"
              src={imgForHelpAnimals}
              alt="img-for-help-animals"
            />
            <p className="event-title">Муня, девочка, 2,5 года</p>
            <p className="event-title">
              Собака — это домашнее животное с продолговатым поджарым телом,
              длинным хвостом и круглой головой. У неё большие глаза
              золотистого, зелёного или орехового цвета.
            </p>
            <button className="btn want-help-btn">Помочь</button>
          </div>
        </div>
      </section>
      <section id="rules" className="marginSection rules">
        <h1 className="title">Что делать, если я нашел животное?</h1>
        <div className="rules-container">
          <p className="numbered-paragraph grid-item-1">
            <span className="number">1.</span>
            <span className="text-of-rules">
              Определите, нужна ли медицинская помощь животному. Если оно
              ранено, накормите его и отвезите в ветеринарную клинику.
            </span>
          </p>
          <p className="numbered-paragraph grid-item-2">
            <span className="number">2.</span>
            <span className="text-of-rules">
              Если животное не ранено, накормите его. Можно дать кошке сухой или
              влажный корм, мясо или мясные субпродукты, а собаке — корм,
              консервы, мясо с крупами или рыбу. Не забудьте про воду.
            </span>
          </p>
          <p className="numbered-paragraph grid-item-3">
            <span className="number">3.</span>
            <span className="text-of-rules">
              Проверьте животное на наличие чипа. Если найдёте код, свяжитесь с
              хозяином через ветеринарную клинику.
            </span>
          </p>
          <p className="numbered-paragraph grid-item-4">
            <span className="number">4.</span>
            <span className="text-of-rules">
              Проверьте животное в ветклинике на наличие инфекций и сделайте
              необходимые прививки.
            </span>
          </p>
          <p className="numbered-paragraph grid-item-5">
            <span className="number">5.</span>
            <span className="text-of-rules">
              Если не удалось найти хозяина, помогите животному найти временный
              дом или обратитесь в наш фонд.
            </span>
          </p>
        </div>
      </section>
    </div>
  );
};

export default MainPage;
