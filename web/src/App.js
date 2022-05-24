import './App.css';

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

import Landing from './views/landing.js';

function App() {
	document.title= 'Vaccined Py'
  return (
    <div className="App">
	  <Landing/>
    </div>
  );
}

export default App;
