import React, { useContext, useEffect, useState } from 'react'
import input from '../styles/register.module.css';
import UserContext from '../context/user/UserContext';

const EditProfile = ({edit}) => {

    const [formData, setFormData] = useState('');
    const { user } = useContext(UserContext);

    useEffect(() => {
        setFormData(user)
    }, [])

    const handleChange = (e) => {
        setFormData({...formData, [e.target.name] : e.target.value})
    }

    return (
        <>
            <div className={input.forms}>
                <h2 className='mb-0 ms-3'> Edit Profile</h2>
                <form action="" className={input.input_field2}>
                    <div className={input.input_field2}>
                        <span>Full Name</span>
                        <input type="text" className='input' name='full_name' value={formData.full_name} onChange={handleChange} placeholder='Enter your full name' />
                    </div>
                    <div className="row g-0">
                        <div className="col-sm-6">
                            <div className={input.input_field2}>
                                <span>Email</span>
                                <input type="email" className='input' name='email' value={formData.email} onChange={handleChange} placeholder='Enter your email' />
                            </div>
                        </div>
                        <div className="col-sm-6">
                            <div className={input.input_field2}>
                                <span>Phone</span>
                                <input type="tel" className='input' name='phone' value={formData.phone} onChange={handleChange} placeholder='Enter your phone number' />
                            </div>
                        </div>
                    </div>
                    <div className={input.input_field2}>
                        <span>Address</span>
                        <input type="text" className='input' name='address' value={formData.address} onChange={handleChange} placeholder='Enter your address' />
                    </div>
                    <div className="row g-0">
                        <div className="col-sm-6">
                            <div className={input.input_field2}>
                                <span>City</span>
                                <input type="text" className='input' name='city' value={formData.city} onChange={handleChange} placeholder='Enter your city' />
                            </div>
                        </div>
                        <div className="col-sm-6">
                            <div className={input.input_field2}>
                                <span>Pincode</span>
                                <input type="text" className='input' name='pincode' value={formData.pincode} onChange={handleChange} placeholder='Enter your pincode' />
                            </div>
                        </div>
                    </div>
                    <div className="d-flex justify-content-end align-items-center">
                        <button type='button' className='button' onClick={() => edit(false)}>Cancel</button>
                        <button type='submit' className='button border' disabled={true}>Save</button>
                    </div>
                </form>
            </div>
        </>
    )
}

export default EditProfile
