import "./App.css";
import React from "react";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  useLocation,
} from "react-router-dom";
import Header from "./components/header/header.jsx";
import Footer from "./components/footer/footer.jsx";
import MainPage from "./pages/mainPage/mainPage";
import OurPets from "./pages/ourPets/ourPets";
import TakeHome from "./pages/takeHome/takeHome";
import FormHelp from "./pages/formForHelp/formForHelp";
import ContactsPage from "./pages/contacts/contactsPage";
import NotFound from "./pages/notFound/notFound";

const ScrollToSection = () => {
  const { hash } = useLocation();

  React.useEffect(() => {
    if (hash) {
      const element = document.getElementById(hash.substring(1));
      if (element) {
        element.scrollIntoView({ behavior: "smooth" });
      }
    }
  }, [hash]);

  return null;
};

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <ScrollToSection />
        <main>
          <Routes>
            <Route path="/" element={<MainPage />} />
            <Route path="/our-pets" element={<OurPets />} />
            <Route path="/take-home/:id" element={<TakeHome />} />
            <Route path="/form-for-help" element={<FormHelp />} />
            <Route path="/contacts" element={<ContactsPage />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
