import './static/css/vaccines_styles.css';
import React, { useState, useEffect } from 'react';



function Vaccines(){
	const all_vaccines_url = "http://localhost:8000/vaccine/get_all_vaccines";
	const [vaccines, setVaccines] = useState();


	useEffect(()=>{
		// FETCH VACCINES
		  async function fetchMyAPI() {
      let response = await fetch(all_vaccines_url)
      response = await response.json()
      setVaccines(response.data)
    }

    fetchMyAPI()
	}, []);




	return(
		<div className='vaccines_container'>
			<p className='vaccine_title resaltar'>Vaccines</p>
			<p className='vaccine_subtitles'>List of vaccines available during the vaccination campaign.</p>
			<div className='vaccines'>

			{vaccines?.map((v,i)=>{
				return(
					<p key={i} className='vaccine'>{v.vaccine_name}</p>
				)
			})}






			</div>
			<a href='/dash' className='btn_go_back'>Go Back</a>
		</div>
	)
}


export default Vaccines;
