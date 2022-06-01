import './static/css/table_styles.css';
import React, { useState, useEffect } from 'react';

import { useNavigate } from "react-router-dom";


function Table(props){
	const [data, setData] = useState([]);
	let navigate = useNavigate();



	const name_changed = (v)=>{
		const filter_by_name_url = `http://localhost:8000/record/filter_by_name_all/${v}`;

		async function fetchMyAPI() {
			let response = await fetch(filter_by_name_url);
			response = await response.json();
			setData(response.data);
		}

		if(v.length>0){
			fetchMyAPI();
		}
	}

	return(
		<div className='table_container'>
			<div className='table_search_bar'>
				<input 
					className='input_search' 
					type='text' 
					placeholder='Name'
					onChange={e => name_changed(e.target.value)}
				/>
				<input className='input_search' type='text' placeholder='Last Name'/>
				<input className='input_search' type='text' placeholder='CI'/>

			</div>

			<table>
				<thead>
					<tr>
						<th>CI</th>
						<th>Application Date</th>
						<th>Name</th>
						<th>Last Name</th>
						<th>Updated</th>
					</tr>
				</thead>
				<tbody>
					{data?.map((d)=>{

						return(
					<tr key={Math.random()} 
							usr_id={d.id} 
							onClick={(e)=>{ navigate(`/card/${e.currentTarget.getAttribute("usr_id")}`)}}
							>
						<td>{d.cedula}</td>
						<td>{d.fecha_aplicacion}</td>
						<td>{d.nombre}</td>
						<td>{d.apellido}</td>
						<td>{d.actualizado_al}</td>
					</tr>
						)
					})}
				</tbody>
			</table>


		</div>
	)
}



export default Table;
