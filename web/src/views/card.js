

import React, { useState, useEffect } from 'react';
import {useParams,  useNavigate } from "react-router-dom";




function Card(props){
	let params = useParams();
	let navigate = useNavigate();

	const record_data_url = `http://localhost:8000/record/get_by_id/${params.id}`;
	const [data, setData] = useState();

	useEffect(()=>{
		// FETCH VACCINES
		  async function fetchMyAPI() {
      let response = await fetch(record_data_url)
      response = await response.json()
      setData(response.data)
    }

    fetchMyAPI()
	console.log(data);
	}, []);

	return(
		<div>
		<center>
			<h1>CARD ! {params.id}</h1>
			<button onClick={() => navigate(-1)}>go back</button>
		</center>
		<div>
		<p> actualizado_al {data.actualizado_al} </p>
		<p> apellido {data.apellido} </p>
		<p> cedula {data.cedula} </p>
		<p> dose {data.dose} </p>
		<p> establishment {data.establishment} </p>
		<p> fecha_aplicacion {data.fecha_aplicacion} </p>
		<p> nombre {data.nombre} </p>
		<p> vaccine {data.vaccine} </p>

		</div>

		</div>
			
		)
}

export default Card;
