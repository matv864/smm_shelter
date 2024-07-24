import "./App.css";
import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Header from "./components/header/header.jsx";
import Footer from "./components/footer/footer.jsx";
import MainPage from "./pages/mainPage";
import OurPets from "./pages/ourPets";
import TakeHome from "./pages/takeHome";
import FormHelp from "./pages/formForHelp";
import ContactsPage from "./pages/contactsPage";

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <main>
          <Routes>
            <Route path="/" element={<MainPage />} />
            <Route path="/our-pets" element={<OurPets />} />
            <Route path="/take-home/:id" element={<TakeHome />} />
            <Route path="/form-for-help" element={<FormHelp />} />
            <Route path="/contacts" element={<ContactsPage />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
