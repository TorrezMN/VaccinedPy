import './static/css/establishments_styles.css';
import axios from 'axios';
import { useState, useEffect } from 'react';
import { useNavigate } from "react-router-dom";

function Establishments(){

	let navigate = useNavigate();
	const establishments_url = `http://localhost:8000/establishments/get_all_establishments`;
	const [data, setDatos] = useState();

	function fetchData() {
			axios.get(establishments_url)
			.then((response) => {
				setDatos(response.data.data);
			});
	  }

	useEffect(()=>{
		fetchData();
	}, []);

	
	return(
		<div className='establishments_container'>

			<center>
				<h1>ESTABLISHMENTS</h1>
				<button onClick={() => navigate(-1)}>go back</button>
			</center>
			<div className='establishments'>
		{data? 
				data.map((d, i)=>{
					return(<p>{ i+1+"| " + d.establishments_name}</p>)
				})
			:<span className='resaltar'>Loading</span>
		}
		</div>




		</div>
	)
}


export default Establishments;
