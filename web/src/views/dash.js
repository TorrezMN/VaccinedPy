import './static/css/dash_styles.css';

import axios from 'axios';
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


	const fetchTotalEstablishments = ()=>{
		// FETCH TOTAL STABLISHMENTS
			axios.get(all_establ_url)
			.then((est_resp) => {
				setTotalStbl(est_resp.data.size);
			});
	}

	const fetchTotalVaccines = ()=>{
		// FETCH TOTAL VACCINES
		axios.get(all_vacc_url)
		.then((vacc_resp)=>{
			setTotalVacc(vacc_resp.data.size);
		});
	}
	const fetchTotalDose = ()=>{
		// FETCH ALL DOSES
		axios.get(all_dose_url)
		.then((dose_resp)=>{
			setTotalDose(dose_resp.data.size);
		});
	}

	useEffect(()=>{
		fetchTotalEstablishments();
		fetchTotalVaccines();
		fetchTotalDose();
	}, []);



	return(
	<div className='dash_container'>
		<div className='cell_title'>
			<a href='/' className='title'>COVID - Py</a>
			<p className='subtitle'>Explorer</p>
		</div>
		<div className='dash_sm_cell cell_stats'>
			<p className='stats_title'>Total Stablishments</p>
			<p className='stat_value'>{t_stabl}</p>
			<a href='/establishments' className='ver_mas'><FaShare/></a>
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
		<div className='dash_xl_cell cell_table'>
			<Table/>
		</div>
	</div>
	)
}

export default Dash;
