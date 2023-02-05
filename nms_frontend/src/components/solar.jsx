import React, { Component } from 'react';

export class Solar extends Component {
    render(){
        return (
            <div className="solar">
                <h1>Hello Solar</h1>
                <div className="inputs">
                    <div className="input-container">
                        <label htmlFor="daylight">Total Daylight Time:</label>
                        <input type="number" name="daylight" className='w100' />
                    </div>
                    <div className="input-container">
                        <label htmlFor="daylight">Daylight Time Remaining When Reaching Full Power:</label>
                        <input type="number" name="daylight_full" />
                    </div>
                    <div className="input-container">
                        <label htmlFor="daylight">Daylight Time Remaining When Reaching Half Power:</label>
                        <input type="number" name="daylight_half" />
                    </div>
                    <div className="input-container">
                        <label htmlFor="daylight">Total Night Time:</label>
                        <input type="number" name="night" />
                    </div>
                    <div className="input-container">
                        <label htmlFor="daylight">Night Time Remaining When Power Is Lost:</label>
                        <input type="number" name="night_cutoff" />
                    </div>
                    <div className="input-container">
                        <label htmlFor="daylight">Night Time Remaining When Reaching Half Power:</label>
                        <input type="number" name="night_half" />
                    </div>
                </div>
            </div>
        );
    }
}

export default Solar;