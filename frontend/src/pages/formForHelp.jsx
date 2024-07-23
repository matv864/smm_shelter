import React from "react";
import "./style-formForHelp.css";

const FormHelpContainer = () => {
  return (
    <div className="form-help-container">
      <h1>
        Вы ежедневно спасаете{" "}
        <span className="light-color">1000 животных!</span>
      </h1>
      <div className="form-for-donat">
        <div className="three-btns-group">
          <button className="btn want-help-btn">Банковская карта</button>
          <button className="btn want-help-btn">SMS</button>
          <button className="btn want-help-btn">Реквизиты</button>
        </div>
        <div className="choise-of-amount">
          <button className="amount-button">200 ₽</button>
          <button className="amount-button">400 ₽</button>
          <button className="amount-button">600 ₽</button>
          <button className="amount-button">200 ₽</button>
          <button className="amount-button other-amount-btn">
            Другая сумма
          </button>
        </div>
        <label className="toggle">
          <input className="toggle-checkbox" type="checkbox" />
          <div className="toggle-switch"></div>
          <p className="toggle-label">Помогать ежемесячно</p>
        </label>
        <p>
          Заполните, пожалуйста, контактные данные, чтобы мы могли отправить вам
          чек пожертвования
        </p>
        <div className="form-container">
          <form>
            <div className="form-group">
              <input
                type="text"
                id="name"
                placeholder="Ваше имя"
                name="name"
                required
              />
            </div>
            <div className="form-group">
              <input
                type="email"
                id="email"
                placeholder="Ваша электронная почта"
                name="email"
                required
              />
            </div>
            <div className="form-group checkbox-group">
              <label className="checkbox-label">
                <input type="checkbox" id="privacy" name="privacy" required />Я
                принимаю условия Политика конфиденциальности, Пользовательское
                соглашение и Условия сотрудничества.
              </label>
            </div>
            <button type="submit" className="btn btn-submit">
              Помочь
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default FormHelpContainer;
