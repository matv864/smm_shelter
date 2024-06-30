import "./App.css";
import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Header from "./components/header/header.jsx";
import Footer from "./components/footer/footer.jsx";
import MainPage from "./pages/mainPage";
import OurPets from "./pages/ourPets";

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <main>
          <Routes>
            <Route path="/" element={<MainPage />} />
            <Route path="/our-pets" element={<OurPets />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
