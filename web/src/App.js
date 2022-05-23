import './App.css';

function App() {
	document.title= 'Vaccined Py'
  return (
    <div className="App">
	  <div className='searchBar'>
		<div className='searchTitle'>
		  <center>
			<h3>Search by</h3>
		  </center>
		</div>
		<div className='searchBoxes'>
			<div className='search_option'>
				<label for="search_name">Name:</label>
				<input type="text" id="search_name" name="search_name"/>
			</div>
			<div className='search_option'>
				<label for="search_date">Date:</label>
				<input type="datetime-local" name="search_date" id="search_date"/>
			</div>
			<div className='search_option'>
				<label for="search_quant">Quantity:</label>
				<input type="range" name="search_quant" id="price" min="50000" max="500000" step="100" value="250000"/>
			</div>
		</div>


	  </div>
    </div>
  );
}

export default App;
