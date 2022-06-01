import './static/css/card_styles.css';
import axios from 'axios';
import { useState, useEffect } from 'react';
import {useParams,  useNavigate } from "react-router-dom";




function Card(props){
	let params = useParams();
	let navigate = useNavigate();
	const record_data_url = `http://localhost:8000/miscellaneous/get_clean_record/${params.id}`;
	const [data, setDatos] = useState();

	
	
	function fetchData() {
			axios.get(record_data_url)
			.then((response) => {
				setDatos(response.data.data);
			});
	  }

	useEffect(()=>{
		fetchData();
	}, []);

	return(
		<div className='card_container'>
			<center>
				<h1>VACCINATION CARD</h1>
				<button onClick={() => navigate(-1)}>go back</button>
			</center>
				{data? 
						<div className='vacc_card'>
							<p>CI : {data.cedula} </p>
							<p>NAME : {data.nombre} </p>
							<p>LAST NAME : {data.apellido} </p>
							<p>APPLICATION DATE : {data.fecha_aplicacion} </p>
							<p>ESTABLISHMENT : {data.establishment} </p>
							<p>VACCINE : {data.vaccine} </p>
							<p>UPDATED TO : {data.actualizado_al} </p>
							<p>DOSE N° : {data.dose} </p>
						</div>
					: <p className='loading'>LOADING</p>
				}
		{/*
		*/}
		</div>
			
		)
}

export default Card;
