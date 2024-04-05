import './App.css';
import Test from './api/api';

function App() {
  // function getMainActorProfileFromMovie(id) {
  //   return fetch(`https://swapi.dev/api/films/${id}/`)
  //     .then((movieResponse) => {
  //       return movieResponse.json()
  //     })
  //     .then((movie) => {
  //       const characterUrl = movie.characters[0].split("//")[1]
  //       return fetch(`https://${characterUrl}`)
  //     })
  //     .then((characterResponse) => {
  //       return characterResponse.json()
  //     })
  //     .catch((err) => {
  //       console.error("Произошла ошибка!", err)
  //     })
  // }
  
  // getMainActorProfileFromMovie(1).then((profile) => {
  //   console.log(profile)
  // })
  return (
    <div className="App">
      <Test/>
    </div>
  );
}

export default App;
