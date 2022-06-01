import './App.css';

import {
  BrowserRouter as Router,
  Routes,
  Route} from "react-router-dom";



// IMPORTING VIEWS
import Landing from './views/landing.js';
import Dash from './views/dash.js';
import Vaccines from './views/vaccines.js';
import Card from './views/card.js';





function App() {

  document.title = 'Vaccined Py - COVID 19';


  return (
    <Router>
    <div className="App">
		<Routes>
			<Route path='/' element={<Landing/>} />
			<Route path='/dash' element={<Dash/>} />
			<Route path='/vaccines' element={<Vaccines/>} />
			<Route path="card/:id" element={<Card/>} />
		</Routes>
    </div>
    </Router>
  );
}

export default App;
