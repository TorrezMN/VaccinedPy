import './static/css/dash_styles.css';

import React, { useState, useEffect } from 'react';


import Table from './table_comp.js';

// ICONS
import {FaShare} from "react-icons/fa";


function  Dash(){
	const [t_stabl, setTotalStbl] = useState();
	const [t_vacc, setTotalVacc] = useState();
	const [t_dose, setTotalDose] = useState();

	const all_establ_url = "http://localhost:8000/establishments/get_all_establishments";
	const all_vacc_url = "http://localhost:8000/vaccine/get_all_vaccines";
	const all_dose_url = "http://localhost:8000/dose/get_all_dose";

	useEffect(()=>{
		// FETCH TOTAL STABLISHMENTS
		fetch(all_establ_url)
		.then(response => response.json())
		.then(data => setTotalStbl(data.size))
		// FETCH TOTAL VACCINES
		fetch(all_vacc_url)
		.then(response => response.json())
		.then(data => setTotalVacc(data.size))
		// FETCH ALL DOSES
		fetch(all_dose_url)
		.then(response => response.json())
		.then(data => setTotalDose(data.size))

	}, []);



	return(
	<div className='dash_container'>
		<div className='cell_title'>
			<a href='/' className='title'>COVID - Py</a>
			<p className='subtitle'>Dashboard</p>
		</div>
		<div className='dash_sm_cell cell_stats'>
			<p className='stats_title'>Total Stablishments</p>
			<p className='stat_value'>{t_stabl}</p>
		</div>
		<div className='dash_sm_cell cell_stats'>
			<p className='stats_title'>Total Vaccines</p>
			<p className='stat_value'>{t_vacc}</p>
			<a href='/vaccines' className='ver_mas'><FaShare/></a>
		</div>
		<div className='dash_sm_cell cell_stats'>
			<p className='stats_title'>N° Doses</p>
			<p className='stat_value'>{t_dose}</p>

		</div>
		<div className='dash_xl_cell cell_menu'></div>
		<div className='dash_xl_cell cell_table'>
			<Table/>
		</div>
	</div>
	)
}

export default Dash;
