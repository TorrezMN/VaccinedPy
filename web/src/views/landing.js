
import './css/landing_styles.css';




function  Landing(){
	return(
		<div className='landing_container'>
			<p className='landing_title'>Paraguay <span className='resaltar'>COVID-19</span></p>
			<p className='landing_subtitle'>A small application to explore vaccination data in Paraguay.</p>
			<a href='#' className='landing_button'>Go to Dash</a>
		</div>
	)
}

export default Landing;
