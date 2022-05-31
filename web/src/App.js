import './App.css';

import {
  BrowserRouter as Router,
  Routes,
  Route} from "react-router-dom";



// IMPORTING VIEWS
import Landing from './views/landing.js';
import Dash from './views/dash.js';
import Vaccines from './views/vaccines.js';





function App() {

  document.title = 'Vaccined Py - COVID 19';


  return (
    <Router>
    <div className="App">
		<Routes>
          <Route path='/' element={<Landing/>} />
          <Route path='/dash' element={<Dash/>} />
          <Route path='/vaccines' element={<Vaccines/>} />
		</Routes>
    </div>
    </Router>
  );
}

export default App;
